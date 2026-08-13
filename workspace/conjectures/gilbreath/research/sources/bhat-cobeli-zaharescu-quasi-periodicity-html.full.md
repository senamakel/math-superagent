<!-- source: https://arxiv.org/html/2307.11776v1 | converted from HTML -->

On quasi-periodicity in Proth-Gilbreath triangles

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2307.11776v1 [math.NT] 19 Jul 2023

# On quasi-periodicity in Proth-Gilbreath triangles Thanks: Key words and phrases: Proth-Gilbreath Conjecture, quasi-periodicity, formal power series, Fibonacci sequences, SP numbers.

Raghavendra N. Bhat Raghavendra N. Bhat Department of Mathematics,University of Illinois at Urbana-Champaign, Urbana, IL 61801, USA Email address: [rnbhat2@illinois.edu][3], Cristian Cobeli Cristian Cobeli ”Simion Stoilow” Institute of Mathematics of the Romanian Academy, 21 Calea Grivitei Street, P. O. Box 1-764, Bucharest 014700, Romania Email address: [cristian.cobeli@imar.ro][4] and Alexandru Zaharescu Alexandru Zaharescu Department of Mathematics,University of Illinois at Urbana-Champaign, Urbana, IL 61801, USA, and ”Simion Stoilow” Institute of Mathematics of the Romanian Academy, 21 Calea Grivitei Street, P. O. Box 1-764, Bucharest 014700, Romania Email address: [zaharesc@illinois.edu][5]

###### Abstract.

Let PG \operatorname{PG} be the Proth-Gilbreath operator that transforms a sequence of integers into the sequence of the absolute values of the differences between all pairs of neighbor terms. Consider the infinite tables obtained by successive iterations of PG \operatorname{PG} applied to different initial sequences of integers. We study these tables of higher order differences and characterize those that have near-periodic features. As a biproduct, we also obtain two results on a class of formal power series over the field with two elements 𝔽 2 \mathbb{F}_{2} that can be expressed as rational functions in several ways.

###### 2020 Mathematics Subject Classification

Primary 11B37; Secondary 11B39, 11B50.

## 1. Introduction and Summary of previous results

Let us consider the evolutionary process that replaces a sequence of integers 𝒂 = { a k } k ≥ 1 \bm{a}=\{a_{k}\}_{k\geq 1} with the distances between its consecutive terms. We write the new generation of differences shifted under the parent generation so that under any two consecutive terms of 𝒂 \bm{a}, just below, is the distance between them. Repeating the process produces the sequences of higher-order differences. These are recorded in the following triangle, which can be finite or infinite as the initial sequence 𝒂 \bm{a} is:

 |

a 1 a_{1} |  | a 2 a_{2} |  | a 3 a_{3} |  | a 4 a_{4} |  | a 5 a_{5} |  | a 6 a_{6} |  | … \dots |  |

 | d 1 ( 1) d_{1}^{(1)} |  | d 2 ( 1) d_{2}^{(1)} |  | d 3 ( 1) d_{3}^{(1)} |  | d 4 ( 1) d_{4}^{(1)} |  | d 5 ( 1) d_{5}^{(1)} |  | … \dots |  |  |

 |  | d 1 ( 2) d_{1}^{(2)} |  | d 2 ( 2) d_{2}^{(2)} |  | d 3 ( 2) d_{3}^{(2)} |  | d 4 ( 2) d_{4}^{(2)} |  | … \dots |  |  |  |

 |  |  | d 1 ( 3) d_{1}^{(3)} |  | d 2 ( 3) d_{2}^{(3)} |  | d 3 ( 3) d_{3}^{(3)} |  | … \dots |  |  |  |  |

 |  |  |  | … \dots |  | … \dots |  | … \dots |  |  |  |  |  |

 |  | (P-G) |

where

 | d k ( j + 1):= | d k + 1 ( j) − d k ( j) | and d k ( 0):= a k for k ≥ 1.
d_{k}^{(j+1)}:=\big|d_{k+1}^{(j)}-d_{k}^{(j)}\big|\quad\text{ and }\quad d_{k}^{(0)}:=a_{k}\quad\text{ for $k\geq 1$.}\\  |  |

The initial sequence is also called the sequence of differences of order 0 0. The key element of the definition is taking the absolute value of differences, which makes all the elements of the triangle ( P-G) positive. The operation that transforms a line to another by taking the absolute differences of nearby integers is also called the PG \operatorname{PG} or the Proth-Gilbreath operator.

The Proth-Gilbreath procedure produces tables of numbers of which their truncated triangles are part of a special family. A slightly modified rule, which, by definition, adds borders to the generating triangles has the effect that the growth is apparently reversed. All these number triangles can also be seen as symbolic dynamic systems that collect and structure a lot of information and links with other not necessarily related fields. In particular the modular versions of various variants of Pascal triangle, the outcome of Ducci games and Proth-Ducci triangles share and complement each other properties of an arithmetic, combinatorial and probabilistic nature (see [15, 11, 10, 9, 8, 7, 6, 5] and the references therein).

The left-edge of the ( P-G) triangle is particularly important because it somehow sums up by averaging the differences of all orders. The interest was raised especially by Proth [18] in the 19th century and then, independently, by Gilbreath [16, 11] (see also [13, Problem A10] and [17]) in the mid-20th century with the observation that if the first line that generates the triangle ( P-G) is the sequence of primes, then on the left-edge there are only ones. The fact that is expected to be very likely true is currently in the conjecture stage. The problem is included in the selected lists of Guy [12, Example 12] and Montgomery [14, Appendix Problem 68]) and has not been proven yet even whether there are an infinity of ones on the left side of the triangle of high order differences.

The higher order difference rows are mainly influenced by the numbers on the first line. And yet, even for sequences somehow related to each other it can be found that the numbers on the left-edge can have a very different structure. One such example is the sequence of square-primes [1, 2, 4]. They are the elements of the ordered union of the sequence of primes scaled by squares larger than 1 1:

 | S ​ 𝒫:= ⋃ k ≥ 2 { k 2 ​ p ∣ p ​ prime }. \begin{split}S\mathcal{P}:=\bigcup_{k\geq 2}\{k^{2}p\mid p\text{ prime}\}.\end{split} |  |

Let s n s_{n} denote the n n th square-prime number. There are 21 21 square-primes in the first hundred natural numbers:

 | 8, 12, 18, 20, 27, 28, 32, 44, 45, 48, 50, 52, 63, 68, 72, 75, 76, 80, 92, 98, 99. 8,12,18,20,27,28,32,44,45,48,50,52,63,68,72,75,76,80,92,98,99. |  |

The ordered sequence S ​ 𝒫 S\mathcal{P} can be thought of as a superposition of layers of primes scaled by non-trivial squares. The rarity of the squares and the multitude of the primes combine to a density of the square-primes that has the same order of magnitude with that of the primes. Thus, the analogue of the prime number theorem gives the following estimate [1] for the size of s n s_{n}, namely

 | s n = ( ζ ⁡ ( 2) − 1) ⋅ n log ⁡ n + O ⁡ ( n log 2 ​ n). \begin{split}s_{n}=\big(\zeta(2)-1\big)\cdot\mbox{\small$\displaystyle\frac{n}{\log n}$}+O\left(\mbox{\small$\displaystyle\frac{n}{\log^{2}n}$}\right).\end{split} |  |

We also mention, among the characteristic properties, that there are infinitely many ‘twin’ square-primes that are next to each other [1], such as ( 27, 28) (27,28) or ( 44, 45) (44,45), (unlike the still incompletely solved conjecture that the sequence of twin primes at distance 2 2 is infinite). Emphasizing the aspect of proximity, we further note that an analogue of Dirichlet’s Theorem for prime numbers in arithmetic progressions holds also for square-primes only with a different density.

Figure 1. The number of 1 1 ’s versus the number of 0 0 ’s on the left-edge of the ( P-G) with square-prime numbers on the first row. The image on the left shows the first 200 200 values and the one on the right shows 2234 2234 values obtained from the square-primes less than 20000 20000. In total there are 1101 1101 ones and 1130 1130 zeros.

Triangle ( P-G) generated by the sequence of square-primes shows interesting properties. For instance, apart from the first three numbers, the left-edge seems to contain only ones and zeros in roughly equal proportions (see Figure 1). We do not know a proof of this fact, but this kind of property is certain to hold for some subsequences of square-primes.

###### Theorem 1 (2023, [3]).

There exits an infinite subsequence of square-prime numbers that generates a ( P-G) triangle where every other element on the left-edge is 1 1.

To test and compare, we filtered out the integer parts of the integers in the triangles keeping only the remainders of their division by some d ≥ 2 d\geq 2. The results in three different cases for two moduli d d are shown in Figure 2. The outcome is singular only for the case of primes mod 2 2. There the shape is trivial because of the simple reason that 2 2 is the only even prime number. Apart from the colors representing the different residue classes mod d d, the pattern structure looks similar in all cases. The intermediate position of the square-primes between primes and random numbers as the first line is not fortuitous. It is just a first step ahead of the cube-primes and higher-power-primes that yield ( P-G) triangles that place themselves in what appears as a continuous transformation of order in a distinguished class of patterns.

[image: Refer to caption]

[image: Refer to caption]

[image: Refer to caption]

[image: Refer to caption]

[image: Refer to caption]

[image: Refer to caption]

Figure 2. The gaps in the ( P-G) triangles generated by primes (left), square-primes (middle) and random numbers (right). The initial rows (not shown) contain the first one hundred primes, the first one hundred square-primes, and one hundred integers selected randomly from [2,550] [2,550], respectively. (Note that p 100 = 541 p_{100}=541 and s 100 = 549 s_{100}=549.) The gaps are represented by two colors in the top triangles and by seven colors at the bottom. The colors correspond to the residue classes of the gaps ( mod 2) \pmod{2} and ( mod 7) \pmod{7}, respectively. The triangles on the right side are obtained by two independent random choices of the numbers on the initial rows.

In his extensive search for a possible counterexample of Gilbreath’s conjecture for lines as long as 3.46 × 10 11 3.46\times 10^{11} and primes less than π ⁡ ( 10 13) \pi(10^{13}), Odlyzko [17] found none, and he notes that similar conjectures are likely to be valid for many other sequences as well.

In Figure 2, in the triangle in the upper left corner, the modulo 2 2 highlights the left edge with 1 1 ’s, but hides the real general phenomenon. But if we ‘unzip the edge’ and draw off the curtain, the ‘random pattern’ reveals when we change the modulus to d=4, for example. Thus, looking at the rays that traverse ( P-G) parallel to the left edge, we notice that the number of 0 0 ’s is approximately equal to the number of 2 2 ’s. Indeed, in the counting summarized in Table 1, the cut-off triangle has the side length 50000 50000, being generated by the first 50 50 thousand prime numbers, and, on the first five parallel lines with the left edge, the difference between the number of 0 0 ’s and the number of 2 2 ’s satisfies the ‘square root rule’ in all five cases, all of them being less than 50 000 ≈ 223.61 \sqrt{50\,000}\approx 223.61. Also, in this range, the difference between the proportion of 0 0 ’s and the proportion of 2 2 ’s is less than one percent.

Table 1. The frequencies of the absolute values of the differences on the rays that cross a cut-off of the ( P-G) triangle passing parallel to its left edge. The generating row contains the first 50 000 prime numbers: 2, 3, …, 611 953 2,3,\dots,611\,953. All differences are reduced modulo 4 4. The notations are as follows: r r is the number of the ray, starting with r = 1 r=1, the ray next to the left edge; N N is the number of differences on the ray (note that there are no differences on the first row of ( P-G)); z z is the number of zeros and t t is the number of two’s.

r r | N N | z z | t t | ( z − t) / N (z-t)/N |

1 | 49998 | 24914 | 25084 | -0.00340 |

2 | 49997 | 25095 | 24902 | 0.00386 |

3 | 49996 | 25033 | 24963 | 0.00140 |

4 | 49995 | 25019 | 24976 | 0.00086 |

5 | 49994 | 25074 | 24920 | 0.00308 |

A similar development comes along even further, on the rays farther away to the right and still, analogue for larger moduli d d, as evidenced by numerical computations. In the simplest, bicolor version of the triangle, for d = 4 d=4, the following statement is likely to hold true.

###### Conjecture 1.

Let r ≥ 1 r\geq 1 be integer and denote by δ k ​ ( r) \delta_{k}(r) the r r th element on the k k th row of the ( P-G) triangle generated by the sequence of primes. Then, with finitely many exceptions, the sequence of differences { δ k ​ ( r) } k ≥ 1 ( mod 4) \{\delta_{k}(r)\}_{k\geq 1}\pmod{4} contains only 0 0 ’s and 2 2 ’s and, in the limit, their proportions are the same being equal to 1 / 2 1/2.

Our object in the following is to characterize the infinite sequences of integers that produce triangles with periodic patterns. We remark that Fibonacci’s sequence has the property of reproducing itself on the next line of a ( P-G) triangle. We may say that it is a fixed point of the Proth-Gilbreath operator. Also, triangles generated by Fibonacci sequences reveal periodic features when their entries are reduced modulo some d ≥ 2 d\geq 2. We will investigate slightly more complex shapes and obtain a general characterization of triangles that are not fully periodic. For this purpose we introduce an equivalence relation “ ≍ \asymp ” whose quotient set is indeed composed only of periodic classes. Our main result is the following characterization of binary sequences that are fixed points of the PG \operatorname{PG} operator.

We say that a row in ( P-G) is ultimately replicated identically into another, if cutting the entries at their beginnings, not necessarily in the same number, the two remaining sequences of numbers on the two rows are identical.

###### Theorem 2.

Let 𝛂 = ( a 0, a 1, a 2, …) \bm{\alpha}=(a_{0},a_{1},a_{2},\dots) be the sequence of entries on a line of the ( P-G) triangle and let ϕ ⁡ ( 𝛂) = ∑ k ≥ 0 a k ​ X k \phi(\bm{\alpha})=\sum_{k\geq 0}a_{k}X^{k} be its associated formal power series. Suppose a k ∈ 𝔽 2 a_{k}\in\mathbb{F}_{2} for k ≥ 0 k\geq 0. Then 𝛂 \bm{\alpha} is ultimately replicated identically in the next line of ( P-G) if and only if there exist an integer r ≥ 0 r\geq 0 and a polynomial P ​ ( X) ∈ 𝔽 2 ​ [X] P(X)\in\mathbb{F}_{2}[X] such that either

 | ϕ ⁡ ( 𝜶) = P ⁡ ( X) 1 + X + X r or ϕ ⁡ ( 𝜶) = P ⁡ ( X) X r ​ ( 1 + X) + 1. \begin{split}\phi(\bm{\alpha})=\mbox{\small$\displaystyle\frac{P(X)}{1+X+X^{r}}$}\ \ \mathrm{or}\ \ \phi(\bm{\alpha})=\mbox{\small$\displaystyle\frac{P(X)}{X^{r}(1+X)+1}$}\,.\end{split} |  | (1) |

As an application, we draw out the following two results that link certain formal power series over 𝔽 2 \mathbb{F}_{2}, and their representations as rational functions.

###### Theorem 3.

Let f ⁡ ( X) f(X) be a formal power series with coefficients in 𝔽 2 \mathbb{F}_{2}. Suppose there exists a polynomial P ​ ( X) ∈ 𝔽 2 ​ [X] P(X)\in\mathbb{F}_{2}[X] and an integer r ≥ 1 r\geq 1 such that f ⁡ ( X) f(X) can be expressed as the rational function

 | f ⁡ ( X) = P ⁡ ( X) 1 + X + X r or f ⁡ ( X) = P ⁡ ( X) X r ​ ( 1 + X) + 1. \begin{split}f(X)=\frac{P(X)}{1+X+X^{r}}\ \ \mathrm{or}\ \ f(X)=\frac{P(X)}{X^{r}(1+X)+1}\,.\end{split} |  |

Then, for any l ≥ 1 l\geq 1, there exists a polynomial P l ​ ( X) ∈ 𝔽 2 ​ [X] P_{l}(X)\in\mathbb{F}_{2}[X] and an integer r l ≥ 1 r_{l}\geq 1 such that either

 | f ⁡ ( X) = P l ​ ( X) ( 1 + X) l + X r l or f ⁡ ( X) = P l ​ ( X) X r l ​ ( 1 + X) l + 1. f(X)=\frac{P_{l}(X)}{(1+X)^{l}+X^{r_{l}}}\ \ \mathrm{or}\ \ f(X)=\frac{P_{l}(X)}{X^{r_{l}}(1+X)^{l}+1}. |  |

###### Theorem 4.

Let f ⁡ ( X) f(X) be a formal power series with coefficients in 𝔽 2 \mathbb{F}_{2}. Suppose there exist m ≥ 1 m\geq 1 polynomials P 1 ​ ( X), P 2 ​ ( X), …, P m ​ ( X) ∈ 𝔽 2 ​ [X] P_{1}(X),P_{2}(X),\dots,P_{m}(X)\in\mathbb{F}_{2}[X] and two sets of m m positive integers r 1, r 2, …, r m r_{1},r_{2},\dots,r_{m} and l 1, l 2, …, l m l_{1},l_{2},\dots,l_{m} such that either

 | f ⁡ ( X) = P j ​ ( X) ( 1 + X) l j + X r j or f ⁡ ( X) = P j ​ ( X) X r j ​ ( 1 + X) l j + 1, f(X)=\frac{P_{j}(X)}{(1+X)^{l_{j}}+X^{r_{j}}}\ \ \mathrm{or}\ \ f(X)=\frac{P_{j}(X)}{X^{r_{j}}(1+X)^{l_{j}}+1}, |  |

for any 1 ≤ j ≤ m 1\leq j\leq m. Let l = gcd ⁡ ( l 1, …, l m) l=\gcd(l_{1},\dots,l_{m}). Then, there exists a polynomial P ​ ( X) ∈ 𝔽 2 ​ [X] P(X)\in\mathbb{F}_{2}[X] and an integer r ≥ 1 r\geq 1 such that either

 | f ⁡ ( X) = P ⁡ ( X) ( 1 + X) l + X r or f ⁡ ( X) = P ⁡ ( X) X r ​ ( 1 + X) l + 1. f(X)=\frac{P(X)}{(1+X)^{l}+X^{r}}\ \ \mathrm{or}\ \ f(X)=\frac{P(X)}{X^{r}(1+X)^{l}+1}. |  |

Theorem 4 covers a multitude of situations, some of them describing patterns of a certain complexity. To give such an example, let us consider the set of integers

 | ℳ = { 1, 2, 3, 4, 5, 8, 10, 12, 13, 14, 17, 18, 20, 24, 27, 28, 29, 30, 34, 36, 41, 42, 48, 55, 56, 57, 58, 59, 60, 61, 63, 65, 67, 70, 71, 74, 75, 76, 78, 79, 80, 82, 85, 87, 88, 92, 93, 95, 96, 97, 98, 100, 101, 103, 105, 106, 108, 109, 112, 115, 119, 120, 121, 126 }. \small\begin{split}\mathcal{M}=\{&1,2,3,4,5,8,10,12,13,14,17,18,20,24,27,28,29,30,34,36,41,42,48,\\ &55,56,57,58,59,60,61,63,65,67,70,71,74,75,76,78,79,80,82,85,87,88,\\ &92,93,95,96,97,98,100,101,103,105,106,108,109,112,115,119,120,121,126\}\,.\end{split} |  |

Let f ​ ( X) ∈ 𝔽 2 ​ [[X]] f(X)\in\mathbb{F}_{2}[[X]] be the formal power series with coefficients in the field with two elements defined by

 | f ⁡ ( X) = ∑ k ≥ 0 ∑ s ∈ ℳ X s + 127 ​ k. f(X)=\sum_{k\geq 0}\sum_{s\in\mathcal{M}}X^{s+127k}. |  | (2) |

The coefficients of f ⁡ ( X) f(X) repeat with a period of length 127 127 and the graph of the first period is shown in Figure 3.

Figure 3. The coefficients of the series f ⁡ ( X) f(X). The graph shows the first 127 127 coefficients, and the following ones are reproduced periodically with the period 127 127. There are 64 64 non-zero coefficients among the first 127 127.

Now, on the one hand, observe that

 | ( ( 1 + X) 3 + X 21) ​ f ​ ( X) = X + X 3 + X 6 + X 9 + X 13 + X 14 + X 15 + X 20, \begin{split}\big((1+X)^{3}+X^{21}\big)f(X)=X+X^{3}+X^{6}+X^{9}+X^{13}+X^{14}+X^{15}+X^{20},\end{split} |  |

so that

 | f ⁡ ( X) = X + X 3 + X 6 + X 9 + X 13 + X 14 + X 15 + X 20 ( 1 + X) 3 + X 21. \begin{split}f(X)=\frac{X+X^{3}+X^{6}+X^{9}+X^{13}+X^{14}+X^{15}+X^{20}}{(1+X)^{3}+X^{21}}\,.\end{split} |  | (3) |

On the other hand, note that

 | ( ( 1 + X) 2 + X 14) ​ f ​ ( X) = X + X 2 + X 6 + X 7 + X 8 + X 13, \begin{split}\big((1+X)^{2}+X^{14}\big)f(X)=X+X^{2}+X^{6}+X^{7}+X^{8}+X^{13},\end{split} |  |

therefore

 | f ⁡ ( X) = X + X 2 + X 6 + X 7 + X 8 + X 13 ( 1 + X) 2 + X 14. \begin{split}f(X)=\frac{X+X^{2}+X^{6}+X^{7}+X^{8}+X^{13}}{(1+X)^{2}+X^{14}}\,.\end{split} |  | (4) |

Then, the hypotheses of Theorem 4 are satisfied with the parameters suggested from ( 3) and ( 4): m = 2 m=2; l 1 = 3 l_{1}=3, r 1 = 21 r_{1}=21, P 1 ​ ( X) = X + X 3 + X 6 + X 9 + X 13 + X 14 + X 15 + X 20 P_{1}(X)=X+X^{3}+X^{6}+X^{9}+X^{13}+X^{14}+X^{15}+X^{20}; l 2 = 2 l_{2}=2, r 2 = 14 r_{2}=14, P 2 ​ ( X) = X + X 2 + X 6 + X 7 + X 8 + X 13 P_{2}(X)=X+X^{2}+X^{6}+X^{7}+X^{8}+X^{13}. Consequently, f ⁡ ( X) f(X) must also have a simpler expression, which it does. Indeed, with 1 = gcd ⁡ ( 2, 3) 1=\gcd(2,3), r = 7 r=7 and P ⁡ ( X) = X + X 6 P(X)=X+X^{6}, we do have

 | f ⁡ ( X) = X ⁡ ( 1 + X 5) 1 + X + X 7, \begin{split}f(X)=\frac{X(1+X^{5})}{1+X+X^{7}}\,,\end{split} |  |

which is the first type of rational function in the conclusion of Theorem 4.

The rest of the paper is organized as follows. We start by discussing in Section 2 the patterns generated by the PG \operatorname{PG} operator applied to the sequence of powers of 2 2 and to Fibonacci sequences. In Section 3 we introduce a relation according to which two rows of a table built with the iteration of the PG \operatorname{PG} operator are equivalent if they coincide except for at most a finite number of numbers on them, and then we prove Theorem 2. In Sections 4 and 5 we address the relation between the (leap-)fixed points of the operator PG \operatorname{PG} and the formal power series over 𝔽 2 \mathbb{F}_{2}, and then we prove Theorems 3 and 4 in Section 6. We conclude with the presentation of some suitable examples in the last section.

## 2. Fibonacci sequences and Proth-Gilbreath’s operator

Let a, b ≥ 0 a,b\geq 0 be the first two integers on the first row of the ( P-G) triangle. If we want the first line to be reproduced on the second line, then the third element has to coincide with | b − a | |b-a|, that is, either with b − a b-a or with − b + a -b+a. If a ≤ b a\leq b, and we also assume this increasing order of the entries that follow, we find that the numbers on the first row are: a a, a ​ 2 1 a2^{1}, a ​ 2 2, … a2^{2},\dots Then, this line is a fixed point of the Proth-Gilbreath operator. Note that the triangle would be perfectly flat if a = 0 a=0.

If the ordering condition is not apriori required, but instead the choice of entries that follow to the right asks that the numbers be bounded, sooner or later a periodic sequence will emerge, maybe except for a few terms at the left end.

A combination of the two types, periodic and interspersed with a ​ 2 k a2^{k} ’s, with k k unlimited, develops if the size bounding condition is no longer imposed. Any such line is a fixed point of the PG \operatorname{PG} operator and they all reduce to periodic patterns if their entries are taken modulo d d, like the one in Figure 4 (left).

Figure 4. Periodic patterns in ( P-G) triangles. The left triangle has on the first row the powers of 2 2 starting with 1, 2, 4, 8, … 1,2,4,8,\dots, and the right triangle has on the first row the terms of the Fibonacci sequence with the initial parameters 15 15 and 7 7. In both images, the colors represent the residue classes modulo 19 19 of all entries.

An augmented pattern is produced with the recursive Fibonacci rule F k − 1 + F k = F k + 1 F_{k-1}+F_{k}=F_{k+1}. The Proth-Gilbreath operator transforms a Fibonacci sequence into a shifted version:

 |

F s F_{s} |  | F s + 1 F_{s+1} |  | F s + 2 F_{s+2} |  | F s + 3 F_{s+3} |  | F s + 4 F_{s+4} | … \dots |  |

 | F s − 1 F_{s-1} |  | F s F_{s} |  | F s + 1 F_{s+1} |  | F s + 2 F_{s+2} |  | F s + 3 F_{s+3} | … \dots |

 |  |

Each repeated application of the operator adds a new number to the left side and shifts the entire row to the right. Thus, depending on the hypothesis assumed with the starting parameters on the left, a new triangle with a different periodic pattern grows attached to the left of the ( P-G) triangle, a triangle like the one in Figure 4 (right). Another numerical example is

 |

3 |  | 1 |  | 4 |  | 5 |  | 9 |  | 14 |  | 23 |  | 37 |  | 60 |  | 97 |  | 157 |  | … \dots |

 | 2 |  | 3 |  | 1 |  | 4 |  | 5 |  | 9 |  | 14 |  | 23 |  | 37 |  | 60 |  | … \dots |  |

 |  | 1 |  | 2 |  | 3 |  | 1 |  | 4 |  | 5 |  | 9 |  | 14 |  | 23 |  | … \dots |  |  |

 |  |  | 1 |  | 1 |  | 2 |  | 3 |  | 1 |  | 4 |  | 5 |  | 9 |  | … \dots |  |  |  |

 |  |  |  | 0 |  | 1 |  | 1 |  | 2 |  | 3 |  | 1 |  | 4 |  | … \dots |  |  |  |  |

 |  |  |  |  | 1 |  | 0 |  | 1 |  | 1 |  | 2 |  | 3 |  | … \dots |  |  |  |  |  |

 |  |  |  |  |  | 1 |  | 1 |  | 0 |  | 1 |  | 1 |  | … \dots |  |  |  |  |  |  |

 |  |  |  |  |  |  | 0 |  | 1 |  | 1 |  | 0 |  | … \dots |  |  |  |  |  |  |  |

 |  |  |  |  |  |  |  | 1 |  | 0 |  | 1 |  | … \dots |  |  |  |  |  |  |  |  |

 |  |  |  |  |  |  |  |  | 1 |  | 1 |  | … \dots |  |  |  |  |  |  |  |  |  |

 |  |  |  |  |  |  |  |  |  | 0 |  | … \dots |  |  |  |  |  |  |  |  |  |  |

 |  |

Then, a simple argument by induction shows that the emerging triangle from the left consists of the repeated alternation of a 0 0 with two 1 1 ’s, and the pattern becomes uniform allover across the entire triangle if all the numbers it contains are taken modulo 2 2. In particular, note that in all these triangles, except for a finite number of cases at the top, the numbers on the left-edge are in exact proportions: one-third 0 0 ’s and two-thirds 1 1 ’s.

In conclusion, together with the previous remarks concerning the sequence of powers of two, we conclude that the fixed and the ’ almost fixed ’ points of the PG \operatorname{PG} operator point to a class of triangles that either have on the left-edge one hundred percent ones or two-thirds of the entries ones.

###### Proposition 1.

1. The Proth-Gilbreath operator applied recursively on Fibonacci sequences generated by non-negative relatively prime integers generates a triangle, which on its left-edge, except for a finite number of entries, contains the periodic sequence 1, 1, 0, 1, 1, 0, … 1,1,0,1,1,0,\dots

2. The left edge of the ( P-G) triangle contains only ones if the sequence of numbers on the first row is 1, 2, 2 2, 2 3, 2 4, … 1,2,2^{2},2^{3},2^{4},\dots

## 3. The characterization of fixed points

To describe the combined nature of horizontal and vertical periodicity observed in the examples discussed in Section 2, we start by introducing an equivalence relation on the sequences that replicate fully or only partially in the triangle.

### 3.1. Notations and definitions

Denote by ℒ \mathcal{L} the set of all sequences of non-negative integers and by ℒ 2 \mathcal{L}_{2} the set of sequences of 0 0 and 1 1.

We say that two sequences in ℒ \mathcal{L} are equivalent if they ultimately coincide. Precisely, if 𝒂 = ( a 1, a 2, …) \bm{a}=(a_{1},a_{2},\dots) and 𝒃 = ( b 1, b 2, …) \bm{b}=(b_{1},b_{2},\dots) are in ℒ \mathcal{L}, then 𝒂 ≍ 𝒃 \bm{a}\asymp\bm{b} if there exists m, n ≥ 1 m,n\geq 1 such that a m + k = b n + k a_{m+k}=b_{n+k} for k ≥ 0 k\geq 0. One immediately checks this relation is reflexive, symmetric and transitive, that is, ‘ ≍ \asymp ’ is an equivalence relation.

Let ℒ ^ = ℒ / ≍ \widehat{\mathcal{L}}=\mathcal{L}{/_{\asymp}} denote the set of equivalence classes. Thus, if 𝜶 ∈ ℒ ^ \bm{\alpha}\in\widehat{\mathcal{L}} and 𝒂 ∈ 𝜶 \bm{a}\in\bm{\alpha}, then 𝜶 = { 𝒃 ∈ ℒ: 𝒃 ≍ 𝒂 } \bm{\alpha}=\{\bm{b}\in\mathcal{L}:\bm{b}\asymp\bm{a}\}. Also, if 𝒂 ∈ ℒ \bm{a}\in\mathcal{L}, we denote by 𝒂 ^ \hat{{\bf\it\bm{a}}} its equivalence class, so that 𝒂 ^ = { 𝒃 ∈ ℒ: 𝒃 ≍ 𝒂 } \hat{{\bf\it\bm{a}}}=\{\bm{b}\in\mathcal{L}:\bm{b}\asymp\bm{a}\}.

Denote now by Ψ: ℒ → ℒ \Psi:\mathcal{L}\to\mathcal{L} the PG \operatorname{PG} operator. Then, immediately by the definition, we see that if 𝒂 ≍ 𝒃 \bm{a}\asymp\bm{b}, it follows that Ψ ⁡ ( 𝒂) ≍ Ψ ⁡ ( 𝒃) \Psi(\bm{a})\asymp\Psi(\bm{b}).

We also have the associated quotient map Ψ ^: ℒ ^ → ℒ ^ \widehat{\Psi}:\widehat{\mathcal{L}}\to\widehat{\mathcal{L}}, which is defined as follows: let 𝜶 ∈ ℒ ^ \bm{\alpha}\in\widehat{\mathcal{L}} and let 𝒂 ∈ 𝜶 \bm{a}\in\bm{\alpha}, so that 𝜶 = 𝒂 ^ \bm{\alpha}=\hat{{\bf\it\bm{a}}}. Then put Ψ ^ ​ ( 𝜶):= Ψ ⁡ ( 𝒂) ^ \widehat{\Psi}(\bm{\alpha}):=\widehat{\Psi(\bm{a})}. Note that Ψ ^ \widehat{\Psi} is well defined, since if 𝒂 \bm{a} and 𝒃 \bm{b} are both in 𝜶 \bm{\alpha}, then 𝒂 ≍ 𝒃 \bm{a}\asymp\bm{b}, which implies Ψ ⁡ ( 𝒂) ≍ Ψ ⁡ ( 𝒃) \Psi(\bm{a})\asymp\Psi(\bm{b}), so that Ψ ⁡ ( 𝒂) ^ = Ψ ⁡ ( 𝒃) ^ \widehat{\Psi(\bm{a})}=\widehat{\Psi(\bm{b})}. Now the problem of characterizing the rows that repeat in the triangle ( P-G) is the same as that of describing the fixed points of Ψ ^ \widehat{\Psi}.

Note that Ψ \Psi and Ψ ^ \widehat{\Psi} restricted to ℒ 2 \mathcal{L}_{2} and the subset of equivalences classes ℒ 2 ^ = ℒ 2 / ≍ \widehat{\mathcal{L}_{2}}=\mathcal{L}_{2}/_{\!\asymp}, which contains only sequences of 0 0 ’s and 1 1 ’s, act in the same manner. Furthermore, we can also describe the rows of the ( P-G) triangle using the formal power series with non-negative integer coefficients or those with coefficients in 𝔽 2 = ℤ / 2 ​ ℤ \mathbb{F}_{2}=\mathbb{Z}/2\mathbb{Z}, denoted by 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]]. Thus, to a sequence 𝜶 = ( a 0, a 1, a 2, …) \bm{\alpha}=(a_{0},a_{1},a_{2},\dots), we associate the formal power series

 | ϕ ⁡ ( 𝜶) = ϕ ⁡ ( 𝜶) ​ ( X):= ∑ k ≥ 0 a k ​ X k. \begin{split}\phi(\bm{\alpha})=\phi(\bm{\alpha})(X):=\sum_{k\geq 0}a_{k}X^{k}.\end{split} |  |

For example, if 𝑭 \bm{F} is the periodic sequence 𝑭 = ( 0, 1, 1, 0, 1, 1, 0, 1, 1, …) \bm{F}=(0,1,1,0,1,1,0,1,1,\dots), then

 | ϕ ⁡ ( 𝑭) = X + X 2 + X 4 + X 5 + X 6 + X 7 + ⋯. \phi(\bm{F})=X+X^{2}+X^{4}+X^{5}+X^{6}+X^{7}+\cdots. |  |

Note that ϕ ⁡ ( 𝑭) \phi(\bm{F}) belongs also to 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] and additionally it can be expressed as a rational function:

 | ϕ ⁡ ( 𝑭) = ( X + X 2) ​ ∑ k ≥ 0 X 3 ​ k = X + X 2 1 + X 3 = X 1 + X + X 2. \phi(\bm{F})=\big(X+X^{2}\big)\sum_{k\geq 0}X^{3k}=\frac{X+X^{2}}{1+X^{3}}=\frac{X}{1+X+X^{2}}. |  | (5) |

Also remark that if 𝜶 = ( α 0, α 1, …) \bm{\alpha}=(\alpha_{0},\alpha_{1},\dots) has components in 𝔽 2 \mathbb{F}_{2}, then the PG \operatorname{PG} operator acts by the following formula:

 | ϕ ⁡ ( Ψ ⁡ ( 𝜶)):= ∑ k ≥ 0 ( a k + a k + 1) ​ X k = ∑ k ≥ 0 a k ​ X k + 1 X ​ ∑ k ≥ 0 a k ​ X k − a 0 X, \phi(\Psi(\bm{\alpha})):=\sum_{k\geq 0}(a_{k}+a_{k+1})X^{k}=\sum_{k\geq 0}a_{k}X^{k}+\frac{1}{X}\sum_{k\geq 0}a_{k}X^{k}-\frac{a_{0}}{X}\,, |  |

that is,

 | ϕ ⁡ ( Ψ ⁡ ( 𝜶)) = ( 1 + X) ​ ϕ ​ ( 𝜶) − α 0 X. \phi\big(\Psi(\bm{\alpha})\big)=\frac{(1+X)\phi(\bm{\alpha})-\alpha_{0}}{X}. |  | (6) |

### 3.2. Proof of Theorem 2

Suppose in the following that the entries from the first line of ( P-G) are only 0 0 ’s and 1 1 ’s, so that we take advantage of the simplicity of operating with power series with coefficients in 𝔽 2 \mathbb{F}_{2}, where − 1 = 1 -1=1.

Note that if 𝜶 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} then Ψ ⁡ ( 𝜶) ∈ ℒ 2 \Psi(\bm{\alpha})\in\mathcal{L}_{2}, so that the whole triangle ( P-G) contains only elements of 𝔽 2 \mathbb{F}_{2}.

In terms of power series, the condition that two rows in ( P-G) are ultimately identical translates into a condition that the difference between one of the series and the shift of the other is a polynomial. We state this observation in the following lemma that holds in ℒ \mathcal{L}.

###### Lemma 1.

Let 𝛂, 𝛃 ∈ ℒ \bm{\alpha},\bm{\beta}\in\mathcal{L}. Then, 𝛂 ≍ 𝛃 \bm{\alpha}\asymp\bm{\beta} if and only if there exists an integer r ≥ 0 r\geq 0 and a polynomial P ⁡ ( X) ∈ ℤ ⁡ [X] P(X)\in\mathbb{Z}[X] such that

 | either ϕ ⁡ ( 𝜶) − X r ​ ϕ ​ ( 𝜷) = P ⁡ ( X) or ϕ ⁡ ( 𝜷) − X r ​ ϕ ​ ( 𝜶) = P ⁡ ( X). \begin{split}\mathrm{either}\quad\phi(\bm{\alpha})-X^{r}\phi(\bm{\beta})=P(X)\quad\mathrm{or}\quad\phi(\bm{\beta})-X^{r}\phi(\bm{\alpha})=P(X).\end{split} |  | (7) |

###### Proof.

Suppose 𝜶 ≍ 𝜷 \bm{\alpha}\asymp\bm{\beta}. Then there exists two integers u, v ≥ 0 u,v\geq 0, a formal series h ⁡ ( X) h(X) and two polynomials U ⁡ ( X), V ⁡ ( X) ∈ ℤ ⁡ [X] U(X),V(X)\in\mathbb{Z}[X] of degrees less than u u and v v, respectively, such that ϕ ⁡ ( 𝜶) = U ⁡ ( X) + X u ​ h ​ ( X) \phi(\bm{\alpha})=U(X)+X^{u}h(X) and ϕ ⁡ ( 𝜷) = V ⁡ ( X) + X v ​ h ​ ( X) \phi(\bm{\beta})=V(X)+X^{v}h(X). Suppose u ≤ v u\leq v and let r = v − u r=v-u. Then X r ​ ϕ ​ ( 𝜶) = X r ​ U ​ ( X) + X v ​ h ​ ( X) X^{r}\phi(\bm{\alpha})=X^{r}U(X)+X^{v}h(X). Then it follows that

 | ϕ ⁡ ( 𝜷) − X r ​ ϕ ​ ( 𝜶) = ( V ⁡ ( X) + X v ​ h ​ ( X)) − ( X r ​ U ​ ( X) + X v ​ h ​ ( X)) = V ⁡ ( X) − X r ​ U ​ ( X), \begin{split}\phi(\bm{\beta})-X^{r}\phi(\bm{\alpha})&=\big(V(X)+X^{v}h(X)\big)-\big(X^{r}U(X)+X^{v}h(X)\big)\\ &=V(X)-X^{r}U(X),\end{split} |  |

equality which is the first of the two alternatives in ( 7) with P ⁡ ( X) = V ⁡ ( X) − X r ​ U ​ ( X) P(X)=V(X)-X^{r}U(X). Similarly, if u > v u>v, we find that the second equality in( 7) holds.

Conversely, suppose ϕ ⁡ ( 𝜶) − X r ​ ϕ ​ ( 𝜷) = P ⁡ ( X) \phi(\bm{\alpha})-X^{r}\phi(\bm{\beta})=P(X), the other possibility being treated symmetrically. Then ϕ ⁡ ( 𝜶) = P ⁡ ( X) + X r ​ ϕ ​ ( 𝜷) \phi(\bm{\alpha})=P(X)+X^{r}\phi(\bm{\beta}). Here, the equality of the series is equivalent with the equality of the coefficients, and this in turn holds modulo a shift of size r r for all terms of 𝜶 \bm{\alpha} and 𝜷 \bm{\beta} of sufficiently large ranks. Therefore 𝜶 ≍ 𝜷 \bm{\alpha}\asymp\bm{\beta}. This concludes the proof of the lemma. ∎

Then, by Lemma 1, the property of 𝜶 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} that 𝜶 ^ \widehat{\bm{\alpha}} is a fixed point of Ψ ^ \widehat{\Psi}, that is, Ψ ⁡ ( 𝜶) ≍ 𝜶 \Psi(\bm{\alpha})\asymp\bm{\alpha}, translates into the existence of an integer r ≥ 0 r\geq 0 such that

 | ϕ ⁡ ( Ψ ⁡ ( 𝜶)) − X r ​ ϕ ​ ( 𝜶) ∈ 𝔽 2 ​ [X] or ϕ ⁡ ( 𝜶) − X r ​ ϕ ​ ( Ψ ⁡ ( 𝜶)) ∈ 𝔽 2 ​ [X]. \begin{split}\phi(\Psi(\bm{\alpha}))-X^{r}\phi(\bm{\alpha})\in\mathbb{F}_{2}[X]\quad\mathrm{or}\quad\phi(\bm{\alpha})-X^{r}\phi(\Psi(\bm{\alpha}))\in\mathbb{F}_{2}[X].\end{split} |  | (8) |

The case r = 0 r=0 holds when the rows ϕ ⁡ ( 𝜶) \phi(\bm{\alpha}) and ϕ ⁡ ( Ψ ⁡ ( 𝜶)) \phi(\Psi(\bm{\alpha})) are the same, with no shifting, with the possible exception of some terms from the beginning, situation that is covered in Theorem 2 by the first expression in ( 1).

Suppose now that r ≥ 1 r\geq 1. Using formula ( 6), we see that this couple of conditions ( 8) is equivalent with the couple:

 | ( 1 + X) ​ ϕ ​ ( 𝜶) − α 0 X − X r ​ ϕ ​ ( 𝜶) ∈ 𝔽 2 ​ [X] or ϕ ⁡ ( 𝜶) − X r ​ ( 1 + X) ​ ϕ ​ ( 𝜶) − α 0 X ∈ 𝔽 2 ​ [X]. \begin{split}\frac{(1+X)\phi(\bm{\alpha})-\alpha_{0}}{X}-X^{r}\phi(\bm{\alpha})\in\mathbb{F}_{2}[X]\quad\mathrm{or}\quad\phi(\bm{\alpha})-X^{r}\frac{(1+X)\phi(\bm{\alpha})-\alpha_{0}}{X}\in\mathbb{F}_{2}[X].\end{split} |  |

Equivalently, these can also be reformulated as

 | ϕ ⁡ ( 𝜶) ​ ( 1 + X + X r + 1) ∈ 𝔽 2 ​ [X] or ϕ ⁡ ( 𝜶) ​ ( X r − 1 ​ ( 1 + X) + 1) ∈ 𝔽 2 ​ [X], \begin{split}\phi(\bm{\alpha})\big(1+X+X^{r+1}\big)\in\mathbb{F}_{2}[X]\quad\mathrm{or}\quad\phi(\bm{\alpha})\big(X^{r-1}(1+X)+1\big)\in\mathbb{F}_{2}[X],\end{split} |  |

relations which, in their turn, are equivalent to formulation in ( 1). This concludes the proof of Theorem 2.

###### Remark 1.

Note that in Theorem 1 we could have let r r take integer values not necessarily positive. Indeed, observing that

 | P ⁡ ( X) 1 + X + X − r = X r ​ P ​ ( X) X r ​ ( 1 + X) + 1 = P ∗ ​ ( X) X r ​ ( 1 + X) + 1, \begin{split}\frac{P(X)}{1+X+X^{-r}}=\frac{X^{r}P(X)}{X^{r}(1+X)+1}=\frac{P^{*}(X)}{X^{r}(1+X)+1},\end{split} |  |

for some polynomial P ∗ ​ ( X) ∈ 𝔽 2 ​ [X] P^{*}(X)\in\mathbb{F}_{2}[X], by letting r r free, not necessarily positive, the two alternatives in ( 1) would have been identified in one. So we could say ( 1) acts like a ‘hinge’ mirroring in the ( P-G) triangle the horizontal ‘waves’ with the vertical ones that pass along both ways from top to bottom and from bottom to top.

### 3.3. The Fibonacci series

The Fibonacci sequence 𝑭 = ( 0, 1, 1, 0, 1, 1, 0, 1, 1, …) mod 2 \bm{F}=(0,1,1,0,1,1,0,1,1,\dots)\mod 2 is periodic and it can be expressed as the rational function ( 5), which is exactly as that in Theorem 2 with P ⁡ ( X) = X P(X)=X and r = 2 r=2. As a consequence it follows that 𝑭 ^ \widehat{\bm{F}} is a fixed point of Ψ ^ \widehat{\Psi}. A direct calculation or else a manipulation of the associated series shows that the other two Fibonacci sequences given by the initial conditions 1, 0 1,0 and 1, 1 1,1 are:

 | 𝑭 ′ = ( 1, 0, 1, 1, 0, 1, 1, 0, 1, …) ​ and ​ ϕ ​ ( 𝑭 ′) = 1 + X 1 + X + X 2, 𝑭 ′′ = ( 1, 1, 0, 1, 1, 0, 1, 1, 0, …) ​ and ​ ϕ ​ ( 𝑭 ′′) = 1 1 + X + X 2. \begin{split}\bm{F}^{\prime}&=(1,0,1,1,0,1,1,0,1,\dots)\text{ and }\phi(\bm{F}^{\prime})=\frac{1+X}{1+X+X^{2}},\\ \bm{F}^{\prime\prime}&=(1,1,0,1,1,0,1,1,0,\dots)\text{ and }\phi(\bm{F}^{\prime\prime})=\frac{1}{1+X+X^{2}}.\end{split} |  |

Note that 𝑭, 𝑭 ′, 𝑭 ′′ \bm{F},\bm{F}^{\prime},\bm{F}^{\prime\prime} are the rows that alternate periodically to build the entire Fibonacci ( P-G) triangle modulo 2 2.

We remark that the closely related sequence 𝑻 = ( 0, 1, 1, 1, 0, 1, 1, 1, 0, …) \bm{T}=(0,1,1,1,0,1,1,1,0,\dots) does not have ϕ ⁡ ( 𝑻) = X 1 + X + X 3 \phi(\bm{T})=\frac{X}{1+X+X^{3}} as the rational function associated from Theorem 2, as one would be tempted to assume. The reason is, on the one hand, the subsequent rows that 𝑻 \bm{T} generates are:

 |

0 |  | 1 |  | 1 |  | 1 |  | 0 |  | 1 |  | 1 |  | 1 |  | 0 |  | 1 |  | 1 |  | ​​​​1 |  | … \!\!\dots |

 | 1 |  | 0 |  | 0 |  | 1 |  | 1 |  | 0 |  | 0 |  | 1 |  | 1 |  | 0 |  | ​​0 |  | … \!\!\dots |  |

 |  | 1 |  | 0 |  | 1 |  | 0 |  | 1 |  | 0 |  | 1 |  | 0 |  | 1 |  | 0 |  | … \!\!\dots |  |  |

 |  |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  | 0 |  | … \!\!\dots |  |  |  |

 |  |

and afterwards all the components become zeros. In particular we see that 𝑻 ^ \widehat{\bm{T}} is not a fixed point of Ψ ^ \widehat{\Psi}. On the other hand, the associated series of 𝑻 \bm{T} is

 | ϕ ⁡ ( 𝑻) = ( X + X 2 + X 3) ​ ∑ k ≥ 0 X 4 ​ k = X ⁡ ( 1 + X + X 2) 1 + X 4, \begin{split}\phi(\bm{T})=(X+X^{2}+X^{3})\sum_{k\geq 0}X^{4k}=\frac{X(1+X+X^{2})}{1+X^{4}},\end{split} |  |

which cannot be expressed as the ratio between a polynomial in 𝔽 2 ​ [X] \mathbb{F}_{2}[X] and 1 + X + X r 1+X+X^{r} or X r ​ ( 1 + X) + 1 X^{r}(1+X)+1 for any integer r ≥ 0 r\geq 0, because if it were possible it would contradict Theorem 2.

## 4. Fixed points and their formal power series

Let r ≥ 2 r\geq 2 be an integer and consider the polynomial f r ​ ( X) = X r + X + 1 f_{r}(X)=X^{r}+X+1. Note that f r ​ ( X) f_{r}(X) has no roots in 𝔽 2 ​ [X] \mathbb{F}_{2}[X], because f r ​ ( 0) = f r ​ ( 1) = 1 f_{r}(0)=f_{r}(1)=1, so that we factor f r ​ ( X) f_{r}(X) over 𝔽 ¯ ​ 𝔽 2 ​ [X] \mathrlap{\hskip 0.3pt\overline{\scalebox{0.860}[1]{\phantom{$\mathbb{F}$}}}}\mathbb{F}_{2}[X], where 𝔽 ¯ ​ 𝔽 2 \mathrlap{\hskip 0.3pt\overline{\scalebox{0.860}[1]{\phantom{$\mathbb{F}$}}}}\mathbb{F}_{2} is an algebraic closure of 𝔽 2 \mathbb{F}_{2}. Thus, f r ( X) = ( X − η 1) ⋅ ( X − η 2) ⋯ ( X − η r) f_{r}(X)=(X-\eta_{1})\cdot(X-\eta_{2})\cdots(X-\eta_{r}), with η 1, η 2, …, η r ∈ 𝔽 ¯ ​ 𝔽 2 \eta_{1},\eta_{2},\dots,\eta_{r}\in\mathrlap{\hskip 0.3pt\overline{\scalebox{0.860}[1]{\phantom{$\mathbb{F}$}}}}\mathbb{F}_{2}.

Let K = 𝔽 2 ​ ( η 1, …, η r) ⊂ 𝔽 ¯ ​ 𝔽 2 K=\mathbb{F}_{2}(\eta_{1},\dots,\eta_{r})\subset\mathrlap{\hskip 0.3pt\overline{\scalebox{0.860}[1]{\phantom{$\mathbb{F}$}}}}\mathbb{F}_{2} be the smallest subfield of 𝔽 ¯ ​ 𝔽 2 \mathrlap{\hskip 0.3pt\overline{\scalebox{0.860}[1]{\phantom{$\mathbb{F}$}}}}\mathbb{F}_{2} that contains all the roots of f r ​ ( X) f_{r}(X) and let d = [K: 𝔽 2] d=[K:\mathbb{F}_{2}] be the degree of the extension. Then, the cardinality of K K is a prime power, and in our case it is | K | = 2 d |K|=2^{d}. Since K × K^{\times}, the largest multiplicative subgroup of K K, is cyclic and contains all the non-zero elements, we have | K × | = 2 d − 1 |K^{\times}|=2^{d}-1. In particular, it follows that

 | η 1 2 d − 1 = η 2 2 d − 1 = ⋯ = η r 2 d − 1 = 1. \eta_{1}^{2^{d}-1}=\eta_{2}^{2^{d}-1}=\cdots=\eta_{r}^{2^{d}-1}=1. |  | (9) |

###### Lemma 2.

All the roots of the polynomial f r ​ ( X) = X r + X + 1 f_{r}(X)=X^{r}+X+1 are distinct in an algebraic closure of 𝔽 2 \mathbb{F}_{2}.

###### Proof.

Suppose η 1, η 2, …, η r \eta_{1},\eta_{2},\dots,\eta_{r} are the roots of f r ​ ( X) f_{r}(X) and there exist distinct indices j j and k k such that η j = η k \eta_{j}=\eta_{k}. Then, f r ​ ( X) = ( X − η j) 2 ​ H ​ ( X) f_{r}(X)=(X-\eta_{j})^{2}H(X) for some polynomial H ​ ( X) ∈ 𝔽 2 ​ [X] H(X)\in\mathbb{F}_{2}[X]. Note that η j \eta_{j} is also a root of the derivative f r ′ ​ ( X) f_{r}^{\prime}(X), since

 | f r ′ ​ ( X) = ( X − η j) ​ ( 2 ​ H ​ ( X) + ( X − η j) ​ H ′ ​ ( X)). f_{r}^{\prime}(X)=(X-\eta_{j})\big(2H(X)+(X-\eta_{j})H^{\prime}(X)\big). |  |

It then follows that

 | η j r + η j + 1 = 0 and r ​ η j r − 1 + 1 = 0. \eta_{j}^{r}+\eta_{j}+1=0\ \ \text{ and }\ \ r\eta_{j}^{r-1}+1=0. |  |

Here, the second equality cannot hold if r r is even (that is, if r r ’s image in 𝔽 2 \mathbb{F}_{2} is 0 0), since, otherwise, it would imply that 1 = 0 1=0.

If r r is odd, then we simultaneously have

 | η j r + η j + 1 = 0 and η j r − 1 + 1 = 0. \eta_{j}^{r}+\eta_{j}+1=0\ \ \text{ and }\ \ \eta_{j}^{r-1}+1=0. |  |

But this again implies the same contradiction 1 = 0 1=0, and, therefore, the lemma is proved.

∎

The equalities ( 9) show that the η j \eta_{j} ’s are roots to both polynomials f r ​ ( X) f_{r}(X) and X 2 d − 1 − 1 X^{2^{d}-1}-1. Therefore, employing Lemma 2, we find that X 2 d − 1 − 1 X^{2^{d}-1}-1 is divisible by f r ​ ( X) f_{r}(X), so that

 | X 2 d − 1 − 1 = ( X r + X + 1) ​ H ​ ( X), X^{2^{d}-1}-1=(X^{r}+X+1)H(X), |  | (10) |

for some H ​ ( X) ∈ 𝔽 2 ​ [X] H(X)\in\mathbb{F}_{2}[X].

Suppose now that 𝜶 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} belongs to a class of the equivalence relation ≍ \asymp that is a fixed point of Ψ ^ \widehat{\Psi}. Then, on combining the conclusion of Theorem 2 with the expression ( 10), we find that the power series associated to 𝜶 \bm{\alpha} can be written as

 | ϕ ⁡ ( 𝜶) = G ⁡ ( X) 1 − X 2 d − 1, \phi(\bm{\alpha})=\frac{G(X)}{1-X^{2^{d}-1}}, |  | (11) |

where G ⁡ ( X) = P ⁡ ( X) ​ H ​ ( X) G(X)=P(X)H(X) is a fixed polynomial in 𝔽 2 ​ [X] \mathbb{F}_{2}[X].

Let us note that the reciprocal of this statement is also true.

And still, taking into account that the operations on the coefficients are made in 𝔽 2 \mathbb{F}_{2}, the rational fraction ( 11) can be written equivalently as a power series that comprises the coefficients of 𝜶 \bm{\alpha}. We state our findings in the next theorem.

###### Theorem 5.

Let 𝛂 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2}. Then, 𝛂 \bm{\alpha} is ultimately identical with Ψ ⁡ ( 𝛂) \Psi(\bm{\alpha}) if and only if there exists a positive integer d d and a polynomial G ​ ( X) ∈ 𝔽 2 ​ [X] G(X)\in\mathbb{F}_{2}[X] such that the power series associated to 𝛂 \bm{\alpha} is

 | ϕ ⁡ ( 𝜶) = G ⁡ ( X) 1 − X 2 d − 1 = G ⁡ ( X) ​ ( 1 + X 2 d − 1 + X 2 ​ ( 2 d − 2) + X 3 ​ ( 2 d − 1) + ⋯). \phi(\bm{\alpha})=\frac{G(X)}{1-X^{2^{d}-1}}=G(X)\left(1+X^{2^{d}-1}+X^{2(2^{d}-2)}+X^{3(2^{d}-1)}+\cdots\right). |  |

## 5. Leap fixed points of the Proth-Gilbreath operator

The next lemma provides the relation between the powers series associated to two rows in the ( P-G) triangle.

###### Lemma 3.

Let 𝛂 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} be a row in the ( P-G) triangle and let k ≥ 0 k\geq 0 be integer. Then, there exits a unique polynomial R ​ ( X) ∈ 𝔽 2 ​ [X] R(X)\in\mathbb{F}_{2}[X] of degree 0 ≤ deg ⁡ ( R ⁡ ( X)) ≤ k − 1 0\leq\deg(R(X))\leq k-1 such that

 | ϕ ⁡ ( Ψ [k] ​ ( 𝜶)) = ( 1 + X) k ​ ϕ ​ ( 𝜶) − R ⁡ ( X) X k ​ for k ≥ 1. \phi\big(\Psi^{[k]}(\bm{\alpha})\big)=\frac{(1+X)^{k}\phi(\bm{\alpha})-R(X)}{X^{k}}\text{\ \ for $k\geq 1$}. |  | (12) |

###### Proof.

Let ϕ ⁡ ( 𝜶) \phi(\bm{\alpha}) be the power series associated to 𝜶 \bm{\alpha}. If k = 0 k=0 relation ( 12) is trivial and if k = 1 k=1 it coincides with ( 6). Next we proceed by induction. Let k ≥ 1 k\geq 1 be fixed and suppose

 | ϕ ⁡ ( Ψ [k] ​ ( 𝜶)) = ( 1 + X) k ​ ϕ ​ ( 𝜶) − R ⁡ ( X) X k, \phi\big(\Psi^{[k]}(\bm{\alpha})\big)=\frac{(1+X)^{k}\phi(\bm{\alpha})-R(X)}{X^{k}}\,, |  | (13) |

for some R ​ ( X) ∈ 𝔽 2 ​ [X] R(X)\in\mathbb{F}_{2}[X], and 0 ≤ deg ⁡ ( R ⁡ ( X)) ≤ k − 1 0\leq\deg(R(X))\leq k-1. Then, by ( 6) it follows that

 | ϕ ⁡ ( Ψ [k + 1] ​ ( 𝜶)) = ϕ ⁡ ( Ψ ⁡ ( ϕ ⁡ ( Ψ [k] ​ ( 𝜶)))) = ( 1 + X) ​ ϕ ​ ( Ψ [k] ​ ( 𝜶)) − a 0 X. \phi\big(\Psi^{[k+1]}(\bm{\alpha})\big)=\phi\big(\Psi(\phi(\Psi^{[k]}(\bm{\alpha})))\big)=\frac{(1+X)\phi\big(\Psi^{[k]}(\bm{\alpha})\big)-a_{0}}{X}\,. |  |

On inserting ( 13), we see that the above is

 | ϕ ​ ( Ψ [k + 1] ​ ( 𝜶)) = ( 1 + X) ​ ( ( 1 + X) k ​ ϕ ​ ( 𝜶) − R ⁡ ( X)) ​ X − k − a 0 X = ( 1 + X) k + 1 ​ ϕ ​ ( 𝜶) − R 1 ​ ( X) X k + 1, \begin{split}\phi\big(\Psi^{[k+1]}(\bm{\alpha})\big)&=\frac{(1+X)\big((1+X)^{k}\phi(\bm{\alpha})-R(X)\big)X^{-k}-a_{0}}{X}\\ &=\frac{(1+X)^{k+1}\phi(\bm{\alpha})-R_{1}(X)}{X^{k+1}}\,,\end{split} |  |

where R 1 ​ ( X) = a 0 ​ X k + ( 1 + X) ​ R ​ ( X) ∈ 𝔽 2 ​ [X] R_{1}(X)=a_{0}X^{k}+(1+X)R(X)\in\mathbb{F}_{2}[X] is a polynomial of degree ≤ k \leq k. This completes the proof of the lemma. ∎

A quasi-periodicity phenomenon that can occur in a triangle is the situation in which two rows situated at l ≥ 0 l\geq 0 ranks apart are identical, except for a finite number of entries at their left-end entry. In the language of the equivalence classes introduced in Section 3.1, we will say that a row 𝜶 \bm{\alpha} of ( P-G) is an *l l -leap fixed point*of the Proth-Gilbreath operator if Ψ [l] ​ ( 𝜶 ^) = 𝜶 ^ {\Psi}^{[l]}(\hat{\mathbf{\bm{\alpha}}})=\hat{\mathbf{\bm{\alpha}}}. Note that any row is a 0 0 -leap fixed point of Ψ \Psi and fixed points are the same as 1 1 -leap fixed points of Ψ \Psi. Similarly, we say that 𝜶 ^ ∈ ℒ ^ \widehat{\bm{\alpha}}\in\widehat{\mathcal{L}} is an l l -leap fixed point of Ψ ^ \widehat{\Psi} if Ψ ^ [l] ​ ( 𝜶 ^) = 𝜶 ^ \widehat{\Psi}^{[l]}(\widehat{\bm{\alpha}})=\widehat{\bm{\alpha}} for some natural number l l.

Then, using the observation from Lemma 1, we know that 𝜶 \bm{\alpha} is an l l -leap fixed point if and only if there exists an integer r ≥ 0 r\geq 0 such that

 | ϕ ⁡ ( Ψ [l] ​ ( 𝜶)) − X r ​ ϕ ​ ( 𝜶) ∈ 𝔽 2 ​ [X] or ϕ ⁡ ( 𝜶) − X r ​ ϕ ​ ( Ψ [l] ​ ( 𝜶)) ∈ 𝔽 2 ​ [X]. \begin{split}\phi\big(\Psi^{[l]}(\bm{\alpha})\big)-X^{r}\phi(\bm{\alpha})\in\mathbb{F}_{2}[X]\quad\mathrm{or}\quad\phi(\bm{\alpha})-X^{r}\phi\big(\Psi^{[l]}(\bm{\alpha})\big)\in\mathbb{F}_{2}[X].\end{split} |  |

On inserting formula ( 12), we find that the above statement is equivalent with

 | ( 1 + X) l ​ ϕ ​ ( 𝜶) − R ⁡ ( X) X l − X r ​ ϕ ​ ( 𝜶) \displaystyle\frac{(1+X)^{l}\phi(\bm{\alpha})-R(X)}{X^{l}}-X^{r}\phi(\bm{\alpha}) | ∈ 𝔽 2 ​ [X] \displaystyle\in\mathbb{F}_{2}[X] |  |

or |

 | ϕ ⁡ ( 𝜶) − X r ​ ( 1 + X) l ​ ϕ ​ ( 𝜶) − R ⁡ ( X) X l \displaystyle\phi(\bm{\alpha})-X^{r}\frac{(1+X)^{l}\phi(\bm{\alpha})-R(X)}{X^{l}} | ∈ 𝔽 2 ​ [X] \displaystyle\in\mathbb{F}_{2}[X] |  |

for some integer r ≥ 0 r\geq 0 and some unique polynomial R ​ ( X) ∈ 𝔽 2 ​ [X] R(X)\in\mathbb{F}_{2}[X] of degree < l <l. The ‘or’ statement above is also equivalent with

 | ( ( 1 + X) l + X l + r) ​ ϕ ​ ( 𝜶) ∈ 𝔽 2 ​ [X] or ( X r − l ​ ( 1 + X) l + 1) ​ ϕ ​ ( 𝜶) ∈ 𝔽 2 ​ [X]. \displaystyle\big((1+X)^{l}+X^{l+r}\big)\phi(\bm{\alpha})\in\mathbb{F}_{2}[X]\quad\mathrm{or}\quad\big(X^{r-l}(1+X)^{l}+1\big)\phi(\bm{\alpha})\in\mathbb{F}_{2}[X]\,. |  |

Next, in the following theorem we restate the obtained result noting that, as in Remark 1, the above belonging relations can be adapted by rewriting them changed from one to the other if we allow the power of X X to be negative or not.

###### Theorem 6.

Let l ≥ 0 l\geq 0 be an integer and let 𝛂 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} be a row in the ( P-G) triangle. Then 𝛂 \bm{\alpha} is ultimately replicated identically in the l l -th row that follows 𝛂 \bm{\alpha} if and only if there exist an integer r ≥ 0 r\geq 0 and a polynomial P l ​ ( X) ∈ 𝔽 2 ​ [X] P_{l}(X)\in\mathbb{F}_{2}[X] such that

 | ϕ ⁡ ( 𝜶) = P l ​ ( X) ( 1 + X) l + X r or ϕ ⁡ ( 𝜶) = P l ​ ( X) X r ​ ( 1 + X) l + 1. \phi(\bm{\alpha})=\frac{P_{l}(X)}{(1+X)^{l}+X^{r}}\ \ \mathrm{or}\ \ \phi(\bm{\alpha})=\frac{P_{l}(X)}{X^{r}(1+X)^{l}+1}\,. |  |

## 6. Proof of Theorems 3 and 4

We can now use Theorem 6 to interpret the patterns of ( P-G) and draw out information about formal power series. For this, the basic link is made clear in the following statement.

###### Remark 2.

Let l ≥ 0 l\geq 0 be an integer and let 𝛂 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} be a row in the ( P-G) triangle. Then Ψ ^ [l] ​ ( 𝛂 ^) = 𝛂 ^ \widehat{\Psi}^{[l]}(\widehat{\bm{\alpha}})=\widehat{\bm{\alpha}} if and only if the series of rows that start with 𝛂 \bm{\alpha} belongs to a sequence of equivalence classes that is periodic and l l is the length of a period.

Let now f ​ ( X) ∈ 𝔽 2 ​ [[X]] f(X)\in\mathbb{F}_{2}[[X]] and suppose f ⁡ ( X) = P ⁡ ( X) 1 + X + X r f(X)=\frac{P(X)}{1+X+X^{r}} or f ⁡ ( X) = P ⁡ ( X) X r ​ ( 1 + X) + 1 f(X)=\frac{P(X)}{X^{r}(1+X)+1} for some integer r ≥ 0 r\geq 0 and some polynomial P ​ ( X) ∈ 𝔽 2 ​ [X] P(X)\in\mathbb{F}_{2}[X]. By Theorem 6 with l = 1 l=1, it follows that f ⁡ ( X) = ϕ ⁡ ( 𝜶) f(X)=\phi(\bm{\alpha}) for some 𝜶 ∈ ℒ 2 \bm{\alpha}\in\mathcal{L}_{2} and 𝜶 ^ = Ψ ^ ​ ( 𝜶 ^) \widehat{\bm{\alpha}}=\widehat{\Psi}(\widehat{\bm{\alpha}}). Then 𝜶 \bm{\alpha} is a fixed point not only for Ψ ^ \widehat{\Psi}, but also for its iterations Ψ ^ [l] \widehat{\Psi}^{[l]} for l ≥ 0 l\geq 0. Using the observation in Remark 2 we see that the statement with the rational expressions of ψ ⁡ ( 𝜶) \psi(\bm{\alpha}) from Theorem 6 is equivalent with the second statement from Theorem 3, which is now proved.

To prove Theorem 4 note that its hypothesis is equivalent with the fact that the row 𝜶 \bm{\alpha} for which f ⁡ ( X) = ϕ ⁡ ( 𝜶) f(X)=\phi(\bm{\alpha}) is a leap-fixed point of orders l 1, l 2, …, l r l_{1},l_{2},\dots,l_{r}. That is, in the ( P-G) triangle 𝜶 ^ \widehat{\bm{\alpha}} repeats periodically with each of the periods l 1, l 2, …, l r l_{1},l_{2},\dots,l_{r}. A simple argument by induction then shows that l:= gcd ⁡ ( l 1, l 2, …, l r) l:=\gcd(l_{1},l_{2},\dots,l_{r}) is also a period on which 𝜶 ^ \widehat{\bm{\alpha}} repeats in the triangle. Then Theorem 4 follows as a consequence of Remark 2 and Theorem 3.

## 7. Some relevant examples

In particular cases the Proth-Gilbreath operator action is similar to the transformations that occur in the Ducci number game [10, 6]. There the action is on the numbers placed around on a torus, which can be unfolded equivalently into a periodic sequence. In the particular case with numbers in 𝔽 2 \mathbb{F}_{2} the Ducci operation replaces the numbers from a generation to the next with the sums of neighbors.

### 7.1. Example 𝜹 \bm{\delta}

Of particular interest in the Ducci game are initial states that generate unusually long cycles. Such an example starts with the finite sequence ( 1, 0, 0, 0, 1) (1,0,0,0,1) placed on a torus. Its periodic unfolded version is then the sequence: 𝜹 = ( 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, …) \bm{\delta}=(1,0,0,0,1,1,0,0,0,1,\dots). Then the lines Ψ [k] ​ ( 𝜹) \Psi^{[k]}(\bm{\delta}), k ≥ 0 {k\geq 0}, are also periodic, and finding their general expressions reduces to finding the evolution of their first five components. But this is the same as the recursive outcome of the Ducci operation:

 | ( 1, 0, 0, 0, 1) → ( 1, 0, 0, 1, 0) → ( 1, 0, 1, 1, 1) → ( 1, 1, 0, 0, 0) → ( 0, 1, 0, 0, 1) → ( 1, 1, 0, 1, 1) → ( 0, 1, 1, 0, 0) → ( 1, 0, 1, 0, 0) → ( 1, 1, 1, 0, 1) → ( 0, 0, 1, 1, 0) → ( 0, 1, 0, 1, 0) → ( 1, 1, 1, 1, 0) → ( 0, 0, 0, 1, 1) → ( 0, 0, 1, 0, 1) → ( 0, 1, 1, 1, 1) → ( 1, 0, 0, 0, 1) → ⋯ \begin{split}&(1,0,0,0,1)\rightarrow(1,0,0,1,0)\rightarrow(1,0,1,1,1)\rightarrow(1,1,0,0,0)\rightarrow(0,1,0,0,1)\rightarrow\\ &(1,1,0,1,1)\rightarrow(0,1,1,0,0)\rightarrow(1,0,1,0,0)\rightarrow(1,1,1,0,1)\rightarrow(0,0,1,1,0)\rightarrow\\ &(0,1,0,1,0)\rightarrow(1,1,1,1,0)\rightarrow(0,0,0,1,1)\rightarrow(0,0,1,0,1)\rightarrow(0,1,1,1,1)\rightarrow(1,0,0,0,1)\rightarrow\cdots\end{split} |  |

We see that the evolution cycles in fifteen steps, so that Ψ [15] ​ ( 𝜹) = 𝜹 \Psi^{[15]}(\bm{\delta})=\bm{\delta}. Then, a closer inspection shows that if we make equivalent sequences that are the same modulo a rotation around the torus, then the cycle length is only 3 3, the repeated pattern being of two ones followed by three zeros.

In the language of the formal series it then follows that the shortest period for the sequence of iterations of Ψ ^ \widehat{\Psi} is 3 3 and Ψ ^ [3 ​ k] ​ ( 𝜹 ^) = 𝜹 ^ \widehat{\Psi}^{[3k]}(\widehat{\bm{\delta}})=\widehat{\bm{\delta}} for k ≥ 0 k\geq 0. Precisely, we have

 | ϕ ⁡ ( 𝜹) = 1 + X 4 + X 5 + X 9 + x 10 + x 14 + x 15 + ⋯ = ( 1 + X 4) ​ ( 1 + X 5 + X 10 + X 15 + ⋯) = 1 + X 4 1 + X 5. \begin{split}\phi(\bm{\delta})&=1+X^{4}+X^{5}+X^{9}+x^{10}+x^{14}+x^{15}+\cdots\\ &=(1+X^{4})\left(1+X^{5}+X^{10}+X^{15}+\cdots\right)\\ &=\frac{1+X^{4}}{1+X^{5}}\,.\end{split} |  | (14) |

To express ϕ ⁡ ( 𝜹) \phi(\bm{\delta}) in the form from Theorem 3, with l = 3 l=3 and r = 4 r=4 we have to find the polynomial P ⁡ ( X) P(X) that satisfies condition

 | P ⁡ ( X) ( 1 + X) 3 + X 4 = 1 + X 4 1 + X 5. \frac{P(X)}{(1+X)^{3}+X^{4}}=\frac{1+X^{4}}{1+X^{5}}\,. |  |

We obtain P ⁡ ( X) = 1 + X + X 2 + X 3 P(X)=1+X+X^{2}+X^{3}, and consequently, besides ( 14), we also have the representation

 | ϕ ⁡ ( 𝜹) = 1 + X + X 2 + X 3 ( 1 + X) 3 + X 4. \phi(\bm{\delta})=\frac{1+X+X^{2}+X^{3}}{(1+X)^{3}+X^{4}}\,. |  |

### 7.2. Example 𝜸 \bm{\gamma}

Consider the sequence 𝜸 = ( 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, …) \bm{\gamma}=(1,1,0,0,0,1,1,1,1,0,0,0,1,1,\dots) in which the first seven entries ( 1, 1, 0, 0, 0, 1, 1) (1,1,0,0,0,1,1) repeat periodically.

 | ( 1, 0, 0, 0, 1, 0, 0) → ( 1, 0, 0, 1, 1, 0, 1) → ( 1, 0, 1, 0, 1, 1, 0) → ( 1, 1, 1, 1, 0, 1, 1) → ( 0, 0, 0, 1, 1, 0, 0) → ( 0, 0, 1, 0, 1, 0, 0) → ( 0, 1, 1, 1, 1, 0, 0) → ( 1, 0, 0, 0, 1, 0, 0) → ⋯ \begin{split}&(1,0,0,0,1,0,0)\rightarrow(1,0,0,1,1,0,1)\rightarrow(1,0,1,0,1,1,0)\rightarrow\\ &(1,1,1,1,0,1,1)\rightarrow(0,0,0,1,1,0,0)\rightarrow(0,0,1,0,1,0,0)\rightarrow\\ &(0,1,1,1,1,0,0)\rightarrow(1,0,0,0,1,0,0)\rightarrow\cdots\end{split} |  |

The series corresponding to 𝜸 \bm{\gamma} is

 | ϕ ⁡ ( 𝜸) = 1 + X 4 1 + X 7. \begin{split}\phi(\bm{\gamma})&=\frac{1+X^{4}}{1+X^{7}}\,.\end{split} |  |

This can also be written as

 | ϕ ⁡ ( 𝜸) = 1 + X + X 2 + X 3 ( 1 + X) 7 + X 7. \begin{split}\phi(\bm{\gamma})=\frac{1+X+X^{2}+X^{3}}{(1+X)^{7}+X^{7}}\,.\end{split} |  |

### 7.3. Example 𝝂 \bm{\nu}

Consider the 5 5 -tuple ( 1, 0, 0, 0, 0) (1,0,0,0,0) that repeats periodically to generate the row

 | 𝝂 = ( 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, …). \begin{split}\bm{\nu}=(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,\dots).\end{split} |  |

Then the series corresponding to 𝝂 \bm{\nu} is

 | ϕ ⁡ ( 𝝂) = ∑ k ≥ 0 X 5 ​ k = 1 1 + X 5. \begin{split}\phi(\bm{\nu})=\sum_{k\geq 0}X^{5k}=\frac{1}{1+X^{5}}\,.\end{split} |  |

Then one can check directly that ϕ ⁡ ( 𝝂) \phi(\bm{\nu}) cannot be expressed as a rational function in any of the forms

 | P ⁡ ( X) ( 1 + X) l + X r or P ⁡ ( X) X r ​ ( 1 + X) l + 1, \frac{P(X)}{(1+X)^{l}+X^{r}}\ \ \mathrm{or}\ \ \frac{P(X)}{X^{r}(1+X)^{l}+1}, |  |

for any positive integers l, r l,r and any polynomial P ​ ( X) ∈ 𝔽 2 ​ [X] P(X)\in\mathbb{F}_{2}[X]. This could have been done if the hypotheses of Theorem 6 had been fulfilled. But the series ϕ ⁡ ( ν) \phi(\nu) does not meet them. Indeed, on the discrete torus of length 5 5, the Ducci operation transforms ( 1, 0, 0, 0, 0) (1,0,0,0,0) into ( 1, 1, 0, 0, 0) (1,1,0,0,0). But, as observed in the above example for the row 𝜹 \bm{\delta}, ( 1, 1, 0, 0, 0) (1,1,0,0,0) belongs to a cycle, whereas ( 1, 0, 0, 0, 0) (1,0,0,0,0) does not, ( 1, 0, 0, 0, 0) (1,0,0,0,0) is part of a pre-cycle not a cycle.

### 7.4. Example 𝜾 \bm{\iota}

The example after Theorem 4 in the introduction is based on the sequence 𝜾 \bm{\iota} whose first 127 127 terms are represented by the dots in Figure 3. Afterwards, the terms repeat periodically, and consequently ϕ ⁡ ( 𝜾) = f ⁡ ( X) \phi(\bm{\iota})=f(X), where f ⁡ ( X) f(X) is the series defined by ( 2). The example was build starting with the observation from Lemma 2 that the roots of X 7 + X + 1 X^{7}+X+1 are distinct, and K K, the smallest field extension 𝔽 2 ⊂ K \mathbb{F}_{2}\subset K that contains all the roots has the multiplicative group of order 2 7 − 1 = 127 2^{7}-1=127. Then we know that X 7 + X + 1 X^{7}+X+1 divides X 127 − 1 X^{127}-1 in 𝔽 2 ​ [X] \mathbb{F}_{2}[X]. It follows that for f ⁡ ( X) f(X), the formal power series corresponding to the periodic consequent line in the triangle ( P-G), there exists Q ​ ( X) ∈ 𝔽 2 ​ [X] Q(X)\in\mathbb{F}_{2}[X] such that

 | f ⁡ ( X):= X + X 6 1 + X + X 7 = Q ⁡ ( X) X 127 − 1 = Q ⁡ ( X) ​ ∑ k ≥ 0 X 127 ​ k. \begin{split}f(X):=\frac{X+X^{6}}{1+X+X^{7}}=\frac{Q(X)}{X^{127}-1}=Q(X)\sum_{k\geq 0}X^{127k}\,.\end{split} |  |

The polynomial Q ⁡ ( X) Q(X) has degree 126 126, the powers of its non-zero terms are the elements of the set ℳ \mathcal{M}, and it can be split as a product of irreducible polynomials in 𝔽 2 ​ [X] \mathbb{F}_{2}[X] as

 | Q ⁡ ( X) = X ​ ( X + 1) 2 ​ ( X 4 + X 3 + X 2 + X + 1) ​ ( X 7 + X 3 + 1) ​ ( X 7 + X 3 + X 2 + X + 1) ⋅ ( X 7 + X 4 + 1) ​ ( X 7 + X 4 + X 3 + X 2 + 1) ​ ( X 7 + X 5 + X 2 + X + 1) ⋅ ( X 7 + X 5 + X 3 + X + 1) ​ ( X 7 + X 5 + X 4 + X 3 + 1) ⋅ ( X 7 + X 5 + X 4 + X 3 + X 2 + X + 1) ​ ( X 7 + X 6 + 1) ⋅ ( X 7 + X 6 + X 3 + X + 1) ​ ( X 7 + X 6 + X 4 + X + 1) ⋅ ( X 7 + X 6 + X 4 + X 2 + 1) ​ ( X 7 + X 6 + X 5 + X 2 + 1) ⋅ ( X 7 + X 6 + X 5 + X 3 + X 2 + X + 1) ​ ( X 7 + X 6 + X 5 + X 4 + 1) ⋅ ( X 7 + X 6 + X 5 + X 4 + X 2 + X + 1) ​ ( X 7 + X 6 + X 5 + X 4 + X 3 + X 2 + 1). \begin{split}Q(X)=&X(X+1)^{2}(X^{4}+X^{3}+X^{2}+X+1)(X^{7}+X^{3}+1)(X^{7}+X^{3}+X^{2}+X+1)\\ &\cdot(X^{7}+X^{4}+1)(X^{7}+X^{4}+X^{3}+X^{2}+1)(X^{7}+X^{5}+X^{2}+X+1)\\ &\cdot(X^{7}+X^{5}+X^{3}+X+1)(X^{7}+X^{5}+X^{4}+X^{3}+1)\\ &\cdot(X^{7}+X^{5}+X^{4}+X^{3}+X^{2}+X+1)(X^{7}+X^{6}+1)\\ &\cdot(X^{7}+X^{6}+X^{3}+X+1)(X^{7}+X^{6}+X^{4}+X+1)\\ &\cdot(X^{7}+X^{6}+X^{4}+X^{2}+1)(X^{7}+X^{6}+X^{5}+X^{2}+1)\\ &\cdot(X^{7}+X^{6}+X^{5}+X^{3}+X^{2}+X+1)(X^{7}+X^{6}+X^{5}+X^{4}+1)\\ &\cdot(X^{7}+X^{6}+X^{5}+X^{4}+X^{2}+X+1)(X^{7}+X^{6}+X^{5}+X^{4}+X^{3}+X^{2}+1)\,.\end{split} |  |

## References

- [1] Raghavendra N. Bhat, Distribution of square-prime numbers, *Missouri J. Math. Sci.*34 (1), 121–126 (2022). [https://doi.org/10.35834/2022/3401121][6] [https://arxiv.org/pdf/2109.10238.pdf][7]
- [2] Raghavendra N. Bhat, Sequences, Series and Uniform distribution of SP Numbers, *arxiv*preprint, 7 pp. (2022). [https://arxiv.org/pdf/2210.04622.pdf][8]
- [3] Raghavendra N. Bhat, Cristian Cobeli, Alexandru Zaharescu, Filtered rays over iterated differences on layers of integers, preprint (2023).
- [4] Raghavendra N. Bhat, Sundarraman Madhusudanan, Algebraic Results on SP Numbers along with a generalization, *arxiv*preprint, 7 pp. (2022). [https://arxiv.org/pdf/2211.09009.pdf][9]
- [5] Mihai Caragiu, Alexandru Zaharescu, Mohammad Zaki, An analogue of the Proth-Gilbreath conjecture, *Far East J. Math. Sci. (FJMS)*81 (1), 1–12 (2013). [http://www.pphmj.com/abstract/7973.htm][10]
- [6] C. I. Cobeli, M. Crâşmaru, A. Zaharescu, A cellular automaton on a torus, *Port. Math.*57 (3), 311–323 (2000). [https://www.emis.de/journals/PM/57f3/pm57f305.pdf][11]
- [7] Cristian Cobeli, Alexandru Zaharescu, Promenade around Pascal triangle – number motives, *Bull. Math. Soc. Sci. Math. Roum., Nouv. Sér.*56(104) (1), 73–98 (2013). [https://www.jstor.org/stable/43679285][12]
- [8] Cristian Cobeli, Alexandru Zaharescu, A game with divisors and absolute differences of exponents, *J. Difference Equ. Appl.*20 (11), 1489–1501 (2014). [https://doi.org/10.1080/10236198.2014.940337][13]
- [9] Cristian Cobeli, Mihai Prunescu, Alexandru Zaharescu, A growth model based on the arithmetic Z Z -game, *Chaos Solitons Fractals*91, 136–147 (2016). [https://doi.org/10.1016/j.chaos.2016.05.016][14]
- [10] Cristian Cobeli, Alexandru Zaharescu, Flurries of Ducci waves, *Bull. Math. Soc. Sci. Math. Roumaine*66(114) (2), 177–188 (2023).
- [11] Norman Gilbreath, Processing process: the Gilbreath conjecture, *J. Number Theory*131 (12), 2436–2441 (2011). [https://doi.org/10.1016/j.jnt.2011.06.008][15]
- [12] Richard K. Guy, The strong law of small numbers, *Am. Math. Mon.*95 (8), 697–712 (1988). [https://doi.org/10.2307/2322249][16]
- [13] Richard K. Guy, *Unsolved problems in number theory*. 3rd ed. Problem Books in Mathematics. New York, NY: Springer-Verlag (ISBN 0-387-20860-7/hbk). xviii, 437 pp. (2004).
- [14] Hugh L. Montgomery, Ten lectures on the interface between analytic number theory and harmonic analysis, *Regional Conference Series in Mathematics*84. Providence, RI: American Mathematical Society (AMS). xii, 220 pp. (1994).
- [15] Mihai Prunescu, Symmetries in the Pascal triangle: p p -adic valuation, sign-reduction modulo p p and the last non-zero digit, *Bull. Math. Soc. Sci. Math. Roumaine*65(113) (4), 431–447 (2022). [https://ssmr.ro/bulletin/pdf/65-4/articol_6.pdf][17]
- [16] R. B. Killgrove, K. E. Ralston, On a conjecture concerning the primes, *Math. Tables Aids Comput.*13, 121–122 (1959). [https://doi.org/10.2307/2001963][18]
- [17] Andrew M. Odlyzko, Iterated absolute values of differences of consecutive primes, *Math. Comput.*61 (203), 373–380 (1993). [https://doi.org/10.2307/2152962][19]
- [18] F. Proth, Sur la série des nombres premiers, *Nouvelle Correspondance Mathématique*4, 236–240 (1878). [https://gdz.sub.uni-goettingen.de/download/pdf/PPN598948236_0004/LOG_0088.pdf][20]


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:rnbhat2@illinois.edu
[4]: mailto:cristian.cobeli@imar.ro
[5]: mailto:zaharesc@illinois.edu
[6]: https://doi.org/10.35834/2022/3401121
[7]: https://arxiv.org/pdf/2109.10238.pdf
[8]: https://arxiv.org/pdf/2210.04622.pdf
[9]: https://arxiv.org/pdf/2211.09009.pdf
[10]: http://www.pphmj.com/abstract/7973.htm
[11]: https://www.emis.de/journals/PM/57f3/pm57f305.pdf
[12]: https://www.jstor.org/stable/43679285
[13]: https://doi.org/10.1080/10236198.2014.940337
[14]: https://doi.org/10.1016/j.chaos.2016.05.016
[15]: https://doi.org/10.1016/j.jnt.2011.06.008
[16]: https://doi.org/10.2307/2322249
[17]: https://ssmr.ro/bulletin/pdf/65-4/articol_6.pdf
[18]: https://doi.org/10.2307/2001963
[19]: https://doi.org/10.2307/2152962
[20]: https://gdz.sub.uni-goettingen.de/download/pdf/PPN598948236_0004/LOG_0088.pdf
