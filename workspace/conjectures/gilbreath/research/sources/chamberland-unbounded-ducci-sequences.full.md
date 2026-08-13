<!-- source: https://chamberland.math.grinnell.edu/papers/ducci_unbounded.pdf | converted from PDF -->

1

UNBOUNDED DUCCI SEQUENCES

Marc Chamberland

Department of Mathematics and Computer Science

Grinnell College

Grinnell, IA, 50112-0806

E-mail: chamberl@math.grin.edu

1 Introduction

A simple iterative problem attributed to E. Ducci (see [10]) asks about the

limiting behavior of ﬁnite strings. Let f : lRn → lRn be deﬁned as

f (x1, . . . , xn) = (|x1 − x2|, |x2 − x3|, . . . , |xn − x1|). (1)

Let the zero-string be a string whose terms are all zero. The following result

was ﬁrst proved by Ciamberlini and Marengoni [4] in 1937.

Theorem 1.1 Every integer string of length n will iterate to the zero-string in

a ﬁnite number steps if and only if n = 2m for some positive integer m.

Remarkably, this theorem has been restated and reproved (using various

techniques) a number of times since then; see [3], [8], [18], [19], [22], [23], [27].

Other references may be found in [17]. This process has been most commonly

referred to as a Ducci sequence or the N -number game.

Other interesting questions and observations concerning the iteration of f

have arisen. Lotan[11] showed that every 4-string with real entries iterates to the

zero-string in ﬁnitely many steps except for strings (up to shifts, reﬂection and

scaling) of the form (1, q, q2, q3) where q .
= 1.839 is a root of q3 − q2 − q − 1 =
 2

0. These exceptional strings iterate to the zero-string asymptotically. Work

towards this result was also pursued geometrically in [16]. Webb[24] showed

that 4-strings may take arbitrarily long to reach the zero-string; if one considers

the Tribonacci numbers deﬁned by

tn = tn−1 + tn−2 + tn−3, t0 = 0, t1 = 1, t2 = 1,

then 3 iterates of (tn, tn−1, tn−2, tn−3) yields 2(tn−2, tn−3, tn−4, tn−5). For strings

whose length is not a power of two, various results concerning cycle lengths,

which strings are in cycles, and the number of iterations needed to reach a cycle

can be found in [1], [5], [7], [12], [13], [14], [15]. Associated to the lengths of

cycles is the structure of Pascal’s triangle; see [2] and [9].

The map f has a weighting of (1, −1). The ﬁrst term is underlined to indicate

the relative position of the weighting when it is applied to each term. The

weighting is bounded since the maximum of any string does not increase under

iteration. This boundedness plays a signiﬁcant role in the proofs of Theorem 1.1

since, among other things, it forces the all strings to eventually enter a cycle.

This paper is principally concerned with unbounded weightings.

Section 2 yields a general result concerning weightings that admit strings

which iterate to the zero-string. Sections 3 and 4 consider the unbounded

weighting (−1, 2, −1), explicitly

f (x1, . . . , xn) = (|2x1 − x2 − xn|, |2x2 − x3 − x1|, . . . , |2xn − x1 − xn−1|). (2)

Speciﬁcally, Section 3 focuses on results akin to Theorem 1.1 for this new

weighting, while Section 4 gives an intricate description of the dynamics of

3-strings. Connections are made to circulant matrices, Fibonacci numbers, and

circle maps.

2 Other weightings

Let the sum of a weighting be the absolute value of the sum of the terms in that

weighting. The next result shows the relevance of the sum.
 3

Theorem 2.1 Let W be a weighting with sum s. For every string length, there

exists a non-zero string which iterates under W to the zero-string if and only if

s = 0.

Proof: Denote the weighting W by (x1, x2, . . . , xk). A string of length n, with

n > k, will to iterate to the zero-string if and only if the n × n circulant matrix

 x1 x2 x3 . . . xk 0 . . . 0

0 x1 x2 . . . xk−1 xk . . .
. . .

x2 x3 . . . x1
 

has a determinant of zero. Note that the position of the underline in the weight-

ing does not change the determinant condition since rows in the circulant matrix

may be permuted; this eﬀectively changes the position of the underline. The

determinant condition occurs if and only if

x1 + x2ω + x3ω2 + . . . + xnωn−1 = 0 (3)

where ω is an nth root of unity; see Weisstein[25] for the basics of circulant

matrices. If s = 0, letting ω = 1 satisﬁes this condition for any n ≥ k. If s ̸= 0,

let n, n > k, be any prime. Since n is prime, ωn − 1 = 0 is the lowest degree

equation the algebraic number ω can satisfy unless ω = 1. However, ω = 1 does

not satisfy Equation (3) if s ̸= 0. ✷

More can be said with regards to s. A one-string – a string with all ones –

iterates to itself times a factor of s. If s = 0, the one-string iterates immediately

to the zero-string. If s = 1, the one-string is ﬁxed. Lastly, if s ≥ 2, the one-string

diverges.

There are many integer weightings besides (1

, −1) which are bounded. Any

integer weighting whose terms are restricted to -1, 0, or 1, and where there are

never more than 3 consecutive non-zero terms, will be bounded. If zeros are not

allowed in the weighting though, only (1, −1) is bounded.

It would be interesting to enrich the dynamics beyond what is seen for (1, −1)

so that both unboundedness and terms iterating to the zero-string are present.
 4

Theorem 2.1 implies a weighting with at least three terms must be considered.

The weighting (−1, 2, −1) is both unbounded and has s = 0, so this is studied

in the following 2 sections.

3 General Limiting Behavior for (−1, 2, −1)

The ﬁrst result proves the negative counterpart of Theorem 1.1.

Theorem 3.1 For any integer n ̸= 2m, there are n-strings which do not iterate

to the zero-string.

Proof: The proof is similar in spirit to that found in [3]. Suppose ﬁrst that

the string has odd length. After factoring out all twos, consider its entries mod

2, so that at least one term equals one. The table below shows how the middle

term of a substring of three numbers mod 2 iterates:

3-string (mod 2) iterate of middle term (mod 2)

0 0 0 0

0 0 1 1

0 1 0 0

1 0 0 1

1 0 1 0

1 1 0 1

0 1 1 1

1 1 1 0

The only non-trivial predecessor of the zero-string is the one-string mod 2.

Using the table, one may show that any predecessor must contain the substring

0011 repeated ﬁnitely many times, hence the string length must be a multiple

of 4, a contradiction. Therefore, there exist strings of any odd length which do

not iterate to the zero-string.
 5

If the string length is n and p|n for some odd prime p, construct a new string

by concatenating n/p copies of a string of length p which does not iterate to the

zero-string. This new string will also not iterate to the zero-string. ✷

It remains now to consider only those strings whose string length is a power

of two. Unfortunately, Theorem 1.1 for the (−1, 2, −1) weighting is false: after

24 iterations, the 8-string
 (1, 2, 3, 0, 1, 0, 1, 2)

maps to
 28(1, 2, 3, 0, 1, 0, 1, 2),

so this string diverges. After 240 iterations, the 16-string

(2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1)

maps to
 240(2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1),

so this string also diverges. It is curious to note that though the terms in these

strings are small, the strings still diverge. Surprisingly, we will show that, in

spite of these counter-examples to our desired result, every 4-strings converges

to the zero-string. For this we will need the following lemma.

Lemma 3.1 Let a, b, c, d be integers. Any string of the form (0, b, d, d), (0, 0, c, d),

(a, 0, c, 2a), (a, a, c, c), or (a, b, a, b) iterates to the zero-string.

The proof is simple and left to the reader.

Theorem 3.2 All integer 4-strings iterate to the zero-string.

This theorem was ﬁrst proved by Robb[20]; the proof below is a streamlined

version of his approach.

Proof: The idea behind the proof is straightforward. We show that the

maximum of any 4-string no more than doubles after two iterations. Since after

two iterations one may always divide out a factor of two, the factored maximum
 6

(0, 0, 0, 1) (0, 0, 1, 1)(0, 1, 1, 1)

(1, 0, 1, 0)
 (0, 0, 0, 0)
 (1, 1, 1, 1)

Figure 1: Iterates of a 4-string mod 2

never increases. Lastly we dispose of the cases where the factored maximum

does not decrease.

The fact that a two may be factored out after two iterations is simple. Figure

1 shows how 4-strings iterate mod 2. Note that all possible 4-strings mod 2 are

represented in the ﬁgure if one allows for shifts.

Having outlined the proof, many messy details emerge. There is no obvious

way to generalize the approaches used in proving Theorem 1.1, so this proof

breaks down into many subcases. Essential details are recorded in tables.

After one iteration of any string, all the entries become non-negative, so let

us assume this is the case to begin with. There are two general cases to consider.

Starting with the string (a, b, c, d), we ﬁrst consider a to be the minimum value

of the string and d the maximum. The following table summarizes the dynamics

after two iterations. In all four subcases, the corresponding inequalities may be

used to show that after two iterations the maximum never exceeds 2d. The

third column records those initial strings where after two iterations one obtains

2d as a maximum, a “borderline situation”.
 7

case string after 2 iterates borderline situations

2b − a − c ≥ 0 (b + d − 2a, |2b − a − c|, (0, b, d, d)

2c − b − d ≥ 0 |2c − b − d|, 2d − a − c) (0,0,0,d)

2b − a − c ≥ 0 (2c − 2a, 2d − 2b, (a, b, a, b)

2c − b − d ≤ 0 2c − 2a, 2d − 2b)

2b − a − c ≤ 0 (4b − 4a, 4b − 4a, (a, a, c, c)

2c − b − d ≥ 0 4d − 4c, 4d − 4c)

2b − a − c ≤ 0 (4b − 4a, |4a − 6b + 4c − 2d|, (0, 0, c, d)

2c − b − d ≤ 0 |4b − 4c|, 2d − 2b)

All the borderline cases are settled wth Lemma 3.1.

The other general case has b as the minimum and d as the maximum. The

following table illustrates the dynamics.

case string after 2 iterates borderline situations

and reductions

2a − b − d ≥ 0 (4d − 4a, 2d − 2b, (a, 0, c, 2a)

2c − b − d ≥ 0 4d − 4c, |6d − 4a − 4c + 2b|) (a, 0, c, 2c)

(a, 0, a, a)

b = 0, maximum in term 2

2a − b − d ≥ 0 (4d − 4a, 4c − 4b, (a, b, b, a)

2c − b − d ≤ 0 4c − 4b, 4d − 4a)

2a − b − d ≤ 0 (4a − 4b, 4a − 4b, (a, a, c, c)

2c − b − d ≥ 0 4d − 4c, 4d − 4c)

2a − b − d ≤ 0 (4a − 4b, |4a + 4c − 6b − 2d|, (a, 0, c, 2a)

2c − b − d ≤ 0 4c − 4b, 2d − 2b) (a, 0, c, 2c)

(a, 0, a, a)

b = 0, maximum in term 4

As in the ﬁrst table, all the subcases may be disposed of, with exceptions

where one has “b = 0, maximum in term 2 or 4”. To handle these exceptions,
 8

note that the only way such strings will not have a maximum which decreases

is to perpetually fall into these exceptions. In the “term 4” subcase, this forces

the second term to be zero, hence using b = 0 implies d = 2a + 2c. This implies

that after two iterations the original string (a, b, c, d) becomes (4a, 0, 4c, 4a+4c),

so a four may be factored out, and the factored maximum has decreased. The

case with “term 2” may be handled similarly. ✷

In attempting to duplicate Lotan’s earlier-mentioned result (see [11]) for

(−1, 2, −1) weighting, another surprise occurs. The real 4-string
(
1, 1 + √5
2 , 2 + √5, 1 + √5
2
 )

maps to
 (√5 − 1)
 (

1, 1 + √5
2 , 2 + √5, 1 + √
5
2
 )
 ,

so this string is divergent. This is stupefying in light of Theorem 3.2. That

theorem implies that any rational 4-string iterates to the zero-string, but now

a string with the simplest kind of irrational entries diverges. These results

highlight the fact that studying the dynamics of this map on lR4 does not give

full insight into what may occur on a subspace, even if that subspace is dense.

Moreover, the appearance of the golden ratio suggests certain strings with Fi-

bonacci numbers are invariant. Letting Fn denote the nth Fibonacci number, it

is easy to show that the string (Fn, Fn+1, Fn+3, Fn+1) maps to 2 (Fn−1, Fn, Fn+2, Fn).

Like the result of Webb[24] for the weighting (1, −1), 4-strings may take arbitrar-

ily long to reach the zero-string. Note that for suﬃciently large n the maximum

term increases since two exceeds the golden ratio. We then have that the string’s

(unfactored) maximum will grow in size almost until its last iteration before it

collapses to the zero-string.

4 Strings of Length 3

Since the weighting (−1, 2, −1) is unbounded, it is unclear whether a given string

will eventually diverge, cycle, or iterate to the zero-string. For example, a few
 9

iterates show that

(5, 1, 4) → (5, 7, 2) → (1, 7, 8) → (13, 5, 8) → (13, 11, 2)

→ (13, 7, 20) → (1, 19, 20) → (37, 17, 20) → (37, 23, 14) → (37, 5, 32) → . . .

This section studies this question for strings of length three. The ﬁrst result

shows the possibilities.

Theorem 4.1

1. Any integer 3-string maps to (a, b, a+b) (or a shifted version thereof ) after

one iteration.

2. The iterate of any string (a, b, a + b) where a, b ∈ ZZ+ and gcd(a, b) = 1,

may only have 3 as a common factor.

3. Any integer 3-string either diverges or iterates to a ﬁxed point (x, x, 2x)

(or shifted version theoreof ).

Proof: Part (1) is trivial and left to the reader. For Part (2), note that

(a, b, a + b) maps to (2b − a, |2a − b|, a + b). If this string has a common factor

of k, then 2b − a ≡ 0 mod k and 2a − b ≡ 0 mod k. Adding these implies

3a ≡ 0 mod k and 3b ≡ 0 mod k, giving the desired result.

To prove Part (3), the key is to observe that the middle term (middle in

size, not position) is non-decreasing under iteration. Without loss of generality,

let b ≥ a so b is the middle term of (a, b, a + b). Since this string maps to

(2b − a, |2a − b|, a + b), and 2b − a ≥ b and a + b ≥ b, the middle is non-

decreasing and remains unchanged if and only a = b. This completes the proof.

✷
 Part (2) of Theorem 4.1 is helpful for computations; one need only look

for threes to factor out. The more challenging question now is: How can we

determine whether a string will diverge or not? The next result provides the

basis for an answer.
 10

Theorem 4.2 Let a, b ∈ ZZ
+ with gcd(a, b) = 1 and a ≤ b. Then if a ̸≡ 1 mod 3

or b ̸≡ 2 mod 3, the string (a, b, a + b) diverges.

Proof: Scale the string (a, b, a + b) so that it is of the form (m, 1, 1 + m),

where m ∈ [0, 1]. The ratio of the smallest term to the middle term is m. If

m ∈ [0, 1/2], this string iterates to (2 − m, 1 − 2m, m + 1), so the ratio of the

smallest term to the middle term is 1−2m
m+1 . If m ∈ [1/2, 1], this string iterates to

(2 − m, 2m − 1, m + 1) and the ratio of the smallest term to the middle term is

2m−1
2−m . In summary, the ratio of the smallest term to the middle term iterates

via the map ¯f : [0, 1] → [0, 1] deﬁned by

¯f(x) =
  (1 − 2x)/(1 + x), x ∈ [0, 1/2]

(2x − 1)/(2 − x), x ∈ (1/2, 1].

By part (3) of Theorem 4.1, the string (a, b, a + b) will diverge if and only a/b

does not iterate to x = 1 under ¯f in ﬁnitely many steps. The ¯f -predecessors of

any x ∈ [0, 1] are 1 − x

x + 2 and 1 + 2x
x + 2 .

If
 x = a
b , a, b ∈ ZZ+, a ≡ 1 mod 3, b ≡ 2 mod 3

this forces the numerator and denominator of the predecessors to have the same

form. Since ¯f −1(1) = 0 or 1 and ¯f −1(0) = 1/2, we have ¯f (k)(x) = 1 for some

k ∈ ZZ+ only if x = 0, x = 1, or

x = a
b , a, b ∈ ZZ+, a ≡ 1 mod 3, b ≡ 2 mod 3,
 ✷

Theorem 4.2 implicitly gives the algorithm one may use to determine if a

3-string will diverge or not. After dividing out any factors of 3 from an integer

string, if either a ̸≡ 1 mod 3 or b ̸≡ 2 mod 3, the string will diverge. Otherwise,

iterate the string and repeat the same steps.

Since ¯f is a 2:1 function on [0, 1]\{1/2}, the complete predecessor set of x = 1

is countable. If we consider strings with real entries, this implies that almost
 11

1
 1/2 1
 1
 1/2 1

y
 x
 y
 y=g(x)
 x

y=f(x)

Figure 2: The maps y = ¯f(x) and y = g(x).

every 3-string will diverge, and if a/b is irrational, the 3-string will diverge.

One may say more about this predecessor set of x = 1. Since | ¯f ′(x)| > 1 on

[0, 1] \ {1/2}, ¯f is an expanding circle map. By an important theorem due to M.

Shub (see [6] or [21]), the function ¯f is topologically conjugate via a nonsmooth

homeomorphism h to the piecewise linear map g(x) = |1 − 2x|; see Figure 2.

The conjugacy h satisﬁes h(1) = 1. The predecessor set of the ﬁxed point x = 1

under the map g is the dense set
{ k
2n : 0 ≤ k ≤ 2n, n = 0, 1, 2, . . .
}

This implies the predecessor set for the ﬁxed point x = 1 under the map f is

also dense on [0, 1]. Therefore, though an arbitrary 3-string will almost always

diverge, it is arbitrarily close to one which iterates to a ﬁxed point.

5 Conclusion

The previous sections have demonstrated how rich the dynamics of unbounded

Ducci sequences can be with the (−1, 2, −1) weighting. Many questions re-

mained to be addressed:

Question 1: What are the dynamics of bounded integer weightings

besides (1, −1) ?

Some examples here are obvious, such as (1, 0 − 1) on any 2n-string; the
 12

dynamics are the same as considering two n-strings with the (1, −1). However,

the dynamics of the weighting (1, 0, 0, −1) on 8-strings is far from clear.

Question 2: Are there unbounded integer weightings with a sum of

zero which have no non-zero cycles?

A candidate for such a weighting is (−1, 3, 2). Numerical evidence suggests

that all 4-strings iterate eventually either to the zero-string or to some multiple

of (5, 1, 1, 7), which diverges.

Question 3: What are the dynamics of weightings with rational terms?

real terms?

Acknowledgement: I would like to thank Grinnell College for ﬁnancially sup-

porting three undergraduate students to assist my investigations during suc-

cessive summers: Oleksiy Andriychenko (1999), Dolph Robb (2000) and John

Wray (2001). I would especially like to thank D.G. Rogers for alerting me to

the richness of work done on the original Ducci problem.

ReferencesK. Boklan. The n-Number Game. Fibonacci Quarterly, 22

:152–155, (1984).

[2] F. Breuer. A Note on a Paper by Glaser and Sch¨oﬄ. Fibonacci Quarterly,

36(5):463–466, (1998).

[3] O. Andriychenko and M. Chamberland. Iterated Strings and Cellular Automata.

Mathematical Intelligencer, 22(4):33–36, (2000).

[4] C. Ciamberlini and A. Marengoni. Su una interessante curiosit`a numerica. Peri-

odiche di Matematiche, 17:25–30, (1937).

[5] J. Creely. The Length of a Three-Number Game. Fibonacci Quarterly, 26:141–143,

(1988).

[6] W. de Melo and S. van Strien. One-Dimensional Dynamics. Springer, 1993.

[7] A. Ehrlich. Periods in Ducci’s n-Number Game of Diﬀerences. Fibonacci Quarterly,

28:302–305, (1990).

[8] B. Freedman. The Four Number Game. Scripta Math., 14:35–47, (1948).
 13

[9] H. Glaser and G. Sch¨oﬄ. Ducci-Sequences and Pascal’s Triangle. Fibonacci Quar-

terly, 33:313–324, (1995).

[10] R. Honsberger. Ingenuity in Mathematics. Yale University, (1970).

[11] M. Lotan. A Problem in Diﬀerence Sets. American Mathematical Monthly,

56:535–541, (1949).

[12] A. Ludington. Length of the 7-Number Game. Fibonacci Quarterly, 26:195–204,

(1988).

[13] A. Ludington-Young. Length of the n-Number Game. Fibonacci Quarterly,

28:259–265, (1990).

[14] A. Ludington-Young. Ducci-Processes of 5-tuples. Fibonacci Quarterly, 36(5):419–

434, (1998).

[15] A. Ludington-Young. Even Ducci-Sequences. Fibonacci Quarterly, 37(2):145–153,

(1999).

[16] K.R. McLean. Playing Diﬀy with real sequences. Mathematical Gazette, 83:58–68,

(1999).

[17] L.F. Meyers. Ducci’s Four-Number Problem: A Short Bibliography. Crux Mathe-

maticorum, 8:262–266, (1982).

[18] R. Miller. A Game with n Numbers. American Mathematical Monthly, 85:183–

185, (1978).

[19] F. Pompili. Evolution of ﬁnite sequences of integers . . . . Mathematical Gazette,

80:322–332, (1996).

[20] D. Robb. An Iterative Process Extension. Report for Grinnell College MAP

Program, 2000.

[21] M. Shub. Endomorphisms of compact diﬀerentiable manifolds. American Journal

of Mathematics, 91:175–199, (1969).

[22] I.R. Sprague. Recreation in Mathematics. Dover, (1963).

[23] B. Thwaites. Two Conjectures or how to win £1100. Mathematical Gazette,

80:35–36, (1996).

[24] W. Webb. The Length of the Four-Number Gane. Fibonacci Quarterly, 20:33–35,

(1982).
 14

[25] E.W. Weisstein. CRC Concise Encyclopedia of Mathematics. Chapman and

Hall/CRC, 1999.

[26] F.-B. Wong. Ducci Processes. Fibonacci Quarterly, 20:97–105, (1982).

[27] P. Zvengrowski. Iterated Absolute Diﬀerences. Mathematics Magazine, 52(1):36–

37, (1979).
