<!-- source: https://en.wikipedia.org/wiki/Totient_summatory_function | converted from HTML -->

Totient summatory function - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Arithmetic function

In [number theory][1], the **totient summatory function**Φ ( n) {\displaystyle \Phi (n)}[image: {\displaystyle \Phi (n)}] is a [summatory function][2] of [Euler's totient function][3] defined by

Φ ( n):= ∑ k = 1 n φ ( k), n ∈ N. {\displaystyle \Phi (n):=\sum _{k=1}^{n}\varphi (k),\quad n\in \mathbb {N} .}[image: {\displaystyle \Phi (n):=\sum _{k=1}^{n}\varphi (k),\quad n\in \mathbb {N} .}]

It is the number of ordered pairs of [coprime][4] integers (*p*,*q*), where 1 ≤*p*≤*q*≤*n*.

The first few values are 0, 1, 2, 4, 6, 10, 12, 18, 22, 28, 32, ... (sequence [A002088][5] in the [OEIS][6]). Values for powers of 10 are 1, 32, 3044, 304192, 30397486, 3039650754, ... (sequence [A064018][7] in the [OEIS][6]).

## Properties

[[edit][8]]

The following identity holds for all real n ≥ 0 {\displaystyle n\geq 0}[image: {\displaystyle n\geq 0}]:

∑ d = 1 n Φ ( n d) = 1 2 ⌊ n ⌋ ⌊ n + 1 ⌋ {\displaystyle \sum _{d=1}^{n}\Phi \left({\frac {n}{d}}\right)={\frac {1}{2}}\lfloor n\rfloor \lfloor n+1\rfloor }[image: {\displaystyle \sum _{d=1}^{n}\Phi \left({\frac {n}{d}}\right)={\frac {1}{2}}\lfloor n\rfloor \lfloor n+1\rfloor }].

This gives an implicit recurrence for the totient summatory function. [1]: 138

Applying [Möbius inversion][9] to the totient function or the above identity yields

Φ ( n) = ∑ k = 1 n k ∑ d ∣ k μ ( d) d = 1 2 ∑ k = 1 n μ ( k) ⌊ n k ⌋ ( 1 + ⌊ n k ⌋), {\displaystyle \Phi (n)=\sum _{k=1}^{n}k\sum _{d\mid k}{\frac {\mu (d)}{d}}={\frac {1}{2}}\sum _{k=1}^{n}\mu (k)\left\lfloor {\frac {n}{k}}\right\rfloor \left(1+\left\lfloor {\frac {n}{k}}\right\rfloor \right),}[image: {\displaystyle \Phi (n)=\sum _{k=1}^{n}k\sum _{d\mid k}{\frac {\mu (d)}{d}}={\frac {1}{2}}\sum _{k=1}^{n}\mu (k)\left\lfloor {\frac {n}{k}}\right\rfloor \left(1+\left\lfloor {\frac {n}{k}}\right\rfloor \right),}]

where μ ( n) {\displaystyle \mu (n)}[image: {\displaystyle \mu (n)}] is the [Möbius function][10]. Then it can be shown that Φ(*n*) has the asymptotic expansion

Φ ( n) ∼ 1 2 ζ ( 2) n 2 + O ( n log ⁡ n) = 3 π 2 n 2 + O ( n log ⁡ n), {\displaystyle \Phi (n)\sim {\frac {1}{2\zeta (2)}}n^{2}+O\left(n\log n\right)={\frac {3}{\pi ^{2}}}n^{2}+O\left(n\log n\right),}[image: {\displaystyle \Phi (n)\sim {\frac {1}{2\zeta (2)}}n^{2}+O\left(n\log n\right)={\frac {3}{\pi ^{2}}}n^{2}+O\left(n\log n\right),}]

where ζ(2) is the [Riemann zeta function][11] evaluated at 2, which is π 2 6 {\displaystyle {\frac {\pi ^{2}}{6}}}[image: {\displaystyle {\frac {\pi ^{2}}{6}}}]. [1]: 462–463 [2]

## Reciprocal totient summatory function

[[edit][12]]

The summatory function of the reciprocal of the totient is

S ( n):= ∑ k = 1 n 1 φ ( k). {\displaystyle S(n):=\sum _{k=1}^{n}{\frac {1}{\varphi (k)}}.}[image: {\displaystyle S(n):=\sum _{k=1}^{n}{\frac {1}{\varphi (k)}}.}]

[Edmund Landau][13] showed in 1900 that this function has the asymptotic behavior [3]

S ( n) ∼ A ( γ + log ⁡ n) + B + O ( log ⁡ n n), {\displaystyle S(n)\sim A(\gamma +\log n)+B+O\left({\frac {\log n}{n}}\right),}[image: {\displaystyle S(n)\sim A(\gamma +\log n)+B+O\left({\frac {\log n}{n}}\right),}]

where γ is the [Euler–Mascheroni constant][14],

A = ∑ k = 1 ∞ μ ( k) 2 k φ ( k) = ζ ( 2) ζ ( 3) ζ ( 6) = ∏ p ∈ P ( 1 + 1 p ( p − 1)), {\displaystyle A=\sum _{k=1}^{\infty }{\frac {\mu (k)^{2}}{k\varphi (k)}}={\frac {\zeta (2)\zeta (3)}{\zeta (6)}}=\prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p(p-1)}}\right),}[image: {\displaystyle A=\sum _{k=1}^{\infty }{\frac {\mu (k)^{2}}{k\varphi (k)}}={\frac {\zeta (2)\zeta (3)}{\zeta (6)}}=\prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p(p-1)}}\right),}]

and

B = ∑ k = 1 ∞ μ ( k) 2 log ⁡ k k φ ( k) = A ∏ p ∈ P ( log ⁡ p p 2 − p + 1). {\displaystyle B=\sum _{k=1}^{\infty }{\frac {\mu (k)^{2}\log k}{k\,\varphi (k)}}=A\,\prod _{p\in \mathbb {P} }\left({\frac {\log p}{p^{2}-p+1}}\right).}[image: {\displaystyle B=\sum _{k=1}^{\infty }{\frac {\mu (k)^{2}\log k}{k\,\varphi (k)}}=A\,\prod _{p\in \mathbb {P} }\left({\frac {\log p}{p^{2}-p+1}}\right).}]

The constant *A*= 1.943596... is sometimes known as **Landau's totient constant**. The sum ∑ k = 1 ∞ 1 / ( k φ ( k)) {\displaystyle \textstyle \sum _{k=1}^{\infty }1/(k\;\varphi (k))}[image: {\displaystyle \textstyle \sum _{k=1}^{\infty }1/(k\;\varphi (k))}] converges to

∑ k = 1 ∞ 1 k φ ( k) = ζ ( 2) ∏ p ∈ P ( 1 + 1 p 2 ( p − 1)) = 2.20386 …. {\displaystyle \sum _{k=1}^{\infty }{\frac {1}{k\varphi (k)}}=\zeta (2)\prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p^{2}(p-1)}}\right)=2.20386\ldots .}[image: {\displaystyle \sum _{k=1}^{\infty }{\frac {1}{k\varphi (k)}}=\zeta (2)\prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p^{2}(p-1)}}\right)=2.20386\ldots .}]

In this case, the product over the primes in the right side is a constant known as the **totient summatory constant**, [4] and its value is

∏ p ∈ P ( 1 + 1 p 2 ( p − 1)) = 1.339784 …. {\displaystyle \prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p^{2}(p-1)}}\right)=1.339784\ldots .}[image: {\displaystyle \prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p^{2}(p-1)}}\right)=1.339784\ldots .}]

## See also

[[edit][15]]

- [Arithmetic function][16]

## References

[[edit][17]]

1. 1 2 Graham, Ronald L.; Knuth, Donald E.; Patashnik, Oren. *Concrete Mathematics*(2 ed.). Addison-Wesley. [ISBN][18] [0-201-55802-5][19].
2. ↑ [Weisstein, Eric W.][20], ["Riemann Zeta Function \zeta(2)"][21], *[MathWorld][22]*
3. ↑ \\varphi(n)</math> und ihre Beziehung zum Goldbachschen Satz"},"url":{"wt":"https://eudml.org/doc/58472"},"volume":{"wt":"1900"},"year":{"wt":"1900"}},"i":0}}]}'/> [Landau, E.][13] (1900), [image: {\displaystyle \varphi (n)}] ["Ueber die zahlentheoretische Funktion φ ( n) {\displaystyle \varphi (n)} und ihre Beziehung zum Goldbachschen Satz"][23], *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, **1900**: 177– 186
4. ↑ [OEIS][6]: [A065483][24]

- [Weisstein, Eric W.][20] ["Totient Summatory Function"][25]. *[MathWorld][22]*.

## External links

[[edit][26]]

- [OEIS Totient summatory function][27]
- [Decimal expansion of totient constant product(1 + 1/(p^2*(p-1))), p prime >= 2)][28]

[image: Stub icon] [29] |

This [number theory][1] –related article is a [stub][30]. You can help Wikipedia by [adding missing information][31].

 |

- [v][32]
- [t][33]
- [e][34]

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Totient_summatory_function&oldid=1355421993][35] "

[Categories][36]:

- [Arithmetic functions][37]
- [Number theory stubs][38]

Hidden categories:

- [Articles with short description][39]
- [Short description is different from Wikidata][40]
- [All stub articles][41]

Search

Totient summatory function

1 language Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Number_theory
[2]: https://en.wikipedia.org/wiki/Summatory_function
[3]: https://en.wikipedia.org/wiki/Euler's_totient_function
[4]: https://en.wikipedia.org/wiki/Coprime_integers
[5]: //oeis.org/A002088
[6]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[7]: //oeis.org/A064018
[8]: /w/index.php?title=Totient_summatory_function&amp;action=edit&amp;section=1
[9]: https://en.wikipedia.org/wiki/Möbius_inversion_formula
[10]: https://en.wikipedia.org/wiki/Möbius_function
[11]: https://en.wikipedia.org/wiki/Riemann_zeta_function
[12]: /w/index.php?title=Totient_summatory_function&amp;action=edit&amp;section=2
[13]: https://en.wikipedia.org/wiki/Edmund_Landau
[14]: https://en.wikipedia.org/wiki/Euler–Mascheroni_constant
[15]: /w/index.php?title=Totient_summatory_function&amp;action=edit&amp;section=3
[16]: https://en.wikipedia.org/wiki/Arithmetic_function
[17]: /w/index.php?title=Totient_summatory_function&amp;action=edit&amp;section=4
[18]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[19]: https://en.wikipedia.org/wiki/Special:BookSources/0-201-55802-5
[20]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[21]: https://mathworld.wolfram.com/RiemannZetaFunctionZeta2.html
[22]: https://en.wikipedia.org/wiki/MathWorld
[23]: https://eudml.org/doc/58472
[24]: //oeis.org/A065483
[25]: https://mathworld.wolfram.com/TotientSummatoryFunction.html
[26]: /w/index.php?title=Totient_summatory_function&amp;action=edit&amp;section=5
[27]: //oeis.org/wiki/Totient_summatory_function
[28]: https://oeis.org/A065483
[29]: https://en.wikipedia.org/wiki/File:Number_theory_symbol.svg
[30]: https://en.wikipedia.org/wiki/Wikipedia:Stub
[31]: https://en.wikipedia.org/w/index.php?title=Totient_summatory_function&amp;action=edit
[32]: https://en.wikipedia.org/wiki/Template:Numtheory-stub
[33]: https://en.wikipedia.org/wiki/Template_talk:Numtheory-stub
[34]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Numtheory-stub
[35]: https://en.wikipedia.org/w/index.php?title=Totient_summatory_function&amp;oldid=1355421993
[36]: /wiki/Help:Category
[37]: /wiki/Category:Arithmetic_functions
[38]: /wiki/Category:Number_theory_stubs
[39]: /wiki/Category:Articles_with_short_description
[40]: /wiki/Category:Short_description_is_different_from_Wikidata
[41]: /wiki/Category:All_stub_articles
