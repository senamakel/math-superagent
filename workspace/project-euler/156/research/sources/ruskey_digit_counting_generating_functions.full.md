<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL12/Ruskey2/ruskey14.pdf | converted from PDF -->

23 11 Article 09.5.6
Journal of Integer Sequences, Vol. 12 (2009),2
 3

6

1

47

Generating Functions for the Digital Sum
and Other Digit Counting Sequences

Franklin T. Adams-Watters
FrankTAW@Netscape.net

Frank Ruskey
University of Victoria
Victoria, BC V8W 3P6
CANADA
ruskey@cs.uvic.ca

Abstract

A numeration system associates a unique string, Ξ(n), with each positive integer
n, where each string is over the same ﬁnite alphabet. Various digit counting statistics
of Ξ(n) are of interest with respect to a numeration system. An example is the digital
sum, which is the sum of the digits in the number. We present a unifying framework
for deriving identities for the generating functions of such statistics in many of the
more popular numeration systems.

1 Introduction

Numeration systems provide a rich source of integer sequences. There are many interesting
digit counting statistics that arise from the various numeration systems. A typical example,
the digital sum, is explained below.
Given a number n represented in binary, n = (bdbd−1 · · · b1b0)2, the (binary) digital sum
of n, denoted s2(n) is b0 + b1 + · · · + bd. The digital sum goes under several other names
including sideways sum, sideways addition, population count, and Hamming weight. It is
denoted νn in Knuth [5], but we use the notation used by Allouche and Shallit [1] (but due
to earlier researchers; e.g., B´esineau [2] and Coquet and Toﬃn [3]). There are two natural
ways in which we might extend the idea to k-ary numbers, either by summing digits, or by
counting non-zeros. We use the notation sk(n) (again following [1]) for the sum-of-digits
function and ck(n) for the counting non-zeros function.

1

According to OEIS A053735, the ordinary generating function of sk(n) has the beautiful
expression given in Theorem 1 below. For k = 2 this generating function may be found in
Knuth [5]; see exercise 7.1.3.41. The purpose of this short paper is to provide a proof of
this and some other related generating functions that are in the OEIS — as part of a more
generalized setting. Table 1 contains some of the sequences to which our results apply.

Theorem 1. For all k ≥ 2,

∑

n≥0 sk(n)zn = 1
1 − z
 ∑

m≥0
 zkm + 2z2km + · · · + (k − 1)z(k−1)km

1 + zkm + z2km + · · · + z(k−1)km

= 1
1 − z
 ∑

m≥0
 zkm − kzkm+1 + (k − 1)z(k+1)km

(1 − zkm)(1 − zkm+1) .

2 Numeration as a sequence of columns

Imagine a table comprised of inﬁnite columns of numbers, C0, C1, C2, . . .. The numbers in
each column are indexed starting at 0 and the numbers found in all of the columns all
come from the same ﬁnite set. In a numeration system each row of the table is distinct.
For example, in the binary number system, Cj consists of the periodic repetition of 2
j 0s
followed by 2
j 1s.
What is the generating function function for the row sums of those columns? Suppose
that the generating function for the m-th column is Cm(z). Then

A(z) = ∑

m≥0 Cm(z) (1)

is the generating function for the row sums. That is, ⟨zn⟩A(z) is the sum of the numbers in
the n-th row, where ⟨zn⟩ means “coeﬃcient of zn”. The generating function (1) will exist so
long as there are constants cn such that ⟨zn⟩Cm(z) = 0 for all m ≥ cn. In many numeration
systems the m-th column can be described as a inﬁnite string of the form smt
∞
m , where sm
and tm are strings with tm ̸= ε and t
∞
m denotes the inﬁnite string t
∞
m = tmtmtm · · · . Let |s|
be the length of the string s. If Sm(z) and Tm(z) are the generating functions (which are
actually polynomials) of s and t, respectively. Then

Cm(z) = Sm(z) + z|sm|Tm(z)
1 − z|tm| (2)

Often sm and tm will have a special form that allows for further simpliﬁcation of Cm(z)
In this paper the most general from that we use is shown below. Here the m-th column
depends on integers bm, am and um, and the sequence of numbers α0, α1, α2, . . .. The following
string is called the column pattern:

smt
∞
m = 0
bm(αam
0 αam
1 · · · αam
(um−1))
∞ (3)

2

For example, the column pattern for the binary digital sum is (0
2m1
2m)
∞; here bm = 0,
am = 2
m, α0 = 1, α1 = 1, and um = 2. The generating function of αam
0 αam
1 · · · αam
(um−1) is

Am(z) = (α0 + α1zam + α1z2am + · · · + αum−1z(um−1)am) 1 − zam

1 − z

Thus, by (2), the generating function for (3) is

zbmAm(z)
1 − zumam = zbm

1 − z · α0 + α1zam + α2z2am + · · · + αum−1z(um−1)am

1 + zam + z2am + · · · + z(um−1)am .

Summing over m ≥ 0 we obtain

A(z) = 1
1 − z
 ∑

m≥0
 zbm(1 − zam)
1 − zumam (α0 + α1zam + α2z2am + · · · + αum−1z(um−1)am) (4)

= 1
1 − z
 ∑

m≥0 zbm α0 + α1zam + α2z2am + · · · + αum−1z(um−1)am

1 + zam + z2am + · · · + z(um−1)am . (5)

In the sections to follow we apply this generating function to various numeration systems,
starting with a new addition to the OEIS.

3 The Balanced Ternary System

In the balanced ternary system each natural number n is expressed as a sum of distinct signed
powers of 3. For example 5 = 9 − 3 − 1 = 3
3 − 3
1 − 3
0. The digital sum is OEIS A065363.
Following Knuth [4] we use ¯1 to denote −1. It is outside the scope of this paper, but it is
not diﬃcult to show that the pattern of the m-th column is

0
3m−3m−1−···−30(1
3m¯1
3m0
3m)
∞.

Since 3
m − 3
m−1 − · · · − 3
0 = (3
m + 1)/2, the generating function for the sum of the digits
of the balanced ternary representation of n is

A(z) = 1
1 − z
 ∑

m≥0 z(3m+1)/2 1 − z3m

1 + z3m + z2·3m = 1
1 − z
 ∑

m≥0 z(3m+1)/2 (1 − z3m)
2

1 − z3m+1 .

4 The k-ary Numeration System and Morphisms

The column pattern for k-ary numbers is

(αkm
0 αkm
1 . . . αkm
k−1)
∞. (6)

Here the row sum of the n-th row, where

n = ∑

k≥0 bkkm, is ∑

k≥0 αbkkm.

3

That is, each digit b is “weighted” by αb. For the digital sum, αb = b.
The special form of (6) implies that there is a “morphism” that underlies the construction;
for the digital sum it is j → j, j + 1, j + 2, . . . , j + k − 1. For example, when k = 3 we get the
sequence s3(0), s3(1), s3(2), . . . as the limit (i.e., ﬁxed-point) of a morphism noted by Robert
G. Wilson in A053735, which gives us successively

0 → 012 → 012 123 234 → 012123234 123234345 234345456 → · · ·

This limit will exist for any morphism of the form

j → j + α0, j + α1, . . . , j + αk−1, (7)

so long as α0 = 0.

Theorem 2. The row sums of the column pattern (6) are generated by the morphism (7) so
long as α0 = 0.

Proof. The column pattern (6) is invariant under the following two-step operation: (a) Take
column m and replace each entry in the column by k identical entries, calling the new column
C ′
m+1. (b) Form a new column C ′
0 with the pattern (01 · · · (k − 1))
∞. The invariance is that
C ′
m = Cm for m = 0, 1, 2, . . ..
A row sum j under operations (a) and (b) becomes the k row sums j + α0, j + α1, . . . , j +
αk−1. This is the morphism (7).

With the pattern (6) equation (5) gives us the theorem below.

Theorem 3. If k is an integer with k ≥ 2 and α0 = 0, then the generating function of the
limit of the morphism (7) is

A(z) = 1
1 − z
 ∑

m≥0
 α1zkm + α2z2km + · · · + αk−1z(k−1)zm

1 + zkm + z2km + · · · + z(k−1)km . (8)

Note that Theorem 1 is the special case where αi = i for i = 0, 1, . . . , k − 1. The
second equality in Theorem 1 follows from the fact that z + 2z + · · · + (k − 1)zk−1 =
(z − kzk + (k − 1)zk+1)/(1 − z)
2. We now return to the non-zero count function, ck(n), which
can be expressed without the inner sums used in (8).

Corollary 4. The generating function of ck(n) is

Ck(z) = 1
1 − z
 ∑

m≥1
 zkm−1 − zkm

1 − zkm . (9)

Proof. Here the morphism is j → j, j + 1, . . . , j + 1 and so Theorem 3 gives us the ﬁrst
equality below.

Ck(z) = 1
1 − z
 ∑

m≥0
 zkm + z2km + · · · + z(k−1)km

1 + zkm + z2km + · · · + z(k−1)km (10)

= 1
1 − z
 ∑

m≥0
 (1 − zkm+1)/(1 − zkm) − (1 − zkm)/(1 − zkm)
(1 − zkm+1)/(1 − zkm)

Cancelling common denominators and simplifying gives (9).

4

Other morphisms would give counts of the number of times individual digits occur in the
obvious way. For example, j → j, j, j + 1, j is the morphism for the number of 2’s that occur
in the 4-ary expansion of n (here the pattern is (0
4m0
4m1
4m0
4m)
∞).

Theorem 5. Let d be an integer with 0 < d < k. The generating function for the number
of digits equal to d in the k-ary expansion of n is

1
1 − z
 ∑

m≥0
 zdkm

1 + zkm + z2km + · · · + z(k−1)km = 1
1 − z
 ∑

m≥0
 zdkm(1 − zkm)
1 − zkm+1 . (11)

The generating function for the number of 0 digits in the k-ary expansion of n is

1
1 − z
 ∑

m≥0
 zkm+1

1 + zkm + z2km + · · · + z(k−1)km = 1
1 − z
 ∑

m≥0
 zkm+1(1 − zkm)
1 − zkm+1 . (12)

Proof. Equation (11) follows from Theorem 3 with the morphism j → j, . . . , j, j + 1, j, . . . , j
where the j + 1 occurs in position d, counting from 0. To prove (12) we use the generating
function T (z) = 1
1 − z
 ∑

m≥0 zkm

for 1 + ⌊logk n⌋, which is the number of k-ary digits in n. Adding (10) and (12) we clearly
obtain T (z).
A second way of ﬁnishing the proof is to note that the column pattern

0
km(1
km2
km · · · (k − 1)
km0
km)
∞

also describes the k-ary listing of numbers. The useful aspect of expressing it this way is
that the leading 0s are correspond to the initial 0
km above. Thus the pattern for counting
(non-leading) 0s is 0
km(0
km0
km · · · 0
km1
km)
∞.

According to (5) the numerator inside the sum of the generating function is zbmz(um−1)am =
zkmz(k−1)km = zkm+1, as desired.

4.1 Digit counts in speciﬁc positions

Let C(n, r, d) be the number of 1 bits in the binary representation of n that are in positions
that are congruent to r mod d. As usual, the “positions” are indexed starting at 0 on
the right. For example, 888 = (1101111000)2, so C(888, 0, 3) = 3, C(888, 1, 3) = 1 and
C(888, 2, 3) = 2.

Theorem 6. For all integers d ≥ 0 and integers r with 0 ≤ r < d,

∑

n≥0 C(n, r, d)zn = ∑

m≥0
 z2r+dm

1 + z2r+dm . (13)

5

OEIS description comment pattern
A023416 0s in binary same as A080791 0
2m(0
2m1
2m)
∞

A000120 1s in binary digital sum, base 2 (0
2m1
2m)
∞

A077267 0s in base 3 same as A081602 0
3m(0
3m0
3m1
3m)
∞

A062756 1s in base 3 (0
3m1
3m0
3m)
∞

A081603 2s in base 3 (0
3m0
3m1
3m)
∞

A160380 0s in base 4 0
4m(0
4m0
4m0
4m1
4m)
∞

A160381 1s in base 4 (0
4m1
4m0
4m0
4m)
∞

A160382 2s in base 4 (0
4m0
4m1
4m0
4m)
∞

A160383 3s in base 4 (0
4m0
4m0
4m1
4m)
∞

A160384 non-0 base 3 (0
3m1
3m1
3m)
∞

A160385 non-0 base 4 (0
4m1
4m1
4m1
4m)
∞

A053735 digital, base 3 (0
3m1
3m2
3m)
∞

A053737 digital, base 4 (0
4m1
4m2
4m3
4m)
∞

A034968 digital, factorial base see also A139365
A065363 digital, balanced base 3 0
(3m+1)/2(1
3m¯1
3m0
3m)
∞

A139351 1s or 3s in base 4 1s in even positions in binary (0
4m1
4m0
4m1
4m)
∞

A139352 2s or 3s in base 4 1s in odd positions in binary (0
4m0
4m1
4m1
4m)
∞

Table 1: Relevant sequences in OEIS.

Proof. Let B(r, d) = {s ∈ Z : 1 ≤ s < 2
d and ⌊s/2
r⌋ is odd}; in other words, the d bit binary
numbers with the r-th bit equal to 1. Let ¯B(r, d) = {0, 1, . . . , 2
d − 1} \ B(r, d). For example,
B(1, 3) = {2, 3, 6, 7} and B(1, 3) = {0, 1, 4, 5}.
Now consider the number n written both in binary and in base 2
d. Note that, in the
binary representation of n, the number of 1 bits in positions that are congruent to r mod d
is the same as the number of digits from the set B(r, d) in the 2
d-ary representation of n.
Thus we may apply Theorem 3 to get the generating function

∑

n≥0 C(n, r, d)zn = ∑

m≥0
 ∑

s∈B(r,d) zs2dm
∑

0≤s<2d zs2dm

Note that the numerator above can be written
∑

s∈B(r,d) zs2dm = z2r2dm ∑

s∈ ¯B(r,d) zs2dm

and the denominator as
∑

0≤s<d zs2dm = ∑

s∈B(r,d) zs2dm + ∑

s∈ ¯B(r,d) zs2dm = (1 + z2r2dm) ∑

s∈ ¯B(r,d) zs2dm.

Canceling the common sum gives the right hand side of (13).

The following corollary allows us to give a generating function for A139351 and A139352.

6

Corollary 7. The generating function for the number of 1’s in even positions in the binary
expansion of n, and the corresponding generating function for the number of 1’s in odd
positions, are given below.

1
1 − z
 ∑

m≥0
 z4m

1 + z4m , 1
1 − z
 ∑

m≥0
 z2·4m

1 + z2·4m .

5 Multi-Radix Numeration Systems

In this section we consider numbers written in the multi-radix base k0 × k1 × k2 × · · · . If
each ki = k then we get the k-ary numeration system considered in the previous section. It
will prove useful to adopt the following notation: (a) k′
j = kj − 1, (b) ¯kj = k0k1 · · · kj−1, with
the usual convention for the empty product, ¯k0 = 1. Then the column pattern is

(α¯km
0 α¯km
1 · · · α¯km
k′
m)
∞.

Theorem 8. The generating function for the digital sum of the number n written in the
multi-radix base k0 × k1 × k2 × · · · is

1
1 − z
 ∑

m≥0
 z¯km + 2z2¯km + · · · + k′
mzk′
m·¯km

1 + z¯km + z2¯km + · · · + zk′
m·¯km .

Proof. The generating function is (5) with bm = 0, αi = i, um = k′
m, and am = ¯km.

In the factorial base, kj = j +1, so that ¯kj = j!. For example, 99 = 3·4!+0·3!+2·2!+1·1!.
We now obtain a generating function for A034968 in the following corollary.

Corollary 9. The generating function for the digital sum of the number n written in the
factorial base is 1
1 − z
 ∑

m≥1
 zm! + 2z2m! + · · · + mzm·m!

1 + zm! + z2m! + · · · + zm·m! .

Proof. This follows directly from the previous theorem. Note that the numerator is zero
when m = 0, so that the summation starts at 1.

6 Final Remarks

It is also possible to approach the derivation of the generating functions used here using
“divide-and-conquer” recurrence relations. See Stephan [8] for examples of this approach in
the k = 2 case. For example the recurrence relation corresponding to the morphism (7) is
a(0) = 0 and a(km + i) = αi + a(m) for integer indices i with 0 ≤ i < k. These recurrence
relations are very useful for actually computing the sequences.
As we have shown here, ﬁnding a generating function for the sum of the digits is straight-
forward when dealing with a simple radix, or a mixed radix system where each positional

7

multiplier is a multiple of the previous one. When this does not hold, the problem is much
more diﬃcult.
The simplest example of such a system is the Zeckendorf [9] or “base Fibonacci” rep-
resentation (A014417, digital sum in A007895). Attempting the same sort of one digit at
a time approach, the low order digit is the inﬁnite Fibonacci word, A003849. Since this
sequence includes arbitrarily long repeated segments, but is not periodic, it does not have a
rational generating function.

References

[1] J.-P. Allouche and J. O. Shallit, Automatic Sequences, Cambridge University Press,
2003.

[2] J. B´esineau, Ind´ependance statistique d’ensembles li´es `a la fonctions “somme des
chiﬀres”, Acta Arith. 20 (1972), 401–416.

[3] J. Coquet and P. Toﬃn, Repr´esentations des entiers naturels et ind´ependance statis-
tique, Bull. Sci. Math., 105 (1981), 289–298.

[4] D. E. Knuth, The Art of Computer Programming, Volume 2, Seminumerical Algorithms,
3rd edition, Addison-Wesley, 1998.

[5] D. E. Knuth, The Art of Computer Programming, Volume 4, Fascicle 1: Bitwise Tricks
& Techniques and Binary Decision Diagrams, Addison-Wesley, 2009.

[6] R. L. Graham, D. E. Knuth, and O. Patashnik, Concrete Mathematics, Addison-Wesley,
second edition, 1994.

[7] N. J. A. Sloane, The On-Line Encyclopedia of Integer Sequences,
www.research.att.com/∼njas/sequences/, accessed April 2009.

[8] R. Stephan, Divide-and-conquer generating functions, part I: elementary sequences,
http://arxiv.org/abs/math/0307027, 2003.

[9] E. Zeckendorf, Repr´esentation des nombres naturels par une somme de nombres de
Fibonacci ou de nombres de Lucas, Bull. Soc. Roy. Sci. Li`ege, 41 (1972), 179–182.

2000 Mathematics Subject Classiﬁcation: Primary 05A15; Secondary 05A10.
Keywords: Generating function, numeration system, digital sum, sideways addition, digit
counting, morphism, factorial base, balanced ternary numbers.

(Concerned with sequences A000120, A003849, A007895, A014417, A023416, A034968, A053735,
A053737, A062756, A065363, A077267, A080791, A081602, A081603, A139351, A139352,
A139365, A160380, A160381, A160382, A160383, A160384, and A160385.)

8

Received June 19 2009; revised version received July 11 2009. Published in Journal of Integer
Sequences, July 12 2009.

Return to Journal of Integer Sequences home page.

9
