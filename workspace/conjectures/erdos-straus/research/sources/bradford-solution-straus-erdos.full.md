<!-- source: https://arxiv.org/html/2602.11774v1 | converted from HTML -->

1Part One

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2602.11774v1 [math.NT] 12 Feb 2026

A SOLUTION TO THE STRAUS ERDŐS CONJECTURE

Kyle Bradford
Unaffiliated
kyle.bradford@gmail.com

Received: , Revised: , Accepted: , Published:

Abstract

This paper outlines a solution to the Straus Erdős Conjecture. Namely for each prime p p there exists positive integers x ≤ y ≤ z x\leq y\leq z so that

 | 4 p = 1 x + 1 y + 1 z. \frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

## 1 Part One

For years, I have been waiting for this moment when I solved the problem. May it bless us all with its simplicity and ease.The Straus-Erdős conjecture has been studied and this paper gives an elementary proof. We are seeking solutions to the diophantine equation mentioned in the abstract.

It should be clear that only one solution exists when the prime p = 2 p=2. This solution is

 | 4 2 = 1 1 + 1 2 + 1 2. \frac{4}{2}=\frac{1}{1}+\frac{1}{2}+\frac{1}{2}. |  |

It should also be clear that a variety of solutions exist when the prime p ≡ 3 mod 4 p\equiv 3\bmod 4. This solution is derived from the greedy algorithm where you can make two unit fractions:

 | 4 p = 4 p + 1 + 4 p ⁡ ( p + 1). \frac{4}{p}=\frac{4}{p+1}+\frac{4}{p(p+1)}. |  |

It has been shown that p ∤ x p\nmid x, p | z p\mid z and p p sometimes divides y y. The common nomenclature is to call solutions with p ∤ y p\nmid y Type I solutions and solutions with p | y p\mid y Type II solutions. The following propositions and lemmata will elucidate the method of proof. We start with Type I solutions.

###### Proposition 1.

Given a prime p ≡ 1 mod 4 p\equiv 1\bmod 4, if a Type I solutions exists, then there exists a nonnegative integer k k so that

 | z = ( 4 ​ k + 3) ​ p 2 + p 4. z=\frac{(4k+3)p^{2}+p}{4}. |  |

###### Proof.

Let p p be a prime so that p ≡ 1 mod 4 p\equiv 1\bmod 4. Suppose that a Type 1 solution exists with x ≤ y ≤ z x\leq y\leq z.

We have from a previous paper that if a solution exists, then

 | z = x ​ y ​ p gcd ⁡ ( x ​ y, x + y) z=\frac{xyp}{\gcd(xy,x+y)} |  |

which would imply that 4 ​ x ​ y − ( x + y) ​ p = gcd ⁡ ( x ​ y, x + y) 4xy-(x+y)p=\gcd(xy,x+y). Notice then that we can write

 | x ​ y ​ p = ( x + y) ​ p 2 + gcd ⁡ ( x ​ y, x + y) ​ p 4. xyp=\frac{(x+y)p^{2}+\gcd(xy,x+y)p}{4}. |  |

This would imply that

 | z = ( ( x + y) / gcd ⁡ ( x ​ y, x + y)) ​ p 2 + p 4. z=\frac{\left((x+y)/\penalty\gcd(xy,x+y)\right)p^{2}+p}{4}. |  |

We know that z z is an integer and p ≡ 1 mod 4 p\equiv 1\bmod 4, so ( x + y) / gcd ⁡ ( x ​ y, x + y) ≡ 3 mod 4 (x+y)/\penalty\gcd(xy,x+y)\equiv 3\bmod 4. This implies that there exists a nonnegative k k so that ( x + y) / gcd ⁡ ( x ​ y, x + y) = 4 ​ k + 3 (x+y)/\penalty\gcd(xy,x+y)=4k+3. This shows that there exists a nonnegative integer k k so that

 | z = ( 4 ​ k + 3) ​ p 2 + p 4. z=\frac{(4k+3)p^{2}+p}{4}. |  |

∎

Given this prime p p and value of k k, unique solutions are determined by the different ways that we can express the following fraction as the sum of two positive unit fractions:

 | 4 ​ k + 3 ( ( ( 4 ​ k + 3) ​ p + 1) / 4). \frac{4k+3}{\left(((4k+3)p+1)/\penalty 4\right)}. |  |

Instead of supposing that a solution exists, we will use this form to outline for which primes a solution exists.

###### Lemma 1.

Let k ≥ 0 k\geq 0, 1 ≤ ℓ ≤ 2 ​ ( 4 ​ k + 3) 1\leq\ell\leq 2(4k+3) so that gcd ⁡ ( ℓ, 4 ​ k + 3) = 1 \gcd(\ell,4k+3)=1 and consider primes of the form p ≡ n mod ( 16 ⋅ ℓ ⋅ ( 4 ​ k + 3) − 4 ⋅ ℓ 2) / ( gcd ⁡ ( ℓ, 4)) 2 p\equiv n\bmod(16\cdot\ell\cdot(4k+3)-4\cdot\ell^{2})/\penalty(\gcd(\ell,4))^{2}, where n n is a positive integer so that ( 4 ​ k + 3) ​ n ≡ − 1 mod ( 16 ⋅ ℓ ⋅ ( 4 ​ k + 3) − 4 ⋅ ℓ 2) / ( gcd ⁡ ( ℓ, 4)) 2 (4k+3)n\equiv-1\bmod(16\cdot\ell\cdot(4k+3)-4\cdot\ell^{2})/\penalty(\gcd(\ell,4))^{2}, then there are solutions

 | 4 p = 4 ​ ( 4 ​ k + 3) − ℓ ( 4 ​ k + 3) ​ p + 1 + ℓ ( 4 ​ k + 3) ​ p + 1 + 4 p ⁡ ( ( 4 ​ k + 3) ​ p + 1). \frac{4}{p}=\frac{4(4k+3)-\ell}{(4k+3)p+1}+\frac{\ell}{(4k+3)p+1}+\frac{4}{p((4k+3)p+1)}. |  |

It should be clear that for primes of these forms, these three fractions will be unit fractions. In fact, they are designed to be unit fractions in a optimal way. The limitation on ℓ \ell guarantees that x ≤ y ≤ z x\leq y\leq z as read from left to right. We next move to Type II solutions for sake of symmetry.

###### Proposition 2.

Given a prime p p, if a Type II solutions exists, then there exists a positive integer k k so that

 | x = p + ( 4 ​ k + 3) 4. x=\frac{p+(4k+3)}{4}. |  |

The proof of this is trivial given my previous work because we showed that integer x ≥ ⌈ p 4 ⌉ x\geq\left\lceil\frac{p}{4}\right\rceil. This time, given this prime p p and value of k k, unique solutions are determined by the different ways that we can express the following fraction as the sum of two positive unit fractions:

 | 4 ​ k + 3 p ⁡ ( ( p + ( 4 ​ k + 3)) / 4). \frac{4k+3}{p\left((p+(4k+3))/\penalty 4\right)}. |  |

We will use this form to outline for which primes a solution exists.

###### Lemma 2.

Let k ≥ 0 k\geq 0, 1 ≤ ℓ ≤ 2 ​ ( 4 ​ k + 3) 1\leq\ell\leq 2(4k+3) so that gcd ⁡ ( ℓ, 4 ​ k + 3) = 1 \gcd(\ell,4k+3)=1 and consider primes of the form p ≡ − ( 4 ​ k + 3) mod ( 16 ⋅ ℓ ⋅ ( 4 ​ k + 3) − 4 ⋅ ℓ 2) / ( gcd ⁡ ( ℓ, 4)) 2 p\equiv-(4k+3)\bmod(16\cdot\ell\cdot(4k+3)-4\cdot\ell^{2})/\penalty(\gcd(\ell,4))^{2}, then there are solutions

 | 4 p = 4 p + ( 4 ​ k + 3) + 4 ​ ( 4 ​ k + 3) − ℓ p ⁡ ( p + ( 4 ​ k + 3)) + ℓ p ⁡ ( p + ( 4 ​ k + 3)). \frac{4}{p}=\frac{4}{p+(4k+3)}+\frac{4(4k+3)-\ell}{p(p+(4k+3))}+\frac{\ell}{p(p+(4k+3))}. |  |

Again it should be clear that these are unit fractions. Combining these two lemmata will help us derive a covering system. Remember we are only considering primes p ≡ 1 mod 4 p\equiv 1\bmod 4. For each k ≥ 0 k\geq 0 and 1 ≤ ℓ ≤ 2 ​ ( 4 ​ k + 3) 1\leq\ell\leq 2(4k+3) such that gcd ⁡ ( ℓ, 4 ​ k + 3) = 1 \gcd(\ell,4k+3)=1, we will find negative 4 ​ k + 3 4k+3 and the negative inverse element of 4 ​ k + 3 4k+3 in the modular group ℤ / ( ( 16 ⋅ ℓ ⋅ ( 4 ​ k + 3) − 4 ⋅ ℓ 2) / ( gcd ⁡ ( ℓ, 4)) 2) ​ ℤ \mathbb{Z}/\penalty((16\cdot\ell\cdot(4k+3)-4\cdot\ell^{2})/\penalty(\gcd(\ell,4))^{2})\mathbb{Z} and this will create our covering system. To clarify this idea, I will consider solutions for all such ℓ \ell when k = 0 k=0.

For primes p ≡ 29 mod 44 p\equiv 29\bmod 44 we have solutions of the form

 | 4 p = 11 3 ​ p + 1 + 1 3 ​ p + 1 + 4 p ⁡ ( 3 ​ p + 1), \frac{4}{p}=\frac{11}{3p+1}+\frac{1}{3p+1}+\frac{4}{p(3p+1)}, |  |

for primes p ≡ 41 mod 44 p\equiv 41\bmod 44 we have solutions of the form

 | 4 p = 4 p + 3 + 11 p ⁡ ( p + 3) + 1 p ⁡ ( p + 3), \frac{4}{p}=\frac{4}{p+3}+\frac{11}{p(p+3)}+\frac{1}{p(p+3)}, |  |

for primes p ≡ 13 mod 20 p\equiv 13\bmod 20 we have solutions of the form

 | 4 p = 10 3 ​ p + 1 + 2 3 ​ p + 1 + 4 p ⁡ ( 3 ​ p + 1), \frac{4}{p}=\frac{10}{3p+1}+\frac{2}{3p+1}+\frac{4}{p(3p+1)}, |  |

for primes p ≡ 17 mod 20 p\equiv 17\bmod 20 we have solutions of the form

 | 4 p = 4 p + 3 + 10 p ⁡ ( p + 3) + 2 p ⁡ ( p + 3), \frac{4}{p}=\frac{4}{p+3}+\frac{10}{p(p+3)}+\frac{2}{p(p+3)}, |  |

for primes p ≡ 5 mod 8 p\equiv 5\bmod 8 we have solutions of the form

 | 4 p = 8 3 ​ p + 1 + 4 3 ​ p + 1 + 4 p ⁡ ( 3 ​ p + 1), \frac{4}{p}=\frac{8}{3p+1}+\frac{4}{3p+1}+\frac{4}{p(3p+1)}, |  |

for primes p ≡ 5 mod 8 p\equiv 5\bmod 8 we have solutions of the form

 | 4 p = 4 p + 3 + 8 p ⁡ ( p + 3) + 4 p ⁡ ( p + 3), \frac{4}{p}=\frac{4}{p+3}+\frac{8}{p(p+3)}+\frac{4}{p(p+3)}, |  |

for primes p ≡ 93 mod 140 p\equiv 93\bmod 140 we have solutions of the form

 | 4 p = 7 3 ​ p + 1 + 5 3 ​ p + 1 + 4 p ⁡ ( 3 ​ p + 1), \frac{4}{p}=\frac{7}{3p+1}+\frac{5}{3p+1}+\frac{4}{p(3p+1)}, |  |

for primes p ≡ 137 mod 140 p\equiv 137\bmod 140 we have solutions of the form

 | 4 p = 4 p + 3 + 7 p ⁡ ( p + 3) + 5 p ⁡ ( p + 3). \frac{4}{p}=\frac{4}{p+3}+\frac{7}{p(p+3)}+\frac{5}{p(p+3)}. |  |

The last thing that we must show is that this is a covering system. From this I notice that 5, 13, 17, 29 5,13,17,29 are the first four primes that are 1 1 modulo 4 4.

## References

- [1] A. A. Abdulaziz, On the Egyptian method of decomposing 2 n \frac{2}{n} into unit fractions, Historia Math. 35 (2008), 1-18.
- [2] M. Bello-Hernández, M. Benito and E. Fernández, On Egyptian fractions, preprint, arXiv: 1010.2035v2.
- [3] K. Bradford, A note on the Erdős-Straus conjecture, Integers 21 (2021), #A24, 1-3.
- [4] K. Bradford and E. Ionascu, A geometric reduction of the Erdős-Straus conjecture, Adv. Mod. and Optim. 17 (1) (2015), 41-54.
- [5] E. S. Croot III, Egyptian Fractions, Ph. D. thesis, University of Georgia, 2000.
- [6] C. Elsholtz and T. Tao, Counting the number of solutions to the Erdős-Straus equation on unit fractions, J. Aust. Math. Soc. 94 (1) (2013), 50-105.
- [7] P. Erdős, Az 1 / x 1 + ⋯ + 1 / x n = a / b 1/\penalty x_{1}+\cdots+1/\penalty x_{n}=a/\penalty b egyenlet egész számú megoldásairól, Mat. Lapok 1 (1950).
- [8] R. Guy, Unsolved Problems in Number Theory, Springer, New York, 2004.
- [9] E. J. Ionascu and A. Wilson, On the Erdős-Straus conjecture, Rev. Roumaine Math. Pures Appl. 56 (1) (2011), 21-30.
- [10] D. Li, On the equation 4 /n = 1 /x + 1 /y + 1 /z, J. Number Theory 13 (1981), 485-494.
- [11] G. G. Martin, The Distribution of Prime Primitive Roots and Dense Egyptian Fractions, Ph.D. thesis, University of Michigan, 1997.
- [12] L. G. Mordell, Diophantine Equations, Academic Press, London, 1969.
- [13] M. R. Obláth, Sur l’ équation diophantienne 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/\penalty n=1/\penalty x_{1}+1/\penalty x_{2}+1/\penalty x_{3}, Mathesis 59 (1950), 308-316.
- [14] Y. Rav, On the representation of rational numbers as a sum of a fixed number of unit fractions, J. Reine Angew. Math. 222 (1966), 207-213.
- [15] L. A. Rosati, Sull’equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3}, Bollettino dell’Unione Math. Ital. 9 (1) (1954), 59-63.
- [16] J. W. Sander, On 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z and Rosser’s sieve, Acta Arith. 49 (1988), 281-289.
- [17] J. W. Sander, On 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z and Iwaniec’ Half Dimensional Sieve, Acta Arith. 59 (1991), 183-204.
- [18] J. W. Sander, Egyptian fractions and the Erdős-Straus Conjecture, Nieuw Arch. Wiskd. (4) 15 (1997), 43-50.
- [19] A. Schinzel, On sums of three unit fractions with polynomial denominators, Funct. Approx. Comment. Math. 28 (2000), 187-194.
- [20] A. Swett, The Erdős Straus conjecture, Current Research on ESC, rev.10/28/99. http://math.uindy.edu/swett.esc.htm.
- [21] D. G. Terzi, On a conjecture by Erdős-Straus, Nordisk Tidskr. Info. (BIT) 11 (1971), 212-216.
- [22] R. C. Vaughan, On a problem of Erdos, Straus and Schinzel, Mathematika 17 (1970), 193-198.
- [23] W. Webb, On 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z, Proc. Amer. Math. Soc. 25 (1970), 578-584.
- [24] W. Webb, On a theorem of Rav concerning Egyptian fractions, Canad. Math. Bull. 18 (1) (1975), 155-156.
- [25] W. Webb, On the diophantine equation k / n = a 1 / x 1 + a 2 / x 2 + a 3 / x 3 k/\penalty n=a_{1}/\penalty x_{1}+a_{2}/\penalty x_{2}+a_{3}/\penalty x_{3}, C ˘ \breve{C} asopis pro p e ˘ \breve{e} stováni matematiy, ro c ˘ \breve{c} 10 (1976), 360-365.
- [26] K. Yamamoto, On the diophantine equation 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z, Memoirs of the Faculty of Science, Kyushu University, Ser. A 19 (1) (1965), 37-47.
- [27] X. Q. Yang, A note on 4 / n = 1 / x + 1 / y + 1 / z 4/\penalty n=1/\penalty x+1/\penalty y+1/\penalty z, Proc. Amer. Math. Soc. 85 (1982), 496-498.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
