<!-- source: https://en.wikipedia.org/wiki/Exponential_formula | converted from HTML -->

Exponential formula - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

In [combinatorial][1] [mathematics][2], the **exponential formula**(called the **polymer expansion**in [physics][3]) states that the [exponential generating function][4] for structures on [finite sets][5] is the [exponential][6] of the exponential generating function for connected structures. The exponential formula is a [power series][7] version of a special case of [Faà di Bruno's formula][8].

## Algebraic statement

[[edit][9]]

Here is a purely [algebraic][10] statement, as a first introduction to the combinatorial use of the formula.

For any [formal power series][11] of the form

f ( x) = a 1 x + a 2 x 2 2 + a 3 x 3 6 + ⋯ + a n x n n! + … {\displaystyle f(x)=a_{1}x+a_{2}{\frac {x^{2}}{2}}+a_{3}{\frac {x^{3}}{6}}+\dots +a_{n}{\frac {x^{n}}{n!}}+\dots }[image: {\displaystyle f(x)=a_{1}x+a_{2}{\frac {x^{2}}{2}}+a_{3}{\frac {x^{3}}{6}}+\dots +a_{n}{\frac {x^{n}}{n!}}+\dots }]

we have

exp ⁡ f ( x) = e f ( x) = ∑ n = 0 ∞ b n x n n! {\displaystyle \exp f(x)=e^{f(x)}=\sum _{n=0}^{\infty }b_{n}{\frac {x^{n}}{n!}}}[image: {\displaystyle \exp f(x)=e^{f(x)}=\sum _{n=0}^{\infty }b_{n}{\frac {x^{n}}{n!}}}]

where

b n = ∑ π = { S 1, …, S k } a | S 1 | ⋯ a | S k | {\displaystyle b_{n}=\sum _{\pi =\left\{S_{1},\dots ,S_{k}\right\}}a_{\left|S_{1}\right|}\cdots a_{\left|S_{k}\right|}}[image: {\displaystyle b_{n}=\sum _{\pi =\left\{S_{1},\dots ,S_{k}\right\}}a_{\left|S_{1}\right|}\cdots a_{\left|S_{k}\right|}}]

and the index π {\displaystyle \pi }[image: {\displaystyle \pi }] runs through all [partitions][12] { S 1, …, S k } {\displaystyle \{S_{1},\ldots ,S_{k}\}}[image: {\displaystyle \{S_{1},\ldots ,S_{k}\}}] of the set { 1, …, n } {\displaystyle \{1,\ldots ,n\}}[image: {\displaystyle \{1,\ldots ,n\}}]. (When k = 0 {\displaystyle k=0}[image: {\displaystyle k=0}], the product is [empty][13] and by definition equals 1 {\displaystyle 1}[image: {\displaystyle 1}].)

### Other expressions

[[edit][14]]

- One can write the exponential formula in the following form

b n = B n ( a 1, a 2, …, a n) {\displaystyle b_{n}=B_{n}(a_{1},a_{2},\dots ,a_{n})}[image: {\displaystyle b_{n}=B_{n}(a_{1},a_{2},\dots ,a_{n})}] and thus exp ⁡ ( ∑ n = 1 ∞ a n x n n!) = ∑ n = 0 ∞ B n ( a 1, …, a n) x n n! {\displaystyle \exp \left(\sum _{n=1}^{\infty }a_{n}{\frac {x^{n}}{n!}}\right)=\sum _{n=0}^{\infty }B_{n}(a_{1},\dots ,a_{n}){\frac {x^{n}}{n!}}}[image: {\displaystyle \exp \left(\sum _{n=1}^{\infty }a_{n}{\frac {x^{n}}{n!}}\right)=\sum _{n=0}^{\infty }B_{n}(a_{1},\dots ,a_{n}){\frac {x^{n}}{n!}}}] where B n ( a 1, …, a n) {\displaystyle B_{n}(a_{1},\ldots ,a_{n})}[image: {\displaystyle B_{n}(a_{1},\ldots ,a_{n})}] is the n {\displaystyle n}[image: {\displaystyle n}] th complete [Bell polynomial][15].

- The exponential formula can also be written as follows:

exp ⁡ ( ∑ n = 1 ∞ a n x n n) = ∑ n = 0 ∞ Z n ( a 1, …, a n) x n {\displaystyle \exp \left(\sum _{n=1}^{\infty }a_{n}{\frac {x^{n}}{n}}\right)=\sum _{n=0}^{\infty }Z_{n}(a_{1},\dots ,a_{n})x^{n}}[image: {\displaystyle \exp \left(\sum _{n=1}^{\infty }a_{n}{\frac {x^{n}}{n}}\right)=\sum _{n=0}^{\infty }Z_{n}(a_{1},\dots ,a_{n})x^{n}}] where Z n {\displaystyle Z_{n}}[image: {\displaystyle Z_{n}}] stands for the [cycle index][16] polynomial for the [symmetric group][17] S n {\displaystyle S_{n}}[image: {\displaystyle S_{n}}], defined as: Z n ( a 1, …, a n) = 1 n! ∑ σ ∈ S n a 1 σ 1 ⋯ a n σ n {\displaystyle Z_{n}(a_{1},\dots ,a_{n})={\frac {1}{n!}}\sum _{\sigma \in S_{n}}a_{1}^{\sigma _{1}}\cdots a_{n}^{\sigma _{n}}}[image: {\displaystyle Z_{n}(a_{1},\dots ,a_{n})={\frac {1}{n!}}\sum _{\sigma \in S_{n}}a_{1}^{\sigma _{1}}\cdots a_{n}^{\sigma _{n}}}] and σ j {\displaystyle \sigma _{j}}[image: {\displaystyle \sigma _{j}}] denotes the number of cycles of σ {\displaystyle \sigma }[image: {\displaystyle \sigma }] of size j ∈ { 1, …, n } {\displaystyle j\in \{1,\dots ,n\}}[image: {\displaystyle j\in \{1,\dots ,n\}}]. This is a consequence of the general relation between Z n {\displaystyle Z_{n}}[image: {\displaystyle Z_{n}}] and Bell polynomials: n! Z n ( a 1, …, a n) = B n ( 0! a 1, 1! a 2, …, ( n − 1)! a n). {\displaystyle n!Z_{n}(a_{1},\dots ,a_{n})=B_{n}(0!\,a_{1},1!\,a_{2},\dots ,(n-1)!\,a_{n}).}[image: {\displaystyle n!Z_{n}(a_{1},\dots ,a_{n})=B_{n}(0!\,a_{1},1!\,a_{2},\dots ,(n-1)!\,a_{n}).}]

## Combinatorial interpretation

[[edit][18]]

In combinatorial applications, the numbers a n {\displaystyle a_{n}}[image: {\displaystyle a_{n}}] count the number of some sort of "connected" structure on an n {\displaystyle n}[image: {\displaystyle n}] -point set, and the numbers b n {\displaystyle b_{n}}[image: {\displaystyle b_{n}}] count the number of (possibly disconnected) structures (see [combinatorial species][19]). The numbers b n / n! {\displaystyle b_{n}/n!}[image: {\displaystyle b_{n}/n!}] count the number of [isomorphism classes][20] of structures on n {\displaystyle n}[image: {\displaystyle n}] points, with each structure being weighted by the reciprocal of its [automorphism group][21], and the numbers a n / n! {\displaystyle a_{n}/n!}[image: {\displaystyle a_{n}/n!}] count isomorphism classes of connected structures in the same way.

## Examples

[[edit][22]]

- b 3 = B 3 ( a 1, a 2, a 3) = a 3 + 3 a 2 a 1 + a 1 3, {\displaystyle b_{3}=B_{3}(a_{1},a_{2},a_{3})=a_{3}+3a_{2}a_{1}+a_{1}^{3},}[image: {\displaystyle b_{3}=B_{3}(a_{1},a_{2},a_{3})=a_{3}+3a_{2}a_{1}+a_{1}^{3},}] because there is one partition of the set { 1, 2, 3 } {\displaystyle \{1,2,3\}}[image: {\displaystyle \{1,2,3\}}] that has a single block of size 3 {\displaystyle 3}[image: {\displaystyle 3}], there are three partitions of { 1, 2, 3 } {\displaystyle \{1,2,3\}}[image: {\displaystyle \{1,2,3\}}] that split it into a block of size 2 {\displaystyle 2}[image: {\displaystyle 2}] and a block of size 1 {\displaystyle 1}[image: {\displaystyle 1}], and there is one partition of { 1, 2, 3 } {\displaystyle \{1,2,3\}}[image: {\displaystyle \{1,2,3\}}] that splits it into three blocks of size 1 {\displaystyle 1}[image: {\displaystyle 1}]. This also follows from Z 3 ( a 1, a 2, a 3) = 1 6 ( 2 a 3 + 3 a 1 a 2 + a 1 3) = 1 6 B 3 ( a 1, a 2, 2 a 3) {\displaystyle Z_{3}(a_{1},a_{2},a_{3})={1 \over 6}(2a_{3}+3a_{1}a_{2}+a_{1}^{3})={1 \over 6}B_{3}(a_{1},a_{2},2a_{3})}[image: {\displaystyle Z_{3}(a_{1},a_{2},a_{3})={1 \over 6}(2a_{3}+3a_{1}a_{2}+a_{1}^{3})={1 \over 6}B_{3}(a_{1},a_{2},2a_{3})}], since one can write the [group][23] S 3 {\displaystyle S_{3}}[image: {\displaystyle S_{3}}] as S 3 = { ( 1) ( 2) ( 3), ( 1) ( 23), ( 2) ( 13), ( 3) ( 12), ( 123), ( 132) } {\displaystyle S_{3}=\{(1)(2)(3),(1)(23),(2)(13),(3)(12),(123),(132)\}}[image: {\displaystyle S_{3}=\{(1)(2)(3),(1)(23),(2)(13),(3)(12),(123),(132)\}}], using cyclic notation for [permutations][24].
- If b n = 2 n ( n − 1) / 2 {\displaystyle b_{n}=2^{n(n-1)/2}}[image: {\displaystyle b_{n}=2^{n(n-1)/2}}] is the number of [graphs][25] whose vertices are a given n {\displaystyle n}[image: {\displaystyle n}] -point set, then a n {\displaystyle a_{n}}[image: {\displaystyle a_{n}}] is the number of [connected graphs][26] whose vertices are a given n {\displaystyle n}[image: {\displaystyle n}] -point set.
- There are numerous variations of the previous example where the graph has certain properties: for example, if b n {\displaystyle b_{n}}[image: {\displaystyle b_{n}}] counts graphs without cycles, then a n {\displaystyle a_{n}}[image: {\displaystyle a_{n}}] counts [trees][27] (connected graphs without cycles).
- If b n {\displaystyle b_{n}}[image: {\displaystyle b_{n}}] counts [directed graphs][28] whose *edges*(rather than vertices) are a given n {\displaystyle n}[image: {\displaystyle n}] point set, then a n {\displaystyle a_{n}}[image: {\displaystyle a_{n}}] counts connected directed graphs with this edge set.
- In [quantum field theory][29] and [statistical mechanics][30], the [partition functions][31] Z {\displaystyle Z}[image: {\displaystyle Z}], or more generally [correlation functions][32], are given by a formal sum over [Feynman diagrams][33]. The exponential formula shows that ln ⁡ ( Z) {\displaystyle \ln(Z)}[image: {\displaystyle \ln(Z)}] can be written as a sum over connected Feynman diagrams, in terms of [connected correlation functions][34].

## See also

[[edit][35]]

- [Surjection of Fréchet spaces][36] – Characterization of surjectivity

## References

[[edit][37]]

- [Stanley, Richard P.][38] (1999), **[Enumerative combinatorics. Vol. 2][39], Cambridge Studies in Advanced Mathematics, vol. 62, [Cambridge University Press][40], [ISBN][41] [978-0-521-56069-6][42], [MR][43] [1676282][44], [ISBN][41] [978-0-521-78987-5][45] Chapter 5 page 3

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Exponential_formula&oldid=1352557308][46] "

[Categories][47]:

- [Exponentials][48]
- [Enumerative combinatorics][49]

Search

Exponential formula

3 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Combinatorics
[2]: https://en.wikipedia.org/wiki/Mathematics
[3]: https://en.wikipedia.org/wiki/Physics
[4]: https://en.wikipedia.org/wiki/Exponential_generating_function
[5]: https://en.wikipedia.org/wiki/Finite_set
[6]: https://en.wikipedia.org/wiki/Exponential_function
[7]: https://en.wikipedia.org/wiki/Power_series
[8]: https://en.wikipedia.org/wiki/Faà_di_Bruno's_formula
[9]: /w/index.php?title=Exponential_formula&amp;action=edit&amp;section=1
[10]: https://en.wikipedia.org/wiki/Algebra
[11]: https://en.wikipedia.org/wiki/Formal_power_series
[12]: https://en.wikipedia.org/wiki/Partition_of_a_set
[13]: https://en.wikipedia.org/wiki/Empty_product
[14]: /w/index.php?title=Exponential_formula&amp;action=edit&amp;section=2
[15]: https://en.wikipedia.org/wiki/Bell_polynomial
[16]: https://en.wikipedia.org/wiki/Cycle_index
[17]: https://en.wikipedia.org/wiki/Symmetric_group
[18]: /w/index.php?title=Exponential_formula&amp;action=edit&amp;section=3
[19]: https://en.wikipedia.org/wiki/Combinatorial_species
[20]: https://en.wikipedia.org/wiki/Isomorphism_class
[21]: https://en.wikipedia.org/wiki/Automorphism_group
[22]: /w/index.php?title=Exponential_formula&amp;action=edit&amp;section=4
[23]: https://en.wikipedia.org/wiki/Group_(mathematics)
[24]: https://en.wikipedia.org/wiki/Permutation
[25]: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
[26]: https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
[27]: https://en.wikipedia.org/wiki/Tree_(graph_theory)
[28]: https://en.wikipedia.org/wiki/Directed_graph
[29]: https://en.wikipedia.org/wiki/Quantum_field_theory
[30]: https://en.wikipedia.org/wiki/Statistical_mechanics
[31]: https://en.wikipedia.org/wiki/Partition_function_(mathematics)
[32]: https://en.wikipedia.org/wiki/Correlation_function
[33]: https://en.wikipedia.org/wiki/Feynman_diagram
[34]: https://en.wikipedia.org/wiki/Connected_correlation_function
[35]: /w/index.php?title=Exponential_formula&amp;action=edit&amp;section=5
[36]: https://en.wikipedia.org/wiki/Surjection_of_Fréchet_spaces
[37]: /w/index.php?title=Exponential_formula&amp;action=edit&amp;section=6
[38]: https://en.wikipedia.org/wiki/Richard_P._Stanley
[39]: http://www-math.mit.edu/~rstan/ec/
[40]: https://en.wikipedia.org/wiki/Cambridge_University_Press
[41]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[42]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-56069-6
[43]: https://en.wikipedia.org/wiki/MR_(identifier)
[44]: https://mathscinet.ams.org/mathscinet-getitem?mr=1676282
[45]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-78987-5
[46]: https://en.wikipedia.org/w/index.php?title=Exponential_formula&amp;oldid=1352557308
[47]: /wiki/Help:Category
[48]: /wiki/Category:Exponentials
[49]: /wiki/Category:Enumerative_combinatorics
