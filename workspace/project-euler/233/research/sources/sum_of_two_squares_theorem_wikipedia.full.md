<!-- source: https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem | converted from HTML -->

Sum of two squares theorem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Characterization by prime factors of sums of two squares

[1] Integers satisfying the sum of two squares theorem are squares of possible distances between integer lattice points; values up to 100 are shown, with

• | Squares (and thus integer distances) in red, and |

• | Non-unique representations (up to rotation and reflection) bolded |

In [number theory][2], the **sum of two squares theorem**relates the [prime decomposition][3] of any [integer][4] 1"}},"i":0}}]}'> n > 1 to whether it can be written as a sum of two [squares][5], such that n = a 2 + b 2 for some integers a, b. [1]

An integer greater than one can be written as a sum of two squares [if and only if][6] its [prime decomposition][3] contains no factor p*k*, where [prime][7] p ≡ 3 ( mod 4) {\displaystyle p\equiv 3{\pmod {4}}}[image: {\displaystyle p\equiv 3{\pmod {4}}}] and *k*is [odd][8].

In writing a number as a sum of two squares, it is allowed for one of the squares to be zero, or for both of them to be equal to each other, so all squares and all doubles of squares are included in the numbers that can be represented in this way. This theorem supplements [Fermat's theorem on sums of two squares][9] which says when a [prime number][7] can be written as a sum of two squares, in that it also covers the case for [composite numbers][10].

A number may have multiple representations as a sum of two squares, counted by the [sum of squares function][11]; for instance, every [Pythagorean triple][12] a 2 + b 2 = c 2 {\displaystyle a^{2}+b^{2}=c^{2}}[image: {\displaystyle a^{2}+b^{2}=c^{2}}] gives a second representation for c 2 {\displaystyle c^{2}}[image: {\displaystyle c^{2}}] beyond the trivial representation c 2 + 0 2 {\displaystyle c^{2}+0^{2}}[image: {\displaystyle c^{2}+0^{2}}].

## Examples

[[edit][13]]

The prime decomposition of the number 2450 is given by 2450 = 2**·**5 2**·**7 2. Of the primes occurring in this decomposition, 2, 5, and 7, only 7 is congruent to 3 modulo 4. Its exponent in the decomposition, 2, is [even][8]. Therefore, the theorem states that it is expressible as the sum of two squares. Indeed, 2450 = 7 2 + 49 2.

The prime decomposition of the number 3430 is 2**·**5**·**7 3. This time, the exponent of 7 in the decomposition is 3, an odd number. So 3430 cannot be written as the sum of two squares.

## Representable numbers

[[edit][14]]

The numbers that can be represented as the sums of two squares form the [integer sequence][15] [2]

0, 1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25, 26, 29, 32, ...

They form the set of all [norms][16] of [Gaussian integers][17]; [2] their square roots form the set of all lengths of [line segments][18] between pairs of points in the two-dimensional [integer lattice][19].

The number of representable numbers in the range from 0 to any number n {\displaystyle n}[image: {\displaystyle n}] is proportional to n log ⁡ n {\displaystyle {\frac {n}{\sqrt {\log n}}}}[image: {\displaystyle {\frac {n}{\sqrt {\log n}}}}], with a limiting constant of proportionality given by the [Landau–Ramanujan constant][20], approximately 0.764. [3]

The product of any two representable numbers is another representable number. Its representation can be derived from representations of its two factors, using the [Brahmagupta–Fibonacci identity][21].

## Jacobi's two-square theorem

[[edit][22]]

n</math> as <math>d(n)</math>, and write <math>d_a(n)</math> for the number of those divisors with <math>d \\equiv a \\pmod 4</math>. Let <math>n = 2^f p_1 ^{r_1} p_2 ^ {r_2} \\cdots q_1^{s_1} q_2^{s_2} \\cdots </math> where <math>p_i \\equiv 1 \\pmod 4, \\ q_i \\equiv 3 \\pmod 4</math>.\n\nLet <math>r_2(n)</math> be the number of ways <math>n</math> can be represented as the sum of two squares.\n\nThen, <math>r_2(n) = 0</math> if any of the exponents <math>s_j</math> are odd. If all <math>s_j</math> are even, then <math display=\"block\">r_2(n) = 4 d (p_1^{r_1} p_2^{r_2} \\cdots ) = 4(d_1(n) - d_3(n)) </math>"},"name":{"wt":"Two-square theorem"}},"i":0}}]}'>

**Two-square theorem**— Denote the [number of divisors][23] of n {\displaystyle n}[image: {\displaystyle n}] as d ( n) {\displaystyle d(n)}[image: {\displaystyle d(n)}], and write d a ( n) {\displaystyle d_{a}(n)}[image: {\displaystyle d_{a}(n)}] for the number of those divisors with d ≡ a ( mod 4) {\displaystyle d\equiv a{\pmod {4}}}[image: {\displaystyle d\equiv a{\pmod {4}}}]. Let n = 2 f p 1 r 1 p 2 r 2 ⋯ q 1 s 1 q 2 s 2 ⋯ {\displaystyle n=2^{f}p_{1}^{r_{1}}p_{2}^{r_{2}}\cdots q_{1}^{s_{1}}q_{2}^{s_{2}}\cdots }[image: {\displaystyle n=2^{f}p_{1}^{r_{1}}p_{2}^{r_{2}}\cdots q_{1}^{s_{1}}q_{2}^{s_{2}}\cdots }] where p i ≡ 1 ( mod 4), q i ≡ 3 ( mod 4) {\displaystyle p_{i}\equiv 1{\pmod {4}},\ q_{i}\equiv 3{\pmod {4}}}[image: {\displaystyle p_{i}\equiv 1{\pmod {4}},\ q_{i}\equiv 3{\pmod {4}}}].

Let r 2 ( n) {\displaystyle r_{2}(n)}[image: {\displaystyle r_{2}(n)}] be the number of ways n {\displaystyle n}[image: {\displaystyle n}] can be represented as the sum of two squares.

Then, r 2 ( n) = 0 {\displaystyle r_{2}(n)=0}[image: {\displaystyle r_{2}(n)=0}] if any of the exponents s j {\displaystyle s_{j}}[image: {\displaystyle s_{j}}] are odd. If all s j {\displaystyle s_{j}}[image: {\displaystyle s_{j}}] are even, then r 2 ( n) = 4 d ( p 1 r 1 p 2 r 2 ⋯) = 4 ( d 1 ( n) − d 3 ( n)) {\displaystyle r_{2}(n)=4d(p_{1}^{r_{1}}p_{2}^{r_{2}}\cdots )=4(d_{1}(n)-d_{3}(n))}[image: {\displaystyle r_{2}(n)=4d(p_{1}^{r_{1}}p_{2}^{r_{2}}\cdots )=4(d_{1}(n)-d_{3}(n))}]

Proved by Gauss using [quadratic forms][24] and Jacobi using [elliptic functions][25]. [4] An elementary proof is based on the [unique factorization][26] of the [Gaussian integers][17]. [4] Hirschhorn gives a short proof derived from the [Jacobi triple product][27]. [5]

## See also

[[edit][28]]

- [Legendre's three-square theorem][29]
- [Lagrange's four-square theorem][30]
- [Sum of squares function][11]
- [Brahmagupta–Fibonacci identity][21]

## References

[[edit][31]]

1. ↑ [Dudley, Underwood][32] (1969). "Sums of Two Squares". *Elementary Number Theory*. W.H. Freeman and Company. pp. 135– 139.
2. 1 2 [Sloane, N. J. A.][33] (ed.). ["Sequence A001481 (Numbers that are the sum of 2 squares)"][34]. *The [On-Line Encyclopedia of Integer Sequences][35]*. OEIS Foundation.
3. ↑ Rebák, Örs (2020). "Generalization of a Ramanujan identity". *[The American Mathematical Monthly][36]*. **127**(1): 80– 83. [arXiv][37]: [1612.08307][38]. [doi][39]: [10.1080/00029890.2020.1668716][40]. [MR][41] [4043992][42].
4. 1 2 Grosswald, Emil (1985). *Representations of integers as sums of squares*. New York Berlin Heidelberg [etc.]: Springer. pp. 15– 19. [ISBN][43] [978-3-540-96126-0][44].
5. ↑ Hirschhorn, Michael (1985). ["A simple proof of Jacobi's two-square theorem"][45] (PDF). *Amer. Math. Monthly*. **92**(8): 579– 580. [doi][39]: [10.1080/00029890.1985.11971686][46].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Sum_of_two_squares_theorem&oldid=1319561489][47] "

[Categories][48]:

- [Additive number theory][49]
- [Squares in number theory][50]
- [Theorems in number theory][51]

Hidden categories:

- [Articles with short description][52]
- [Short description is different from Wikidata][53]

Search

Sum of two squares theorem

5 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Sum_of_two_squares_theorem.svg
[2]: https://en.wikipedia.org/wiki/Number_theory
[3]: https://en.wikipedia.org/wiki/Prime_decomposition
[4]: https://en.wikipedia.org/wiki/Integer
[5]: https://en.wikipedia.org/wiki/Square_number
[6]: https://en.wikipedia.org/wiki/If_and_only_if
[7]: https://en.wikipedia.org/wiki/Prime_number
[8]: https://en.wikipedia.org/wiki/Parity_(mathematics)
[9]: https://en.wikipedia.org/wiki/Fermat's_theorem_on_sums_of_two_squares
[10]: https://en.wikipedia.org/wiki/Composite_number
[11]: https://en.wikipedia.org/wiki/Sum_of_squares_function
[12]: https://en.wikipedia.org/wiki/Pythagorean_triple
[13]: /w/index.php?title=Sum_of_two_squares_theorem&amp;action=edit&amp;section=1
[14]: /w/index.php?title=Sum_of_two_squares_theorem&amp;action=edit&amp;section=2
[15]: https://en.wikipedia.org/wiki/Integer_sequence
[16]: https://en.wikipedia.org/wiki/Field_norm
[17]: https://en.wikipedia.org/wiki/Gaussian_integer
[18]: https://en.wikipedia.org/wiki/Line_segment
[19]: https://en.wikipedia.org/wiki/Integer_lattice
[20]: https://en.wikipedia.org/wiki/Landau–Ramanujan_constant
[21]: https://en.wikipedia.org/wiki/Brahmagupta–Fibonacci_identity
[22]: /w/index.php?title=Sum_of_two_squares_theorem&amp;action=edit&amp;section=3
[23]: https://en.wikipedia.org/wiki/Number_of_divisors
[24]: https://en.wikipedia.org/wiki/Quadratic_form
[25]: https://en.wikipedia.org/wiki/Elliptic_function
[26]: https://en.wikipedia.org/wiki/Unique_factorization_domain
[27]: https://en.wikipedia.org/wiki/Jacobi_triple_product
[28]: /w/index.php?title=Sum_of_two_squares_theorem&amp;action=edit&amp;section=4
[29]: https://en.wikipedia.org/wiki/Legendre's_three-square_theorem
[30]: https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem
[31]: /w/index.php?title=Sum_of_two_squares_theorem&amp;action=edit&amp;section=5
[32]: https://en.wikipedia.org/wiki/Underwood_Dudley
[33]: https://en.wikipedia.org/wiki/Neil_Sloane
[34]: https://oeis.org/A001481
[35]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[36]: https://en.wikipedia.org/wiki/The_American_Mathematical_Monthly
[37]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[38]: https://arxiv.org/pdf/1612.08307
[39]: https://en.wikipedia.org/wiki/Doi_(identifier)
[40]: https://doi.org/10.1080%2F00029890.2020.1668716
[41]: https://en.wikipedia.org/wiki/MR_(identifier)
[42]: https://mathscinet.ams.org/mathscinet-getitem?mr=4043992
[43]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[44]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-96126-0
[45]: https://web.maths.unsw.edu.au/~mikeh/webpapers/paper21.pdf
[46]: https://doi.org/10.1080%2F00029890.1985.11971686
[47]: https://en.wikipedia.org/w/index.php?title=Sum_of_two_squares_theorem&amp;oldid=1319561489
[48]: /wiki/Help:Category
[49]: /wiki/Category:Additive_number_theory
[50]: /wiki/Category:Squares_in_number_theory
[51]: /wiki/Category:Theorems_in_number_theory
[52]: /wiki/Category:Articles_with_short_description
[53]: /wiki/Category:Short_description_is_different_from_Wikidata
