<!-- source: https://en.wikipedia.org/wiki/Multiplicative_order | converted from HTML -->

Multiplicative order - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Concept in modular arithmetic

In [number theory][1], given a positive integer *n*and an [integer][2]*a*[coprime][3] to *n*, the **multiplicative order**of *a*modulo *n*is the smallest positive integer *k*such that ''k''</sup> ≡ 1 (mod ''n'')"}},"i":0}}]}'>*a**k*≡ 1 (mod *n*). [1]

In other words, the multiplicative order of *a*modulo *n*is the [order][4] of *a*in the [multiplicative group][5] of the [units][6] in the [ring][7] of the integers [modulo][8]*n*.

The order of *a*modulo *n*is sometimes written as ord*n*(*a*). [2]

## Example

[[edit][9]]

The powers of 4 modulo 7 are as follows:

4 0 = 1 = 0 × 7 + 1 ≡ 1 ( mod 7) 4 1 = 4 = 0 × 7 + 4 ≡ 4 ( mod 7) 4 2 = 16 = 2 × 7 + 2 ≡ 2 ( mod 7) 4 3 = 64 = 9 × 7 + 1 ≡ 1 ( mod 7) 4 4 = 256 = 36 × 7 + 4 ≡ 4 ( mod 7) 4 5 = 1024 = 146 × 7 + 2 ≡ 2 ( mod 7) ⋮ {\displaystyle {\begin{array}{llll}4^{0}&=1&=0\times 7+1&\equiv 1{\pmod {7}}\\4^{1}&=4&=0\times 7+4&\equiv 4{\pmod {7}}\\4^{2}&=16&=2\times 7+2&\equiv 2{\pmod {7}}\\4^{3}&=64&=9\times 7+1&\equiv 1{\pmod {7}}\\4^{4}&=256&=36\times 7+4&\equiv 4{\pmod {7}}\\4^{5}&=1024&=146\times 7+2&\equiv 2{\pmod {7}}\\\vdots \end{array}}}[image: {\displaystyle {\begin{array}{llll}4^{0}&=1&=0\times 7+1&\equiv 1{\pmod {7}}\\4^{1}&=4&=0\times 7+4&\equiv 4{\pmod {7}}\\4^{2}&=16&=2\times 7+2&\equiv 2{\pmod {7}}\\4^{3}&=64&=9\times 7+1&\equiv 1{\pmod {7}}\\4^{4}&=256&=36\times 7+4&\equiv 4{\pmod {7}}\\4^{5}&=1024&=146\times 7+2&\equiv 2{\pmod {7}}\\\vdots \end{array}}}]

The smallest positive integer *k*such that ''k''</sup> ≡ 1 (mod 7)"}},"i":0}}]}'>4*k*≡ 1 (mod 7) is 3, so the order of 4 (mod 7) is 3. Note that a 0 = 1 ≡ 1 ( mod n) {\displaystyle a^{0}=1\equiv 1{\pmod {n}}}[image: {\displaystyle a^{0}=1\equiv 1{\pmod {n}}}] is trivially true for any non-zero a {\displaystyle a}[image: {\displaystyle a}], but since zero is not a positive integer, trivial solutions are not valid.

## Properties

[[edit][10]]

Even without knowledge that we are working in the [multiplicative group of integers modulo n][11], we can show that *a*actually has an order by noting that the powers of *a*can only take a finite number of different values modulo *n*, so according to the [pigeonhole principle][12] there must be two powers, say *s*and *t*and [without loss of generality][13]*s*>*t*, such that *a**s*≡*a**t*(mod*n*). Since *a*and *n*are [coprime][3], *a*has an inverse element *a*−1 and we can multiply both sides of the congruence with *a*−*t*, yielding ''s''−''t''</sup> ≡ 1 (mod ''n'')"}},"i":0}}]}'>*a**s*−*t*≡ 1 (mod *n*).

The concept of multiplicative order is a special case of the [order of group elements][4]. The multiplicative order of a number *a*modulo *n*is the order of *a*in the [multiplicative group][11] whose elements are the residues modulo *n*of the numbers coprime to *n*, and whose group operation is multiplication modulo*n*. This is the [group of units][14] of the [ring][7]**Z***n*; it has *φ*(*n*) elements, *φ*being [Euler's totient function][15], and is denoted as *U*(*n*) or*U*(**Z***n*).

As a consequence of [Lagrange's theorem][16], the order of *a*(mod *n*) always [divides][17]*φ*(*n*). If the order of *a*is actually equal to *φ*(*n*), and therefore as large as possible, then *a*is called a [primitive root][18] modulo *n*. This means that the group *U*(*n*) is [cyclic][19] and the residue class of *a*[generates][20] it.

The order of *a*(mod *n*) also divides *λ*(*n*), a value of the [Carmichael function][21], which is an even stronger statement than the divisibility of*φ*(*n*).

## Programming languages

[[edit][22]]

- [Maxima CAS][23]: zn_order (a, n) [3]
- [Wolfram Language][24]: MultiplicativeOrder[k, n] [4]
- [Rosetta Code][25] – examples of multiplicative order in various languages [5]

## See also

[[edit][26]]

- [Discrete logarithm][27]
- [Modular arithmetic][8]

## References

[[edit][28]]

1. ↑ Niven, Zuckerman & Montgomery 1991, Section 2.8 Definition 2.6
2. ↑ [von zur Gathen, Joachim][29]; Gerhard, Jürgen (2013). **[Modern Computer Algebra][30] (3rd ed.). Cambridge University Press. Section 18.1. [ISBN][31] [9781107039032][32].
3. ↑ [Maxima 5.42.0 Manual: zn_order][33]
4. ↑ [Wolfram Language documentation][34]
5. ↑ [rosettacode.org – examples of multiplicative order in various languages][35]

- [Niven, Ivan][36]; Zuckerman, Herbert S.; [Montgomery, Hugh L.][37] (1991). *An Introduction to the Theory of Numbers*(5th ed.). [John Wiley & Sons][38]. [ISBN][31] [0-471-62546-9][39].

## External links

[[edit][40]]

- [Weisstein, Eric W.][41] ["Multiplicative Order"][42]. *[MathWorld][43]*.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Multiplicative_order&oldid=1363920538][44] "

[Category][45]:

- [Modular arithmetic][46]

Hidden categories:

- [Articles with short description][47]
- [Short description is different from Wikidata][48]

Search

Multiplicative order

12 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Number_theory
[2]: https://en.wikipedia.org/wiki/Integer
[3]: https://en.wikipedia.org/wiki/Coprime
[4]: https://en.wikipedia.org/wiki/Order_(group_theory)
[5]: https://en.wikipedia.org/wiki/Multiplicative_group
[6]: https://en.wikipedia.org/wiki/Unit_(ring_theory)
[7]: https://en.wikipedia.org/wiki/Ring_(mathematics)
[8]: https://en.wikipedia.org/wiki/Modular_arithmetic
[9]: /w/index.php?title=Multiplicative_order&amp;action=edit&amp;section=1
[10]: /w/index.php?title=Multiplicative_order&amp;action=edit&amp;section=2
[11]: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
[12]: https://en.wikipedia.org/wiki/Pigeonhole_principle
[13]: https://en.wikipedia.org/wiki/Without_loss_of_generality
[14]: https://en.wikipedia.org/wiki/Group_of_units
[15]: https://en.wikipedia.org/wiki/Euler's_totient_function
[16]: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
[17]: https://en.wikipedia.org/wiki/Divisor
[18]: https://en.wikipedia.org/wiki/Primitive_root_modulo_n
[19]: https://en.wikipedia.org/wiki/Cyclic_group
[20]: https://en.wikipedia.org/wiki/Cyclic_group#Definition_and_notation
[21]: https://en.wikipedia.org/wiki/Carmichael_function
[22]: /w/index.php?title=Multiplicative_order&amp;action=edit&amp;section=3
[23]: https://en.wikipedia.org/wiki/Maxima_CAS
[24]: https://en.wikipedia.org/wiki/Wolfram_Language
[25]: https://en.wikipedia.org/wiki/Rosetta_Code
[26]: /w/index.php?title=Multiplicative_order&amp;action=edit&amp;section=4
[27]: https://en.wikipedia.org/wiki/Discrete_logarithm
[28]: /w/index.php?title=Multiplicative_order&amp;action=edit&amp;section=5
[29]: https://en.wikipedia.org/wiki/Joachim_von_zur_Gathen
[30]: https://books.google.com/books?id=7fE9baKyqSEC&amp;pg=PA517
[31]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[32]: https://en.wikipedia.org/wiki/Special:BookSources/9781107039032
[33]: https://maxima.sourceforge.net/docs/manual/maxima_29.html#zn_005forder
[34]: https://reference.wolfram.com/language/ref/MultiplicativeOrder.html
[35]: https://rosettacode.org/wiki/Multiplicative_order
[36]: https://en.wikipedia.org/wiki/Ivan_M._Niven
[37]: https://en.wikipedia.org/wiki/Hugh_Lowell_Montgomery
[38]: https://en.wikipedia.org/wiki/John_Wiley_&amp;_Sons
[39]: https://en.wikipedia.org/wiki/Special:BookSources/0-471-62546-9
[40]: /w/index.php?title=Multiplicative_order&amp;action=edit&amp;section=6
[41]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[42]: https://mathworld.wolfram.com/MultiplicativeOrder.html
[43]: https://en.wikipedia.org/wiki/MathWorld
[44]: https://en.wikipedia.org/w/index.php?title=Multiplicative_order&amp;oldid=1363920538
[45]: /wiki/Help:Category
[46]: /wiki/Category:Modular_arithmetic
[47]: /wiki/Category:Articles_with_short_description
[48]: /wiki/Category:Short_description_is_different_from_Wikidata
