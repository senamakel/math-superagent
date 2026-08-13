<!-- source: https://ar5iv.labs.arxiv.org/html/2105.06440 | converted from HTML -->

[2105.06440] Powers of 3 with few nonzero bits and a conjecture of Erdős

# Powers of 3 3 with few nonzero bits
and a conjecture of Erdős

Vassil S. Dimitrov Dimitrov Center for Information Security and Cryptography, University of Calgary, 2500 University Drive NW, Calgary, AB T2N 1N4, Canada Email address: [vdimitro@ucalgary.ca][1] Dimitrov Lemurian Labs, Inc. Email address: [vassil@lemurianlabs.com][2] and Everett W. Howe Howe Independent mathematician, San Diego, CA 92104, USA Email address: [however@alumni.caltech.edu][3] URL: [http://ewhowe.com][4]

Date: May 12, 2023

###### Abstract.

Using completely elementary methods, we find all powers of 3 3 that can be written as the sum of at most twenty-two distinct powers of 2 2, as well as all powers of 2 2 that can be written as the sum of at most twenty-five distinct powers of 3 3. The latter result is connected to a conjecture of Erdős, namely, that 1 1, 4 4, and 256 256 are the only powers of 2 2 that can be written as a sum of distinct powers of 3 3.

We present this work partly as a reminder that for certain exponential Diophantine equations, elementary techniques based on congruences can yield results that would be difficult or impossible to obtain with more advanced techniques involving, for example, linear forms in logarithms.

###### Key words and phrases:

Exponential Diophantine equation, binary digit

###### 2020 Mathematics Subject Classification

Primary 11D61; Secondary 11A63, 11D72, 11D79

## 1. Introduction

To introduce our topic, we begin with some numerical observations. For an integer x ≥ 0 x\geq 0, consider the binary representation of 3 x 3^{x}. In Table 1 we give this representation for x ≤ 25 x\leq 25, and we tabulate the number of bits in the binary representation together with the number of those bits that are equal to 1 1.

Table 1. For each x x between 0 0 and 25 25 we give the binary representation of 3 x 3^{x}, together with the total number of bits in the representation and the number of those bits that are equal to 1 1.

x x | Binary representation of 3 x 3^{x} |  | #Bits | #Ones |

0 0 | 1 1 |  | 1 \phantom{0}1 | 1 \phantom{0}1 |

1 1 | 11 11 |  | 2 \phantom{0}2 | 2 \phantom{0}2 |

2 2 | 1001 1001 |  | 4 \phantom{0}4 | 2 \phantom{0}2 |

3 3 | 11011 11011 |  | 5 \phantom{0}5 | 4 \phantom{0}4 |

4 4 | 1010001 1010001 |  | 7 \phantom{0}7 | 3 \phantom{0}3 |

5 5 | 11110011 11110011 |  | 8 \phantom{0}8 | 6 \phantom{0}6 |

6 6 | 1011011001 1011011001 |  | 10 10 | 6 \phantom{0}6 |

7 7 | 100010001011 100010001011 |  | 12 12 | 5 \phantom{0}5 |

8 8 | 1100110100001 1100110100001 |  | 13 13 | 6 \phantom{0}6 |

9 9 | 100110011100011 100110011100011 |  | 15 15 | 8 \phantom{0}8 |

10 10 | 1110011010101001 1110011010101001 |  | 16 16 | 9 \phantom{0}9 |

11 11 | 101011001111111011 101011001111111011 |  | 18 18 | 13 13 |

12 12 | 10000001101111110001 10000001101111110001 |  | 20 20 | 10 10 |

13 13 | 110000101001111010011 110000101001111010011 |  | 21 21 | 11 11 |

14 14 | 10010001111101101111001 10010001111101101111001 |  | 23 23 | 14 14 |

15 15 | 110110101111001001101011 110110101111001001101011 |  | 24 24 | 15 15 |

16 16 | 10100100001101011101000001 10100100001101011101000001 |  | 26 26 | 11 11 |

17 17 | 111101100101000010111000011 111101100101000010111000011 |  | 27 27 | 14 14 |

18 18 | 10111000101111001000101001001 10111000101111001000101001001 |  | 29 29 | 14 14 |

19 19 | 1000101010001101011001111011011 1000101010001101011001111011011 |  | 31 31 | 17 17 |

20 20 | 11001111110101000001101110010001 11001111110101000001101110010001 |  | 32 32 | 17 17 |

21 21 | 1001101111011111000101001010110011 1001101111011111000101001010110011 |  | 34 34 | 20 20 |

22 22 | 11101001110011101001111100000011001 11101001110011101001111100000011001 |  | 35 35 | 19 19 |

23 23 | 1010111101011010111101110100001001011 1010111101011010111101110100001001011 |  | 37 37 | 22 22 |

24 24 | 100000111000010000111001011100011100001 100000111000010000111001011100011100001 |  | 39 39 | 16 16 |

25 25 | 1100010101000110010101100010101010100011 1100010101000110010101100010101010100011 |  | 40 40 | 18 18 |

Based on this limited data, it looks like about half of the bits of the binary representation of 3 x 3^{x} are equal to 1 1, which is what one would expect if 3 x 3^{x} were to behave like a random integer of the appropriate size. Computations with larger values of x x seem to indicate that the fraction of 1 1 s does tend toward 1 / 2 1/2 as x x increases to infinity, but proving that this is the case seems far beyond the reach of existing techniques.

A much weaker observation is that as x x goes to infinity, the number of 1 1 s in the binary representation of 3 x 3^{x} tends to infinity as well; that is, one would certainly be tempted to guess that there are only finitely many x x such that the binary representation of 3 x 3^{x} contains fewer than ten 1 1 s, or a hundred 1 1 s, or any given finite number of 1 1 s. This observation *is*in fact true, and was proven by Senge and Straus in 1973; their result [20, Theorem 3, p. 100] implies that for any given n n, there are only finitely many x x such that the binary representation of 3 x 3^{x} has n n or fewer bits equal to 1 1. In 1980 Cameron Stewart proved an effective version of this result [21, Theorem 1, p. 64] — which means that given a value of n n, Stewart’s arguments produce a bound B ⁡ ( n) B(n) so that if x > B ⁡ ( n) x>B(n), then 3 x 3^{x} has more than n n bits equal to 1 1. Unfortunately, the values of B ⁡ ( n) B(n) produced by Stewart’s method grow very quickly; for example, we can show 1 1 1 Stewart’s Theorem 1 shows that the largest x x for which 3 x 3^{x} has at most 22 22 bits equal to 1 1 satisfies 23 > ( log ⁡ log ⁡ 3 x) / ( C + log ⁡ log ⁡ log ⁡ 3 x) 23>(\log\log 3^{x})/(C+\log\log\log 3^{x}) for some positive constant C C. We only get a stronger upper bound on x x if we solve for x x when C = 0 C=0, and this is how we get our lower bound for B ⁡ ( 22) B(22). that B ( 22) > × 10 46 B(22)>4.9\!\times\!10^{46}.

In this paper, we use completely elementary techniques to find all powers of 3 3 whose binary representations have at most twenty-two bits equal to 1 1. In fact, these powers of 3 3 are exactly the ones displayed in Table 1.

###### Theorem 1.1.

The only powers of 3 3 that can be written as the sum of twenty-two or fewer distinct powers of 2 2 are 3 x 3^{x}, where 0 ≤ x ≤ 25 0\leq x\leq 25.

In other words, there are more than twenty-two 1 1 s in the binary representation of 3 x 3^{x} exactly when x > 25 x>25. Clearly, this bound is much smaller than the one obtained from Stewart’s theorem!

We also look at the complementary problem of finding powers of 2 2 whose base- 3 3 representations contain no 2 2 s and at most twenty-five 1 1 s. Stewart’s theorem applies here as well, and says that if 2 x 2^{x} can be expressed in this manner, then x x is less than a computable bound that is larger than × 10 54 5.4\!\times\!10^{54}. Our result shows that in fact x ≤ 8 x\leq 8.

###### Theorem 1.2.

The only powers of 2 2 that can be written as the sum of twenty-five or fewer distinct powers of 3 3 are:

 | 2 0 \displaystyle 2^{0} | = 3 0 \displaystyle=3^{0} |  |

 | 2 2 \displaystyle 2^{2} | = 3 0 + 3 1 \displaystyle=3^{0}+3^{1} |  |

 | 2 8 \displaystyle 2^{8} | = 3 0 + 3 1 + 3 2 + 3 5. \displaystyle=3^{0}+3^{1}+3^{2}+3^{5}. |  |

Put differently, if x ∉ { 0, 2, 8 } x\not\in\{0,2,8\} then the base- 3 3 representation of 2 x 2^{x} will contain either at least one 2 2, or at least twenty-six 1 1 s. This provides a tiny bit of confirmation for a conjecture of Erdős [15, Problem 1, p. 67], which states that the only powers of 2 2 whose base- 3 3 representations contain only 0 0 s and 1 1 s are the three examples given in Theorem 1.2. (For work on Erdős’s conjecture and closely related problems, see for example [5, 14, 17, 18] and the papers these articles cite.)

Theorems 1.1 and 1.2 can be expressed in terms of exponential Diophantine equations. In particular, Theorem 1.1 gives us all solutions of

(1) |  | 3 x = 2 a 1 + ⋯ + 2 a n, x ≥ 0, 0 ≤ a 1 < ⋯ < a n 3^{x}=2^{a_{1}}+\cdots+2^{a_{n}},\qquad x\geq 0,\quad 0\leq a_{1}<\cdots<a_{n} |  |

for n ≤ 22 n\leq 22, and Theorem 1.2 gives us all solutions to

(2) |  | 2 x = 3 a 1 + ⋯ + 3 a n, x ≥ 0, 0 ≤ a 1 < ⋯ < a n 2^{x}=3^{a_{1}}+\cdots+3^{a_{n}},\qquad x\geq 0,\quad 0\leq a_{1}<\cdots<a_{n} |  |

for n ≤ 25 n\leq 25.

Our method for solving equations ( 1) and ( 2) involves considering the equations modulo M M for a sequence of well-chosen moduli M M, each one dividing the next. We will postpone our discussion of what “well-chosen” means, and for now we will simply illustrate our method with an example.

Let us look at the case n = 3 n=3 of equation ( 1). We start by considering the related problem of writing a power of 3 3 as the sum of three powers of 2 2 in the finite ring 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}} for M 1 = 5440 = 2 6 ⋅ 5 ⋅ 17 M_{1}=5440=2^{6}\cdot 5\cdot 17, where we no longer insist that the powers of 2 2 be distinct. The following diagram enumerates the powers of 2 2 modulo M 1 M_{1}; here the arrows indicate multiplication by 2 2.

(3) |  | 1 \textstyle{1} 2 \textstyle{2} 4 \textstyle{4} 8 \textstyle{8} 16 \textstyle{16} 32 \textstyle{32} 64 \textstyle{64} 128 \textstyle{128} 256 \textstyle{256} 512 \textstyle{512} 1024 \textstyle{1024} 2048 \textstyle{2048} 4096 \textstyle{4096} 2752 \textstyle{2752} |  |

We see there are 14 14 distinct powers of 2 2 modulo M 1 M_{1}, and likewise we find that there are 16 16 distinct powers of 3 3. Using a computer to enumerate sums of three powers of 2 2 in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}}, we find that (up to the order of the summands) there are only three ways to write a power of 3 3 in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}} as a sum of three powers of 2 2:

(4) |  | 3 1 \displaystyle 3^{1} | ≡ 2 0 + 2 0 + 2 0 mod M 1 \displaystyle\equiv 2^{0}+2^{0}+2^{0}\bmod M_{1} |  |

(5) |  | 3 2 \displaystyle 3^{2} | ≡ 2 0 + 2 2 + 2 2 mod M 1 \displaystyle\equiv 2^{0}+2^{2}+2^{2}\bmod M_{1} |  |

(6) |  | 3 4 \displaystyle 3^{4} | ≡ 2 0 + 2 4 + 2 6 mod M 1. \displaystyle\equiv 2^{0}+2^{4}+2^{6}\bmod M_{1}. |  |

For each of the summands 2 i 2^{i} on the right-hand side of one of these equations, we can ask for the exponents b b such that 2 b ≡ 2 i mod M 1 2^{b}\equiv 2^{i}\bmod M_{1}. Looking at diagram ( 3), we see that for i = 0, 2 i=0,2, and 4 4, the only exponent b b with 2 b ≡ 2 i mod M 1 2^{b}\equiv 2^{i}\bmod M_{1} is i i itself, because 1 1, 4 4, and 16 16 are all on the “tail” of the diagram. On the other hand, the exponents b b with 2 b ≡ 2 6 mod M 1 2^{b}\equiv 2^{6}\bmod M_{1} are { 6, 14, 22, 30, … } = { 6 + 8 ​ j: j ≥ 0 } \{6,14,22,30,\ldots\}={\{6+8j:j\geq 0\}}, because the “loop” part of diagram ( 3) goes around in a cycle of 8 8 steps.

Every solution to equation ( 1) with n = 3 n=3 must reduce modulo M 1 M_{1} to one of the three equations ( 4), ( 5), or ( 6). However, no solution to equation ( 1) can reduce to ( 4), because the summands in ( 1) would have to be 2 0 2^{0}, 2 0 2^{0}, and 2 0 2^{0}, which are not distinct. Likewise, no solution to equation ( 1) can reduce modulo M 1 M_{1} to ( 5), because two of the summands in ( 1) would have to be 2 2 2^{2}. Therefore, every solution to equation ( 1) with n = 3 n=3 reduces modulo M 1 M_{1} to ( 6), and we see that two of the summands in ( 1) must be 2 0 2^{0} and 2 4 2^{4}.

Now we consider information modulo M 2 = 2 7 ⋅ 5 ⋅ 17 ⋅ 257 M_{2}=2^{7}\cdot 5\cdot 17\cdot 257. If a solution to equation ( 1) reduces modulo M 1 M_{1} to ( 6), what can it reduce to modulo M 2 M_{2}? There are 16 16 powers of 3 3 in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} that reduce to 3 4 3^{4} in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}}, namely 3 4, 3 4 + 16, …, 3 4 + 15 ⋅ 16 3^{4},3^{4+16},\ldots,3^{4+15\cdot 16}, and there are 3 3 powers of 2 2 in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} that reduce to 2 6 2^{6} in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}}, namely 2 6 2^{6}, 2 14 2^{14}, and 2 22 2^{22}. We check that in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} neither 2 0 + 2 4 + 2 14 2^{0}+2^{4}+2^{14} nor 2 0 + 2 4 + 2 22 2^{0}+2^{4}+2^{22} is equal to any of the possible powers of 3 3. However, 3 4 ≡ 2 0 + 2 4 + 2 6 3^{4}\equiv 2^{0}+2^{4}+2^{6} in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}}.

Therefore, every solution to equation ( 1) with n = 3 n=3 must reduce modulo M 2 M_{2} to the congruence 3 4 ≡ 2 0 + 2 4 + 2 6 mod M 2 3^{4}\equiv 2^{0}+2^{4}+2^{6}\bmod M_{2}. But we check that 2 0 2^{0}, 2 4 2^{4}, and 2 6 2^{6} lie on the tail of the analog of diagram ( 3) for M 2 M_{2}, so the only powers of 2 2 in the integers that reduce to 2 0 2^{0}, 2 4 2^{4}, and 2 6 2^{6} modulo M 2 M_{2} are 2 0 2^{0}, 2 4 2^{4}, and 2 6 2^{6} themselves. We see that if there is a solution to equation ( 1) with n = 3 n=3, the right-hand side must be 2 0 + 2 4 + 2 6 2^{0}+2^{4}+2^{6}. As it happens, in the integers this sum is equal to 3 4 3^{4}, so 3 4 = 2 0 + 2 4 + 2 6 3^{4}=2^{0}+2^{4}+2^{6} is the unique solution to equation ( 1) with n = 3 n=3.

This simple example displays the basic idea that we use to prove Theorem 1.1. For such a small example we could have *started*by considering the equation modulo M 2 M_{2}, instead of first looking modulo M 1 M_{1}, but for larger examples it is much more efficient to cut down the solution space by looking first at small moduli before building up to larger ones.

Solving exponential Diophantine equations using congruence arguments is not a new technique. In 1976, for example, Alex [2] used congruences to find all solutions to x + y = z x+y=z, where x x, y y, and z z are mutually coprime integers divisible by no prime larger than 7 7. In 1982, Brenner and Foster [10] presented a whole bestiary of exponential Diophantine equations that can be solved in this way. (They mention in particular that Alex found all solutions to our example 3 x = 2 a 1 + 2 a 2 + 2 a 3 3^{x}=2^{a_{1}}+2^{a_{2}}+2^{a_{3}} using “a few small moduli,” although this had been solved earlier by Pillai, as we discuss below.) In 2009, Ádám, Hajdu, and Luca [1] used a result of Erdős, Pomerance, and Schmutz [16] to show that for every finite set S S of primes and finite set A ⊂ 𝐙 A\subset{\mathbf{Z}} of coefficients, the number of integers less than x x that can be written as the sum of a fixed number of terms of the form a ​ s as, where a ∈ A a\in A and s ∈ 𝐙 s\in{\mathbf{Z}} is a product of powers of primes in S S, grows more slowly than a specific power of log ⁡ x \log x. Independently, in a 2011 paper [12] we studied representations of integers as sums of terms of the form ± 2 a ​ 3 b \pm 2^{a}3^{b}, which is the case A = { ± 1 } A=\{\pm 1\}, S = { 2, 3 } S=\{2,3\} of the problem studied in [1]. We presented one way of finding moduli M M that could be used to prove that certain integers cannot be represented by a given number of such terms, and we used the same result of Erdős, Pomerance, and Schmutz to show that there is a positive constant c c such that infinitely many integers n n cannot be written as a sum of fewer than c ​ log ⁡ n / ( log ⁡ log ⁡ n ​ log ⁡ log ⁡ log ⁡ n) c\log n/(\log\log n\log\log\log n) such terms.

In 2016 Bertók and Hajdu [7] studied exponential Diophantine equations in general, again using arguments based on [16], and they conjectured that if an exponential Diophantine equation has only a finite number of solutions 2 2 2 The statement of the conjecture [7, p. 849] only applies to Diophantine equations with *no*solutions, but later in the paper the authors show how the conjecture, if true, can be applied to equations that have finitely many solutions. and satisfies some other natural restrictions, then there is an integer M M such that the solutions to the equation modulo M M lift uniquely to the solutions in 𝐙 {\mathbf{Z}}. In a later paper [8] the same authors generalized this conjecture to number fields. One can view our work in this paper as providing evidence in support of the Bertók–Hajdu conjectures.

Our main contribution in this paper is the method we describe for choosing a sequence of moduli that allows us to refine the collection of solutions modulo M M, for larger and larger M M, until every solution modulo M M can be lifted to at most one solution in the integers. Our moduli are chosen in a careful order that makes each refinement step computationally feasible. The closest predecessor to our technique seems to be the method used by Bertók and Hajdu in [7], in which they choose a modulus M M and then piece together information gleaned from solutions to the original Diophantine equation modulo the prime power divisors of M M. Another new observation in this paper appears in Section 3, where we show that any modulus M M that provides us with all solutions to equation ( 1) or ( 2) must satisfy an unexpected condition.

We study the problem of writing powers of 2 2 as sums of distinct powers of 3 3, as well as the complementary problem of writing powers of 3 3 as sums of distinct powers of 2 2, for several reasons. First, these problems are simply-stated and natural. Second, we wanted to see what we could say about Erdős’s conjecture. Third, we were curious how far the modular methods discussed by Brenner and Foster can be pushed, since even modest laptop computers are much more powerful than anything available at the time their paper was written. And finally, we hope to bring these straightforward modular techniques to the attention of the community of mathematicians who are interested in exponential Diophantine equations.

As a historical note, we observe that the solutions to the case n = 2 n=2 of equations ( 1) and ( 2) were determined nearly seven centuries ago by Levi ben Gerson [4], who showed that the only pairs of integers of the form 2 r ​ 3 s 2^{r}3^{s} that differ by 1 1 are ( 1, 2) (1,2), ( 2, 3) (2,3), ( 3, 4) (3,4), and ( 8, 9) (8,9). A paraphrase of ben Gerson’s argument, more legible 3 3 3 The adjective is chosen with intention. Follow the link in the bibliography to understand why. than [4], is given in [11, Appendice, pp. 183–191]. One way to prove ben Gerson’s theorem is to observe that every solution to ben Gerson’s problem is a solution to the case n = 2 n=2 of either equation ( 1) or equation ( 2), and then to consider those two equations modulo 80 80.

In 1945, Pillai [19] found all solutions to ± ( 2 x − 3 y) = 2 X + 3 Y \pm(2^{x}-3^{y})=2^{X}+3^{Y}; taking either x x or y y to be 0 0 leads to the solutions for the case n = 3 n=3 of equations ( 1) and ( 2). Between 2011 and 2013, Bennett, Bugeaud, and Mignotte [5, 6] used linear forms in two logarithms to find all perfect powers whose binary representations have at most four bits equal to 1 1 (extending a result of Szalay [22] that gives all perfect squares with at most three bits equal to 1 1), and this solves the case n = 4 n=4 of equation ( 1). These are all of the previous solutions to cases of equations ( 1) and ( 2) that we are aware of; however, the paper of Bertók and Hajdu [7] discussed earlier includes solutions to many very similar equations, including, for example, finding all powers of 17 17 that can be expressed as the sum of nine distinct powers of 5 5. Surely their methods could have been used to solve some more instances of equations ( 1) and ( 2).

The structure of this paper is as follows: In Section 2 we briefly review some notation. In Section 3 we observe that in some situations there will necessarily be solutions to equations ( 1) or ( 2) modulo M M that are not reductions of solutions in the integers, unless some specific conditions on M M hold. These conditions shape our strategy of choosing a specific sequence of moduli to use in the proofs of Theorems 1.1 and 1.2. In Section 4 we give examples of two different ways of lifting solutions to ( 1) modulo M 1 M_{1} to solutions modulo M 2 M_{2}, suitable for two different circumstances. These examples help clarify the process by which we proved Theorems 1.1 and 1.2. We present the proofs of these theorem in Sections 5 and 6.

The programs we used to complete our calculations were written in Magma [9] and are available as supplementary material attached to the ArXiv version of this paper [13]. They are also available on the second author’s web site.

### Acknowledgments

We are grateful to Lajos Hajdu for his comments on an earlier version of this paper, and to the anonymous referees for their helpful suggestions.

## 2. Notation and conventions

In this paper we will often want to count or enumerate the number of solutions to an exponential Diophantine equation modulo M M, but there is some natural ambiguity as to what this might mean. For instance, there are infinitely many pairs of integers x ≥ 0 x\geq 0 and y ≥ 0 y\geq 0 for which the congruence 3 x ≡ 2 y + 5 mod 28 3^{x}\equiv 2^{y}+5\bmod 28 holds, but for every such x x and y y we have 3 x ≡ 9 mod 28 3^{x}\equiv 9\bmod 28 and 2 y ≡ 1 mod 28 2^{y}\equiv 1\bmod 28, so it might not be unreasonable to say that there is only one solution. In order to avoid any confusion, we remove this ambiguity by adopting the following convention.

###### Convention 2.1.

When we count or enumerate solutions to an exponential Diophantine equation modulo M M, we will consider two solutions to be the same if the corresponding terms in the equation are congruent modulo M M.

This means, for example, that for the congruence 3 x ≡ 2 y + 5 mod 28 3^{x}\equiv 2^{y}+5\bmod 28 we consider the solutions ( x, y) = ( 2, 2) (x,y)=(2,2), ( x, y) = ( 8, 2) (x,y)=(8,2), and ( x, y) = ( 8, 5) (x,y)=(8,5) to be the same, because in each case 3 x ≡ 9 mod 28 3^{x}\equiv 9\bmod 28 and 2 y ≡ 4 mod 28 2^{y}\equiv 4\bmod 28.

This convention does have one drawback, which is that for some exponential Diophantine equation modulo M M, there truly are only finitely many integer solutions. For example, the only integers x ≥ 0 x\geq 0 and y ≥ 0 y\geq 0 such that 3 x ≡ 2 y + 5 mod 216 3^{x}\equiv 2^{y}+5\bmod 216 are x = 2 x=2 and y = 2 y=2. This distinction will in fact be important to us, so we make the following definition.

###### Definition 2.2.

Let M > 0 M>0 be an integer and p p a prime. We say that a power of p p, say p i p^{i}, is *determinate*modulo M M if the only integer b ≥ 0 b\geq 0 with p b ≡ p i mod M p^{b}\equiv p^{i}\bmod M is b = i b=i; otherwise, we say that p i p^{i} is an *indeterminate*power of p p modulo M M.

Thus, we will say that the congruence 3 x ≡ 2 y + 5 mod 28 3^{x}\equiv 2^{y}+5\bmod 28 has one solution, namely 3 2 ≡ 2 2 + 5 mod 28 3^{2}\equiv 2^{2}+5\bmod 28, but that 3 2 3^{2} is an indeterminate power of 3 3 modulo 28 28 and 2 2 2^{2} is an indeterminate power of 2 2 modulo 28 28. On the other hand, 3 x ≡ 2 y + 5 mod 216 {3^{x}\equiv 2^{y}+5\bmod 216} also has only one solution, but the power of 3 3 and the power of 2 2 involved are both determinate.

Given a prime p p and an integer M > 0 M>0, we can construct a diagram like diagram ( 3) of the powers of p p modulo M M. Note that a determinate power of p p modulo M M is exactly a power of p p that lies on the tail of this diagram, and a straightforward argument shows that for i ≥ 0 i\geq 0, the integer p i p^{i} is a determinate power of p p modulo M M if and only if M M is divisible by p i + 1 p^{i+1}.

Recall that if M M is a positive integer then the group of units in the ring 𝐙 / M ​ 𝐙 {\mathbf{Z}}/M{\mathbf{Z}} has order φ ⁡ ( M) \varphi(M), where φ \varphi is the Euler φ \varphi -function, which can be computed using the formula φ ⁡ ( n) = n ​ ∏ p | n ( 1 − 1 / p) \varphi(n)=n\prod_{p\mid n}(1-1/p); see [3, §2.3, §2.5]. Also, if M M is an odd prime power then the group of units in 𝐙 / M ​ 𝐙 {\mathbf{Z}}/M{\mathbf{Z}} is cyclic [3, Theorem 10.4, p. 207].

For every prime p p, we let v p v_{p} be the *p p -adic valuation*function, so that v p ​ ( M) v_{p}(M) is the largest x x such that p x p^{x} divides M M. And lastly, we set some notation related to the behavior of the numbers 2 2 and 3 3 in finite rings.

###### Notation 2.3.

Let M M be a positive integer and write M = 2 u ​ 3 v ​ M ′ M=2^{u}3^{v}M^{\prime}, where u = v 2 ​ ( M) u=v_{2}(M) and v = v 3 ​ ( M) v=v_{3}(M), so that M ′ M^{\prime} is coprime to 6 6.

- •

We let O 2 ​ ( M) O_{2}(M) be the multiplicative order of 2 2 in the ring 𝐙 / 3 v ​ M ′ ​ 𝐙 {\mathbf{Z}}/3^{v}M^{\prime}{\mathbf{Z}}.

- •

We let O 2 ′ ​ ( M) O_{2}^{\prime}(M) be the multiplicative order of 2 2 in the ring 𝐙 / M ′ ​ 𝐙 {\mathbf{Z}}/M^{\prime}{\mathbf{Z}}.

- •

We let O 3 ​ ( M) O_{3}(M) be the multiplicative order of 3 3 in the ring 𝐙 / 2 u ​ M ′ ​ 𝐙 {\mathbf{Z}}/2^{u}M^{\prime}{\mathbf{Z}}.

- •

We let O 3 ′ ​ ( M) O_{3}^{\prime}(M) be the multiplicative order of 3 3 in the ring 𝐙 / M ′ ​ 𝐙 {\mathbf{Z}}/M^{\prime}{\mathbf{Z}}.

We see, for example, that there are v 2 ​ ( M) + O 2 ​ ( M) v_{2}(M)+O_{2}(M) elements in the tail-and-loop diagram of the powers of 2 2 modulo M M, with v 2 ​ ( M) v_{2}(M) in the tail and O 2 ​ ( M) O_{2}(M) in the loop. Similarly, there are v 3 ​ ( M) + O 3 ​ ( M) v_{3}(M)+O_{3}(M) elements in the tail-and-loop diagram of the powers of 3 3 modulo M M.

## 3. Extraneous solutions to congruences

The basic heuristic behind our strategy for solving instances of equations ( 1) and ( 2) is that if M M is large and there are very few powers of 2 2 in 𝐙 / M ​ 𝐙 {\mathbf{Z}}/M{\mathbf{Z}} and very few powers of 3 3 in 𝐙 / M ​ 𝐙 {\mathbf{Z}}/M{\mathbf{Z}}, then there should be very few “extraneous” solutions to equations ( 1) or ( 2) modulo M M — that is, solutions that are not the reduction modulo M M of a solution in the integers. If M M is divisible by sufficiently high powers of 2 2 and/or 3 3, we can hope that every solution modulo M M to equation ( 1) or ( 2) will involve only determinate powers of 2 2 or of 3 3 modulo M M (where *determinate*is as defined in Section 2). If this is the case, then each solution will lift uniquely to the integers, if it lifts at all. However, it turns out that for many moduli M M, if there is *any*solution to one of these equations, then there is *also*a solution that includes indeterminate powers of 2 2 and of 3 3.

For example, we saw in the introduction that if M 1 = 5440 = 2 6 ⋅ 5 ⋅ 17 M_{1}=5440=2^{6}\cdot 5\cdot 17 then the equation 3 x ≡ 2 a 1 + 2 a 2 + 2 a 3 mod M 1 3^{x}\equiv 2^{a_{1}}+2^{a_{2}}+2^{a_{3}}\bmod M_{1} has the three solutions given by ( 4), ( 5), and ( 6), and we see that ( 6) involves an indeterminate power of 2 2 (and of 3 3). If we look at the same equation modulo M 2 M_{2}, where M 2 = 2 ​ M 1 = 2 7 ⋅ 5 ⋅ 17 M_{2}=2M_{1}=2^{7}\cdot 5\cdot 17, then we find four solutions, including 3 20 ≡ 2 0 + 2 4 + 2 14 3^{20}\equiv 2^{0}+2^{4}+2^{14}, and this involves indeterminate powers of 2 2 and of 3 3 modulo M 2 M_{2}. When we look at the same equation modulo M 3 M_{3}, where M 3 = 41 ​ M 2 = 2 7 ⋅ 5 ⋅ 17 ⋅ 41 M_{3}=41M_{2}=2^{7}\cdot 5\cdot 17\cdot 41, there is once again a solution with indeterminate powers of 2 2 and 3 3, namely 3 20 ≡ 2 0 + 2 4 + 2 46 3^{20}\equiv 2^{0}+2^{4}+2^{46}. And the same happens yet again when we work modulo M 4 M_{4}, where M 4 = 193 ​ M 3 = 2 7 ⋅ 5 ⋅ 17 ⋅ 41 ⋅ 193 M_{4}=193M_{3}=2^{7}\cdot 5\cdot 17\cdot 41\cdot 193.

And yet in the introduction, when we considered solutions to 3 x ≡ 2 a 1 + 2 a 2 + 2 a 3 3^{x}\equiv 2^{a_{1}}+2^{a_{2}}+2^{a_{3}} modulo 2 7 ⋅ 5 ⋅ 17 ⋅ 257 2^{7}\cdot 5\cdot 17\cdot 257, we did *not*wind up with extraneous solutions. What is the difference between 2 7 ⋅ 5 ⋅ 17 ⋅ 257 2^{7}\cdot 5\cdot 17\cdot 257 and 2 7 ⋅ 5 ⋅ 17 ⋅ 41 ⋅ 193 2^{7}\cdot 5\cdot 17\cdot 41\cdot 193?

The following proposition, which uses Notation 2.3, explains one way in which solutions with indeterminate powers of 2 2 or 3 3 can arise, and suggests a condition that we will want to impose on the moduli we use.

###### Lemma 3.1.

Let M M be a positive integer. Suppose x > 2 x>2, y > 0 y>0, and c c are integers such that 3 y ≡ c + 2 x mod M 3^{y}\equiv c+2^{x}\bmod M. If O 3 ′ ​ ( M) O_{3}^{\prime}(M) is not divisible by 2 x − 1 2^{x-1} and O 2 ′ ​ ( M) O_{2}^{\prime}(M) is not divisible by 3 y 3^{y}, then there are integers x ′ ≥ 0 x^{\prime}\geq 0 and y ′ ≥ 0 y^{\prime}\geq 0 such that

1. (a)

3 y ′ ≡ c + 2 x ′ mod M 3^{y^{\prime}}\equiv c+2^{x^{\prime}}\bmod M,

2. (b)

2 x ′ 2^{x^{\prime}} is an indeterminate power of 2 2 modulo M M, and

3. (c)

3 y ′ 3^{y^{\prime}} is an indeterminate power of 3 3 modulo M M.

Lemma 3.1 shows that in the example we presented in the introduction, it was necessary for us to use a modulus divisible by a prime (in our case, 257 257) for which either the order of 3 3 is divisible by 2 5 2^{5} or the order of 2 2 is divisible by 3 4 3^{4}. Since 3 4 = 2 0 + 2 4 + 2 6 {3^{4}=2^{0}+2^{4}+2^{6}}, if we use a modulus M M that is divisible by 2 7 2^{7} (so that 2 0 2^{0}, 2 4 2^{4}, and 2 6 2^{6} are determinate powers of 2 2 modulo M M), Lemma 3.1 shows that there will be other, extraneous, solutions modulo M M unless M M is divisible by such a prime.

###### Proof of Lemma 3.1.

Write M = 2 u ​ 3 v ​ M ′ M=2^{u}3^{v}M^{\prime} where M ′ M^{\prime} is an integer coprime to 6 6, and set o 2 = O 2 ′ ​ ( M) o_{2}=O_{2}^{\prime}(M) and o 3 = O 3 ′ ​ ( M) o_{3}=O_{3}^{\prime}(M). First we claim that there is an integer s s such that y + s ​ o 3 > v y+so_{3}>v and 3 y + s ​ o 3 ≡ c mod 2 u 3^{y+so_{3}}\equiv c\bmod 2^{u}.

Suppose u ≤ x u\leq x, so that 3 y ≡ c mod 2 u 3^{y}\equiv c\bmod 2^{u}. We know that 3 s ≡ 1 mod 2 u 3^{s}\equiv 1\bmod 2^{u} if s s is a multiple of φ ⁡ ( 2 u) \varphi(2^{u}), so we can simply take s s to be a large enough multiple φ ⁡ ( 2 u) \varphi(2^{u}) so that y + s ​ o 3 > v y+so_{3}>v, and this s s meets the conditions of our claim.

Suppose u > x u>x. Then M M is even, and since c c differs from 3 y 3^{y} by a multiple of the even number M M, we see that c c must be odd. Therefore there is an integer d d such that c ​ d ≡ 1 mod 2 u cd\equiv 1\bmod 2^{u}. Choose such a d d and consider the integer z = 1 + 2 x ​ d z=1+2^{x}d, which is congruent to 1 mod 8 1\bmod 8 because x > 2 x>2. If we apply part 1 of Lemma 3.2 (below) to this z z, we find that there is an integer e 0 e_{0}, divisible by 2 x − 2 2^{x-2}, such that every integer e e with e ≡ e 0 mod 2 u − 2 e\equiv e_{0}\bmod 2^{u-2} satisfies 3 e ≡ 1 + 2 x ​ d mod 2 u 3^{e}\equiv 1+2^{x}d\bmod 2^{u}. By assumption, the highest power of 2 2 that divides o 3 o_{3} is at most 2 x − 2 2^{x-2}. Therefore there is an integer s s such that s ​ o 3 ≡ − e 0 mod 2 u − 2 so_{3}\equiv-e_{0}\bmod 2^{u-2}, and we can choose such an s s that is large enough so that y + s ​ o 3 > v y+so_{3}>v.

We have 3 − s ​ o 3 ≡ 1 + 2 x ​ d mod 2 u 3^{-so_{3}}\equiv 1+2^{x}d\bmod 2^{u}. Multiplying both sides of this congruence by c ​ 3 s ​ o 3 c\,3^{so_{3}} gives c ≡ ( c + 2 x) ​ 3 s ​ o 3 mod 2 u {c\equiv(c+2^{x})3^{so_{3}}\bmod 2^{u}}, and since c + 2 x ≡ 3 y mod M c+2^{x}\equiv 3^{y}\bmod M and hence also modulo 2 u 2^{u}, we find that c ≡ 3 y + s ​ o 3 mod 2 u c\equiv 3^{y+so_{3}}\bmod 2^{u}. Thus, this s s has the properties we desire, and we have proven our claim.

Similarly, using part 2 of Lemma 3.2, we can show that there is an integer r r such that x + r ​ o 2 > u x+ro_{2}>u and 2 x + r ​ o 2 ≡ − c mod 3 v 2^{x+ro_{2}}\equiv-c\bmod 3^{v}.

Let x ′ = x + r ​ o 2 x^{\prime}=x+ro_{2} and let y ′ = y + s ​ o 3 y^{\prime}=y+so_{3}. We claim that this x ′ x^{\prime} and y ′ y^{\prime} satisfy conditions (a), (b), and (c) from the lemma. It is easy to check conditions (b) and (c) because x ′ > u x^{\prime}>u and y ′ > v y^{\prime}>v by construction. To check condition (a), we use the Chinese Remainder Theorem: It suffices to check that 3 y ′ ≡ c + 2 x ′ 3^{y^{\prime}}\equiv c+2^{x^{\prime}} modulo M ′ M^{\prime}, modulo 2 u 2^{u}, and modulo 3 v 3^{v}.

We have 2 o 2 ≡ 1 mod M ′ 2^{o_{2}}\equiv 1\bmod M^{\prime} and 3 o 3 ≡ 1 mod M ′ 3^{o_{3}}\equiv 1\bmod M^{\prime} by the definitions of o 2 o_{2} and o 3 o_{3}, so 3 y ′ ≡ 3 y mod M ′ 3^{y^{\prime}}\equiv 3^{y}\bmod M^{\prime} and 2 x ′ ≡ 2 x mod M ′ 2^{x^{\prime}}\equiv 2^{x}\bmod M^{\prime}, and we have 3 y ′ ≡ c + 2 x ′ mod M ′ 3^{y^{\prime}}\equiv c+2^{x^{\prime}}\bmod M^{\prime}.

We have 2 x ′ ≡ 0 mod 2 u 2^{x^{\prime}}\equiv 0\bmod 2^{u} because x + r ​ o 2 > u x+ro_{2}>u by construction. Since 3 y ′ ≡ 3 y + s ​ o 3 ≡ c mod 2 u 3^{y^{\prime}}\equiv 3^{y+so_{3}}\equiv c\bmod 2^{u}, we have 3 y ′ ≡ c + 2 x ′ mod 2 u 3^{y^{\prime}}\equiv c+2^{x^{\prime}}\bmod 2^{u}.

The same reasoning shows that we have 3 y ′ ≡ 0 mod 3 v 3^{y^{\prime}}\equiv 0\bmod 3^{v}, and since 2 x ′ ≡ 2 x + r ​ o 2 ≡ − c mod 3 v 2^{x^{\prime}}\equiv 2^{x+ro_{2}}\equiv-c\bmod 3^{v}, we have 3 y ′ ≡ c + 2 x ′ mod 3 v {3^{y^{\prime}}\equiv c+2^{x^{\prime}}\bmod 3^{v}}. This shows that condition (a) holds for this x ′ x^{\prime} and y ′ y^{\prime}, and completes the proof of the lemma. ∎

###### Lemma 3.2.

1. (1)

Let z z be an integer with z ≡ 1 mod 8 z\equiv 1\bmod 8. For every integer u ≥ 3 u\geq 3 there is an integer e 0 e_{0} such that the integers e e that satisfy 3 e ≡ z mod 2 u 3^{e}\equiv z\bmod 2^{u} are precisely the integers e e that satisfy e ≡ e 0 mod 2 u − 2 e\equiv e_{0}\bmod 2^{u-2}. If x ≤ u x\leq u is an integer with z ≡ 1 mod 2 x z\equiv 1\bmod 2^{x}, then e 0 e_{0} is divisible by 2 x − 2 2^{x-2}.

2. (2)

Let z z be an integer with z ≡ 1 mod 3 z\equiv 1\bmod 3. For every integer v ≥ 1 v\geq 1 there is an integer e 0 e_{0} such that the integers e e that satisfy 2 e ≡ z mod 3 v 2^{e}\equiv z\bmod 3^{v} are precisely the integers e e that satisfy e ≡ e 0 mod 2 ⋅ 3 v − 1 e\equiv e_{0}\bmod 2\cdot 3^{v-1}. If y ≤ v y\leq v is an integer with z ≡ 1 mod 3 y z\equiv 1\bmod 3^{y}, then e 0 e_{0} is divisible by 2 ⋅ 3 y − 1 2\cdot 3^{y-1}.

###### Proof.

For statement 1: We leave the reader to show that for every u ≥ 3 u\geq 3, the order of 3 3 modulo 2 u 2^{u} is 2 u − 2 2^{u-2}. (The proof can be modeled after the proof of [3, Theorem 10.11, p. 218].) Since there are 2 u − 1 2^{u-1} units in 𝐙 / 2 u ​ 𝐙 {\mathbf{Z}}/2^{u}{\mathbf{Z}}, and the order of 3 3 is half of this, it follows that half of the units are powers of 3 3. A power of 3 3 is never congruent to 5 5 or 7 7 modulo 8 8, and this accounts for half of the units. Therefore, every unit that is 1 1 or 3 3 modulo 8 8 is a power of 3 3. Thus, there is an e 0 e_{0} such that 3 e 0 ≡ z 3^{e_{0}}\equiv z. The fact that 3 e ≡ z mod 2 u 3^{e}\equiv z\bmod 2^{u} if and only if e ≡ e 0 mod 2 u − 2 e\equiv e_{0}\bmod 2^{u-2} is simply a consequence of the fact that the order of 3 3 modulo 2 u 2^{u} is 2 u − 2 2^{u-2}.

If z ≡ 1 mod 2 x z\equiv 1\bmod 2^{x} with x ≤ u x\leq u, then 3 e 0 ≡ 1 mod 2 x 3^{e_{0}}\equiv 1\bmod 2^{x}, so e 0 e_{0} is a multiple of the order of 3 3 modulo 2 x 2^{x}, and hence e 0 e_{0} is divisible by 2 x − 2 2^{x-2}.

The proof of statement 2 is analogous, and we leave it to the reader. ∎

When we look at cases of equation ( 1) with larger values of n n, we will find that Lemma 3.1 tells us that we will need to include information gleaned from moduli divisible by primes p p such that the order of 3 3 modulo p p is divisible by quite large powers of 2 2. In Section 5 we show how we can work our way up to such moduli.

## 4. Lifting solutions

Our proofs of Theorems 1.1 and 1.2 are computational. In each proof, we consider a sequence of moduli M 1, M 2, … M_{1},M_{2},\ldots, each dividing the next. Roughly speaking, we first compute the solutions to equation ( 1) or ( 2) modulo M 1 M_{1}; then for each i > 1 i>1 in turn we “lift” the solutions modulo M i − 1 M_{i-1} to solutions modulo M i M_{i}. We stop when we have reached an M i M_{i} where all of the summands that appear on the right-hand side of the solutions modulo M i M_{i} are determinate (in the sense defined in Section 2); at that point, each solution modulo M i M_{i} can be lifted uniquely to a solution in the integers, if it lifts to a solution at all.

This strategy depends on our having efficient methods for lifting a solution modulo M i − 1 M_{i-1} to a solution modulo M i M_{i}. In Section 5 we will spell out our methods more formally, but in this section we would like to give two examples to help make the methods more clear. For the sake of exposition, we will focus on finding solutions to equation ( 1) modulo M M for various M M, and as we did in the introduction, we will ignore the requirement that the summands be distinct.

As an example of one extreme case of the lifting problem, let M 1 = 439 M_{1}=439 and let n = 12 n=12 and consider the following solution to equation ( 1) modulo M 1 M_{1}:

(7) |  | 3 57 ≡ 2 0 + 2 1 + 2 11 + 2 12 + 2 15 + 2 16 + 2 26 + 2 27 + 2 37 + 2 57 + 2 65 + 2 68. 3^{57}\equiv 2^{0}+2^{1}+2^{11}+2^{12}+2^{15}+2^{16}+2^{26}+2^{27}+2^{37}+2^{57}+2^{65}+2^{68}. |  |

Let p p be the prime 9361973132609 9361973132609 and let M 2 = p ​ M 1 M_{2}=pM_{1}. We will try to find a lift of the solution ( 7) to a solution modulo M 2 M_{2}. We compute that the graph of the powers of 2 2 modulo M 1 M_{1} forms a loop of cycle length 73 73 with no tail… and we compute that the graph of powers of 2 2 modulo M 2 M_{2} is *also*a tailless loop of cycle length 73 73. That means that there is *exactly one*power of 2 2 in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} that reduces to a given power of 2 2 in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}}. If we can lift equation ( 7) to a solution modulo M 2 M_{2}, then the right-hand side of the lifted solution will have to be

 | 2 0 + 2 1 + 2 11 + 2 12 + 2 15 + 2 16 + 2 26 + 2 27 + 2 37 + 2 57 + 2 65 + 2 68 mod M 2. 2^{0}+2^{1}+2^{11}+2^{12}+2^{15}+2^{16}+2^{26}+2^{27}+2^{37}+2^{57}+2^{65}+2^{68}\bmod M_{2}. |  |

If we let z z be this sum, then to determine whether there is a lift of equation ( 7) to a solution modulo M 2 M_{2}, we simply have to determine whether there is an x x such that 3 x ≡ z mod M 2 3^{x}\equiv z\bmod M_{2}.

It turns out that the graph of powers of 3 3 modulo M 2 M_{2} is a tailless loop with cycle length p − 1 = 9361973132608 p-1=9361973132608, so we definitely do *not*want to find x x (if it exists) by enumeration. Instead, we can find x x by using discrete logarithms.

If there is an x x with 3 x ≡ z mod M 2 3^{x}\equiv z\bmod M_{2}, then that same x x satisfies 3 x ≡ z mod p 3^{x}\equiv z\bmod p for the prime p = M 2 / M 1 p=M_{2}/M_{1}. We can find an x x that satisfies this congruence if and only if z ∈ ( 𝐙 / p ​ 𝐙) ∗ z\in({\mathbf{Z}}/p{\mathbf{Z}})^{*} lies in the subgroup of ( 𝐙 / p ​ 𝐙) ∗ ({\mathbf{Z}}/p{\mathbf{Z}})^{*} generated by 3 3. Using the computer algebra package Magma, we find that in fact 3 3 generates the whole group of units, and Magma very quickly computes a discrete logarithm of z z with respect to 3 3 — that is, an integer x x with 3 x ≡ z mod p 3^{x}\equiv z\bmod p. In fact, every integer x x satisfying

(8) |  | x ≡ 3976447101915 mod ( p − 1) x\equiv 3976447101915\bmod(p-1) |  |

will give a solution to this congruence.

In order for x x to give a solution modulo M 2 M_{2}, we also need to have 3 x ≡ z mod M 1 3^{x}\equiv z\bmod M_{1}. The graph of powers of 3 3 modulo M 1 M_{1} is a tailless loop with cycle length 146 146, and we find that for x x to solve this congruence modulo M 1 M_{1} we need to have x ≡ 57 mod 146 x\equiv 57\bmod 146.

But 146 146 is a divisor of p − 1 p-1, and reducing equation ( 8) modulo 146 146, we find that it becomes x ≡ 31 mod 146 x\equiv 31\bmod 146. This is incompatible with the congruence from the preceding paragraph, so there is no x x with 3 x ≡ z mod M 2 3^{x}\equiv z\bmod M_{2}. This shows that equation ( 7) cannot be lifted to a solution modulo M 2 M_{2}.

Let us turn to another example, which demonstrates a different approach to the lifting problem. We again take M 1 = 439 M_{1}=439 and start with the solution to equation ( 1) modulo M 1 M_{1} given by ( 7). This time, however, we take p = 1753 p=1753 and M 2 = p ​ M 1 M_{2}=pM_{1}. We will try to find a lift of the solution ( 7) to a solution modulo M 2 M_{2}.

The graph of powers of 2 2 modulo M 2 M_{2} is a tailless loop of cycle length 146 146, which is exactly twice as long as the cycle of powers of 2 2 modulo M 1 M_{1}. That means that there are *exactly two*powers of 2 2 modulo M 2 M_{2} that reduce to a given power of 2 2 modulo M 1 M_{1}. In particular, the two lifts to 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} of the element 2 i ∈ 𝐙 / M 1 ​ 𝐙 2^{i}\in{\mathbf{Z}}/M_{1}{\mathbf{Z}} are 2 i 2^{i} and 2 i + 73 2^{i+73}.

Similarly, we can also compute that there are six lifts of 3 57 ∈ 𝐙 / M 1 ​ 𝐙 3^{57}\in{\mathbf{Z}}/M_{1}{\mathbf{Z}} to powers of 3 3 in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}}, namely 3 57 3^{57}, 3 203 3^{203}, 3 349 3^{349}, 3 495 3^{495}, 3 641 3^{641}, and 3 787 3^{787}.

We see that every summand on the right-hand side of ( 7) has two lifts to 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}}, and the left-hand side has six lifts. In principle, we could compute all 6 ⋅ 2 12 = 24,576 6\cdot 2^{12}=24{,}576 lifts of the terms appearing in ( 7) and check to see which combinations of lifts give us an equality modulo M 2 M_{2}, but this would be inefficient… and for larger values of n n, it would become more and more inefficient.

Instead, we use a “meet in the middle” technique. We rewrite equation ( 7) to get the following congruence modulo M 1 M_{1}:

(9) |  | 3 57 − 2 0 − 2 1 − 2 11 − 2 12 − 2 15 ≡ 2 16 + 2 26 + 2 27 + 2 37 + 2 57 + 2 65 + 2 68. 3^{57}-2^{0}-2^{1}-2^{11}-2^{12}-2^{15}\equiv 2^{16}+2^{26}+2^{27}+2^{37}+2^{57}+2^{65}+2^{68}. |  |

There are 6 ⋅ 2 5 = 192 6\cdot 2^{5}=192 lifts to 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} of the terms appearing on the left-hand side of ( 9), and 2 7 = 128 2^{7}=128 lifts of the terms on the right-hand side. We compute the values (modulo M 2 M_{2}) of all of the left-hand lifts, and the values of all of the right-hand lifts, and then compare the two lists to see whether there are any values in common. (We can quickly find these common values if we sort each list first.) Each such common value w w gives us one (or more) lifts to 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} of ( 9), and hence also of ( 7). And clearly, all solutions to ( 1) modulo M 2 M_{2} that are lifts of ( 7) will arise in this way. In point of fact, for this particular example we found eight values of w w, from which we obtained eight solutions to ( 1) in 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}} that were lifts of ( 7).

The two techniques we have demonstrated here for lifting solutions of ( 1) modulo M 1 M_{1} to solutions modulo M 2 M_{2} are the basis for the procedure for proving Theorem 1.1 that we sketch in the following section.

## 5. Proof of Theorem 1.1

To prove Theorem 1.1 we consider the sequence of moduli M i M_{i}, where M i = ∏ j ≤ i m j M_{i}=\prod_{j\leq i}m_{j} for the factors m 1 m_{1}, …, m 64 m_{64} listed in Table , so that each M i M_{i} divides the next. As we explained in Section 4, roughly speaking we first compute the solutions to equation ( 1) in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}}; then, using the ideas sketched out in the examples in Section 4, we lift the solutions to 𝐙 / M 2 ​ 𝐙 {\mathbf{Z}}/M_{2}{\mathbf{Z}}, then to 𝐙 / M 3 ​ 𝐙 {\mathbf{Z}}/M_{3}{\mathbf{Z}}, then to 𝐙 / M 4 ​ 𝐙 {\mathbf{Z}}/M_{4}{\mathbf{Z}}, and so on, stopping when we have reached an M i M_{i} where all of the powers of 2 2 that appear in the solutions are determinate. If all the powers of 2 2 in a solution are determinate, the solution can be lifted uniquely to a solution in the integers, if it lifts to a solution at all.

To be more precise: For a given i i, we write M i = 2 u i ​ 3 v i ​ M i ′ M_{i}=2^{u_{i}}3^{v_{i}}M_{i}^{\prime} where M i ′ M_{i}^{\prime} is coprime to 6 6. As we noted in Section 2, there are u i + O 2 ​ ( M i) u_{i}+O_{2}(M_{i}) distinct powers of 2 2 modulo M i M_{i}, and v i + O 3 ​ ( M i) v_{i}+O_{3}(M_{i}) distinct powers of 3 3. For each M i M_{i} in turn, we set M = M i M=M_{i} and compute the solutions ( x, a 1, …, a n) (x,a_{1},\ldots,a_{n}) to

(10) |  | { 3 x ≡ 2 a 1 + ⋯ + 2 a n mod M 0 ≤ x < v + O 3 ​ ( M) 0 = a 1 ≤ ⋯ ≤ a n < u + O 2 ​ ( M), \begin{cases}&3^{x}\equiv 2^{a_{1}}+\cdots+2^{a_{n}}\bmod M\\ &0\leq x<v+O_{3}(M)\\ &0=a_{1}\leq\cdots\leq a_{n}<u+O_{2}(M),\end{cases} |  |

with the added condition that for every pair ( j, k) (j,k) of indices with j ≠ k j\neq k, if a j a_{j} and a k a_{k} are both less than u i u_{i}, then a j ≠ a k a_{j}\neq a_{k}. This last condition reflects the fact that if a < u i a<u_{i}, then 2 a 2^{a} is a determinate power of 2 2 in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}}, and the right-hand side exponents in the solutions to equation ( 1) are required to be distinct. (Note that the upper bounds given in ( 10) have the effect of keeping us in line with Convention 2.1.)

For M 1 = 2 4 ⋅ 7 ⋅ 73 M_{1}=2^{4}\cdot 7\cdot 73 we compute the solutions to ( 10) by brute force. The powers of 2 2 in 𝐙 / M 1 ​ 𝐙 {\mathbf{Z}}/M_{1}{\mathbf{Z}} are 2 0 2^{0} through 2 12 2^{12}. To every n n -tuple ( a 1, …, a n) (a_{1},\ldots,a_{n}) of exponents between 0 0 and 12 12 with 0 = a 1 ≤ ⋯ ≤ a n 0=a_{1}\leq\cdots\leq a_{n}, we can associate the 13 13 -tuple ( b 0, …, b 12) (b_{0},\ldots,b_{12}), where b i b_{i} is the number of a j a_{j} that are equal to i i. Then instead of enumerating all of the n n -tuples ( a 1, …, a n) (a_{1},\ldots,a_{n}), we can simply run through all of the 13 13 -tuples ( b 0, …, b 12) (b_{0},\ldots,b_{12}) of non-negative integers such that

 | b 0 + ⋯ + b 12 = n b_{0}+\cdots+b_{12}=n |  |

and

 | b 0 = 1, b 1 ≤ 1, b 2 ≤ 1, and ​ b 3 ≤ 1. b_{0}=1,\quad b_{1}\leq 1,\quad b_{2}\leq 1,\quad\text{and\ }b_{3}\leq 1. |  |

When we find such a 13 13 -tuple with the additional property that ∑ b j ​ 2 j \sum b_{j}2^{j} is congruent to 3 x 3^{x} modulo M 1 M_{1} for one of the 12 12 powers of 3 3 modulo M 1 M_{1}, we can compute the associated n n -tuple ( a 1, …, a n) (a_{1},\ldots,a_{n}) and add ( x, a 1, …, a n) (x,a_{1},\ldots,a_{n}) to our list of solutions of equation ( 10) with M = M 1 M=M_{1}. We obtain all solutions to the equation in this way.

Now suppose we have a list of solutions to ( 10) with M = M i − 1 M=M_{i-1}, and we want to create the list of solutions with M = M i M=M_{i}, where M i = m i ​ M i − 1 M_{i}=m_{i}M_{i-1}. Write M i = 2 u i ​ 3 v i ​ M i ′ M_{i}=2^{u_{i}}3^{v_{i}}M_{i}^{\prime} with M i ′ M_{i}^{\prime} coprime to 6 6. For each solution ( x, a 1, …, a n) (x,a_{1},\ldots,a_{n}) to the problem modulo M i − 1 M_{i-1}, we go through the following steps.

### Step One:

*Compute the powers of 2 2 in 𝐙 / M i ​ 𝐙 {\mathbf{Z}}/M_{i}{\mathbf{Z}} that lift the 2 a j ∈ 𝐙 / M i − 1 ​ 𝐙 2^{a_{j}}\in{\mathbf{Z}}/M_{i-1}{\mathbf{Z}}.*

For each j = 1, …, n j=1,\ldots,n, we compute a list A j A_{j} of the values of a ′ a^{\prime} with 0 ≤ a ′ < u i + O 2 ​ ( M i) 0\leq a^{\prime}<u_{i}+O_{2}(M_{i}) such that 2 a ′ ≡ 2 a j mod M i − 1 2^{a^{\prime}}\equiv 2^{a_{j}}\bmod M_{i-1}.

### Step Two:

*Compute the number of powers of 3 3 in 𝐙 / M i ​ 𝐙 {\mathbf{Z}}/M_{i}{\mathbf{Z}} that lift 3 x ∈ 𝐙 / M i − 1 ​ 𝐙 3^{x}\in{\mathbf{Z}}/M_{i-1}{\mathbf{Z}}.*

Let χ \chi denote the number of values of x ′ x^{\prime} with 0 ≤ x ′ < v i + O 3 ​ ( M i) 0\leq x^{\prime}<v_{i}+O_{3}(M_{i}) such that 3 x ′ ≡ 3 x mod M i − 1 3^{x^{\prime}}\equiv 3^{x}\bmod M_{i-1}. If 3 x 3^{x} is a determinate power of 3 3 modulo M i − 1 M_{i-1}, then χ = 1 \chi=1. If 3 x 3^{x} is an indeterminate power of 3 3 modulo M i M_{i}, then χ = O 3 ​ ( M i) / O 3 ​ ( M i − 1) \chi=O_{3}(M_{i})/O_{3}(M_{i-1}). And if 3 x 3^{x} is indeterminate modulo M i − 1 M_{i-1} but determinate modulo M i M_{i}, then χ = 1 + O 3 ​ ( M i) / O 3 ​ ( M i − 1) \chi=1+O_{3}(M_{i})/O_{3}(M_{i-1}).

### Step Three:

*Compute the lifted solutions.*

We compute lifted solutions in one of two ways; to decide between the two methods, we check to see whether χ > ∏ j = 1 n #​ A j \chi>\prod_{j=1}^{n}\#A_{j} and whether m i m_{i} is a prime that does not divide 6 ​ M i − 1 6M_{i-1}. If both these conditions hold, we say we are in the *unbalanced*case, and if not we say we are in the *balanced*case.

1. (1)

*The unbalanced case.*In this case we must have χ > 1 \chi>1, so 3 x 3^{x} is an indeterminate power of 3 3 modulo M i − 1 M_{i-1}; also, in this case we have v i = v i − 1 v_{i}=v_{i-1} because m i ≠ 3 m_{i}\neq 3. We proceed as follows, for each n n -tuple ( a 1 ′, …, a n ′) (a_{1}^{\prime},\ldots,a_{n}^{\prime}) in A 1 × ⋯ × A n A_{1}\times\cdots\times A_{n}:

  1. (a)

*Compute the right-hand side sum.*Set s: ⁣ = ∑ j 2 a j ′ s\mathrel{\mathchoice{\vbox{\hbox{$\displaystyle:$}}}{\vbox{\hbox{$\textstyle:$}}}{\vbox{\hbox{$\scriptstyle:$}}}{\vbox{\hbox{$\scriptscriptstyle:$}}}{=}}\sum_{j}2^{a_{j}^{\prime}}.

  2. (b)

*Check to see whether the right-hand side sum is a power of 3 3 modulo M i M_{i}.*To check to see whether there is a power of 3 3, say 3 x ′ 3^{x^{\prime}}, with 3 x ′ ≡ s mod M i 3^{x^{\prime}}\equiv s\bmod M_{i}, we use discrete logarithms as follows.

Let g g be a generator of the group of units of 𝐙 / m i ​ 𝐙 {\mathbf{Z}}/m_{i}{\mathbf{Z}}, let z z be the smallest non-negative integer with g z ≡ s mod m i g^{z}\equiv s\bmod m_{i}, and let y y be the smallest positive integer with g y ≡ 3 mod m i g^{y}\equiv 3\bmod m_{i}, so that z z and y y are discrete logarithms of s s and of 3 3 with respect to the base g g. If there is an x ′ x^{\prime} such that 3 x ′ ≡ s mod M i 3^{x^{\prime}}\equiv s\bmod M_{i}, then for this x ′ x^{\prime} we have 3 x ′ ≡ s mod m i 3^{x^{\prime}}\equiv s\bmod m_{i}, so we must have x ′ ​ y ≡ z mod ( p − 1) {x^{\prime}y\equiv z\bmod(p-1)}; for this x ′ x^{\prime} we have 3 x ′ ≡ s mod 2 v i − 1 ​ M i − 1 3^{x^{\prime}}\equiv s\bmod 2^{v_{i-1}}M_{i-1}, so we must have x ′ ≡ x mod O 3 ​ ( M i − 1) x^{\prime}\equiv x\bmod O_{3}(M_{i-1}); and for this x ′ x^{\prime} we have 3 x ′ ≡ 3 x ≡ 0 mod 3 v i 3^{x^{\prime}}\equiv 3^{x}\equiv 0\bmod 3^{v_{i}}, so we must have x ′ ≥ v i x^{\prime}\geq v_{i}. Conversely, any x ′ x^{\prime} that satisfies these three conditions will also satisfy 3 x ′ ≡ s mod M i 3^{x^{\prime}}\equiv s\bmod M_{i}.

For primes m i m_{i} of the size we are considering, the computation of the discrete logarithms z z and y y is easily done by the computer algebra package Magma, in which we have written our code. It is also a straightforward matter to compute the values of x ′ x^{\prime} that meet the three conditions, if any exist.

For each x ′ x^{\prime} that we find, we add ( x ′, a 1 ′, …, a n ′) (x^{\prime},a^{\prime}_{1},\ldots,a^{\prime}_{n}) to our list of solutions of equation ( 10) with M = M i M=M_{i}.

The time required to carry out this step is proportional to the number of n n -tuples ( a 1 ′, …, a n ′) (a^{\prime}_{1},\ldots,a^{\prime}_{n}) that we have to consider, which is ∏ #​ A i \prod\#A_{i}.

2. (2)

*The balanced case.*We proceed as follows.

  1. (a)

*Compute the left-hand side lifts.*We compute the set X X of the values of x ′ x^{\prime} with 0 ≤ x ′ < v i + O 3 ​ ( M i) 0\leq x^{\prime}<v_{i}+O_{3}(M_{i}) such that 3 x ′ ≡ 3 x mod M i − 1 3^{x^{\prime}}\equiv 3^{x}\bmod M_{i-1}.

  2. (b)

*Group the variables into two balanced sets.*Compute the value of k k so that the product #​ X ⋅ ∏ j ≤ k #​ A j \#X\cdot\prod_{j\leq k}\#A_{j} and the product ∏ j > k #​ A j \prod_{j>k}\#A_{j} are as close in size as possible.

  3. (c)

*Compute the lifts of the variables in each grouping.*We make two lists. The first is the list of all ( k + 2) (k+2) -tuples

 | ( 3 x ′ − 2 a 1 ′ − ⋯ − 2 a k ′, x ′, a 1 ′, …, a k ′) (3^{x^{\prime}}-2^{a_{1}^{\prime}}-\cdots-2^{a_{k}^{\prime}},x^{\prime},a_{1}^{\prime},\ldots,a_{k}^{\prime}) |  |

for all ( x ′, a 1 ′, …, a k ′) ∈ X × A 1 × ⋯ × A k (x^{\prime},a_{1}^{\prime},\ldots,a_{k}^{\prime})\in X\times A_{1}\times\cdots\times A_{k}, where we view the first entry of the tuple as an element of 𝐙 / M i ​ 𝐙 {\mathbf{Z}}/M_{i}{\mathbf{Z}}. The second is the list of all ( n − k + 1) (n-k+1) -tuples

 | ( 2 a k + 1 ′ + ⋯ + 2 a n ′, a k + 1 ′, …, a n ′) (2^{a_{k+1}^{\prime}}+\cdots+2^{a_{n}^{\prime}},a_{k+1}^{\prime},\ldots,a_{n}^{\prime}) |  |

for all ( a k + 1 ′, …, a n ′) ∈ A k + 1 × ⋯ × A n (a_{k+1}^{\prime},\ldots,a_{n}^{\prime})\in A_{k+1}\times\cdots\times A_{n}, where again we view the first entry as an element of 𝐙 / M i ​ 𝐙 {\mathbf{Z}}/M_{i}{\mathbf{Z}}.

  4. (d)

*Compare the lists for matching values.*Sort each of these lists according to the value of the first entry of each tuple, and then compare the two sorted lists to find all pairs of elements, one from the first list and one from the second, whose first entries are equal. Every such pair gives us a solution to

 | 3 x ′ ≡ 2 a 1 ′ + ⋯ + 2 a n ′ ​ in ​ 𝐙 / M i ​ 𝐙 3^{x^{\prime}}\equiv 2^{a_{1}^{\prime}}+\cdots+2^{a_{n}^{\prime}}\text{ in }{\mathbf{Z}}/M_{i}{\mathbf{Z}} |  |

that reduces to our original solution in 𝐙 / M i − 1 ​ 𝐙 {\mathbf{Z}}/M_{i-1}{\mathbf{Z}}. Add each such solution to our list of solutions of equation ( 10) with M = M i M=M_{i}.

The time it takes to carry out this step is proportional to the larger of #​ X ⋅ ∏ j ≤ k #​ A j {\#X\cdot\prod_{j\leq k}\#A_{j}} and ∏ j > k #​ A j \prod_{j>k}\#A_{j}. If these two numbers are somewhat balanced, the time required for this step will be roughly proportional to the square root of #​ X ⋅ ∏ j ≤ n #​ A j {\#X\cdot\prod_{j\leq n}\#A_{j}}.

Once we have computed all of the solutions to equation ( 10) with M = M i M=M_{i} by this method, we check to see whether all of the powers of 2 2 that occur anywhere on our list are determinate. If they are not, then we increase i i by 1 1 and iterate the procedure. If they are, then for each solution to ( 10) with M = M i M=M_{i}, we can check to see whether the (unique) lifts of the terms in the right-hand side of ( 10) to powers of 2 2 in 𝐙 {\mathbf{Z}} add up to a power of 3 3. In this way, we hope to find all solutions to ( 1).

###### Proof of Theorem 1.1.

We ran through the procedure described above for all values of n n from 3 3 to 22 22. For each n n, the procedure did terminate before we ran out of values of M i M_{i}, so we successfully found all solutions to equation ( 1) for n ≤ 22 n\leq 22. We found that the binary representation of 3 x 3^{x} has at most twenty-two bits equal to 1 1 exactly when x ≤ 25 x\leq 25. ∎

In Table 2, we give for each n n the value of i i for which the modulus M i M_{i} gave us all solutions to the equation. We also give the total time for the computation. As mentioned earlier, the programs we used to implement this computation were written in Magma and are available as supplementary material attached to the ArXiv version of this paper [13], as well as on the second author’s web site.

Table 2. For each n n, we list the value of i i such that our procedure for solving equation ( 1) iterated up to the modulus M i M_{i} from Table . We also give the wall-clock time it took for the computation to complete on a 2.8 GHz Quad-Core Intel Core i7 with 16GB RAM running Magma V2.23-1 on Mac OS 11.2.3. For n ≥ 20 n\geq 20 the computation was split into parts that were run by separate processes; the time given is the sum of the wall-clock times for each process.

n n | i i | Time (sec) |  | n n | i i | Time (sec) |

3 3 | 10 10 | 0.01 0.01 |  | 13 13 | 37 37 | 19 \phantom{0000}19 |

4 4 | 10 10 | 0.02 0.02 |  | 14 14 | 45 45 | 52 \phantom{0000}52 |

5 5 | 14 14 | 0.04 0.04 |  | 15 15 | 45 45 | 145 \phantom{000}145 |

6 6 | 14 14 | 0.07 0.07 |  | 16 16 | 59 59 | 457 \phantom{000}457 |

7 7 | 14 14 | 0.14 0.14 |  | 17 17 | 59 59 | 1469 \phantom{00}1469 |

8 8 | 14 14 | 0.29 0.29 |  | 18 18 | 62 62 | 5746 \phantom{00}5746 |

9 9 | 14 14 | 0.62 0.62 |  | 19 19 | 62 62 | 17744 \phantom{0}17744 |

10 10 | 27 27 | 1.54 1.54 |  | 20 20 | 62 62 | 53617 \phantom{0}53617 |

11 11 | 37 37 | 3.81 3.81 |  | 21 21 | 62 62 | 139347 139347 |

12 12 | 37 37 | 8.03 8.03 |  | 22 22 | 62 62 | 743737 743737 |

The procedure we described in the proof of Theorem 1.1 suggests the properties we looked for when choosing the factors m i m_{i} out of which our moduli M i M_{i} are built. In the balanced case, we want the sets A j A_{j} to be as small as possible, since the work in the balanced case is roughly on the order of the square root of the product #​ X ⋅ ∏ j ≤ n #​ A j \#X\cdot\prod_{j\leq n}\#A_{j}. Of course, we’d like #​ X \#X to be small as well, but since there are n n sets A j A_{j} we concentrate first on them.

For a given solution ( x, a 1, …, a n) (x,a_{1},\ldots,a_{n}) to ( 10) with M = M i − 1 M=M_{i-1}, how large are the A j A_{j}? The answer is analogous to the computation of the value of χ \chi given in Step Two of our procedure. Suppose we are in the case where m i m_{i} is odd. If 2 a j 2^{a_{j}} is a determinate power of 2 2 modulo M i − 1 M_{i-1}, then #​ A j = 1 \#A_{j}=1. If 2 a j 2^{a_{j}} is indeterminate modulo M i − 1 M_{i-1}, then it is indeterminate modulo M i M_{i} as well because m i m_{i} is odd, and we have #​ A j = O 2 ​ ( M i) / O 2 ​ ( M i − 1) \#A_{j}=O_{2}(M_{i})/O_{2}(M_{i-1}). If m i m_{i} is coprime to M i − 1 M_{i-1}, which is the case for all of the values we chose, then O 2 ​ ( M i) O_{2}(M_{i}) is the least common multiple of O 2 ​ ( m i) O_{2}(m_{i}) and O 2 ​ ( M i − 1) O_{2}(M_{i-1}).

The ideal case would be for O 2 ​ ( m i) O_{2}(m_{i}) to be a divisor of O 2 ​ ( M i − 1) O_{2}(M_{i-1}), so that the ratio O 2 ​ ( M i) / O 2 ​ ( M i − 1) O_{2}(M_{i})/O_{2}(M_{i-1}) would be 1 1. The next-best case would be for O 2 ​ ( m i) O_{2}(m_{i}) to divide 2 ​ O 2 ​ ( M i − 1) 2O_{2}(M_{i-1}) but not O 2 ​ ( M i − 1) O_{2}(M_{i-1}), so that O 2 ​ ( M i) / O 2 ​ ( M i − 1) O_{2}(M_{i})/O_{2}(M_{i-1}) would be 2 2. We were able to stay in these two cases for every i i with m i m_{i} odd, except for i = 54 i=54, where we have O 2 ​ ( M i) / O 2 ​ ( M i − 1) = 3 O_{2}(M_{i})/O_{2}(M_{i-1})=3.

For those i i for which O 2 ​ ( M i) / O 2 ​ ( M i − 1) = 1 O_{2}(M_{i})/O_{2}(M_{i-1})=1, we can focus more on the unbalanced case. These i i give us the opportunity to build up the number of powers of 2 2 in O 3 ′ ​ ( M i) O_{3}^{\prime}(M_{i}). For example, for i = 13 i=13 we have O 2 ​ ( M i) / O 2 ​ ( M i − 1) = 1 O_{2}(M_{i})/O_{2}(M_{i-1})=1, and with the value of m i m_{i} that we chose, we increase the 2 2 -part of the order of 3 3 from 2 8 2^{8} in O 3 ′ ​ ( M i − 1) O_{3}^{\prime}(M_{i-1}) to 2 16 2^{16} in O 3 ′ ​ ( M i) O_{3}^{\prime}(M_{i}).

We found our m i m_{i} mostly by looking for primes p p congruent to 1 1 modulo 2 a ​ 3 b 2^{a}3^{b} for various values of a a and b b, and computing the orders of 2 2 and 3 3 in ( 𝐙 / p ​ 𝐙) ∗ ({\mathbf{Z}}/p{\mathbf{Z}})^{*}.

We make one final note about our choice of the m i m_{i}. We would also like the number of solutions we have to consider at any given stage to be small. This becomes especially critical for the larger values of n n that we consider. Our choices for m i m_{i}, especially for small i i, reflect this. For example, we have chosen m 4 m_{4} to be 241 ⋅ 433 241\cdot 433, which puts us in the balanced case with #​ A j = 2 \#A_{j}=2 for most j j and with #​ X = 10 \#X=10. After this m 4 m_{4}, we have m 5 = 17 m_{5}=17, m 6 = 2 2 m_{6}=2^{2}, and m 7 = 38737 m_{7}=38737. For smaller values of n n, it turns out that it would be faster to take m 4 = 433 m_{4}=433 (which gives us #​ X = 1 \#X=1), m 5 = 17 m_{5}=17, m 6 = 2 2 m_{6}=2^{2}, and then to add in a factor of 241 241 before moving on to m 7 = 38737 m_{7}=38737. According to the heuristic mentioned in Step Three, the time it takes to process a solution in the balanced case is very roughly proportional to ( #​ X ⋅ ∏ j ≤ n #​ A j) 1 / 2 (\#X\cdot\prod_{j\leq n}\#A_{j})^{1/2}, so having #​ X \#X equal to 1 1 instead of 10 10 should speed up this step by a factor of about 10 \sqrt{10}. But for large n n, this improved speed for i = 4 i=4 would be outweighed by the extra time it would take to process the large number of solutions that would make it through to the next step. To simplify our exposition, we have simply given one single sequence of m i m_{i} to use for all n n, optimized for large values of n n, even though different choices would have made the program run faster for smaller n n.

## 6. Proof of Theorem 1.2

The proof of Theorem 1.2 is also computational, and is essentially the same as that of Theorem 1.1. The sequence of moduli we use is given in Table 3, and the time it took to run our program for n n up to 24 24 is given in Table 4. The only other comment we make here is that if n n is odd and greater than 1 1, then there are no solutions to equation ( 2), because no power of 2 2 (other than 1 1) can be written as the sum of an odd number of powers of 3 3. ∎

Table 3. Data for the factors m i m_{i} and the moduli M i = ∏ j ≤ i m j M_{i}=\prod_{j\leq i}m_{j} used in the proof of Theorem 1.2. The notation in the table headings is as in Notation 2.3.

i i | m i m_{i} | O 3 ​ ( m i) O_{3}(m_{i}) | O 3 ​ ( M i) O_{3}(M_{i}) | O 2 ′ ​ ( m i) O_{2}^{\prime}(m_{i}) | v 3 ​ ( O 2 ′ ​ ( M i)) v_{3}(O_{2}^{\prime}(M_{i})) |

1 1 | 2 ⋅ 3 4 ⋅ 13 ⋅ 757 2\cdot 3^{4}\cdot 13\cdot 757 | 3 2 3^{2} | 3 2 3^{2} | 28 ⋅ 3 3 28\cdot 3^{3\phantom{0}} | 3 \phantom{0}3 |

2 2 | 7 ⋅ 19 ⋅ 37 7\cdot 19\cdot 37 | 2 ⋅ 3 2 2\cdot 3^{2} | 2 ⋅ 3 2 2\cdot 3^{2} | 4 ⋅ 3 2 4\cdot 3^{2\phantom{0}} | 3 \phantom{0}3 |

3 3 | 5 ⋅ 73 5\cdot 73 | 2 2 ⋅ 3 2^{2}\cdot 3^{\phantom{0}} | 2 2 ⋅ 3 2 2^{2}\cdot 3^{2} | 4 ⋅ 3 2 4\cdot 3^{2\phantom{0}} | 3 \phantom{0}3 |

4 4 | 530713 530713 | 2 2 ⋅ 3 2 2^{2}\cdot 3^{2} | 2 2 ⋅ 3 2 2^{2}\cdot 3^{2} | 91 ⋅ 3 6 91\cdot 3^{6\phantom{0}} | 6 \phantom{0}6 |

5 5 | 3 3 3^{3} | — | 2 2 ⋅ 3 2 2^{2}\cdot 3^{2} | — | 6 \phantom{0}6 |

6 6 | 41 ⋅ 6481 41\cdot 6481 | 2 3 ⋅ 3 2^{3}\cdot 3^{\phantom{0}} | 2 3 ⋅ 3 2 2^{3}\cdot 3^{2} | 20 ⋅ 3 4 20\cdot 3^{4\phantom{0}} | 6 \phantom{0}6 |

7 7 | 282429005041 282429005041 | 2 3 ⋅ 3 2 2^{3}\cdot 3^{2} | 2 3 ⋅ 3 2 2^{3}\cdot 3^{2} | 66430 ⋅ 3 12 66430\cdot 3^{12} | 12 12 |

8 8 | 3 6 3^{6} | — | 2 3 ⋅ 3 2 2^{3}\cdot 3^{2} | — | 12 12 |

Table 4. For each n n, we list the value of i i such that our procedure for solving equation ( 2) iterated up to the modulus M i M_{i} from Table 3. We also give the wall-clock time it took for the computation to complete on a 2.8 GHz Quad-Core Intel Core i7 with 16GB RAM running Magma V2.23-1 on Mac OS 11.2.3.

n n | i i | Time (sec) |  | n n | i i | Time (sec) |

4 4 | 5 5 | 0.01 0.01 |  | 16 16 | 8 8 | 14 \phantom{0000}14 |

6 6 | 5 5 | 0.01 0.01 |  | 18 18 | 8 8 | 84 \phantom{0000}84 |

8 8 | 5 5 | 0.07 0.07 |  | 20 20 | 8 8 | 789 \phantom{000}789 |

10 10 | 8 8 | 0.23 0.23 |  | 22 22 | 8 8 | 9792 \phantom{00}9792 |

12 12 | 8 8 | 0.92 0.92 |  | 24 24 | 8 8 | 140036 140036 |

14 14 | 8 8 | 3.44 3.44 |  |  |  |  |

## References

- [1] Zsolt Ádám, Lajos Hajdu, and Florian Luca, **[Representing integers as linear combinations of S S -units][5], Acta Arith. 138 (2009), no. 2, 101–107. [MR 2520130][6]
- [2] Leo J. Alex, **[Diophantine equations related to finite groups][7], Comm. Algebra 4 (1976), no. 1, 77–100. [MR 424675][8]
- [3] Tom M. Apostol, **[Introduction to analytic number theory][9], Springer-Verlag, New York, 1976, Undergraduate Texts in Mathematics. [MR 0434929][10]
- [4] Levi ben Gerson [Magistri Leonis Hebraei], **[De numeris harmonicis][11], Scripta diversa super scientiam mathematicam et physicam, 14th century, Bibliothèque nationale de France, Département des manuscrits, Latin 7378A, pp. 55v–57r.
- [5] Michael A. Bennett, Yann Bugeaud, and Maurice Mignotte, **[Perfect powers with few binary digits and related Diophantine problems][12], Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 12 (2013), no. 4, 941–953. [MR 3184574][13]
- [6] by same author, **[Perfect powers with few binary digits and related Diophantine problems, II][14], Math. Proc. Cambridge Philos. Soc. 153 (2012), no. 3, 525–540. [MR 2990629][15]
- [7] Csanád Bertók and Lajos Hajdu, **[A Hasse-type principle for exponential Diophantine equations and its applications][16], Math. Comp. 85 (2016), no. 298, 849–860. [MR 3434884][17]
- [8] by same author, **[A Hasse-type principle for exponential Diophantine equations over number fields and its applications][18], Monatsh. Math. 187 (2018), no. 3, 425–436. [MR 3858424][19]
- [9] Wieb Bosma, John Cannon, and Catherine Playoust, **[The Magma algebra system. I. The user language][20], J. Symbolic Comput. 24 (1997), no. 3-4, 235–265, Computational algebra and number theory (London, 1993). Software available at [http://magma.maths.usyd.edu.au/][21]. [MR 1484478][22]
- [10] Joel Lee Brenner and Lorraine L. Foster, **[Exponential Diophantine equations][23], Pacific J. Math. 101 (1982), no. 2, 263–301. [MR 675401][24]
- [11] Karine Chemla and Serge Pahaut, **[Remarques sur les ouvrages mathématiques de Gersonide][25], Studies on Gersonides — A Fourteenth-Century Jewish Philosopher-Scientist (G. Freudenthal, ed.), Collection de Travaux de l’Académie Internationale d’Histoire des Sciences, vol. 36, E. J. Brill, Leiden, 1992, pp. 149–191.
- [12] Vassil S. Dimitrov and Everett W. Howe, **[Lower bounds on the lengths of double-base representations][26], Proc. Amer. Math. Soc. 139 (2011), no. 10, 3423–3430. [MR 2813374][27]
- [13] by same author, **[Powers of 3 with few nonzero bits and a conjecture of Erdős][28], 2021. [arXiv:2105.06440 [math.NT]][29]
- [14] Taylor Dupuy and David E. Weirich, **[Bits of 3 n 3^{n} in binary, Wieferich primes and a conjecture of Erdős][30], J. Number Theory 158 (2016), 268–280. [MR 3393551][31]
- [15] Paul Erdős, **[Some unconventional problems in number theory][32], Math. Mag. 52 (1979), no. 2, 67–70. [MR 527408][33]
- [16] Paul Erdős, Carl Pomerance, and Eric Schmutz, **[Carmichael’s lambda function][34], Acta Arith. 58 (1991), no. 4, 363–385. [MR 1121092][35]
- [17] Jeffrey C. Lagarias, **[Ternary expansions of powers of 2][36], J. Lond. Math. Soc. (2) 79 (2009), no. 3, 562–588. [MR 2506687][37]
- [18] Władysław Narkiewicz, **[A note on a paper of H. Gupta concerning powers of two and three][38], Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. (1980), no. 678-715, 173–174 (1981). [MR 623247][39]
- [19] S. Sivasankaranarayana Pillai, **[On the equation 2 x − 3 y = 2 X + 3 Y 2^{x}-3^{y}=2^{X}+3^{Y}][40], Bull. Calcutta Math. Soc. 37 (1945), 15–20. [MR 13386][41]
- [20] Hans Georg Senge and Ernst Gabor Straus, **[PV {\rm PV} -numbers and sets of multiplicity][42], Period. Math. Hungar. 3 (1973), 93–100. [MR 340185][43]
- [21] Cameron L. Stewart, **[On the representation of an integer in two different bases][44], J. Reine Angew. Math. 319 (1980), 63–72. [MR 586115][45]
- [22] László Szalay, **[The equations 2 n ± 2 m ± 2 l = z 2 2^{n}\pm 2^{m}\pm 2^{l}=z^{2}][46], Indag. Math. (N.S.) 13 (2002), no. 1, 131–142. [MR 2014980][47]

[◄][48][image: ar5iv homepage] [49]
[Feeling lucky?][50] [51]
[Conversion report][52]
[Report an issue][53]
[View original on arXiv][54] [►][55]


## Links

[1]: mailto:vdimitro@ucalgary.ca
[2]: mailto:vassil@lemurianlabs.com
[3]: mailto:however@alumni.caltech.edu
[4]: http://ewhowe.com
[5]: http://dx.doi.org/10.4064/aa138-2-1
[6]: http://www.ams.org/mathscinet-getitem?mr=2520130
[7]: http://dx.doi.org/10.1080/00927877608822095
[8]: http://www.ams.org/mathscinet-getitem?mr=424675
[9]: http://dx.doi.org/10.1007/978-1-4757-5579-4
[10]: http://www.ams.org/mathscinet-getitem?mr=0434929
[11]: https://gallica.bnf.fr/ark:/12148/btv1b525016914/f114.item
[12]: http://www.numdam.org/item/ASNSP_2013_5_12_4_941_0/
[13]: http://www.ams.org/mathscinet-getitem?mr=3184574
[14]: http://dx.doi.org/10.1017/S0305004112000345
[15]: http://www.ams.org/mathscinet-getitem?mr=2990629
[16]: http://dx.doi.org/10.1090/mcom/3002
[17]: http://www.ams.org/mathscinet-getitem?mr=3434884
[18]: http://dx.doi.org/10.1007/s00605-018-1169-8
[19]: http://www.ams.org/mathscinet-getitem?mr=3858424
[20]: http://dx.doi.org/10.1006/jsco.1996.0125
[21]: http://magma.maths.usyd.edu.au/
[22]: http://www.ams.org/mathscinet-getitem?mr=1484478
[23]: http://projecteuclid.org/euclid.pjm/1102724775
[24]: http://www.ams.org/mathscinet-getitem?mr=675401
[25]: http://www.worldcat.org/oclc/911650818
[26]: http://dx.doi.org/10.1090/S0002-9939-2011-10764-0
[27]: http://www.ams.org/mathscinet-getitem?mr=2813374
[28]: http://dx.doi.org/10.48550/arXiv.2105.06440
[29]: http://arxiv.org/abs/2105.06440
[30]: http://dx.doi.org/10.1016/j.jnt.2015.05.022
[31]: http://www.ams.org/mathscinet-getitem?mr=3393551
[32]: http://dx.doi.org/10.2307/2689842
[33]: http://www.ams.org/mathscinet-getitem?mr=527408
[34]: http://dx.doi.org/10.4064/aa-58-4-363-385
[35]: http://www.ams.org/mathscinet-getitem?mr=1121092
[36]: http://dx.doi.org/10.1112/jlms/jdn080
[37]: http://www.ams.org/mathscinet-getitem?mr=2506687
[38]: https://www.jstor.org/stable/43667894
[39]: http://www.ams.org/mathscinet-getitem?mr=623247
[40]: https://web.archive.org/web/20230629153023/https://s3.ap-south-1.amazonaws.com/calcutta-university/departmental-journals/H00535.pdf
[41]: http://www.ams.org/mathscinet-getitem?mr=13386
[42]: http://dx.doi.org/10.1007/BF02018464
[43]: http://www.ams.org/mathscinet-getitem?mr=340185
[44]: http://dx.doi.org/10.1515/crll.1980.319.63
[45]: http://www.ams.org/mathscinet-getitem?mr=586115
[46]: http://dx.doi.org/10.1016/S0019-3577(02)90011-X
[47]: http://www.ams.org/mathscinet-getitem?mr=2014980
[48]: /html/2105.06439
[49]: /
[50]: /feeling_lucky
[51]: /land_of_honey_and_milk
[52]: /log/2105.06440
[53]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2105.06440
[54]: https://arxiv.org/abs/2105.06440
[55]: /html/2105.06441
