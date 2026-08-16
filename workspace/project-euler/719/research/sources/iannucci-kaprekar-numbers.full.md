<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL3/iann2a.html | converted from HTML -->

The Kaprekar Numbers

 | [Journal of Integer Sequences,][1] Vol. 3 (2000), Article 00.1.2 |

## **The Kaprekar Numbers**

### Douglas E. Iannucci
The University of the Virgin Islands
2 John Brewers Bay
St. Thomas, VI 00802
Email address: [diannuc@uvi.edu][2]

**Abstract:**The (decimal) *n*-Kaprekar numbers are defined and are shown to be in one-one correspondence with the unitary divisors of 10*n*- 1. In particular, this establishes the correctness of an algorithm for generating the Kaprekar numbers proposed by Charosh in 1981. The even perfect numbers are shown to be Kaprekar numbers in the binary base.

**1. INTRODUCTION**

****The *Kaprekar numbers *(sequence [A006886][3] in **[4]**) were introduced by the eponymous D. R. Kaprekar **[3]**in 1980. They have been the subject of several articles, and are mentioned in David Wells's *Dictionary of Curious and Interesting Numbers***[5].**
****What makes the Kaprekar numbers curious or interesting? Let's consider an example. The number 703 is Kaprekar because

703 2 = 494209 and 494 + 209 = 703 .

Here are some further examples:

9 2 = 81 , 8 + 1 = 9 ;
45 2 = 2025 , 20 + 25 = 45 ;
297 2 = 88209 , 88 + 209 = 297 ;
4879 2 = 23804641 , 238 + 4641 = 4879 ;
17344 2 = 300814336 , 3008 + 14336 = 17344 ;
538461 2 = 289940248521 , 289940 + 248521 = 538461 .

Formally, an *n*-Kaprekar number *k*>= 1 (for *n*= 1, 2, ...) satisfies the pair of equations

*k*= *q*+ *r*,

*k*2 = *q** 10*n*+ *r*

where *q*>= 1 and 0 <= r < 10*n*. As the 5-Kaprekar number *k*= 4879 shows, *r*may have fewer than *n*digits. We adopt the convention that 1 is an *n*-Kaprekar number for all *n*>= 1, since

1 2 = 0 * 10*n*+ 1, 1 = 0 + 1 ;

but by fiat 0 and 10*m*for *m*>= 1 are not Kaprekar numbers.
Kaprekar **[3]**listed 9 as a Kaprekar number, but failed to list 99, 999, ... However, 10*n*- 1 (for all *n*>= 1) is *n*-Kaprekar since

99 **. . . **99 2 = 9 **. . . **9980 **. . . **001 , 9 **. . . **998 + 0 **. . . **001 = 99**. . . **99 ;
\______/ \______/ \_____/ \_____/ \_____/ \______/
*n*nines *n*-1 nines *n*-1 zeros *n*-1 nines *n*-1 zeros *n*nines

that is,

(10*n*- 1) 2 = (10*n*- 2) * 10*n*+ 1 , 10*n*- 1 = (10*n*- 2) + 1 .

Charosh **[2] **noted Kaprekar's omission of the numbers 10*n*- 1 (*n*>= 1), as well as the 6-Kaprekar numbers 181819 and 818181. In fact, Charosh correctly devised a method by which to construct Kaprekar numbers of any size. In this paper, we will refine Charosh's result by establishing a bijection between the *n*-Kaprekar numbers and the unitary divisors of 10*n*-1 (thus refining and proving Charosh's result). Recall that *a*is a *unitary divisor *of *m *if *ab = m*and (*a, b*) = 1 .

**2. THE MAIN RESULT**

For each integer *N*> 1, let *K*(*N*) denote the set of positive integers *k*for which there exists integers *q *and *r *such that

*k*2 = *qN + r *( 0 <= *r < N *) **(1)** |

*k*= *q + r . ***(2)** |

As a matter of convention, we shall ignore the vacuous solution *k = N *(for which *q = N *and *r = *0). **(1)**and **(2)**imply

*k*(*k*- 1) = *q*(*N*- 1) **(3)** |

Since we disregard the vacuous solution, we have 1 <= *k*<= *N*- 1 (for if *k*>= *N*then **(3)**implies *q*> *k*, contradicting **(2)**).
The set *K*(*N*) is nonempty, for always 1 is in *K*(*N*). Suppose *k *were in *K*(*N*). Since (*k, k - *1) = 1, it follows from **(3)**that *d | k *and *d' | k - *1 for some positive *d*and *d' *such that *dd' = N -*1 and (*d, d' *) = 1. Let *k' = N - k .*Because 1 <= *k <= N - *1 , we have *k' >*0 . Since *k' = *(*N - *1) - (*k *- 1) , we have *d' | k' *. Thus *k = dm *and *k' = d'm' *for some positive *m*and *m'*, whence follows

*dm + d'm' = N = dd' + *1****(4)** |

**Definition: **If (*a , b *) = 1 , we denote by ***Inv***(*a , b *) the least positive integer *m*such that *am*= 1 (mod *b*). It follows that *m*= ***Inv***(*a , b *) if and only if 1 <= *m*< *b*and *a**m*=1 (mod *b*). |

It is not difficult to show the next result.

**Lemma 1: **Suppose (*a , b *) = 1 . Then *m*= ***Inv***( *a , b *) and *n*= ***Inv***(*b , a *) if and only if *m*and *n*are positive and *a**m*+ *b**n*= *ab + *1 . |

Applying Lemma 1 to **(4)**gives

*k = d **Inv***(*d , d' *) ; *k' = d' **Inv***(*d ', d *) . **(5)** |

Conversely, let *dd' = N - *1 , (*d, d'*) = 1, and let *m = **Inv***(*d, d' *) and *m' = **Inv***(*d', d *) . Then by Lemma 1 we have *dm + d'm' = N . *Therefore

*d*2*m*2 = (*N - d'm'*) 2
= *N *2 - *N d'm' - *(*dm + d'm'*) *d'm'*+ (*d'm'*) 2
= *N *2 - *N d'm' - mm'dd'*
= (*N - d'm' - mm'*) *N*+ *mm' .*

Thus
(*dm*) 2 = (*N - d'm' - mm'*) *N*+ *mm'*(*mm' < N*) ,
*dm*= (*N - d'm' - mm'*) + *mm' .*

That is, *dm *satisfies **(1)**and **(2)**(with *q = N - d'm' - mm' *and *r = mm'*), whence *dm *is in *K*(*N)*. Note that *d'm' *is in *K*(*N*) by symmetry. We have proved the following results:

**Theorem 1: ***k *is in *K*(*N*) if and only if *k = d **Inv***(*d, *(*N*-1)/*d*) for some unitary divisor *d*of *N - *1 . |

**Corollary A: **The elements *k *of *K*(*N*) occur in complementary pairs. For each *k*in *K*(*N*), *N - k *is in *K*(*N*). |

Let *w*(*M*) denote the number of distinct primes dividing *M*; then *M*has exactly 2*w*(*M*) unitary divisors. The following result is immediate:

**Corollary B: ***K*(*N*) contains exactly 2*w*(*N*- 1) elements.  |

The convention that *N*not be an element of *K*(*N*) was taken to ensure the bijection between the elements of *K*(*N*) and the unitary divisors of *N - *1 .

**3. APPLICATIONS**

****If we let *N = *10*n*for some *n >= *1 in Theorem 1, we get the set of *n*-Kaprekar numbers, which is thus given by

*K*(10*n*) = {*d **Inv***(*d , d' *) **:***dd' = *10*n*- 1 , (*d , d' *) = 1 }.

The following table lists all *n*-Kaprekar numbers *k*for 1 <= *n*<= 6, along with the associated unitary divisors *d*of 10*n*- 1 . These same Kaprekar numbers were given by Charosh **[2]**. By Corollary A, the *n*-Kaprekar numbers occur in complementary pairs which sum to 10*n*.

***n d k*** | ***n d k*** | ***n d k*** | ***n d k*** |

**1**1 1 | **4**909 7272 | **6 **11 181819 | **6 **259 208495 |

9 9 | 1111 7777  | 297 329967 | 6993 356643 |

**2 **1 1 | 9999 9999 | 77 38962 | 407 533170 |

9 45 | **5**1 1 | 2079 187110 | 10989 681318 |

11 55 | 9 77778 | 13 461539 | 2849 390313 |

99 99 | 41 4879 | 351 609687 | 76923 538461 |

**3 **1 1 | 369 82656 | 91 318682 | 481 812890 |

27 297 | 271 17344 | 2457 466830 | 12987 961038 |

37 703 | 2439 95121 | 143 643357 | 3367 670033 |

999 999 | 11111 22222 | 3861 791505 | 90909 818181 |

**4 **1 1 | 99999 99999 | 1001 500500 | 5291 994708 |

9 2223 | **6 **1 1 | 27027 648648 | 142857 142857 |

11 2728 | 27 148149 | 37 351352 | 37037 851851 |

99 4950 | 7 857143 | 999 499500 | 999999 999999 |

101 5050 | 189 5292 |  |  |

For example, consider *n*= 3: 27 and 37 are unitary divisors of 10 3 - 1 = 27 * 37. Then ***Inv***(27, 37) = 11 and ***Inv***(37, 27) = 19, and we obtain the complementary 3-Kaprekar numbers 27 * 11 = 297 and 37 * 19 = 703.
The universal Kaprekar number 1 corresponds to the unitary divisor 1 of 10*n*- 1, which is why we allow unity as a Kaprekar number. For each *n*>= 1 , we disallow 10*n*as a Kaprekar number since it is the vacuous solution to **(1)**and **(2)**when *N = *10*n*.
If we let *N = b n*in Theorem 1 for some *b >= *2 and *n*>= 1 , we get the base-*b*generalization of the Kaprekar numbers. The case *b =*2 is especially interesting.

**Theorem 2: **Every even perfect number is a Kaprekar number in the binary base. |

**Proof: **Let *n*>= 1. It is clear that 2*n*- 1 and 2*n*+ 1 are relatively prime, and that

2*n*-1 (2*n*- 1) = 1 (mod 2*n*+ 1) , 0 < 2*n*-1 < 2*n*+ 1 .

Therefore 2*n*-1 = ***Inv***( 2*n*- 1 , 2*n*+ 1), and so 2*n*-1 (2*n*- 1) is in *K*(2 2*n*)by Theorem 1. It is well known that every even perfect number has the form 2*n*-1 (2*n*- 1) where 2*n*- 1 is prime; hence the result follows. **QED**

To illustrate Theorem 2, we see that 28 = 2 2 (2 3 - 1) is perfect and 6-Kaprekar in the binary base: (28) 2 = 11100, and

11100 2 = 1100010000 , 1100 + 010000 = 11100 .

Similarly, *b n*-1 (*b n*- 1) and *b n*-1 (*b n*+ 1) are complementary 2*n*-Kaprekar numbers in the base *b*whenever *b*is even. This pattern, among others, was noted by Charosh **[2]**in the case when *b =*10.

**4. CONCLUDING REMARKS**
It is not worth compiling a more extensive list of Kaprekar numbers, since they can be obtained from the prime factorization of 10*n*- 1 cf. Brillhart et al. **[1]**.
Corollary B shows that the Kaprekar numbers have natural density zero.

**REFERENCES.**

**[1] **Brillhart, J., Lehmer, D.H., Selfridge, J., Tuckerman, B., Wagstaff, S. "Factorizations of (*b n *+/- 1) , *b*= 2, 3, 5, 6, 7, 10, 11, 12 up to high powers." 2nd ed., *Contemporary Mathematics, *v. 22, American Mathematical Society, Providence, RI, 1988.

**[2]**Charosh, M. "Some Applications of Casting Out 999**...**'s." *Journal of Recreational Mathematics*, v. 14, no. 2 (1981-82), pp. 111-118.

**[3]**Kaprekar, D. "On Kaprekar Numbers." *Journal of Recreational Mathematics*, v. 13, no. 2 (1980-81), pp. 81-82.

**[4] **Sloane, N.J.A. *The On-Line Encyclopedia of Integer Sequences*, published electronically at [http://oeis.org][4]

**[5] **Wells, D. *The Penguin Dictionary of Curious and Interesting Numbers, *Penguin Books USA, Inc., New York 1986.

---

(Concerned with sequences [A006886][3], [A037042][5], [A053394][6], [A053395][7], [A053396][8], [A053397][9].)

---

Received Feb 3, 1999; revised version received Mar 21, 1999. Published in Journal of Integer Sequences, Jan. 13, 2000.

---

Return to ****[Journal of Integer Sequences home page][1]

---


## Links

[1]: ..
[2]: mailto:diannuc@uvi.edu
[3]: http://oeis.org/A006886
[4]: http://oeis.org
[5]: http://oeis.org/A037042
[6]: http://oeis.org/A053394
[7]: http://oeis.org/A053395
[8]: http://oeis.org/A053396
[9]: http://oeis.org/A053397
