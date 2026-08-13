<!-- source: https://www.jstage.jst.go.jp/article/iar/3/0/3_28/_pdf | converted from PDF -->

1

An Efficient Constructive Algorithm for the Erdős-
Straus Conjecture: Solutions for Massive Integers

Yuichi Suzuki
CEO, BothSides, LLC, Tokyo, Japan

Abstract:

The Erdős-Straus Conjecture (ESC) states that for all integers n greater than or equal to two, the number four divided by
n is a sum of three positive unit fractions. Although computationally verified for all integers up to ten to the seventeenth
power, no general constructive proof has been available, particularly for prime numbers and certain notorious modular-
exception residues. This paper presents a comprehensive theorem, based on our divisibility condition, that provides a
novel constructive approach with explicit solution formulas. Remarkably, this divisibility condition also functions as a
necessary and sufficient condition for the solvability of the ESC, including all prime cases and previously known Modell
exceptional values. Our resulting algorithm achieves a success rate exceeding ninety-two percent for massive numbers,
including primes exceeding three thousand digits, and obtains a one hundred percent success rate for the tested class of
integers involving all Mordell exceptional values, with solution times under one hundred and forty-two milliseconds per
case on consumer hardware. We demonstrate that discovering mathematical structure can overcome computational
intractability more effectively than raw computing power, achieving a performance improvement of an astronomical
scale over brute force methods. These results have fundamental implications for cryptographic security, suggesting that,
complementing the preparation for advances in quantum computing, it is also crucial to explore the potential for hidden
mathematical structures in cryptographic problems.

Keywords:

Egyptian Fractions,  Erdős-Straus Conjecture,  Numerical Calculation

1  INTRODUCTION

The Erdős–Straus Conjecture [1] asserts that every
integer n ≥ 2 for the equation

4

𝑛 = 1

𝑥 + 1

𝑦 + 1

𝑧 , 𝑥, 𝑦, 𝑧 ∈ ℕ         (1)

While  computational  searches  have  verified  the
conjecture  for  all  integers  up  to  1017  [3],  and  recent
work by Terence Tao et al. [4] has shown that solutions
exist  for  "almost  all"  n,  these  approaches  are  non-
constructive, and a general constructive proof  has  not
been available. The problem is known to be notoriously
difficult when n is a prime number satisfying n ≡ a (mod
840), for a ∈ {1, 121, 169, 289, 361, 529}. These are
known as "Mordell's exceptional values." [2]

In contrast, for most integers n that do not fall into these
Mordell  exceptional  values,  solutions  can  be  found
using  known  identities,  even  for  massive  prime
numbers.

This  paper  addresses  this  long-standing  challenge
by proposing a constructive method based on a new
theorem. We further demonstrate that our algorithm
can  instantaneously  find  solutions  even  for  3000-
digit primes in the Mordell exceptional classes, thus
showing  the  theoretical  value  and  practical
effectiveness of our approach.

2  Well Known Results

Known Fact 1: If an ESC solution exists for n with 𝑥 ≤
𝑦, 𝑥 ≤ 𝑧, then:
 𝑠 < 𝑥

Proof of Known Fact 1: See also [1].

For completeness, we provide proofs below.

 2

4
4𝑠 + 1 = 1
𝑥 + 1
𝑦 + 1
𝑧

and 𝑥 ≤ 𝑦, 𝑥 ≤ 𝑧:

•  Since 1

𝑦 + 1

𝑧 > 0, we have:

4
4𝑠 + 1 > 1
𝑥 ⇒ 𝑥 > 4𝑠 + 1
4 = 𝑠 + 1
4 ⇒ 𝑥 ≥ 𝑠 + 1 > 𝑠

Known Fact 2: If 𝑛 is prime and an ESC solution
exists, then 𝑦 or 𝑧 (or both) is divisible by 𝑛.

Proof of Known Fact 2: See also [1].

For completeness, we provide proofs below.

 4
𝑛 = 1
𝑥 + 1
𝑦 + 1
𝑧 ⇒ 4𝑥𝑦𝑧 = 𝑛(𝑦𝑧 + 𝑥𝑧 + 𝑥𝑦)

Since 𝑥 < 𝑛 and 𝑛 is prime:

gcd(𝑥, 𝑛) = 1 and gcd(4, 𝑛) = 1

For the equation to hold, we need:

𝑛 ∣ 𝑦𝑧

•  Since 𝑛 is prime, this implies:

𝑛 ∣ 𝑦 or 𝑛 ∣ 𝑧

3  Theorem for Constructive Approach

Necessary and Sufficient Condition for ESC Solutions
when 𝑛 = 4𝑠 + 1, where 𝑛 is prime and 𝑠 ≥ 1 is a
natural number:

An ESC solution exists if and only if there exist natural
numbers 𝑘 ≥ 1 and 𝐴 ≥ 1 such that:

(4𝑘 − 1)𝐴 − (𝑠 + 𝑘) ∣ 𝐴𝑛(𝑠 + 𝑘)

ESC Solution (when condition is satisfied):

𝑥 = 𝑠 + 𝑘
 𝑦 = 𝐴𝑛

𝑧 = 𝐴𝑛(𝑠 + 𝑘)
(4𝑘 − 1)𝐴 − (𝑠 + 𝑘)

These values satisfy the ESC equation:

4
𝑛 = 1
𝑥 + 1
𝑦 + 1
𝑧

Proof:
Necessity (⇒):

Suppose an ESC solution exists.
By Known Fact 1, we can write:

𝑥 = 𝑠 + 𝑘

for some natural number 𝑘.

By Known Fact 2,

Case 1: If 𝑛 ∣ 𝑦, then
 𝑦 = 𝐴𝑛

for some natural number 𝐴.

From the ESC equation:

1
𝑧 = 4
𝑛 − 1
𝑥 − 1
𝑦 = 4
4𝑠 + 1 − 1
𝑠 + 𝑘 − 1
𝐴(4𝑠 + 1)

Computing this gives:

𝑧 = 𝐴𝑛(𝑠 + 𝑘)
(4𝑘 − 1)𝐴 − (𝑠 + 𝑘)

For 𝑧 to be a natural number, we require:

(4𝑘 − 1)𝐴 − (𝑠 + 𝑘) ∣ 𝐴𝑛(𝑠 + 𝑘)

Case 2: If n∣ z, then
 𝑧 = 𝐴𝑛

for some natural number 𝐴.

 1
𝑦 = 4
𝑛 − 1
𝑥 − 1
𝑧 = 4
4𝑠 + 1 − 1
𝑠 + 𝑘 − 1
𝐴(4𝑠 + 1)

Computing this gives:

 3

𝑦 = 𝐴𝑛(𝑠 + 𝑘)
(4𝑘 − 1)𝐴 − (𝑠 + 𝑘)

For 𝑦 to be a natural number, we require:

(4𝑘 − 1)𝐴 − (𝑠 + 𝑘) ∣ 𝐴𝑛(𝑠 + 𝑘)

Sufficiency (⇐):

If natural numbers 𝑘, 𝐴 exist such that:

(4𝑘 − 1)𝐴 − (𝑠 + 𝑘) ∣ 𝐴𝑛(𝑠 + 𝑘)

then:
 𝑧 = 𝐴𝑛(𝑠 + 𝑘)
(4𝑘 − 1)𝐴 − (𝑠 + 𝑘)

is a natural number, and direct computation shows that:

𝑥 = 𝑠 + 𝑘, 𝑦 = 𝐴𝑛, 𝑧 = 𝐴𝑛(𝑠 + 𝑘)
(4𝑘 − 1)𝐴 − (𝑠 + 𝑘)

satisfy:
 4
𝑛 = 1
𝑥 + 1
𝑦 + 1
𝑧

Therefore, the theorem is proved.

4  Numerical Calculation and Results

4.1  Algorithm Development

We focus on n satisfying n ≡ m (mod 840), for m ∈ {1,
121, 169, 289, 361, 529} for solvability. Our algorithm
development  was  based  on  theorem  guided
exploration  for  parameters  k  and  A,  followed  by
systematic  observation  of  the  result.  Through  this
process, we discovered that solutions are more readily
found when k=1 and parameter A is a number with one
less digit than n, beginning with 7. Similarly, we found
that  when  k=2,  solutions  are  more  easily  obtained
when A begins with 3.

Based on these findings, we developed an algorithm
that  dramatically  narrows  the  theorem-based  search
space and validated it through Numerical Calculation
1  and  Numerical  Calculation  2.  For  Numerical
Calculation 2, we implemented a two-stage algorithm:
the  primary  stage  uses  the  same  methodology  as
 Numerical  Calculation  1,  while  the  secondary  stage
employs  a  slightly  expanded  search  space  for  cases
where the initial approach fails to find solutions.

4.2  Numerical Calculation Results

We applied our algorithm to find solutions for
n = 840 × 10
𝑖 + m, where m represents Mordell
exceptional values m ∈ {1, 121, 169, 289, 361, 529}
and i ranges from 1 to 3,000. The resulting
values of n include massive numbers exceeding
3,000 digits, including primes. The total number
of cases was 3,000×6=18,000.

We  applied  our  algorithm  to  find  solutions  for n =
840 × 𝑖 + m, where m represents Mordell exceptional
values  and  i  ranges  from  1  to  10,000. The  resulting
values of n include numbers up to 7 digits, including
primes.
 Numerical Evaluation

Metric   Numerical
Calculation 1  Numerical
Calculation 2
Problem form  n = 840 × 10
i + m  n = 840 × i + m

Range of i  1 to 3,000  1 to 10,000

Total cases   18,000  60,000

Successful solutions  16,701  60,000

Failed cases  1,299  0

Success rate  92%  100%

Avg time/case  63 sec
(3.5 msec/case)  142 min
(142 msec/case)

Numerical Sample Result
Case 1:

4
84000000000000000001

= 1
21000000000000000001 + 1
588000000000000000343000000000000000004

+ 1
1122545454545454546162818181818181818220636363636363636364

Case 2:
 4
840000000000000000000000000169

= 1
210000000000000000000000000043

+ 1
58800000000000000000000000026950000000000000000000000003042

+ 1
1122545454545454545454545455289809090909090909090909091072515454545454545454545454557346

 4

Case 3:

4
840000000169 = 1
210000000043 + 1
58800000026950000003042

+ 1
1122545455289809091072515454557346

4.3  Computational Environment

All calculations were executed using Python code on
a standard laptop computer.

5  Evaluation and Observations

5.1  Algorithm Development and Performance

In Numerical Calculation 1, we developed an algorithm
capable of instantaneously obtaining ESC solutions with
over  92%  success  rate  for  massive  numbers  of  the
specific  form  n = 840 × 10𝑖 + m ,  including  primes
exceeding  103000.  To  our  knowledge,  no  previous
algorithm has achieved such performance for numbers of
this magnitude.

In Numerical Calculation 2, we addressed numbers of
the  form  n = 840 × 𝑖 + m  (Mordell  exceptional
values). When  solutions could  not  be found  using  the
same  search  space  methodology  as  Numerical
Calculation 1, we implemented a slightly relaxed search
space  approach,  achieving  100%  success  rate  for
instantaneous solutions. We believe this represents the
first  practical,  theorem-based  algorithm  to  achieve
perfect success rate for this problem class.

5.2  Algorithm Design and Optimization

The  developed  algorithm  was  refined  based  on
observations from preliminary trials conducted prior to
Numerical  Calculation  1.  We  identified  that  solutions
are more readily found when k=1 and parameter A is a
number with one fewer digit than n, beginning with 7.
Similarly, we discovered that when k=2, solutions are
more easily obtained when A begins with 3.

5.3  Observational Evidence of Structure

Analysis  of  solutions  obtained  using  this  algorithm
reveals intriguing patterns. We observed "sibling-like"
 solutions that exhibit visual similarities despite different
values of n or digit counts. Additionally, we frequently
detected consecutive occurrences of identical numerical
sequences  (e.g.,  45)  within  solutions.  These
observations  further  support  the  hypothesis  that  ESC
solutions  possess  deeper  structural  properties.  Our
achievement  of  3.5-millisecond solution  times  with  a
92%  success  rate  on  ordinary  laptop  hardware
represents  a  computational  breakthrough  of
unprecedented magnitude.

6  Conclusion

6.1  Structural Implications

The  algorithm's  exceptional  performance  suggests  the
existence of previously unrecognized structures in ESC
solutions.  Specifically,  our  ability  to  obtain  solutions
instantaneously  with  high  success  rates  for n = 840 ×
10𝑖 + m  (including  primes  exceeding  3000  digits)  and
achieve 100% success rate for the more general case n =
840 × 𝑖 + m  (encompassing  all  Mordell  exceptional
values) through modest search space expansion indicates
underlying  mathematical  structures.  Our  success
suggests  we  have  identified  fragments  of  previously
unknown structures in ESC solutions, enabling what was
considered computationally impossible to become trivial.

6.2  Computational Complexity and
Implications

Conventionally,  finding  ESC  solutions  for  massive
numbers  n  (such  as  those  exceeding  3000  digits  in
Numerical  Calculation  1)  requires  astronomical
computation  time,  except  for  constructively  obtainable
cases. To  illustrate  this  computational  challenge:  using
traditional a brute-force search would involve exploring
a  vast,  super  polynomial  search  space. The  number  of
operations  required  would  be  so  immense  that  the
problem  would  remain  intractable  even  on  the  most
powerful  exascale  supercomputers,  with  any  realistic
estimate of runtime far exceeding the age of the universe.

6.3  Quantum Computing Perspective

This problem can be contrasted with integer factorization,
which is famously susceptible to Shor's algorithm. Shor's
algorithm provides an exponential speedup on a quantum
computer,  rendering  classically  intractable  problems
solvable in a practical timeframe.

 5

In contrast, the Erdős-Straus Conjecture problem has no
known  specialized  quantum  algorithm.  The  best
applicable  method,  Grover's  algorithm,  offers  only  a
quadratic speedup. For a problem with an exponentially
large  search  space,  a  quadratic  improvement  is
insufficient to make it tractable.

This  fundamental  difference  in  available  speedups
exponential versus quadratic is why quantum computers
pose a revolutionary threat to current cryptography based
on  factorization,  while  offering  limited  advantage  for
solving problems like the Erdős-Straus Conjecture.

6.4  Cryptographic Security Implications

The transition to Post-Quantum Cryptography (PQC) is
underway to defend against the threat of future quantum
computers.  Our  research,  however,  reveals  a  different
kind  of  vulnerability:  the  discovery  of  hidden
mathematical structures. We demonstrated that solutions
for previously intractable cases of this problem including
for 3000-digit primes in the Mordell exceptional classes
can be found instantaneously, not with more computing
power,  but  by  exploiting  an  undiscovered  structural
shortcut.

This implies that the true security of any cryptographic
system,  including  new  PQC  standards,  relies  on  two
foundations: its computational difficulty and the absence
of hidden structural shortcuts. Therefore, future security
audits  must  expand  beyond  traditional  complexity
analysis to include a dedicated search for these potential
structural vulnerabilities.

Acknowledgments

This paper is based on a theorem I conceived 45 years
ago during my high school years in the United States. I
would first like to express my profound gratitude to the
following  professors who  provided  me with  individual
guidance during that time. Without encountering them, I
believe I would never have returned to this research after
45  years:  Professor  Carl  Pomerance  (currently  at
Dartmouth College, then at University of Georgia), the
late  Professor  Edwin  Moise  (then  at  CUNY  Queens
College),  Professor  Kenneth  Kramer  (CUNY  Queens
College), and Professor Joseph Malkevitch (CUNY York
 College).  I  would  also  like  to  extend  my  sincere
appreciation to Professor Kiyoshi Nagata (Daito Bunka
University),  who  recommended  my  participation  in
IAR2025  and  submission  of  this  paper,  and  provided
invaluable support throughout the process.

References

[1] Richard K. Guy, "Unsolved Problems in Number
Theory" (2004)

[2] L. J. Mordell, "Diophantine Equations" (1969)

[3] A. Swett. Online ESC Database, 2000,
http://math.uindy.edu/swett/esc.htm.

[4] C. Elsholtz and T. Tao. Counting solutions of the
Erdős–Straus equation. J. Th´eorie des Nombres de
Bordeaux 26 (2014), 755–772.
