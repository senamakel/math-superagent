<!-- source: https://encyclopediaofmath.org/wiki/Abundant_number | converted from HTML -->

Abundant number - Encyclopedia of Mathematics

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

# Abundant number

From Encyclopedia of Mathematics

Jump to: navigation, search

Let $\sigma ( n )$ denote the sum of the distinct divisors of an integer $n$ (cf. [Divisor][23]; [Number of divisors][24]). The integer $n$ is called abundant if $\sigma ( n ) > 2 n$; deficient if $\sigma ( n ) < 2 n$; and perfect if $\sigma ( n ) = 2 n$ (cf. also [Perfect number][25]). Note that some authors call a number $n$ abundant if $\sigma ( n ) \geq 2 n$. Clearly, these numbers are in fact perfect or abundant (i.e. "non-deficient") numbers.

In [a5], L.E. Dickson gives details on the early history of abundant numbers. G. Nicomachus (about 100) separated the even numbers into abundant, deficient and perfect, and dwelled on the ethical importance of the three types. A.M.S. Boethius (around 500), in a Latin exposition of the arithmetic of Nicomachus, stated that perfect numbers are rare, while abundant ( "superfluous" ) and deficient ( "diminutos" ) numbers are found to an unlimited extent. N. Jordanus (around 1236) stated that every multiple of a perfect or abundant number is abundant. He attempted to prove the erroneous statement that all abundant numbers are even. C. Bovillus (around 1509) corrected this statement, by citing $45045 = 5.7.9 .11 .13$ and its multiples. Bachet de Méziriac (around 1600) gave a proof that $2 ^ { n } p$ is perfect if $p = 2 ^ { n + 1 } - 1$ is a [prime number][26], and abundant if $p$ is composite. He remarked that the odd number $945$ is abundant. J. Broscius (around 1652) showed that there are only $21$ abundant numbers between $10$ and $100$ and all of them are even; the only odd abundant number less than $1000$ is $945$. (The statement by E. Lucas (1891) that $3 ^ { 3 } .5 .7.9$ is the smallest odd abundant number is probably a misprint for $945 = 3 ^ { 3 } .5 .7$.) Ch. de Neuveglise (1700) proved that the products $3 \cdot 4 , \ldots , 8 \cdot 9$ of two consecutive numbers are abundant, and all multiplies of $6$ or an abundant number are abundant. J. Struve (1808) considered abundant numbers which are products $a b c$ of three distinct prime numbers in ascending order; for $a = 2$, $b = 3$, $c = 5$ or $7$, and for $a = 2$, $b = 5$, $c = 7$, $abcd$ is abundant for any prime number $d > c$. Of the numbers $\leq 1000$, $52$ are abundant.

Dickson (1913, [a6]) called a non-deficient number primitive abundant if it is not a multiple of a smaller non-deficient number. He proved that there are only a finite number of primitive non-deficient numbers having a given number of distinct odd prime factors and a given number of factors $2$.

There is no odd abundant number with fewer than three distinct prime factors, the primitive ones with three are

\begin{equation*} 3 ^ { 3 } .5 .7,3 ^ { 2 } .5 ^ { 2 } .7,3 ^ { 2 } .5 .7 ^ { 2 } \end{equation*}

\begin{equation*} 3 ^ { 2 } \cdot 5 ^ { 2 } \cdot 11,\; 3 ^ { 5 } \cdot 5 ^ { 2 } \cdot 13,\; 3 ^ { 4 } \cdot 5 ^ { 2 } \cdot 13 ^ { 2 } ,\; 3 ^ { 3 } \cdot 5 ^ { 3 } \cdot 13 ^ { 2 }. \end{equation*}

He gave also a table of all even abundant numbers $< 6232$. Dickson's result was a starting point for much further research. In 1949 and 1968, H.N. Shapiro ( [a20], [a21]) proved the following result. Let $\alpha$ be a rational number. A necessary and sufficient condition that there exist infinitely many primitive $\alpha$-abundant numbers (i.e. $\sigma ( n ) / n \geq \alpha$ but $\sigma ( d ) / d < \alpha$ for all $d | n$, $d < n$) with $k$ distinct prime factors is that $\alpha$ has a representation

\begin{equation*} \alpha = \frac { b \sigma ( a ) } { a \varphi ( b ) } \end{equation*}

with $\operatorname { GCD } ( a , b ) = 1$, $b > 1$, where $\omega ( a ) + \omega ( b ) < k$. Here, $\varphi$ is the Euler [totient function][27] and $\omega ( a )$ denotes the number of distinct prime factors of $a$.

In 1933, F. Behrend, H. Davenport and S. Chowla [a4] showed that the density of non-deficient numbers exists and is positive. This result follows also from a theorem of P. Erdős [a7] stating that the sum of reciprocals of primitive abundant numbers converges. Let

\begin{equation*} A _ { \alpha } ( x ) = \operatorname { card } \{ n \leq x :\ \text{primitive} \ \alpha\text{-abundant} \} \end{equation*}

be the counting function of primitive $\alpha$-abundant numbers. Erdős proved that [a10]

\begin{equation*} A _ { \alpha } ( x ) = o \left( \frac { x } { \operatorname { log } x } \right) \end{equation*}

and that [a8]

\begin{equation*} x \operatorname { exp } ( - 8 ( \operatorname { log } x\operatorname { log } \operatorname { log } x ) ^ { 1 / 2 } ) < A _ { 2 } ( x ) < \end{equation*}

\begin{equation*} < x \operatorname { exp } ( - \frac { 1 } { 25 } \left( \operatorname { log } x \operatorname { log } \operatorname { log } x ) ^ { 1 / 2 } \right). \end{equation*}

This was sharpened successively by A. Ivić [a13], with $- ( \sqrt { 6 } + \varepsilon )$ in place of $- 8$ and $- ( 1 / \sqrt { 12 } - \varepsilon )$ in place of $- 1 / 25$; and by M.R. Avidon [a2], who considered $- ( \sqrt { 2 } + \varepsilon )$ in place of $- ( \sqrt { 6 } + \varepsilon )$, and $- ( 1 - \varepsilon )$ in place of $- ( 1 / \sqrt { 12 } - \varepsilon )$.

L. Alaoglu and Erdős [a1] call a number $n$ superabundant if

\begin{equation*} \frac { \sigma ( n ) } { n } > \frac { \sigma ( m ) } { m } \end{equation*}

for all $1 \leq m < n$. Let $Q ( x )$ be the counting function of superabundant numbers. For two consecutive superabundant numbers $n$, $n ^ { \prime }$ they prove that

\begin{equation*} \frac { n ^ { \prime } } { n } < 1 + C \frac { ( \operatorname { log } \operatorname { log } n ) ^ { 2 } } { \operatorname { log } n } , C = \text { const } > 0, \end{equation*}

and this was sharpened to $n ^ { \prime } / n \leq 1 + 1 / \sqrt { \operatorname { log } n }$ for an infinity of $n$ by J.-L. Nicolas [a16]. Alaoglu and Erdős showed that $Q ( x ) \geq C \operatorname { log } x \operatorname { log } \operatorname { log } x / ( \operatorname { log } \operatorname { log } \operatorname { log } x ) ^ { 2 }$, while Erdős and Nicolas [a11] demonstrated that $\lim \inf _{x \rightarrow \infty} \operatorname { log } Q ( x ) / \operatorname { log } \operatorname { log } x \geq 5 / 48$. Alaoglu and Erdős [a1] introduced also the notion of highly abundant number, a number $n$ with the property that $\sigma ( n ) > \sigma ( m )$ for all $m < n$. For the counting function $H ( x )$ of these numbers one has $H ( x ) > ( 1 - \varepsilon ) ( \operatorname { log } x ) ^ { 2 }$ for all $\varepsilon > 0$ and large $x$; if $n$ is highly abundant, then the largest prime factor of $n$ is less than $C \log n ( \log \log n)^3$.

Erdős and Nicolas [a11] call a number $n$ cube-free superabundant if $m < n$ implies $\sigma ^ { 0 } ( m ) / m < \sigma ^ { 0 } ( n ) / n$, where $\sigma ^ { 0 } ( p ^ { \alpha } ) = \sigma ( p ^ { \alpha } )$ for $\alpha \leq 2$ and $\sigma ^ { 0 } ( p ^ { \alpha } ) = 0$ for $\alpha \geq 3$ (with $p$ a prime number and $\alpha$ a positive integer). They prove that if $n ^ { 0 }$ and $n^{\prime 0 }$ are two consecutive cube-free superabundant numbers, then $\operatorname{limsup} n ^ { \prime 0 } / n ^ { 0 } \geq 2 ^ { 1 / 4 } \sim 1,19$. A non-deficient number is called weird by S.J. Benkovski and Erdős [a3] if it is not pseudo-perfect (cf. also [Perfect number][25]). They proved that the density of weird numbers is positive.

V. Siva Rama Prasad and D.R. Reddy [a23] say that a number $n$ is primitive unitary $\alpha$-abundant if $\sigma ^ { * } ( n ) > \alpha n$ but $\sigma ^ { * } ( d ) < \alpha d$ for all $d | n$, $d < n$ ($\alpha \geq 2$). Here, $\sigma ^ { * } ( n )$ denotes the sum of unitary divisors of $n$ (for these functions, as well as related results, see also [a15]). Let $U _ { a }$ be the set of these numbers. Then

\begin{equation*} \limsup_{ n \rightarrow \infty , n \in U _ { \alpha } } \frac { \sigma ^ { * } ( n ) } { n } = \alpha. \end{equation*}

## Miscellaneous results.

Let $\alpha \in \RR$. A number $n$ is called $\alpha$-non-deficient if $\sigma ( n ) / n \geq \alpha$. By sharpening a result of O. Grün [a12], H. Salié [a18] proved that the least prime factor of every $\alpha$-non-deficient number with $m$ prime factors is less than $C(m\operatorname{log} n) ^{1 / \alpha}$.

Ch.R. Wall [a24] proved that there exist infinitely many abundant integers $n \equiv a ( \operatorname { mod } b )$ (with $a$ and $b$ given). Let $k$ be fixed. Then there exist $k$ consecutive abundant numbers. There exist infinitely many sequences of five consecutive deficient numbers. (See [a25].) See [a14] for a table of odd primitive abundant numbers $n$ with five distinct prime factors for which

\begin{equation*} 2 < \frac { \sigma ( n ) } { n } < 2 + \frac { 2 } { 10 ^ { 10 } }. \end{equation*}

If $k \geq 8$, the number $n = 1.3 .5 ... ( 2 k - 1 )$ is abundant, see [a22].

For others results on deficient, perfect, or related numbers, see [a15], [a8], [a9], [a19], [a17].

L. Moser [a26] proved that every integer $> 10 ^ { 5 }$ can be expressed as the sum of two abundant numbers. Actually, this is valid for integers $> 20162$, see [a27].

For a table of abundant numbers less than $10 ^ { 4 }$, see [a28].

#### References

[a1] | L. Alaoglu, P. Erdös, "On highly composite and similar numbers" *Trans. Amer. Math. Soc.*, **56**(1944) pp. 448–469 |

[a2] | M.R. Avidon, "On the distribution of primitive abundant numbers" *Acta Arith.*, **77**(1996) pp. 195–205 |

[a3] | S.J. Benkovski, P. Erdös, "On weird and pseudoperfect numbers" *Math. Comput.*, **28**(1974) pp. 617–623 |

[a4] | H. Davenport, "Über numeri abundantes" *Preuss. Akad. Wiss. Sitzungsber*, **26/29**(1933) pp. 830–837 |

[a5] | L.E. Dickson, "History of the theory of numbers" , **I (Divisibility and primality)**, Chelsea (1919) (Reprint: AMS 1999) |

[a6] | L.E. Dickson, "Finiteness of odd perfect and primitive abundent numbers with $n$ distinct prime factors" *Amer. J. Math.*, **35**(1913) pp. 413–422 |

[a7] | P. Erdös, "On the density of the abundant numbers" *J. London Math. Soc.*, **9**(1934) pp. 278–282 |

[a8] | P. Erdös, "On primitive abundant numbers" *J. London Math. Soc.*, **9**(1935) pp. 49–58 |

[a9] | P. Erdös, "Note on consecutive abundant numbers" *J. London Math. Soc.*, **13**(1938) pp. 128–131 |

[a10] | P. Erdös, "Remarks on number theory I, On primitive $\alpha$-abundant numbers" *Acta Arith.*, **5**(1958) pp. 25–33 |

[a11] | P. Erdös, J.-L. Nicolas, "Répartition des nombres superabondantes" *Bull. Soc. Math. France*, **103**(1975) pp. 65–90 |

[a12] | O. Grün, "Über ungerade vollkommene Zahlen" *Math. Z.*, **55**(1952) pp. 353–354 |

[a13] | A. Ivić, "The distribution of primitive abundant numbers" *Studia Sci. Math. Hung.*, **20**(1985) pp. 183–187 |

[a14] | M. Kishore, "Odd integers $n$ with five distinct prime factors for which $2 - 10 ^ { - 12 } < \sigma ( n ) / n < 2 + 10 ^ { - 12 }$" *Math. Comput.*, **32**(1978) pp. 303–309 |

[a15] | D.S. Mitrinović, J. Sándor, "Handbook of number theory" , Kluwer Acad. Publ. (1995) (In coop. with B. Crstici) |

[a16] | J.-L. Nicolas, "Ordre maximal d'un élément du groupe $S _ { n }$ des permutations et `highly composite numbers'" *Bull. Soc. Math. France*, **97**(1969) pp. 129–191 |

[a17] | H.J.J. te Riele, "A theoretical and computational study of generalized aliquot sequences" *Math. Centrum, Amsterdam*(1975) |

[a18] | H. Salié, "Über abundante Zahlen" *Math. Nachr.*, **9**(1953) pp. 217–220 |

[a19] | J. Sándor, "On a method of Galambos and Kátai concerning the frequency of deficient numbers" *Publ. Math. (Debrecen)*, **39**(1991) pp. 155–157 |

[a20] | H.N. Shapiro, "Note on a theorem of Dickson" *Bull. Amer. Math. Soc.*, **55**(1949) pp. 450–452 |

[a21] | H.N. Shapiro, "On primitive abundant numbers" *Commun. Pure Appl. Math.*, **21**(1968) pp. 111–118 |

[a22] | W. Sierpinski, "Teoria liczb" , **II**, Warsawa (1959) |

[a23] | V. Siva Rama Prasad, D.R. Reddy, "On primitive unitary abundant numbers" *Indian J. Pure Appl. Math.*, **21**(1990) pp. 40–44 |

[a24] | Ch.R. Wall, "Problem E3002" *Amer. Math. Monthly*, **90**(1983) pp. 400 (Solution by N.J. Fine: 93 (1986), 814) |

[a25] | Ch.R. Wall, "Problem, 6356" *Amer. Math. Monthly*, **88**(1981) pp. 623 (Solution by L.L. Foster: 90 (1983), 215-216) |

[a26] | L. Moser, "Problem E848" *Amer. Math. Monthly*, **56**(1949) pp. 478 |

[a27] | E. Bach, J. Shallit, "Algorithmic number theory" , MIT (1996) pp. 334 |

[a28] | J.W.L. Glaiser, "Number-Divisor Tables" , British Assoc. Math. Tables (1940) |

**How to Cite This Entry:**
Abundant number. *Encyclopedia of Mathematics.*URL: http://encyclopediaofmath.org/index.php?title=Abundant_number&oldid=55516

This article was adapted from an original article by J. SÃ¡ndor (originator), which appeared in Encyclopedia of Mathematics - ISBN 1402006098. [See original article][28]

Retrieved from " [https://encyclopediaofmath.org/index.php?title=Abundant_number&oldid=55516][29] "

[Categories][30]:

- [TeX semi-auto][31]
- [TeX done][32]

- This page was last edited on 15 February 2024, at 05:54.

- [Privacy policy][33]
- [About Encyclopedia of Mathematics][34]
- [Disclaimers][35]

- [Copyrights][36]
- [Impressum-Legal][37]

Manage Cookies


## Links

[1]: /
[2]: /index.php?title=Special:UserLogin&returnto=Abundant+number
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
[14]: /wiki/Special:WhatLinksHere/Abundant_number
[15]: /wiki/Special:RecentChangesLinked/Abundant_number
[16]: /wiki/Special:SpecialPages
[17]: /index.php?title=Abundant_number&amp;oldid=55516
[18]: /index.php?title=Abundant_number&amp;action=info
[19]: /wiki/Abundant_number
[20]: /index.php?title=Talk:Abundant_number&amp;action=edit&amp;redlink=1
[21]: /index.php?title=Abundant_number&amp;action=edit
[22]: /index.php?title=Abundant_number&amp;action=history
[23]: /wiki/Divisor
[24]: /wiki/Number_of_divisors
[25]: /wiki/Perfect_number
[26]: /wiki/Prime_number
[27]: /wiki/Totient_function
[28]: http://encyclopediaofmath.org/index.php?title=Abundant_number&oldid=18512
[29]: https://encyclopediaofmath.org/index.php?title=Abundant_number&amp;oldid=55516
[30]: /wiki/Special:Categories
[31]: /wiki/Category:TeX_semi-auto
[32]: /wiki/Category:TeX_done
[33]: /wiki/Encyclopedia_of_Mathematics:Privacy_policy
[34]: /wiki/Encyclopedia_of_Mathematics:About
[35]: /wiki/Encyclopedia_of_Mathematics:General_disclaimer
[36]: /index.php/Encyclopedia_of_Mathematics:Copyrights
[37]: /index.php/Encyclopedia_of_Mathematics:Legal
