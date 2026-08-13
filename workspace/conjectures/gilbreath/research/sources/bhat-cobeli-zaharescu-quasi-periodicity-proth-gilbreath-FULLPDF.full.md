<!-- source: https://arxiv.org/pdf/2307.11776 | pdftotext -layout of the FULL PDF -->

                                                ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES

                                                   RAGHAVENDRA N. BHAT, CRISTIAN COBELI, AND ALEXANDRU ZAHARESCU


                                                   Abstract. Let PG be the Proth-Gilbreath operator that transforms a sequence of integers
                                                   into the sequence of the absolute values of the differences between all pairs of neighbor
                                                   terms. Consider the infinite tables obtained by successive iterations of PG applied to
                                                   different initial sequences of integers. We study these tables of higher order differences
                                                   and characterize those that have near-periodic features. As a biproduct, we also obtain




arXiv:2307.11776v1 [math.NT] 19 Jul 2023
                                                   two results on a class of formal power series over the field with two elements F2 that can
                                                   be expressed as rational functions in several ways.




                                                             1. Introduction and Summary of previous results
                                              Let us consider the evolutionary process that replaces a sequence of integers a = {ak }k≥1
                                           with the distances between its consecutive terms. We write the new generation of differences
                                           shifted under the parent generation so that under any two consecutive terms of a, just below,
                                           is the distance between them. Repeating the process produces the sequences of higher-order
                                           differences. These are recorded in the following triangle, which can be finite or infinite as
                                           the initial sequence a is:
                                                             a1              a2            a3                a4                a5            a6          ...
                                                                       (1)           (1)               (1)           (1)               (1)
                                                                   d1               d2             d3               d4                d5           ...
                                                                              (2)           (2)               (2)               (2)
                                                                             d1            d2                d3            d4                ...               (P-G)
                                                                                     (3)               (3)           (3)
                                                                                    d1             d2               d3                ...
                                                                                           ...               ...               ...
                                           where
                                                                   (j+1)            (j)          (j)                     (0)
                                                                  dk         := dk+1 − dk                    and     dk := ak                for k ≥ 1.
                                           The initial sequence is also called the sequence of differences of order 0. The key element
                                           of the definition is taking the absolute value of differences, which makes all the elements of
                                           the triangle (P-G) positive. The operation that transforms a line to another by taking the
                                           absolute differences of nearby integers is also called the PG or the Proth-Gilbreath operator.
                                              The Proth-Gilbreath procedure produces tables of numbers of which their truncated
                                           triangles are part of a special family. A slightly modified rule, which, by definition, adds
                                           borders to the generating triangles has the effect that the growth is apparently reversed.
                                           All these number triangles can also be seen as symbolic dynamic systems that collect and
                                           structure a lot of information and links with other not necessarily related fields. In particular
                                           the modular versions of various variants of Pascal triangle, the outcome of Ducci games
                                           and Proth-Ducci triangles share and complement each other properties of an arithmetic,
                                           combinatorial and probabilistic nature (see [5–11, 15] and the references therein).
                                              2020 Mathematics Subject Classification. Primary 11B37; Secondary 11B39, 11B50.
                                              Key words and phrases: Proth-Gilbreath Conjecture, quasi-periodicity, formal power series, Fibonacci
                                           sequences, SP numbers.
                                                                                                              1
                  ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                             2

   The left-edge of the (P-G) triangle is particularly important because it somehow sums up
by averaging the differences of all orders. The interest was raised especially by Proth [18] in
the 19th century and then, independently, by Gilbreath [11, 16] (see also [13, Problem A10]
and [17]) in the mid-20th century with the observation that if the first line that generates
the triangle (P-G) is the sequence of primes, then on the left-edge there are only ones. The
fact that is expected to be very likely true is currently in the conjecture stage. The problem
is included in the selected lists of Guy [12, Example 12] and Montgomery [14, Appendix
Problem 68]) and has not been proven yet even whether there are an infinity of ones on the
left side of the triangle of high order differences.
   The higher order difference rows are mainly influenced by the numbers on the first line.
And yet, even for sequences somehow related to each other it can be found that the numbers
on the left-edge can have a very different structure. One such example is the sequence of
square-primes [1,2,4]. They are the elements of the ordered union of the sequence of primes
scaled by squares larger than 1:
                                           [
                                   SP :=      {k 2 p | p prime}.
                                            k≥2

Let sn denote the nth square-prime number. There are 21 square-primes in the first hundred
natural numbers:
           8, 12, 18, 20, 27, 28, 32, 44, 45, 48, 50, 52, 63, 68, 72, 75, 76, 80, 92, 98, 99.
The ordered sequence SP can be thought of as a superposition of layers of primes scaled
by non-trivial squares. The rarity of the squares and the multitude of the primes combine
to a density of the square-primes that has the same order of magnitude with that of the
primes. Thus, the analogue of the prime number theorem gives the following estimate [1]
for the size of sn , namely
                                                            
                                           n             n
                            sn = ζ(2) − 1 ·       +O       2   .
                                                  log n         log n
We also mention, among the characteristic properties, that there are infinitely many ‘twin’
square-primes that are next to each other [1], such as (27, 28) or (44, 45), (unlike the still
incompletely solved conjecture that the sequence of twin primes at distance 2 is infinite).
Emphasizing the aspect of proximity, we further note that an analogue of Dirichlet’s Theo-
rem for prime numbers in arithmetic progressions holds also for square-primes only with a
different density.
   Triangle (P-G) generated by the sequence of square-primes shows interesting properties.
For instance, apart from the first three numbers, the left-edge seems to contain only ones
and zeros in roughly equal proportions (see Figure 1). We do not know a proof of this fact,
but this kind of property is certain to hold for some subsequences of square-primes.
Theorem 1 (2023, [3]). There exits an infinite subsequence of square-prime numbers that
generates a (P-G) triangle where every other element on the left-edge is 1.
   To test and compare, we filtered out the integer parts of the integers in the triangles
keeping only the remainders of their division by some d ≥ 2. The results in three different
cases for two moduli d are shown in Figure 2. The outcome is singular only for the case of
primes mod 2. There the shape is trivial because of the simple reason that 2 is the only even
prime number. Apart from the colors representing the different residue classes mod d, the
pattern structure looks similar in all cases. The intermediate position of the square-primes
between primes and random numbers as the first line is not fortuitous. It is just a first step
                          ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                                              3


  100
                                                                 1000
   80
                                                                  800
   60
                                                                  600
   40
                                                                  400

   20                                                             200

       0                                                              0
           0         50        100              150        200            0              500        1000        1500        2000


           Figure 1. The number of 1’s versus the number of 0’s on the left-edge of the (P-G)
           with square-prime numbers on the first row. The image on the left shows the first 200
           values and the one on the right shows 2234 values obtained from the square-primes less
           than 20000. In total there are 1101 ones and 1130 zeros.



ahead of the cube-primes and higher-power-primes that yield (P-G) triangles that place
themselves in what appears as a continuous transformation of order in a distinguished class
of patterns.


  80                                       80                                              80

  70                                       70                                              70

  60                                       60                                              60

  50                                       50                                              50

  40                                       40                                              40

  30                                       30                                              30

  20                                       20                                              20

  10                                       10                                              10

  0                                        0                                               0
       0       20   40    60   80    100        0     20   40    60           80   100          0   20     40     60   80          100


  80                                       80                                              80

  70                                       70                                              70

  60                                       60                                              60

  50                                       50                                              50

  40                                       40                                              40

  30                                       30                                              30

  20                                       20                                              20

  10                                       10                                              10

  0                                        0                                               0
       0       20   40    60   80    100        0     20   40    60           80   100          0   20     40     60   80          100


           Figure 2. The gaps in the (P-G) triangles generated by primes (left), square-primes
           (middle) and random numbers (right). The initial rows (not shown) contain the first one
           hundred primes, the first one hundred square-primes, and one hundred integers selected
           randomly from [2, 550], respectively. (Note that p100 = 541 and s100 = 549.) The gaps
           are represented by two colors in the top triangles and by seven colors at the bottom. The
           colors correspond to the residue classes of the gaps (mod 2) and (mod 7), respectively.
           The triangles on the right side are obtained by two independent random choices of the
           numbers on the initial rows.
                   ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                               4

   In his extensive search for a possible counterexample of Gilbreath’s conjecture for lines
as long as 3.46 × 1011 and primes less than π(1013 ), Odlyzko [17] found none, and he notes
that similar conjectures are likely to be valid for many other sequences as well.
   In Figure 2, in the triangle in the upper left corner, the modulo 2 highlights the left
edge with 1’s, but hides the real general phenomenon. But if we ‘unzip the edge’ and
draw off the curtain, the ‘random pattern’ reveals when we change the modulus to d=4, for
example. Thus, looking at the rays that traverse (P-G) parallel to the left edge, we notice
that the number of 0’s is approximately equal to the number of 2’s. Indeed, in the counting
summarized in Table 1, the cut-off triangle has the side length 50000, being generated by
the first 50 thousand prime numbers, and, on the first five parallel lines with the left edge,
the difference between the number of 0’s and the    √ number of 2’s satisfies the ‘square root
rule’ in all five cases, all of them being less than 50 000 ≈ 223.61. Also, in this range, the
difference between the proportion of 0’s and the proportion of 2’s is less than one percent.
     Table 1. The frequencies of the absolute values of the differences on the rays that
     cross a cut-off of the (P-G) triangle passing parallel to its left edge. The generating row
     contains the first 50 000 prime numbers: 2, 3, . . . , 611 953. All differences are reduced
     modulo 4. The notations are as follows: r is the number of the ray, starting with r = 1,
     the ray next to the left edge; N is the number of differences on the ray (note that there
     are no differences on the first row of (P-G)); z is the number of zeros and t is the number
     of two’s.

                        r         N          z           t        (z − t)/N
                        1       49998      24914      25084        -0.00340
                        2       49997      25095      24902         0.00386
                        3       49996      25033      24963         0.00140
                        4       49995      25019      24976         0.00086
                        5       49994      25074      24920         0.00308


   A similar development comes along even further, on the rays farther away to the right
and still, analogue for larger moduli d, as evidenced by numerical computations. In the
simplest, bicolor version of the triangle, for d = 4, the following statement is likely to hold
true.
Conjecture 1. Let r ≥ 1 be integer and denote by δk (r) the rth element on the kth row of
the (P-G) triangle generated by the sequence of primes. Then, with finitely many exceptions,
the sequence of differences {δk (r)}k≥1 (mod 4) contains only 0’s and 2’s and, in the limit,
their proportions are the same being equal to 1/2.
   Our object in the following is to characterize the infinite sequences of integers that pro-
duce triangles with periodic patterns. We remark that Fibonacci’s sequence has the property
of reproducing itself on the next line of a (P-G) triangle. We may say that it is a fixed
point of the Proth-Gilbreath operator. Also, triangles generated by Fibonacci sequences
reveal periodic features when their entries are reduced modulo some d ≥ 2. We will inves-
tigate slightly more complex shapes and obtain a general characterization of triangles that
are not fully periodic. For this purpose we introduce an equivalence relation “≍” whose
quotient set is indeed composed only of periodic classes. Our main result is the following
characterization of binary sequences that are fixed points of the PG operator.
   We say that a row in (P-G) is ultimately replicated identically into another, if cutting the
entries at their beginnings, not necessarily in the same number, the two remaining sequences
of numbers on the two rows are identical.
                     ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                       5

Theorem 2. Let α = P      (a0 , a1 , a2 , . . . ) be the sequence of entries on a line of the (P-G)
triangle and let ϕ(α) = k≥0 ak X k be its associated formal power series. Suppose ak ∈ F2
for k ≥ 0. Then α is ultimately replicated identically in the next line of (P-G) if and only
if there exist an integer r ≥ 0 and a polynomial P (X) ∈ F2 [X] such that either
                                      P (X)                P (X)
                         ϕ(α) =             r
                                              or ϕ(α) = r            .                                     (1)
                                    1+X +X             X (1 + X) + 1
   As an application, we draw out the following two results that link certain formal power
series over F2 , and their representations as rational functions.
Theorem 3. Let f (X) be a formal power series with coefficients in F2 . Suppose there exists
a polynomial P (X) ∈ F2 [X] and an integer r ≥ 1 such that f (X) can be expressed as the
rational function
                                     P (X)                 P (X)
                        f (X) =            r
                                             or f (X) = r            .
                                   1+X +X              X (1 + X) + 1
Then, for any l ≥ 1, there exists a polynomial Pl (X) ∈ F2 [X] and an integer rl ≥ 1 such
that either
                               Pl (X)                       Pl (X)
                 f (X) =                  or f (X) = r                  .
                          (1 + X)l + X rl              X l (1 + X)l + 1
Theorem 4. Let f (X) be a formal power series with coefficients in F2 . Suppose there exist
m ≥ 1 polynomials P1 (X), P2 (X), . . . , Pm (X) ∈ F2 [X] and two sets of m positive integers
r1 , r2 , . . . , rm and l1 , l2 , . . . , lm such that either
                                    Pj (X)                      Pj (X)
                    f (X) =                     or f (X) = r                ,
                               (1 + X)lj + X rj           X j (1 + X)lj + 1
for any 1 ≤ j ≤ m. Let l = gcd(l1 , . . . , lm ). Then, there exists a polynomial P (X) ∈ F2 [X]
and an integer r ≥ 1 such that either
                                     P (X)                   P (X)
                      f (X) =           l    r
                                               or f (X) = r             .
                                 (1 + X) + X             X (1 + X)l + 1

  Theorem 4 covers a multitude of situations, some of them describing patterns of a certain
complexity. To give such an example, let us consider the set of integers
      M = {1, 2, 3, 4, 5, 8, 10, 12, 13, 14, 17, 18, 20, 24, 27, 28, 29, 30, 34, 36, 41, 42, 48,
              55, 56, 57, 58, 59, 60, 61, 63, 65, 67, 70, 71, 74, 75, 76, 78, 79, 80, 82, 85, 87, 88,
              92, 93, 95, 96, 97, 98, 100, 101, 103, 105, 106, 108, 109, 112, 115, 119, 120, 121, 126} .
Let f (X) ∈ F2 [[X]] be the formal power series with coefficients in the field with two elements
defined by                                 XX
                                  f (X) =          X s+127k .                                (2)
                                                   k≥0 s∈M
The coefficients of f (X) repeat with a period of length 127 and the graph of the first period
is shown in Figure 3.
   Now, on the one hand, observe that
          (1 + X)3 + X 21 f (X) = X + X 3 + X 6 + X 9 + X 13 + X 14 + X 15 + X 20 ,
                           

so that
                               X + X 3 + X 6 + X 9 + X 13 + X 14 + X 15 + X 20
                    f (X) =                                                    .                           (3)
                                              (1 + X)3 + X 21
                   ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                  6

 1



 0
     0            20             40             60             80            100            120 126

     Figure 3. The coefficients of the series f (X). The graph shows the first 127 coefficients,
     and the following ones are reproduced periodically with the period 127. There are 64
     non-zero coefficients among the first 127.


On the other hand, note that
                  (1 + X)2 + X 14 f (X) = X + X 2 + X 6 + X 7 + X 8 + X 13 ,
                                 

therefore
                                      X + X 2 + X 6 + X 7 + X 8 + X 13
                          f (X) =                                      .                           (4)
                                              (1 + X)2 + X 14
   Then, the hypotheses of Theorem 4 are satisfied with the parameters suggested from (3)
and (4): m = 2; l1 = 3, r1 = 21, P1 (X) = X + X 3 + X 6 + X 9 + X 13 + X 14 + X 15 + X 20 ;
l2 = 2, r2 = 14, P2 (X) = X +X 2 +X 6 +X 7 +X 8 +X 13 . Consequently, f (X) must also have
a simpler expression, which it does. Indeed, with 1 = gcd(2, 3), r = 7 and P (X) = X + X 6 ,
we do have
                                              X(1 + X 5 )
                                     f (X) =              ,
                                             1 + X + X7
which is the first type of rational function in the conclusion of Theorem 4.
   The rest of the paper is organized as follows. We start by discussing in Section 2 the
patterns generated by the PG operator applied to the sequence of powers of 2 and to
Fibonacci sequences. In Section 3 we introduce a relation according to which two rows of a
table built with the iteration of the PG operator are equivalent if they coincide except for
at most a finite number of numbers on them, and then we prove Theorem 2. In Sections 4
and 5 we address the relation between the (leap-)fixed points of the operator PG and the
formal power series over F2 , and then we prove Theorems 3 and 4 in Section 6. We conclude
with the presentation of some suitable examples in the last section.

             2. Fibonacci sequences and Proth-Gilbreath’s operator
   Let a, b ≥ 0 be the first two integers on the first row of the (P-G) triangle. If we want
the first line to be reproduced on the second line, then the third element has to coincide
with |b − a|, that is, either with b − a or with −b + a. If a ≤ b, and we also assume this
increasing order of the entries that follow, we find that the numbers on the first row are: a,
a21 , a22 , . . . Then, this line is a fixed point of the Proth-Gilbreath operator. Note that the
triangle would be perfectly flat if a = 0.
   If the ordering condition is not apriori required, but instead the choice of entries that
follow to the right asks that the numbers be bounded, sooner or later a periodic sequence
will emerge, maybe except for a few terms at the left end.
   A combination of the two types, periodic and interspersed with a2k ’s, with k unlimited,
develops if the size bounding condition is no longer imposed. Any such line is a fixed point of
the PG operator and they all reduce to periodic patterns if their entries are taken modulo d,
like the one in Figure 4 (left).
                                ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                                              7



  40                                                                          40

  35                                                                          35

  30                                                                          30

  25                                                                          25

  20                                                                          20

  15                                                                          15

  10                                                                          10

  5                                                                           5

  0                                                                           0
       0           10            20           30             40                    0          10           20          30           40

           Figure 4. Periodic patterns in (P-G) triangles. The left triangle has on the first row
           the powers of 2 starting with 1, 2, 4, 8, . . . , and the right triangle has on the first row the
           terms of the Fibonacci sequence with the initial parameters 15 and 7. In both images,
           the colors represent the residue classes modulo 19 of all entries.


  An augmented pattern is produced with the recursive Fibonacci rule Fk−1 + Fk = Fk+1 .
The Proth-Gilbreath operator transforms a Fibonacci sequence into a shifted version:
                       Fs                 Fs+1               Fs+2                      Fs+3               Fs+4     ...

                                Fs−1                   Fs               Fs+1                  Fs+2                Fs+3 . . .

Each repeated application of the operator adds a new number to the left side and shifts
the entire row to the right. Thus, depending on the hypothesis assumed with the starting
parameters on the left, a new triangle with a different periodic pattern grows attached to
the left of the (P-G) triangle, a triangle like the one in Figure 4 (right). Another numerical
example is
           3       1        4         5       9         14        23           37             60           97           157              ...
               2        3        1        4        5         9          14               23         37           60           ...
                   1        2         3       1         4          5               9          14           23           ...
                        1        1        2        3         1           4               5           9           ...
                            0         1       1         2          3               1           4           ...
                                 1        0        1         1           2               3          ...
                                      1       1         0         1                1          ...
                                          0        1         1           0              ...
                                              1         0         1            ...
                                                   1         1          ...
                                                        0         ...

 Then, a simple argument by induction shows that the emerging triangle from the left
consists of the repeated alternation of a 0 with two 1’s, and the pattern becomes uniform
allover across the entire triangle if all the numbers it contains are taken modulo 2. In
                     ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                  8

particular, note that in all these triangles, except for a finite number of cases at the top,
the numbers on the left-edge are in exact proportions: one-third 0’s and two-thirds 1’s.
   In conclusion, together with the previous remarks concerning the sequence of powers of
two, we conclude that the fixed and the ’almost fixed ’ points of the PG operator point to a
class of triangles that either have on the left-edge one hundred percent ones or two-thirds
of the entries ones.
Proposition 1. 1. The Proth-Gilbreath operator applied recursively on Fibonacci sequences
generated by non-negative relatively prime integers generates a triangle, which on its left-
edge, except for a finite number of entries, contains the periodic sequence 1, 1, 0, 1, 1, 0, . . .
   2. The left edge of the (P-G) triangle contains only ones if the sequence of numbers on
the first row is 1, 2, 22 , 23 , 24 , . . .

                         3. The characterization of fixed points
  To describe the combined nature of horizontal and vertical periodicity observed in the
examples discussed in Section 2, we start by introducing an equivalence relation on the
sequences that replicate fully or only partially in the triangle.
3.1. Notations and definitions. Denote by L the set of all sequences of non-negative
integers and by L2 the set of sequences of 0 and 1.
   We say that two sequences in L are equivalent if they ultimately coincide. Precisely, if
a = (a1 , a2 , . . . ) and b = (b1 , b2 , . . . ) are in L, then a ≍ b if there exists m, n ≥ 1 such that
am+k = bn+k for k ≥ 0. One immediately checks this relation is reflexive, symmetric and
transitive, that is, ‘≍’ is an equivalence relation.
   Let Lb = L/≍ denote the set of equivalence classes. Thus, if α ∈ Lb and a ∈ α, then
α = {b ∈ L : b ≍ a}. Also, if a ∈ L, we denote by â its equivalence class, so that
â = {b ∈ L : b ≍ a}.
   Denote now by Ψ : L → L the PG operator. Then, immediately by the definition, we see
that if a ≍ b, it follows that Ψ(a) ≍ Ψ(b).
   We also have the associated quotient map b               Ψ : Lb → L,b which is defined as follows: let
α ∈ L and let a ∈ α, so that α = â. Then put Ψ(α) := Ψ(a).
      b                                                            b         [ Note that Ψ      b is well
defined, since if a and b are both in α, then a ≍ b, which implies Ψ(a) ≍ Ψ(b), so that
 [ =[
Ψ(a)     Ψ(b). Now the problem of characterizing the rows that repeat in the triangle (P-G)
is the same as that of describing the fixed points of Ψ.          b
   Note that Ψ and b      Ψ restricted to L2 and the subset of equivalences classes L         c2 = L2 /≍ ,
which contains only sequences of 0’s and 1’s, act in the same manner. Furthermore, we can
also describe the rows of the (P-G) triangle using the formal power series with non-negative
integer coefficients or those with coefficients in F2 = Z/2Z, denoted by F2 [[X]]. Thus, to a
sequence α = (a0 , a1 , a2 , . . . ), we associate the formal power series
                                                                X
                                      ϕ(α) = ϕ(α)(X) :=             ak X k .
                                                           k≥0

  For example, if F is the periodic sequence F = (0, 1, 1, 0, 1, 1, 0, 1, 1, . . . ), then
                         ϕ(F ) = X + X 2 + X 4 + X 5 + X 6 + X 7 + · · · .
Note that ϕ(F ) belongs also to F2 [[X]] and additionally it can be expressed as a rational
function:
                                     X 3k     X + X2            X
                 ϕ(F ) = X + X 2         X =          3
                                                         =              .               (5)
                                                1+X         1 + X + X2
                                           k≥0
                  ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                           9

  Also remark that if α = (α0 , α1 , . . . ) has components in F2 , then the PG operator acts
by the following formula:
                          X                        X          1 X             a0
              ϕ(Ψ(α)) :=    (ak + ak+1 )X k =        ak X k +        ak X k −    ,
                                                              X               X
                          k≥0                    k≥0            k≥0

that is,
                                       (1 + X)ϕ(α) − α0
                                ϕ Ψ(α) =                 .                                 (6)
                                               X
3.2. Proof of Theorem 2. Suppose in the following that the entries from the first line
of (P-G) are only 0’s and 1’s, so that we take advantage of the simplicity of operating with
power series with coefficients in F2 , where −1 = 1.
   Note that if α ∈ L2 then Ψ(α) ∈ L2 , so that the whole triangle (P-G) contains only
elements of F2 .
   In terms of power series, the condition that two rows in (P-G) are ultimately identical
translates into a condition that the difference between one of the series and the shift of the
other is a polynomial. We state this observation in the following lemma that holds in L.
Lemma 1. Let α, β ∈ L. Then, α ≍ β if and only if there exists an integer r ≥ 0 and a
polynomial P (X) ∈ Z[X] such that
              either   ϕ(α) − X r ϕ(β) = P (X)    or   ϕ(β) − X r ϕ(α) = P (X).            (7)

Proof. Suppose α ≍ β. Then there exists two integers u, v ≥ 0, a formal series h(X) and
two polynomials U (X), V (X) ∈ Z[X] of degrees less than u and v, respectively, such that
ϕ(α) = U (X) + X u h(X) and ϕ(β) = V (X) + X v h(X). Suppose u ≤ v and let r = v − u.
Then X r ϕ(α) = X r U (X) + X v h(X). Then it follows that
              ϕ(β) − X r ϕ(α) = V (X) + X v h(X) − X r U (X) + X v h(X)
                                                                        

                                = V (X) − X r U (X),
equality which is the first of the two alternatives in (7) with P (X) = V (X) − X r U (X).
Similarly, if u > v, we find that the second equality in(7) holds.
   Conversely, suppose ϕ(α) − X r ϕ(β) = P (X), the other possibility being treated symmet-
rically. Then ϕ(α) = P (X) + X r ϕ(β). Here, the equality of the series is equivalent with
the equality of the coefficients, and this in turn holds modulo a shift of size r for all terms
of α and β of sufficiently large ranks. Therefore α ≍ β. This concludes the proof of the
lemma.                                                                                        □

   Then, by Lemma 1, the property of α ∈ L2 that α                        b that is, Ψ(α) ≍ α,
                                                    b is a fixed point of Ψ,
translates into the existence of an integer r ≥ 0 such that
              ϕ(Ψ(α)) − X r ϕ(α) ∈ F2 [X]     or ϕ(α) − X r ϕ(Ψ(α)) ∈ F2 [X].              (8)

  The case r = 0 holds when the rows ϕ(α) and ϕ(Ψ(α)) are the same, with no shifting,
with the possible exception of some terms from the beginning, situation that is covered in
Theorem 2 by the first expression in (1).
  Suppose now that r ≥ 1. Using formula (6), we see that this couple of conditions (8) is
equivalent with the couple:
    (1 + X)ϕ(α) − α0                                          (1 + X)ϕ(α) − α0
                     − X r ϕ(α) ∈ F2 [X]      or ϕ(α) − X r                    ∈ F2 [X].
           X                                                         X
                      ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                                   10

Equivalently, these can also be reformulated as

          ϕ(α) 1 + X + X r+1 ∈ F2 [X] or ϕ(α) X r−1 (1 + X) + 1 ∈ F2 [X],
                                                              


relations which, in their turn, are equivalent to formulation in (1). This concludes the proof
of Theorem 2.

Remark 1. Note that in Theorem 1 we could have let r take integer values not necessarily
positive. Indeed, observing that

                            P (X)        X r P (X)      P ∗ (X)
                                  −r
                                     = r            = r            ,
                          1+X +X      X (1 + X) + 1  X (1 + X) + 1

for some polynomial P ∗ (X) ∈ F2 [X], by letting r free, not necessarily positive, the two
alternatives in (1) would have been identified in one. So we could say (1) acts like a ‘hinge’
mirroring in the (P-G) triangle the horizontal ‘waves’ with the vertical ones that pass along
both ways from top to bottom and from bottom to top.

3.3. The Fibonacci series. The Fibonacci sequence F = (0, 1, 1, 0, 1, 1, 0, 1, 1, . . . ) mod 2
is periodic and it can be expressed as the rational function (5), which is exactly as that in
Theorem 2 with P (X) = X and r = 2. As a consequence it follows that Fb is a fixed point
of Ψ.
    b A direct calculation or else a manipulation of the associated series shows that the
other two Fibonacci sequences given by the initial conditions 1, 0 and 1, 1 are:
                                                                                  1+X
                     F ′ = (1, 0, 1, 1, 0, 1, 1, 0, 1, . . . ) and ϕ(F ′ ) =              ,
                                                                               1 + X + X2
                                                                                    1
                     F ′′ = (1, 1, 0, 1, 1, 0, 1, 1, 0, . . . ) and ϕ(F ′′ ) =             .
                                                                               1 + X + X2
Note that F , F ′ , F ′′ are the rows that alternate periodically to build the entire Fibonacci (P-G)
triangle modulo 2.
  We remark that the closely related sequence T = (0, 1, 1, 1, 0, 1, 1, 1, 0, . . . ) does not have
            X
ϕ(T ) = 1+X+X  3 as the rational function associated from Theorem 2, as one would be
tempted to assume. The reason is, on the one hand, the subsequent rows that T generates
are:
             0        1       1       1       0       1       1       1       0       1       1         1           ...
                 1        0       0       1       1       0       0       1       1       0        0          ...
                      1       0       1       0       1       0       1       0       1       0         ...
                          0       0       0       0       0       0       0       0       0       ...

and afterwards all the components become zeros. In particular we see that Tb is not a fixed
point of b
         Ψ. On the other hand, the associated series of T is
                                                              X                   X(1 + X + X 2 )
                          ϕ(T ) = (X + X 2 + X 3 )                    X 4k =                      ,
                                                                                      1 + X4
                                                              k≥0

which cannot be expressed as the ratio between a polynomial in F2 [X] and 1 + X + X r
or X r (1 + X) + 1 for any integer r ≥ 0, because if it were possible it would contradict
Theorem 2.
                   ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                              11

                    4. Fixed points and their formal power series
    Let r ≥ 2 be an integer and consider the polynomial fr (X) = X r + X + 1. Note that
fr (X) has no roots in F2 [X], because fr (0) = fr (1) = 1, so that we factor fr (X) over F2 [X],
where F2 is an algebraic closure of F2 . Thus, fr (X) = (X − η1 ) · (X − η2 ) · · · (X − ηr ), with
η1 , η2 , . . . , ηr ∈ F2 .
    Let K = F2 (η1 , . . . , ηr ) ⊂ F2 be the smallest subfield of F2 that contains all the roots of
fr (X) and let d = [K : F2 ] be the degree of the extension. Then, the cardinality of K is a
prime power, and in our case it is |K| = 2d . Since K × , the largest multiplicative subgroup
of K, is cyclic and contains all the non-zero elements, we have |K × | = 2d − 1. In particular,
it follows that
                                       d        d                d
                                    η12 −1 = η22 −1 = · · · = ηr2 −1 = 1.                        (9)


Lemma 2. All the roots of the polynomial fr (X) = X r + X + 1 are distinct in an algebraic
closure of F2 .
Proof. Suppose η1 , η2 , . . . , ηr are the roots of fr (X) and there exist distinct indices j and k
such that ηj = ηk . Then, fr (X) = (X − ηj )2 H(X) for some polynomial H(X) ∈ F2 [X].
Note that ηj is also a root of the derivative fr′ (X), since
                         fr′ (X) = (X − ηj ) 2H(X) + (X − ηj )H ′ (X) .
                                                                           

It then follows that
                             ηjr + ηj + 1 = 0   and rηjr−1 + 1 = 0.
Here, the second equality cannot hold if r is even (that is, if r’s image in F2 is 0), since,
otherwise, it would imply that 1 = 0.
  If r is odd, then we simultaneously have
                             ηjr + ηj + 1 = 0    and ηjr−1 + 1 = 0.
But this again implies the same contradiction 1 = 0, and, therefore, the lemma is proved.
                                                                                        □
                                                                                           d
The equalities (9) show that the ηj ’s are roots to both polynomials fr (X) and X 2 −1 − 1.
                                                  d
Therefore, employing Lemma 2, we find that X 2 −1 − 1 is divisible by fr (X), so that
                                  d
                               X 2 −1 − 1 = (X r + X + 1)H(X),                                 (10)
for some H(X) ∈ F2 [X].
   Suppose now that α ∈ L2 belongs to a class of the equivalence relation ≍ that is a fixed
point of Ψ.
         b Then, on combining the conclusion of Theorem 2 with the expression (10), we
find that the power series associated to α can be written as
                                                  G(X)
                                       ϕ(α) =               ,                                  (11)
                                                1 − X 2d −1
where G(X) = P (X)H(X) is a fixed polynomial in F2 [X].
  Let us note that the reciprocal of this statement is also true.
  And still, taking into account that the operations on the coefficients are made in F2 ,
the rational fraction (11) can be written equivalently as a power series that comprises the
coefficients of α. We state our findings in the next theorem.
                  ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                         12

Theorem 5. Let α ∈ L2 . Then, α is ultimately identical with Ψ(α) if and only if there
exists a positive integer d and a polynomial G(X) ∈ F2 [X] such that the power series
associated to α is
                     G(X)             
                                              2d −1     2(2d −2)     3(2d −1)
                                                                                      
          ϕ(α) =               = G(X)   1 + X       + X          + X          + · · ·   .
                   1 − X 2d −1
             5. Leap fixed points of the Proth-Gilbreath operator
   The next lemma provides the relation between the powers series associated to two rows
in the (P-G) triangle.
Lemma 3. Let α ∈ L2 be a row in the (P-G) triangle and let k ≥ 0 be integer. Then, there
exits a unique polynomial R(X) ∈ F2 [X] of degree 0 ≤ deg(R(X)) ≤ k − 1 such that
                                  (1 + X)k ϕ(α) − R(X)
                      ϕ Ψ[k] (α) =                            for k ≥ 1.                (12)
                                               Xk
Proof. Let ϕ(α) be the power series associated to α. If k = 0 relation (12) is trivial and if
k = 1 it coincides with (6). Next we proceed by induction. Let k ≥ 1 be fixed and suppose
                                        (1 + X)k ϕ(α) − R(X)
                             ϕ Ψ[k] (α) =                         ,                     (13)
                                                    Xk
for some R(X) ∈ F2 [X], and 0 ≤ deg(R(X)) ≤ k − 1. Then, by (6) it follows that
                                                  (1 + X)ϕ Ψ[k] (α) − a0
                                                                       
                   [k+1]                 [k]
                            
               ϕ Ψ       (α) = ϕ Ψ(ϕ(Ψ (α))) =                              .
                                                                 X
On inserting (13), we see that the above is
                               (1 + X) (1 + X)k ϕ(α) − R(X) X −k − a0
                                                                  
                     [k+1]
                 ϕ Ψ       (α) =
                                                      X
                                   (1 + X)k+1 ϕ(α) − R1 (X)
                                =                           ,
                                             X k+1
where R1 (X) = a0 X k +(1+X)R(X) ∈ F2 [X] is a polynomial of degree ≤ k. This completes
the proof of the lemma.                                                                   □
   A quasi-periodicity phenomenon that can occur in a triangle is the situation in which
two rows situated at l ≥ 0 ranks apart are identical, except for a finite number of entries
at their left-end entry. In the language of the equivalence classes introduced in Section 3.1,
we will say that a row α of (P-G) is an l-leap fixed point of the Proth-Gilbreath operator if
Ψ[l] (α̂) = α̂. Note that any row is a 0-leap fixed point of Ψ and fixed points are the same
as 1-leap fixed points of Ψ. Similarly, we say that α b ∈ Lb is an l-leap fixed point of Ψb if
b [l]
Ψ (b  α) = αb for some natural number l.
   Then, using the observation from Lemma 1, we know that α is an l-leap fixed point if
and only if there exists an integer r ≥ 0 such that
              ϕ Ψ[l] (α) − X r ϕ(α) ∈ F2 [X] or ϕ(α) − X r ϕ Ψ[l] (α) ∈ F2 [X].
                                                                       

On inserting formula (12), we find that the above statement is equivalent with
                         (1 + X)l ϕ(α) − R(X)
                                              − X r ϕ(α) ∈ F2 [X]
                                   Xl
or
                                      (1 + X)l ϕ(α) − R(X)
                         ϕ(α) − X r                        ∈ F2 [X]
                                                Xl
                       ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                                               13

for some integer r ≥ 0 and some unique polynomial R(X) ∈ F2 [X] of degree < l. The ‘or’
statement above is also equivalent with
          (1 + X)l + X l+r ϕ(α) ∈ F2 [X] or X r−l (1 + X)l + 1 ϕ(α) ∈ F2 [X] .
                                                             

Next, in the following theorem we restate the obtained result noting that, as in Remark 1,
the above belonging relations can be adapted by rewriting them changed from one to the
other if we allow the power of X to be negative or not.
Theorem 6. Let l ≥ 0 be an integer and let α ∈ L2 be a row in the (P-G) triangle. Then α
is ultimately replicated identically in the l-th row that follows α if and only if there exist an
integer r ≥ 0 and a polynomial Pl (X) ∈ F2 [X] such that
                                       Pl (X)                 Pl (X)
                        ϕ(α) =             l   r
                                                 or ϕ(α) = r             .
                                   (1 + X) + X            X (1 + X)l + 1
                                    6. Proof of Theorems 3 and 4
  We can now use Theorem 6 to interpret the patterns of (P-G) and draw out information
about formal power series. For this, the basic link is made clear in the following statement.
Remark 2. Let l ≥ 0 be an integer and let α ∈ L2 be a row in the (P-G) triangle. Then
b [l] ( b
Ψ      α) = α
            b if and only if the series of rows that start with α belongs to a sequence of
equivalence classes that is periodic and l is the length of a period.
                                                              P (X)                   P (X)
   Let now f (X) ∈ F2 [[X]] and suppose f (X) = 1+X+X               r or f (X) = X r (1+X)+1 for some

integer r ≥ 0 and some polynomial P (X) ∈ F2 [X]. By Theorem 6 with l = 1, it follows
that f (X) = ϕ(α) for some α ∈ L2 and α     b = Ψ(   b b α). Then α is a fixed point not only for Ψ, b
                            b [l] for l ≥ 0. Using the observation in Remark 2 we see that
but also for its iterations Ψ
the statement with the rational expressions of ψ(α) from Theorem 6 is equivalent with the
second statement from Theorem 3, which is now proved.
   To prove Theorem 4 note that its hypothesis is equivalent with the fact that the row α
for which f (X) = ϕ(α) is a leap-fixed point of orders l1 , l2 , . . . , lr . That is, in the (P-G)
triangle α
         b repeats periodically with each of the periods l1 , l2 , . . . , lr . A simple argument by
induction then shows that l := gcd(l1 , l2 , . . . , lr ) is also a period on which α  b repeats in the
triangle. Then Theorem 4 follows as a consequence of Remark 2 and Theorem 3.

                                      7. Some relevant examples
   In particular cases the Proth-Gilbreath operator action is similar to the transformations
that occur in the Ducci number game [6, 10]. There the action is on the numbers placed
around on a torus, which can be unfolded equivalently into a periodic sequence. In the par-
ticular case with numbers in F2 the Ducci operation replaces the numbers from a generation
to the next with the sums of neighbors.
7.1. Example δ. Of particular interest in the Ducci game are initial states that generate
unusually long cycles. Such an example starts with the finite sequence (1, 0, 0, 0, 1) placed on
a torus. Its periodic unfolded version is then the sequence: δ = (1, 0, 0, 0, 1, 1, 0, 0, 0, 1, . . . ).
Then the lines Ψ[k] (δ), k ≥ 0, are also periodic, and finding their general expressions reduces
to finding the evolution of their first five components. But this is the same as the recursive
outcome of the Ducci operation:
   (1, 0, 0, 0, 1) → (1, 0, 0, 1, 0) → (1, 0, 1, 1, 1) → (1, 1, 0, 0, 0) → (0, 1, 0, 0, 1) →
   (1, 1, 0, 1, 1) → (0, 1, 1, 0, 0) → (1, 0, 1, 0, 0) → (1, 1, 1, 0, 1) → (0, 0, 1, 1, 0) →
   (0, 1, 0, 1, 0) → (1, 1, 1, 1, 0) → (0, 0, 0, 1, 1) → (0, 0, 1, 0, 1) → (0, 1, 1, 1, 1) → (1, 0, 0, 0, 1) → · · ·
                    ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                              14

 We see that the evolution cycles in fifteen steps, so that Ψ[15] (δ) = δ. Then, a closer
inspection shows that if we make equivalent sequences that are the same modulo a rotation
around the torus, then the cycle length is only 3, the repeated pattern being of two ones
followed by three zeros.
   In the language of the formal series it then follows that the shortest period for the
sequence of iterations of Ψ          b [3k] (δ)
                          b is 3 and Ψ       b = δb for k ≥ 0. Precisely, we have
                       ϕ(δ) = 1 + X 4 + X 5 + X 9 + x10 + x14 + x15 + · · ·
                            = (1 + X 4 ) 1 + X 5 + X 10 + X 15 + · · ·
                                                                       
                                                                                (14)
                            1 + X4
                         =          .
                            1 + X5
To express ϕ(δ) in the form from Theorem 3, with l = 3 and r = 4 we have to find the
polynomial P (X) that satisfies condition
                                           P (X)        1 + X4
                                                      =        .
                                       (1 + X)3 + X 4   1 + X5
We obtain P (X) = 1 + X + X 2 + X 3 , and consequently, besides (14), we also have the
representation
                                     1 + X + X2 + X3
                           ϕ(δ) =                     .
                                       (1 + X)3 + X 4
7.2. Example γ. Consider the sequence γ = (1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, . . . ) in which
the first seven entries (1, 1, 0, 0, 0, 1, 1) repeat periodically.
                     (1, 0, 0, 0, 1, 0, 0) → (1, 0, 0, 1, 1, 0, 1) → (1, 0, 1, 0, 1, 1, 0) →
                     (1, 1, 1, 1, 0, 1, 1) → (0, 0, 0, 1, 1, 0, 0) → (0, 0, 1, 0, 1, 0, 0) →
                     (0, 1, 1, 1, 1, 0, 0) → (1, 0, 0, 0, 1, 0, 0) → · · ·
The series corresponding to γ is
                                                         1 + X4
                                              ϕ(γ) =            .
                                                         1 + X7
This can also be written as
                                                  1 + X + X2 + X3
                                      ϕ(γ) =                       .
                                                    (1 + X)7 + X 7
7.3. Example ν. Consider the 5-tuple (1, 0, 0, 0, 0) that repeats periodically to generate
the row
                            ν = (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, . . . ).
Then the series corresponding to ν is
                                                 X                  1
                                      ϕ(ν) =           X 5k =           .
                                                                 1 + X5
                                                 k≥0

Then one can check directly that ϕ(ν) cannot be expressed as a rational function in any of
the forms
                                  P (X)               P (X)
                                     l     r
                                             or                  ,
                              (1 + X) + X       X (1 + X)l + 1
                                                   r

for any positive integers l, r and any polynomial P (X) ∈ F2 [X]. This could have been done
if the hypotheses of Theorem 6 had been fulfilled. But the series ϕ(ν) does not meet them.
Indeed, on the discrete torus of length 5, the Ducci operation transforms (1, 0, 0, 0, 0) into
                    ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                              15

(1, 1, 0, 0, 0). But, as observed in the above example for the row δ, (1, 1, 0, 0, 0) belongs to
a cycle, whereas (1, 0, 0, 0, 0) does not, (1, 0, 0, 0, 0) is part of a pre-cycle not a cycle.
7.4. Example ι. The example after Theorem 4 in the introduction is based on the se-
quence ι whose first 127 terms are represented by the dots in Figure 3. Afterwards, the
terms repeat periodically, and consequently ϕ(ι) = f (X), where f (X) is the series defined
by (2). The example was build starting with the observation from Lemma 2 that the roots
of X 7 + X + 1 are distinct, and K, the smallest field extension F2 ⊂ K that contains all the
roots has the multiplicative group of order 27 − 1 = 127. Then we know that X 7 + X + 1
divides X 127 − 1 in F2 [X]. It follows that for f (X), the formal power series corresponding
to the periodic consequent line in the triangle (P-G), there exists Q(X) ∈ F2 [X] such that
                                X + X6          Q(X)            X
                    f (X) :=               =            =  Q(X)     X 127k .
                              1 + X + X7      X 127 − 1
                                                                      k≥0

The polynomial Q(X) has degree 126, the powers of its non-zero terms are the elements of
the set M, and it can be split as a product of irreducible polynomials in F2 [X] as
      Q(X) =X(X + 1)2 (X 4 + X 3 + X 2 + X + 1)(X 7 + X 3 + 1)(X 7 + X 3 + X 2 + X + 1)
               · (X 7 + X 4 + 1)(X 7 + X 4 + X 3 + X 2 + 1)(X 7 + X 5 + X 2 + X + 1)
               · (X 7 + X 5 + X 3 + X + 1)(X 7 + X 5 + X 4 + X 3 + 1)
               · (X 7 + X 5 + X 4 + X 3 + X 2 + X + 1)(X 7 + X 6 + 1)
               · (X 7 + X 6 + X 3 + X + 1)(X 7 + X 6 + X 4 + X + 1)
               · (X 7 + X 6 + X 4 + X 2 + 1)(X 7 + X 6 + X 5 + X 2 + 1)
               · (X 7 + X 6 + X 5 + X 3 + X 2 + X + 1)(X 7 + X 6 + X 5 + X 4 + 1)
               · (X 7 + X 6 + X 5 + X 4 + X 2 + X + 1)(X 7 + X 6 + X 5 + X 4 + X 3 + X 2 + 1) .

                                           References
  [1] Raghavendra N. Bhat, Distribution of square-prime numbers, Missouri J. Math. Sci. 34 (1), 121–
      126 (2022). https://doi.org/10.35834/2022/3401121 https://arxiv.org/pdf/2109.10238.pdf 2
  [2] Raghavendra N. Bhat, Sequences, Series and Uniform distribution of SP Numbers, arxiv preprint,
      7 pp. (2022). https://arxiv.org/pdf/2210.04622.pdf 2
  [3] Raghavendra N. Bhat, Cristian Cobeli, Alexandru Zaharescu, Filtered rays over iterated
      differences on layers of integers, preprint (2023). 2
  [4] Raghavendra N. Bhat, Sundarraman Madhusudanan, Algebraic Results on SP Numbers along
      with a generalization, arxiv preprint, 7 pp. (2022). https://arxiv.org/pdf/2211.09009.pdf 2
  [5] Mihai Caragiu, Alexandru Zaharescu, Mohammad Zaki, An analogue of the Proth-Gilbreath
      conjecture, Far East J. Math. Sci. (FJMS) 81 (1), 1–12 (2013). http://www.pphmj.com/abstract/
      7973.htm 1
  [6] C. I. Cobeli, M. Crâşmaru, A. Zaharescu, A cellular automaton on a torus, Port. Math. 57 (3),
      311–323 (2000). https://www.emis.de/journals/PM/57f3/pm57f305.pdf 1, 13
  [7] Cristian Cobeli, Alexandru Zaharescu, Promenade around Pascal triangle – number motives,
      Bull. Math. Soc. Sci. Math. Roum., Nouv. Sér. 56(104) (1), 73–98 (2013). https://www.jstor.org/
      stable/43679285 1
  [8] Cristian Cobeli, Alexandru Zaharescu, A game with divisors and absolute differences
      of exponents, J. Difference Equ. Appl. 20 (11), 1489–1501 (2014). https://doi.org/10.1080/
      10236198.2014.940337 1
  [9] Cristian Cobeli, Mihai Prunescu, Alexandru Zaharescu, A growth model based on
      the arithmetic Z-game, Chaos Solitons Fractals 91, 136–147 (2016). https://doi.org/10.1016/
      j.chaos.2016.05.016 1
 [10] Cristian Cobeli, Alexandru Zaharescu, Flurries of Ducci waves, Bull. Math. Soc. Sci. Math.
      Roumaine 66(114) (2), 177–188 (2023). 1, 13
                   ON QUASI-PERIODICITY IN PROTH-GILBREATH TRIANGLES                               16

[11] Norman Gilbreath, Processing process: the Gilbreath conjecture, J. Number Theory 131 (12),
     2436–2441 (2011). https://doi.org/10.1016/j.jnt.2011.06.008 1, 2
[12] Richard K. Guy, The strong law of small numbers, Am. Math. Mon. 95 (8), 697–712 (1988).
     https://doi.org/10.2307/2322249 2
[13] Richard K. Guy, Unsolved problems in number theory. 3rd ed. Problem Books in Mathematics. New
     York, NY: Springer-Verlag (ISBN 0-387-20860-7/hbk). xviii, 437 pp. (2004). 2
[14] Hugh L. Montgomery, Ten lectures on the interface between analytic number theory and harmonic
     analysis, Regional Conference Series in Mathematics 84. Providence, RI: American Mathematical
     Society (AMS). xii, 220 pp. (1994). 2
[15] Mihai Prunescu, Symmetries in the Pascal triangle: p-adic valuation, sign-reduction modulo p and
     the last non-zero digit, Bull. Math. Soc. Sci. Math. Roumaine 65(113) (4), 431–447 (2022). https:
     //ssmr.ro/bulletin/pdf/65-4/articol 6.pdf 1
[16] R. B. Killgrove, K. E. Ralston, On a conjecture concerning the primes, Math. Tables Aids Comput.
     13, 121–122 (1959). https://doi.org/10.2307/2001963 2
[17] Andrew M. Odlyzko, Iterated absolute values of differences of consecutive primes, Math. Comput.
     61 (203), 373–380 (1993). https://doi.org/10.2307/2152962 2, 4
[18] F. Proth, Sur la série des nombres premiers, Nouvelle Correspondance Mathématique 4, 236–240
     (1878). https://gdz.sub.uni-goettingen.de/download/pdf/PPN598948236 0004/LOG 0088.pdf 2

  (Raghavendra N. Bhat) Department of Mathematics,University of Illinois at Urbana-Champaign,
Urbana, IL 61801, USA
  Email address: rnbhat2@illinois.edu

  (Cristian Cobeli) ”Simion Stoilow” Institute of Mathematics of the Romanian Academy, 21
Calea Grivitei Street, P. O. Box 1-764, Bucharest 014700, Romania
  Email address: cristian.cobeli@imar.ro

  (Alexandru Zaharescu) Department of Mathematics,University of Illinois at Urbana-Champaign,
Urbana, IL 61801, USA, and ”Simion Stoilow” Institute of Mathematics of the Romanian Acad-
emy, 21 Calea Grivitei Street, P. O. Box 1-764, Bucharest 014700, Romania
  Email address: zaharesc@illinois.edu
