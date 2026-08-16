<!-- source: https://www.mathed.page/attc/in-addition/cmj-sq-sum-partitions.pdf | converted from PDF -->

Square–Sum Pair Partitions

Gordon Hamilton, Kiran S. Kedlaya, and Henri Picciotto

Gordon Hamilton (gord@mathpickle.com) has a Ph.D. in mathematical biology from
the University of Calgary and is now a puzzle and board game designer and the
director of MathPickle.com. MathPickle’s primary objective is to get 13 curricular,
unsolved problems into classrooms worldwide—one for each grade K–12. He also
enjoys spending time with his two children. Kiran S. Kedlaya (kedlaya@ucsd.edu) is
a professor of mathematics at the University of California, San Diego, having
previously been a faculty member at the Massachusetts Institute of Technology. He is
a long-time contributor to the USA Mathematical Olympiad and co-authored the third
MAA compilation of the Putnam competition. He is an avid travel photographer and
placed fourth at the 2015 American Crossword Puzzle Tournament. Henri Picciotto
(henri@mathedpage.org) is a math education consultant and author; he shares
ideas on www.MathEducationPage.org. He received his B.A. and M.A. in
mathematics from the University of California, Berkeley. Picciotto retired from the
classroom after 42 years of teaching at every level from counting to calculus. He is
interested in puzzles, manipulatives, and technological teaching tools. His cryptic
crosswords appear in The Nation every week.

Here is a classic problem aimed at students in grades 5 to 7.

Exercise 1. Arrange the whole numbers from 1 to 18 into nine pairs so that the sum
of the numbers in each pair is a perfect square.

We will consider several generalizations of the problem in this article, many of
which are well-suited for use in teacher preparation and in undergraduate discrete
mathematics or introduction to proof courses. The following features of the problem
make it a good choice.

1. The prerequisites are minimal (recognizing perfect squares, being able to add
pairs); thus, it is accessible to a wide range of students.
2. The answer is not obvious.
3. Students’ insights increase as they explore the problem.
4. Partial solutions are possible (e.g., one can ﬁnd eight pairs that satisfy the con-
dition).
5. The problem can be generalized.

The fourth point suggests a rewording of the problem.

Exercise 1’. Arrange the whole numbers from 1 to 18 into nine pairs so that the sum
of the numbers in as many pairs as possible is a perfect square.

http://dx.doi.org/10.4169/college.math.j.46.4.264
MSC: 05C70, 97A20

264 © THE MATHEMATICAL ASSOCIATION OF AMERICA

This is perhaps a better place to start because students can immediately ﬁnd
solutions, and a healthy competition develops around ﬁnding solutions with more
and more pairs.
Solving this problem provides an arena for comparing student approaches. For
example, is it better to start with small pairs such as {1, 3} or large ones such as {17, 8}?
The latter is in fact more efﬁcient since it presents fewer choices early on. An optimal
strategy is suggested in [6, p. 191].
When the nine-pair solution has been found, i.e., when {1, 2,..., 18} has been parti-
tioned into square–sum pairs, the class can launch into the most natural generalization.

Exercise 2. For what numbers is this possible?

In an initial trial-and-error exploration, students will ﬁnd that this partition into
square–sum pairs can be done, e.g., for 14 and 18 but not for 12 or 20. A system-
atic exploration, perhaps conducted by small groups of students, shows that most even
numbers between 2 and 22 do not yield a solution. However, students may be sur-
prised to learn that, in fact, a square-sum pairs partition is possible for all even num-
bers greater than 22. This is a strong argument for moving beyond trial and error, as
such experimentation becomes increasingly difﬁcult and time consuming when num-
bers get larger. Using a computer program becomes a useful complement to manual
exploration. One such program by the third author can be found under “Links” at [3,
A253472].
The set {1, 2,..., 8} offers a particularly straightforward solution: {1, 8}, {2, 7},
{3, 6}, {4, 5}. This suggests an elegant visual “rainbow” representation.

12 3 4 5 6 7 8

We will call this a rainbow pairing. The technique can be used to create problems for
precollege explorations in an accessible, puzzle-like format, such as the following.

Exercise 3. Complete these two square–sum pair partitions of the set {1, 2,..., 26}.

12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

VOL. 46, NO. 4, SEPTEMBER 2015 THE COLLEGE MATHEMATICS JOURNAL 265

12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

See [1] for more examples and an engaging story involving leprechauns!
Rainbow pairing is a helpful tool in the following proof by induction that gives a
complete answer to Exercise 2.

Theorem. For n a positive integer, the set {1, 2,..., 2n} admits a partition into
square–sum pairs except when n ∈{1, 2, 3, 5, 6, 10, 11}.

Proof. We will proceed by strong induction on n, treating all of the cases for n ≤ 30 as
base cases. These are most easily handled by a computer search, as suggested earlier;
while many can be treated by hand, a few (especially n = 29) are quite intricate.
Our strategy will be to construct a rainbow pairing on {2m + 1, ..., 2n} for some
m, pairing 2m + 1 with 2n,2m + 2 with 2n − 1, and so on. Then we can invoke the
induction hypothesis with n replaced by m to ﬁnish. For this to work, we require the
following conditions.

• m < n, for this construction to make sense.

• m ≥ 12, to avoid the known exceptional cases.

• 2m + 2n + 1 is a perfect square.

Since this square is odd, it must have the form (2k + 1)2 for some nonnegative integer
k, so the third condition can be written as m + n = 2k2 + 2k.
For each k, we see that we can complete the induction in the cases n = k2 + k + 1
up to n = 2k2 + 2k − 12 (using the bound on m). We want this to overlap with the
analogous list for k + 1, i.e., we need 2k2 + 2k − 12 ≥ (k + 1)2 + k + 1. It is straight-
forward to show that this inequality holds for k ≥ 5. Since the list for k = 5 starts at
n = 31, the lists together cover all of the integers 31, 32,... without any gaps. This
means that for each n > 30, we indeed have a construction that reduces the problem
to an earlier case.

A note on the proof: If one replaces the condition m ≥ 12 with the more precise
m /∈{1, 2, 3, 5, 6, 10, 11}, then with care the number of base cases can be reduced
from 30 to 17, eliminating many of the higher values, although n = 29 and n = 30
remain. The reduction comes primarily from considering k = 4.

Exercise 4. There is a similar theorem for the “odd” version of the problem, where
the initial number set is {0, 1,..., 2n − 1}. State and prove the theorem.

See [2, p. 77] for one approach to Exercise 4.
In Exercise 4, we have an input number set different from the previous problems.
Other related changes are possible, such as in the following two exercises.

Exercise 5. For an integer p, is there a similar theorem for { p,..., p + 2n − 1}?

From this point of view, our theorem is the case p = 1 and Exercise 4 is the case
p = 0; see [1].

266 © THE MATHEMATICAL ASSOCIATION OF AMERICA

Exercise 6. Even more generally, is there a similar theorem for a general 2n-term
arithmetic progression { p, p + d, p + 2d,..., p + (2n − 1)d}?

Changing targets

Using square numbers as targets produces some beautiful puzzles, but the number of
solutions explodes. Table 1 shows the number of solutions for {1, 2,..., 2n} from [3,
A252897].

Table 1. Number of square–sum pair partitions of {1, 2,..., 2n} for 1 ≤ n ≤ 30.

1 2 345 6 7 8 9 10

0 0 010 0 1 1 1 0

11 12 13 14 15 16 17 18 19 20

0 1 6 18 12 36 156 295 429 755

21 22 23 24 25 26 27 28 29 30

2603 7122 19232 32818 54363 172374 384053 933748 1639656 4366714

Here is one of the 4,366,714 solutions for {1, 2,..., 60}.123456789
10
11

12

13
14
15
16
17
18
19
20
21
22

2324252627282930313233343536373839
40

41

42
43
44
45
46 47 48 49 50 51 52 5354555657585960
One way to constrain the problem is to look for solutions that minimize the number
of target squares. (Looking at the coloring/position of the arcs, one can see that the
solution above uses ﬁve squares for sums.)
Squares are not the only possible targets for problems of this type. Below are some
interesting variations.

Exercise 7. Explore using powers of 2 as targets.

Exercise 8. Explore using numbers that are one less than a power of 2 as targets.

VOL. 46, NO. 4, SEPTEMBER 2015 THE COLLEGE MATHEMATICS JOURNAL 267

Exercise 9. Explore using prime numbers as targets. (This is solved in [2,p.78].)

Exercise 10. Explore using Fibonacci numbers as targets.

In an unpublished 2003 paper, “Fibonacci plays billiards,” Elwyn Berlekamp and
Richard Guy show that, unlike in the case of squares, the number of Fibonacci–sum
pair partitions does not grow quickly.
Among the many more possibilities, one could vary both the input set (as in
Exercises 4–6 for square–sum pairs) and the target numbers (Exercises 7–10). We
hope that the reader will explore some of them and ﬁnd ones that provide satisfying
puzzles or interesting proofs. (For example, when the targets are given by the values
of a polynomial, one can imitate our earlier proof to show that pairings always exist
once n is sufﬁciently large.)
Finally, here are two puzzles from [4] that are closely related to Exercise 1.
Bernardo Recam·an suggests that the numbers {1, 2,..., n} be ordered in a row so
that adjacent numbers sum to a square.

Exercise 11. Lay out the numbers from 1 to 15 so that adjacent numbers sum to a
square. (This is the smallest value for which the puzzle can be solved.)

Joe Kisenwether asks a similar question but for a necklace of numbers—again
adjacent numbers must sum to a square.

Exercise 12. Four pairs of neighbors are given below. Fill in the remaining beads so
that all adjacent numbers sum to a square and all the numbers from 1 to 32 have been
used once. (This is the smallest value for which the puzzle can be solved.)

15 1
 19

30

115

9

27

The square–sum pair partition problem and its variations combine both access and
challenge in one easy-to-present package. Undergraduates should ﬁnd it engaging.
If some of them become teachers, they will be able to share it with their precollege
students in math classes and math clubs.

Acknowledgment. Thanks to Joshua Zucker for providing the references [2, 6].

268 © THE MATHEMATICAL ASSOCIATION OF AMERICA

Summary. We present a middle school problem and generalize it in several ways, including
many new variations for readers to explore. The problems should be attractive to students, as
they have few prerequisites and lend themselves to beautiful visual representations.

References

1. G. Antonick, Picciotto–Hamilton rainbow squares, New York Times, Numberplay blog, Apr. 6, 2015, http://
wordplay.blogs.nytimes.com/2015/04/06/picciotto-hamilton/.
2. T. Kilkelly, The ARML Power Contest, American Mathematical Society, Providence, RI, 2014.
3. OEIS Foundation Inc. (2015), The On-Line Encyclopedia of Integer Sequences, http://oeis.org.
4. E. Pegg, Jr., MathPuzzle (2000), http://mathpuzzle.com/Solution.htm.
5. H. Picciotto, I’ve got a problem! and Getting help, My Math Education Blog (2015), http://blog.
mathedpage.org/2015/04/ive-got-problem.html and http://blog.mathedpage.org/2015/04/
getting-help.html.
6. A. S. Posamentier, S. Krulik, Problem-Solving Strategies for Efﬁcient and Elegant Solutions, Grades 6–12: A
Resource for the Mathematics Teacher, Corwin Press, Thousand Oaks, CA, 2008.
7. A. Wah, H. Picciotto. Algebra: Themes, Tools, Concepts. Creative Publications, Mountain View, CA, 1994,
http://www.mathedpage.org/attc/index.html.

Coming soon in Mathematics Magazine

On the Shape of a Violin by Roel J. Stoeker
A New Angle on an Old Construction: Approximating Inscribed n-gons by Robert
S. Milnikel
M¤obius Maps and Periodic Continued Fractions by A. F. Beardon

A Combinatorial Formula for Powers of 2 × 2 Matrices by John Konvalina

VOL. 46, NO. 4, SEPTEMBER 2015 THE COLLEGE MATHEMATICS JOURNAL 269
