<!-- source: https://arxiv.org/pdf/1305.3062 | converted from PDF -->

arXiv:1305.3062v2  [math.NT]  1 Apr 2014
NUMERICAL VERIFICATION OF THE TERNARY GOLDBACH
CONJECTURE UP TO 8.875 · 1030

H. A. HELFGOTT AND DAVID J. PLATT

Abstract. We describe a computation that conﬁrms the ternary Goldbach
Conjecture up to 8, 875, 694, 145, 621, 773, 516, 800, 000, 000, 000 (> 8.875·1030).

1. Introduction

The ternary Goldbach Conjecture, which has been open since 1742, is the as-
sertion that every odd number n > 5 is the sum of three primes. The binary, or
strong, Goldbach Conjecture states that every even number > 2 is the sum of two
primes; this would imply ternary Goldbach trivially.
Using results from analytic number theory, speciﬁcally Theorems 2 and 3 and
Table 1 of [11], and the truth of the Riemann Hypothesis to T = 3.33 · 109, Ramar´e
and Saouter showed that ternary Goldbach holds to at least 8.37 · 1026 (see their
Theorem 2.1). In the ﬁrst version of [6], the ﬁrst author used the same argument
to show that the veriﬁcation of the Riemann Hypothesis by the second author [10]
(to T > 3.061 · 1010), Wedeniwski [14] (to T > 2.419 · 1011) or Gourdon [3] (to
T > 2.4599 · 1012) imply ternary Goldbach holds to 1.23163 · 1027, 6.15697 · 1028 or
5.90698 · 1029 respectively.
In contrast, the most extensive previous explicit veriﬁcation of ternary Goldbach
was by Saouter [12] in 1998 who showed that ternary Goldbach holds to 1020. He
in turn relied on a 1993 result of Sinisalo who showed that the binary conjecture
holds to 4 · 1011 [13]. Saouter’s approach was to construct a “ladder” of primes
starting below 4 · 1011 where each rung of the ladder is no more than 4 · 1011 wide.
(That is, pi+1 − pi ≤ 4 · 1011.) Clearly, such a ladder establishes ternary Goldbach
up to 4 · 1011 past the last rung and does not rely on any numerical veriﬁcation of
the Riemann Hypothesis.
Since Saouter’s result, the binary Goldbach Conjecture has been numerically
veriﬁed to 4 · 1018 by Oliviera e Silva, Siegfried Herzog and Silvio Pardi [9]. Thus
we can immediately gain an advantage of a factor of 107. In addition, there have
been signiﬁcant improvements in hardware capabilities in the intervening 15 years.
We will now describe a computation that exploits both advances.

2. Proth Primes

Proving a number of general form is prime can be computationally expensive.
For example, testing a number of size N using Elliptic Curve Primality Proving

2010 Mathematics Subject Classiﬁcation. Primary 11P32 Secondary 11A41 11Y11.
We would like to thank the staﬀ of the Direction des Syst`emes d’Information at Universit´e
Paris VI/VII (Pierre et Marie Curie) and Bill Hart at Warwick University for allowing us to use
their computer systems for this project. We would also like to thank Andrew Booker for suggesting
we exploit Proth primes. Travel was funded in part by the Leverhulme Prize.
1

2 H. A. HELFGOTT AND DAVID J. PLATT

(ECPP) has time complexity (heuristically) O(log4+ǫ N ). Fortunately, there exist
primes of special forms that are much easier to test. We use Proth primes1

Deﬁnition 2.1. A Proth number is of the form k · 2n + 1 with k, n ∈ Z>0 and
k < 2n.

Deﬁnition 2.2. A Proth prime is a Proth number that is also prime.

Theorem 2.3 (Proth’s Theorem). A Proth number N = k · 2n + 1 is prime if for
some integer a with

(2.1) ( a
N
 ) = −1

we have

(2.2) a N −1
2 ≡ −1 mod N.

Proof. See, for example, § 5.3.3 of [2]. □

(Conversely, if N is prime, then (2.2) holds for every a satisfying (2.1).)
This suggests the following algorithm for testing a Proth number for primality.

(1) Let n, k ∈ Z>0 with k < 2n. Fix a small prime bound B.
(2) Set N ← k · 2n + 1.
(3) Set p ← 2.
(4) While p <= B if ( p
N ) = −1, then break, else set p to the ﬁrst prime after
p.
(5) If p > B (we ran out of small primes) return false.
(6) Return true if p N −1
2 ≡ −1 mod N and false if p N −1
2 ̸≡ −1 mod N .

The modular exponentiation at step 6 requires O(log N ) multiplications. Com-
puting the Jacobi symbol at step 4 has (since a is bounded) time complexity
O(log(N )); we do it O(1) times. The algorithm may return a false negative if
none of the primes ≤ B are quadratic non-residues but N happens to be prime.
However, the algorithm never returns a false positive.

3. The Prime Ladder Algorithm

We can now formulate the algorithm to construct our prime ladder.

(1) Fix n, ∆ ∈ Z>0 with ∆ > 2n. Fix a prime N0.
(2) Let k0 be the largest integer such that k0 · 2n + 1 < N0 and k1 the largest
integer such that k1 · 2n + 1 < N0 + ∆.
(3) While k1 > k0 if k1 · 2n + 1 is a Proth prime then break else k1 ← k1 − 1.
(4) If k1 = k0 (no Proth prime was found) set N0 to the largest prime (of
general form) less than N0 + ∆; else set N0 ← k1 · 2n + 1.
(5) Repeat from 2.

1Saouter exploited numbers of the form N = 222 · R + 1 with N < 1020, N ≡ 3 mod 10 and R
odd.

NUMERICAL VERIFICATION OF THE TERNARY GOLDBACH CONJECTURE UP TO 8.875·10
303

4. Implementation

We implemented the above algorithm in the C programming language using the
GMP package [4] to manage integers larger than 64 bits. To ﬁnd general primes
when no suitable Proth prime could be located, we used Pari’s “precprime” library
routine [1]. Since “precprime” returns a probable prime, we checked each instance
with Pari’s “isprime”2.
We initially hoped to reach about 1031; this required that n be at least 52. We
set B to 29 so we had 10 potential candidates for a. As each one has about a 50%
chance of success, we failed to ﬁnd a suitable a in about 0.1% of cases.
To improve run time at the expense of space, we test the Proth numbers relating
to a given range of k for divisibility by “small” primes. We do this by sieving on the
arithmetic progression k · 2n + 1. We aimed to exploit the multi-core architecture
of modern CPUs so we ﬁxed the maximum width of the interval so that there
was suﬃcient memory available for each core to run our code in parallel. We
used intervals of width 254 · 109 each containing about 4 · 109 candidate Proth
numbers. Experiments indicated that sieving for all prime divisors < 16, 000 was
an appropriate compromise3.
It took about 270 seconds to sieve such an interval and construct a ladder of
primes starting within 2 · 1018 of the left end point, ending within 2 · 1018 of the
right end point and where no gap between primes exceeded 4 · 1018. This included
writing out the values of k and a for every Proth prime found, and storing any
general primes found using Pari.
The values of k and a stored were used to check that the relevant Proth number
was indeed prime (using Proth’s theorem again) and that they were suﬃciently
closely spaced to establish the required ladder. This check program was written in
C++ using the Class Library for Numbers package [5], conﬁgured not to use GMP so
that the primality and spacing of the Proth numbers were conﬁrmed independantly
of GMP. As expected, no errors in either package were evident. The check program
took a further 40 seconds for each interval running on a single core and the data
ﬁle was then deleted. Again the memory demands of the check program were
suﬃciently modest that all the cores in a CPU could be utilised simultaneously.
In total, we checked 492, 700 ranges of width 254·109, requiring about 40, 000 core
hours. We used three resources, a 48 core, AMD Magny Cours cluster at Warwick
University and two PowerPC clusters at Universit´e de Paris VI/VII (UPMC - DSI
- Pˆole Calcul). All three beneﬁt from ECC memory.
The 130, 917 primes of general form we had to ﬁnd using Pari were independently
checked using Fran¸cois Morain’s ECPP program [8]. This took a trivial amount of
computer time and again revealed no discrepancies.

Theorem 4.1. Every odd number between 7 and T , where

T = 8, 875, 694, 145, 621, 773, 516, 800, 000, 000, 000

can be written as the sum of three primes.

We note that this is factor of > 8 · 1010 higher than the 1998 result. As already
observed, an improvement of ×107 can be attributed to starting with the stronger
statement on binary Goldbach and our computation consumed about 10 times as

2In fact, the numbers returned by “precprime” were always prime
3For comparison, Saouter sieved with the ﬁrst 10 primes.

4 H. A. HELFGOTT AND DAVID J. PLATT

much CPU time. The remaining factor of 800 is at least partially down to the
increased clock speed and word length of modern CPUs. Increases in the speed and
capacity of memory also allow us to sieve more eﬃciently and this will also have
contributed to the higher throughput we observed.

5. Going Further

Clearly, continuing this computation with the current parameters, it is only a
matter of CPU cycles to reach (252 −1)·252+1 ≈ 2·1031. However, the ﬁrst author’s
proof that ternary Goldbach holds unconditionally above 1029 [6][7] renders any
such computation nugatory.
 References

1. C. Batut, K. Belabas, D. Bernardi, H. Cohen, and M. Olivier, User’s Guide to PARI-GP,
2000.
2. Benjamin Fine and Gerhard Rosenberger, Number Theory: an Introduction via the Distribu-
tion of Primes, Birkhauser Boston, 2007.
3. X. Gourdon, The 1013 First Zeros of the Riemann Zeta Function, and Zeros Computation at
Very Large Height, http://numbers.computation.free.fr/Constants/Miscellaneous/
zetazeros1e13-1e24.pdf.
4. Torbj¨orn Granlund, The GNU Multiple Precision Arithmetic Library, 5.1.1 ed., February
2013.
5. Bruno Haible and Richard B. Kreckel, CLN, A Class Library for Numbers, 2008,
http://www.ginac.de/CLN/.
6. H.A. Helfgott, Minor arcs for Goldbach’s problem, arXiv preprint arXiv:1205.5252 (2012).
7. , Major arcs for Goldbach’s problem, arXiv preprint arXiv:1305.2897 (2013).
8. F. Morain, Easy numbers for the Elliptic Curve Primality Proving algorithm, ISSAC ’92 (New
York) (P. S. Wang, ed.), ACM Press, 1992, Proceedings, July 27–29, Berkeley, pp. 263–268.
9. Tom´as Oliveira e Silva, Siegreid Herzog, and Silvio Pardi, Empirical Veriﬁcation of the Even
Goldbach Conjecture, and Computation of Prime Gaps, up to 4·1018, Accepted for Publication
in Math. Comp. (2013).
10. David J. Platt, Computing Degree 1 L-functions Rigorously, Ph.D. thesis, University of Bris-
tol, 2011.
11. Olivier Ramar´e and Yannick Saouter, Short Eﬀective Intervals Containing Primes, J. Number
Theory 98 (2003), no. 1, 10–33.
12. Yannick Saouter, Checking the odd Goldbach conjecture up to 1022, Math. Comp. 67 (1998),
no. 222, 863–866.
13. Matti K Sinisalo, Checking the Goldbach conjecture up to 4 · 1011, Math. Comp. 61 (1993),
no. 204, 931–934.
14. S. Wedeniwski, ZetaGrid–Computations connected with the Veriﬁcation of the Riemann Hy-
pothesis, Foundations of Computational Mathematics Conference, Minnesota, USA, 2002.

Ecole Normale Sup´erieure, D´epartement de Math´ematiques, 45 rue dUlm, F-75230
Paris, France
E-mail address: harald.helfgott@ens.fr

Heilbronn Institute for Mathematical Research, University of Bristol
E-mail address: dave.platt@bris.ac.uk
