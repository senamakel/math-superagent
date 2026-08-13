<!-- source: https://web.archive.org/web/20060803103919/http://math.uindy.edu/swett/esc.htm | converted from HTML -->

Swett, Research, Erdos-Strauss Conj

*Allan Swett, Current Research on ESC... rev. 10/28/99*

**The Erdos-Strauss Conjecture**

The "Erdos-Strauss conjecture" (ESC) is the statement that for any integer n > 1 there are integers a, b, and c with

4/n = 1/a + 1/b + 1/c,

 |

 | a > 0, b > 0, c > 0. |

 |

[*]

 |

Let ESC(n) abbreviate the statement that [*] is true for a particular positive integer n.

ESC(n) is known to be true for all integers n, 1 < n <= 10^8. This page, and its links, establish that **ESC(n) is true for all integers n, 1 < n <= 10^14.**

(Note: Some of the linked pages are under revision.)

**Principal Ideas, Part 1: ***A C++ Program*

***

 |

One may establish ESC(n) for a particular class of integers n using an identity. For example, the identity

4/(2+3x) = 1/(2+3x) + 1/(1+x) + 1/((1+x)(2+3x))

establishes that ESC(n) is true for n = 2, 5, 8, 11, 14, 17, ... (simply take x = 0, 1, 2, 3, 4, 5, ...). That is, ESC(n) is true for all positive integers n which are congruent to 2, mod 3.

(Two integers are said to be "congruent mod n", if and only if n divides their difference. We abbreviate the fact that A and B are congruent mod n as A == B (mod n) .)

A "generic" identity provides a set of similar results:

 |

**Vocabulary:**

 |

 |

For n > 0, let **S(n)**denote the set of integers A in {0, 1, 2, ..., 4n-2} such that

AX + W == 0 (mod 4n-1)

for some positive integer divisors X and W of n.

Let **E(n)**denote the set of positive integers congruent, mod 4n-1, to an element of S(n).

*Then*

 |

 |

 |

 |

 |

 |

**Theorem:**

 |

 |

If k > 0 and for some n > 0 k is in E(n) then ESC(k) is true.

 |

[Link][1] to a proof of the Theorem.

A table of values of S(n):

**Values of S(n)** |

**n** | **The modulus, 4n-1** | **The set S(n)** |

1 | 3 | {2} |

2 | 7 | {3, 5, 6} |

3 | 11 | {7, 8, 10} |

4 | 15 | {7, 11, 13, 14} |

5 | 19 | {14, 15, 18} |

6 | 23 | {7, 10, 11, 15, 17, 19, 20, 21, 22} |

7 | 27 | {20, 23, 26} |

8 | 31 | {15, 23, 27, 29, 30} |

9 | 35 | {23, 26, 31, 32, 34} |

10 | 39 | {17, 19, 23, 29, 31, 34, 35, 37, 38} |

**A ******[Link][2]**to a larger table, and Related Comments.** |

**Alternative calculation of S(n)... a ******[Link][3] |

We think of E(n), or its abbreviated form S(n), as a "filter". Gathering a set of such filters, we use a C++ program to establish that a relatively small set of integers less than one hundred trillion (=10^14) "pass through" this larger filter. For the remaining integers k, those "trapped" by the filter, ESC(k) is known to be true by the Theorem (and by a pair of Lemmas, below).

An additional but basic fact about ESC is used to tighten the filter, and the C++ algorithm avoids consideration of some "well-known" residue classes mod 840. Specifically,

 |

**Lemma 1:**

 |

 |

If k > 0 and k is not relatively prime to some positive integer m < 4000 then ESC(k) is true.

 |

 |

 |

 |

 |

 |

**Lemma 2:**

 |

 |

If k > 0 and the least residue of k, mod 840, is not in {1, 121, 169, 289, 361, 529} then ESC(k) is true.

 |

The current version of the C++ program "filters" the first 100.8 trillion positive integers, using the two Lemmas and the filters S(n) for n = 1, 2, ..., 1000. Since ESC(n) need only be proven for prime n within this range (see Lemma 4 below), the program then eliminates perfect squares. There remain 7132 "potentially prime" exceptional cases n for which the status of ESC(n) is undecided. The C++ program writes these special cases to a sequence of 100 data files, for further consideration by a *Mathematica *program.

 |

***

**Principal Ideas, Part 2: ***A Mathematica Program*

***

 |

A *unit fraction*(sometimes called an *Egyptian fraction*) is a fraction of the form 1/k for k a positive integer.

Necessary and sufficient conditions for a rational number to be the sum of two unit fractions are apparently well-known, namely,

 |

**Lemma 3: **

 |

 |

Suppose that n and d are relatively prime positive integers. Then n/d is the sum of two unit fractions if and only if there are positive integer divisors A and B of d such that A+B is divisible by n.

 |

Since *Mathematica*'s Divisors[] function provides the set of positive integer divisors of a given positive integer, it is a relatively straightforward matter to design a *Mathematica*function which determines whether a given rational is the sum of two unit fractions. (However there is some peril in the algorithm, since factorization issues may give rise to time-consuming or incomplete evaluation.)

This derived function is called by a "greedy" routine which searches for three-unit-fraction decompositions of 4/n, looking for a decomposition which has the smallest possible denominator. (This algoithm has proven rather effective. For example, for primes n less than 1 billion, this provides a three-unit-fraction decomposition for 4/n in 27 or fewer "guesses".)

The *Mathematica*program reads the 100 data files produced as C++ output, and using PrimeQ[] establishes that 3209 of the 7132 exceptional cases are prime. It then applies the greedy search algorithm to the prime cases, and establishes that ESC(n) is true for each of these 3209 primes. Thus, ESC(n) is true for 1 < n <= 100.8 trillion, since

 |

**Lemma 4: **

 |

 |

If ESC(n) is true for a positive integer n, then ESC(m) is true for every positive integer multiple m of n.

 |

 |

***
**Links to Software Source Code**

**

(1)

 |

 |

Link to a plain text version of the [source code][4] of the C++ program.

 |

 |

 |

**
Notes: **

 |

This compiles and runs sucessfully using CodeWarrior (Versions 2.1 and 3.0). (Execution time, on a "typical" PC: approximately 150 hours.)

Other compilers may need modification of the #include and #pragma directives, special consideration for 64-bit arithmetic (long long integers), and a directive to use 32-bit integers as the default integer type.

 |

 |

 |

**
Warning: **

 |

The program is set to produce 100 output files.

 |

 |

 |

 |

 |

(2)

 |

 |

Link to a plain text version of the [source code][5] of the *Mathematica*program. Reference to the source directory for the data files (and perhaps the file numbers) should be user-modified. (Total execution time, *Mathematica 4.0*: about 3 minutes.)

 |

 |

 |

 |

 |

(3)

 |

 |

Link to copies of selected data files, text files produced by the C++ program and used as input for the *Mathematica*program. (Note: the data are not in ascending order.)

 |

 |

 |

 |

[1.txt][6]

 |

 |

52 "cases" (26 primes)

 |

 |

[5.txt][7]

 |

72 "cases" (34 primes)

 |

[50.txt][8]

 |

68 "cases" (33 primes)

 |

[100.txt][9]

 |

71 "cases" (34 primes)

 |

 |

**

**

---

**

**

Up: ****[Research Page][10] |

 | Up Up: ****[My Faculty Page][11] |

**


## Links

[1]: theorem.htm
[2]: s_table.htm
[3]: other_form.htm
[4]: prog1.txt
[5]: prog2.txt
[6]: 1.txt
[7]: 5.txt
[8]: 50.txt
[9]: 100.txt
[10]: swettres.htm
[11]: math_swett.htm
