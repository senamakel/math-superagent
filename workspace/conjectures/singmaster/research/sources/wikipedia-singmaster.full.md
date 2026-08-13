<!-- source: https://en.wikipedia.org/wiki/Singmaster%27s_conjecture | converted from HTML -->

Singmaster's conjecture - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Conjecture in combinatorial number theory

Unsolved problem in mathematics

Is there some constant *N*such that every entry (apart from 1) of Pascal's triangle appears fewer than *N*times?

[More unsolved problems in mathematics][1]

**Singmaster's conjecture**is a [conjecture][2] in [combinatorial number theory][3], named after the British mathematician [David Singmaster][4] who proposed it in 1971. It says that there is a finite [upper bound][5] on the [multiplicities][6] of entries in [Pascal's triangle][7] (other than the number 1, which appears infinitely many times). It is clear that the only number that appears infinitely many times in [Pascal's triangle][7] is 1, because any other number *x*can appear only within the first *x*+ 1 rows of the triangle.

## Statement

[[edit][8]]

Let *N*(*a*) be the number of times the number *a*> 1 appears in Pascal's triangle. In [big O notation][9], the conjecture is:

N ( a) = O ( 1). {\displaystyle N(a)=O(1).}[image: {\displaystyle N(a)=O(1).}]

In other words, there exists a [natural number][10] M {\textstyle M}[image: {\textstyle M}] such that:

N ( a) ≤ M f o r a l l a. {\displaystyle N(a)\leq M\ \qquad ~{\mathsf {\ for\ all\ }}~\quad a.}[image: {\displaystyle N(a)\leq M\ \qquad ~{\mathsf {\ for\ all\ }}~\quad a.}]

## Known bound

[[edit][11]]

Singmaster (1971) showed that

N ( a) = O ( log ⁡ a). {\displaystyle N(a)=O(\log a).}[image: {\displaystyle N(a)=O(\log a).}]

Abbott, [Erdős][12], and Hanson (1974) (see References) refined the estimate to:

N ( a) = O ( log ⁡ a log ⁡ log ⁡ a). {\displaystyle N(a)=O\left({\frac {\log a}{\log \log a}}\right).}[image: {\displaystyle N(a)=O\left({\frac {\log a}{\log \log a}}\right).}]

The best currently known (unconditional) bound is

N ( a) = O ( ( log ⁡ a) ( log ⁡ log ⁡ log ⁡ a) ( log ⁡ log ⁡ a) 3), {\displaystyle N(a)=O\left({\frac {(\log a)(\log \log \log a)}{(\log \log a)^{3}}}\right),}[image: {\displaystyle N(a)=O\left({\frac {(\log a)(\log \log \log a)}{(\log \log a)^{3}}}\right),}]

and is due to [Kane][13] (2007). Abbott, Erdős, and Hanson note that, conditional on [Cramér's conjecture][14] on gaps between consecutive primes,

N ( a) = O ( ( log ⁡ a) 2 / 3 + ε) {\displaystyle N(a)=O\left((\log a)^{2/3+\varepsilon }\right)}[image: {\displaystyle N(a)=O\left((\log a)^{2/3+\varepsilon }\right)}]

holds for every 0 "}}'> 0}"> ε > 0 {\displaystyle \varepsilon >0} 0}"/>.

Singmaster (1975) showed that the [Diophantine equation][15]

( n + 1 k + 1) = ( n k + 2) {\displaystyle {n+1 \choose k+1}={n \choose k+2}}[image: {\displaystyle {n+1 \choose k+1}={n \choose k+2}}]

has infinitely many solutions for the two variables *n*, *k*. It follows that there are infinitely many triangle entries of multiplicity at least 6: For any non-negative *i*, a number *a*with six appearances in Pascal's triangle is given by either of the above two expressions with

n = F 2 i + 2 F 2 i + 3 − 1, {\displaystyle n=F_{2i+2}F_{2i+3}-1,}[image: {\displaystyle n=F_{2i+2}F_{2i+3}-1,}] k = F 2 i F 2 i + 3 − 1, {\displaystyle k=F_{2i}F_{2i+3}-1,}[image: {\displaystyle k=F_{2i}F_{2i+3}-1,}]

where *F**j*is the *j*th [Fibonacci number][16] (indexed according to the convention that *F*0 = 0 and *F*1 = 1). The above two expressions locate two of the appearances; two others appear symmetrically in the triangle with respect to those two; and the other two appearances are at ( a 1) {\displaystyle {a \choose 1}}[image: {\displaystyle {a \choose 1}}] and ( a a − 1). {\displaystyle {a \choose a-1}.}[image: {\displaystyle {a \choose a-1}.}]

## Elementary examples

[[edit][17]]

- 2 appears just once; all larger positive integers appear more than once;
- 3, 4, 5 each appear two times; infinitely many numbers appear exactly twice;
- all odd [prime numbers][18] appear two times;
- 6 appears three times, as do all [central binomial coefficients][19] except for 1 and 2;
(it is in principle not excluded that such a coefficient would appear five, seven, or more times, but no such example is known)
- all numbers of the form ( p 2) {\displaystyle {p \choose 2}}[image: {\displaystyle {p \choose 2}}] for prime 3"}}'> 3}"> p > 3 {\displaystyle p>3} 3}"/> appear four times;
- Infinitely many appear exactly six times, including each of the following:

120 = ( 120 1) = ( 120 119) = ( 16 2) = ( 16 14) = ( 10 3) = ( 10 7) {\displaystyle 120={120 \choose 1}={120 \choose 119}={16 \choose 2}={16 \choose 14}={10 \choose 3}={10 \choose 7}}[image: {\displaystyle 120={120 \choose 1}={120 \choose 119}={16 \choose 2}={16 \choose 14}={10 \choose 3}={10 \choose 7}}]

210 = ( 210 1) = ( 210 209) = ( 21 2) = ( 21 19) = ( 10 4) = ( 10 6) {\displaystyle 210={210 \choose 1}={210 \choose 209}={21 \choose 2}={21 \choose 19}={10 \choose 4}={10 \choose 6}}[image: {\displaystyle 210={210 \choose 1}={210 \choose 209}={21 \choose 2}={21 \choose 19}={10 \choose 4}={10 \choose 6}}]

1540 = ( 1540 1) = ( 1540 1539) = ( 56 2) = ( 56 54) = ( 22 3) = ( 22 19) {\displaystyle 1540={1540 \choose 1}={1540 \choose 1539}={56 \choose 2}={56 \choose 54}={22 \choose 3}={22 \choose 19}}[image: {\displaystyle 1540={1540 \choose 1}={1540 \choose 1539}={56 \choose 2}={56 \choose 54}={22 \choose 3}={22 \choose 19}}]

7140 = ( 7140 1) = ( 7140 7139) = ( 120 2) = ( 120 118) = ( 36 3) = ( 36 33) {\displaystyle 7140={7140 \choose 1}={7140 \choose 7139}={120 \choose 2}={120 \choose 118}={36 \choose 3}={36 \choose 33}}[image: {\displaystyle 7140={7140 \choose 1}={7140 \choose 7139}={120 \choose 2}={120 \choose 118}={36 \choose 3}={36 \choose 33}}]

11628 = ( 11628 1) = ( 11628 11627) = ( 153 2) = ( 153 151) = ( 19 5) = ( 19 14) {\displaystyle 11628={11628 \choose 1}={11628 \choose 11627}={153 \choose 2}={153 \choose 151}={19 \choose 5}={19 \choose 14}}[image: {\displaystyle 11628={11628 \choose 1}={11628 \choose 11627}={153 \choose 2}={153 \choose 151}={19 \choose 5}={19 \choose 14}}]

24310 = ( 24310 1) = ( 24310 24309) = ( 221 2) = ( 221 219) = ( 17 8) = ( 17 9) {\displaystyle 24310={24310 \choose 1}={24310 \choose 24309}={221 \choose 2}={221 \choose 219}={17 \choose 8}={17 \choose 9}}[image: {\displaystyle 24310={24310 \choose 1}={24310 \choose 24309}={221 \choose 2}={221 \choose 219}={17 \choose 8}={17 \choose 9}}] The next number in Singmaster's infinite family (given in terms of Fibonacci numbers), and the next smallest number to occur six or more times, is a = 61218182743304701891431482520 {\displaystyle a=61218182743304701891431482520}[image: {\displaystyle a=61218182743304701891431482520}]: [1] a = ( a 1) = ( a a − 1) = ( 104 39) = ( 104 65) = ( 103 40) = ( 103 63) {\displaystyle a={a \choose 1}={a \choose a-1}={104 \choose 39}={104 \choose 65}={103 \choose 40}={103 \choose 63}}[image: {\displaystyle a={a \choose 1}={a \choose a-1}={104 \choose 39}={104 \choose 65}={103 \choose 40}={103 \choose 63}}]

- The smallest number to appear eight times – indeed, the only number known to appear eight times – is 3003, which is also a member of Singmaster's infinite family of numbers with multiplicity at least 6:

3003 = ( 3003 1) = ( 78 2) = ( 15 5) = ( 14 6) = ( 14 8) = ( 15 10) = ( 78 76) = ( 3003 3002) {\displaystyle 3003={3003 \choose 1}={78 \choose 2}={15 \choose 5}={14 \choose 6}={14 \choose 8}={15 \choose 10}={78 \choose 76}={3003 \choose 3002}}[image: {\displaystyle 3003={3003 \choose 1}={78 \choose 2}={15 \choose 5}={14 \choose 6}={14 \choose 8}={15 \choose 10}={78 \choose 76}={3003 \choose 3002}}] It is not known whether infinitely many numbers appear eight times, nor even whether any other numbers than 3003 appear eight times.

The number of times *n*appears in Pascal's triangle is

∞, 1, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 2, 4, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 4, 2, 2, ... (sequence [A003016][20] in the [OEIS][21])

By Abbott, Erdős, and Hanson (1974), the number of integers no larger than *x*that appear more than twice in Pascal's triangle is O ( x 1 / 2) {\displaystyle O(x^{1/2})}[image: {\displaystyle O(x^{1/2})}].

The smallest natural number greater than 1 that appears (at least) *n*times in Pascal's triangle is

2, 3, 6, 10, 120, 120, 3003, 3003, ... (sequence [A062527][22] in the [OEIS][21])

The numbers which appear at least five times in Pascal's triangle are

1, 120, 210, 1540, 3003, 7140, 11628, 24310, 61218182743304701891431482520, ... (sequence [A003015][23] in the [OEIS][21])

Of these, the ones in Singmaster's infinite family are

1, 3003, 61218182743304701891431482520, ... (sequence [A090162][24] in the [OEIS][21])

## Open questions

[[edit][25]]

It is not known whether any number appears more than eight times, nor whether any number besides 3003 appears that many times. The conjectured finite upper bound could be as small as 8, but Singmaster thought it might be 10 or 12. It is also unknown whether any numbers appear exactly five or seven times.

## See also

[[edit][26]]

- [Binomial coefficient][27]

## References

[[edit][28]]

1. ↑ De Weger, Benjamin M.M. (August 1995). ["Equal binomial coefficients: some elementary considerations"][29] (PDF). *Econometric Institute Research Papers*: 3. Retrieved 6 September 2024.

- [Singmaster, D.][4] (1971), "Research Problems: How often does an integer occur as a binomial coefficient?", *[American Mathematical Monthly][30]*, **78**(4): 385– 386, [doi][31]: [10.2307/2316907][32], [JSTOR][33] [2316907][34], [MR][35] [1536288][36].

- [Singmaster, D.][4] (1975), ["Repeated binomial coefficients and Fibonacci numbers"][37] (PDF), *[Fibonacci Quarterly][38]*, **13**(4): 295– 298, [doi][31]: [10.1080/00150517.1975.12430610][39], [MR][35] [0412095][40].

- Abbott, H. L.; [Erdős, P.][12]; Hanson, D. (1974), "On the number of times an integer occurs as a binomial coefficient", *[American Mathematical Monthly][30]*, **81**(3): 256– 261, [doi][31]: [10.2307/2319526][41], [JSTOR][33] [2319526][42], [MR][35] [0335283][43].

- [Kane, Daniel M.][13] (2007), **["Improved bounds on the number of ways of expressing t as a binomial coefficient"][44] (PDF), *[INTEGERS: The Electronic Journal of Combinatorial Number Theory][45]*, **7**: #A53, [MR][35] [2373115][46].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Singmaster%27s_conjecture&oldid=1363330357][47] "

[Categories][48]:

- [Combinatorics][49]
- [Factorial and binomial topics][50]
- [Triangles of numbers][51]
- [Conjectures][52]
- [Unsolved problems in number theory][53]

Hidden categories:

- [Articles with short description][54]
- [Short description matches Wikidata][55]

Search

Singmaster's conjecture

8 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[2]: https://en.wikipedia.org/wiki/Conjecture
[3]: https://en.wikipedia.org/wiki/Combinatorial_number_theory
[4]: https://en.wikipedia.org/wiki/David_Singmaster
[5]: https://en.wikipedia.org/wiki/Upper_bound
[6]: https://en.wikipedia.org/wiki/Multiplicity_(mathematics)
[7]: https://en.wikipedia.org/wiki/Pascal's_triangle
[8]: /w/index.php?title=Singmaster%27s_conjecture&amp;action=edit&amp;section=1
[9]: https://en.wikipedia.org/wiki/Big_O_notation
[10]: https://en.wikipedia.org/wiki/Natural_number
[11]: /w/index.php?title=Singmaster%27s_conjecture&amp;action=edit&amp;section=2
[12]: https://en.wikipedia.org/wiki/Paul_Erdős
[13]: https://en.wikipedia.org/wiki/Daniel_Kane_(mathematician)
[14]: https://en.wikipedia.org/wiki/Cramér's_conjecture
[15]: https://en.wikipedia.org/wiki/Diophantine_equation
[16]: https://en.wikipedia.org/wiki/Fibonacci_number
[17]: /w/index.php?title=Singmaster%27s_conjecture&amp;action=edit&amp;section=3
[18]: https://en.wikipedia.org/wiki/Prime_number
[19]: https://en.wikipedia.org/wiki/Central_binomial_coefficient
[20]: //oeis.org/A003016
[21]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[22]: //oeis.org/A062527
[23]: //oeis.org/A003015
[24]: //oeis.org/A090162
[25]: /w/index.php?title=Singmaster%27s_conjecture&amp;action=edit&amp;section=4
[26]: /w/index.php?title=Singmaster%27s_conjecture&amp;action=edit&amp;section=5
[27]: https://en.wikipedia.org/wiki/Binomial_coefficient
[28]: /w/index.php?title=Singmaster%27s_conjecture&amp;action=edit&amp;section=6
[29]: https://repub.eur.nl/pub/1356/1356_ps.pdf
[30]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[31]: https://en.wikipedia.org/wiki/Doi_(identifier)
[32]: https://doi.org/10.2307%2F2316907
[33]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[34]: https://www.jstor.org/stable/2316907
[35]: https://en.wikipedia.org/wiki/MR_(identifier)
[36]: https://mathscinet.ams.org/mathscinet-getitem?mr=1536288
[37]: http://www.fq.math.ca/Scanned/13-4/singmaster.pdf
[38]: https://en.wikipedia.org/wiki/Fibonacci_Quarterly
[39]: https://doi.org/10.1080%2F00150517.1975.12430610
[40]: https://mathscinet.ams.org/mathscinet-getitem?mr=0412095
[41]: https://doi.org/10.2307%2F2319526
[42]: https://www.jstor.org/stable/2319526
[43]: https://mathscinet.ams.org/mathscinet-getitem?mr=0335283
[44]: http://www.emis.de/journals/INTEGERS/papers/h53/h53.pdf
[45]: https://en.wikipedia.org/wiki/INTEGERS:_The_Electronic_Journal_of_Combinatorial_Number_Theory?action=edit&amp;redlink=1
[46]: https://mathscinet.ams.org/mathscinet-getitem?mr=2373115
[47]: https://en.wikipedia.org/w/index.php?title=Singmaster%27s_conjecture&amp;oldid=1363330357
[48]: /wiki/Help:Category
[49]: /wiki/Category:Combinatorics
[50]: /wiki/Category:Factorial_and_binomial_topics
[51]: /wiki/Category:Triangles_of_numbers
[52]: /wiki/Category:Conjectures
[53]: /wiki/Category:Unsolved_problems_in_number_theory
[54]: /wiki/Category:Articles_with_short_description
[55]: /wiki/Category:Short_description_matches_Wikidata
