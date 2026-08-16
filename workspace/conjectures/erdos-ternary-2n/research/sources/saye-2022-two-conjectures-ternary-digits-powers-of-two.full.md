<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL25/Saye/saye3.pdf | converted from PDF -->

23 11 Article 22.3.4
Journal of Integer Sequences, Vol. 25 (2022),2
 3

6

1

47
 On Two Conjectures Concerning the
Ternary Digits of Powers of Two

Robert I. Saye
Lawrence Berkeley National Laboratory
Berkeley, CA 94720
USA
rsaye@lbl.gov

Abstract

Erd˝os conjectured that 1, 4, and 256 are the only powers of two whose ternary
representations consist solely of 0s and 1s. Sloane conjectured that, except for
{20, 21, 22, 23, 24, 215}, every other power of two has at least one 0 in its ternary represen-
tation. In this paper, numerical results are given in strong support of these conjectures.
In particular, we verify both conjectures for all 2n with n ≤ 2 · 345 ≈ 5.9 × 1021. Our
approach makes use of a simple recursive construction of numbers 2n having prescribed
patterns in their trailing ternary digits.

1 Introduction

Circa 1978, Erd˝os [2] conjectured that the only powers of two which do not have a 2 anywhere
in their ternary representation are the numbers 20, 22, and 28. Gupta [3] veriﬁed this to
be the case for every 2n with n ≤ 4373. Extending this bound, a numerical study of Vardi
[6] conﬁrmed no counterexamples exist for n ≤ 2 · 320 ≈ 7 × 109. The conjecture remains
open; see the additional references and analysis of Lagarias [4]; see also Dimitrov & Howe [1]
who study a closely related question and prove that the only powers of two whose ternary
representation contains no 2 and at most twenty-ﬁve 1s are the aforementioned numbers, 2
0,
2
2, and 2
8.
Similar in spirit, Sloane [5] conjectured that, except for the numbers {2
0, 2
1, 2
2, 2
3, 2
4, 2
15},
every other power of two contains a 0 somewhere in its ternary representation. Along the
same lines, one may conjecture that, for all but ﬁnite number of cases, every power of two

1

contains a 1 somewhere in its ternary representation—however, it is straightforward to show
this is essentially equivalent to the conjecture of Erd˝os (the exceptional cases being replaced
by 21, 23, and 2
9).
One may summarize all three conjectures to say that, except for a handful of small,
easily predictable cases, every power of two has every possible digit somewhere in its ternary
representation. Heuristically, we anticipate this to be the case because the ternary digits of
powers of two are expected to be essentially random, implying that the chances of omitting a
particular digit becomes vanishingly small as the overall digit count increases. However, this
is far from a proof; indeed, the conjectures represent examples of exponential Diophantine
equations for which few methods of attack have been found [1, 4].
In this note, numerical results are given in strong support of these conjectures. In
particular, we signiﬁcantly extend prior veriﬁcation bounds and conﬁrm that the ternary
representation of 2
n contains every possible ternary digit, for all 16 ≤ n ≤ 2 · 3
45 ≈ 5.9 × 10
21.
Our approach focuses on examining the trailing ternary digits of 2
n, which can be eﬃciently
calculated even for massive exponents. In particular, we develop a recursive algorithm to
construct numbers 2
n having prescribed patterns in their trailing ternary digits. For example,
to ﬁnd a potential counterexample to Erd˝os’s conjecture, one may directly enumerate in
increasing order the numbers 2
n whose trailing digits are some combination of 0s and 1s. We
note the recursive algorithm shares some aspects with the sieving method of Gupta [3].
As part of our analysis, we also compute the smallest power of two which has no 0 in
the last k digits of its ternary expansion, for k = 1, 2, . . . (and similarly for trailing digits
excluding 1 and 2). The results agree very well with what one may expect supposing that
the ternary digits of 2n are essentially rolls of a three-sided die.

2 Notation

It is convenient to deﬁne a shorthand notation for the purposes of examining the trailing
ternary digits of a number: for integers a, b and k a positive integer, a ≡k b means a ≡ b
(mod 3k). In addition, dk(a) is deﬁned as the kth ternary digit of a, with d1(a) being the
least signiﬁcant digit: more precisely, if a = ∑n
i=0 ai3i is the ternary representation of a,
then dk(a) := ak−1. As a ﬁnal piece of notation, (· · · )3 indicates the digits in the ternary
expansion of a number, e.g., 28 = (100111)3.

3 Method

A simple recursive construction of numbers 2n, having prescribed patterns in their trailing
ternary digits, is made possible via the results of the following lemma; its proof is elementary,
and shares some aspects with the method of Gupta [3]. A self-contained proof of the lemma
is deferred to Section 5 so as to simplify the presentation.

2

Lemma 1. For a positive integer k, deﬁne1 uk := 2 · 3
k−1. Then

(i) uk is the smallest positive integer such that 2
uk ≡k 1;

(ii) if i, j ∈ N and 2
i ≡k 2
j, then i and j diﬀer by a multiple of uk;

(iii) if i, j ∈ N, the (k + 1)st ternary digit of 2
iuk+j is related to that of 2
j via

dk+1(2
iuk+j) ≡ dk+1(2j) + i · d1(2
j) (mod 3).

We demonstrate the recursive construction process by means of a generic ﬁve-digit example.
(There is nothing special about the digit count of ﬁve.) Suppose we have constructed a
positive integer j < u5 such that the last ﬁve ternary digits of 2j is abcde, for some ﬁxed
a, . . . , d ∈ {0, 1, 2} and e ∈ {1, 2}. Then, for i ∈ {0, 1, 2}, we claim the numbers ji := iu5 + j
are such that 2ji are the smallest possible powers of two whose last six ternary digits are
0abcde, 1abcde, and 2abcde. (The order of these six-digit combinations, as i iterates from 0
to 2, depends on e.) To see why, note that:

• Applying part (i) of the lemma with k = 5, observe that 2
ji = (2
u5)
i2
j ≡5 2
j, and so the
last ﬁve digits are preserved.

• For i held ﬁxed, suppose that ℓ is a positive integer such that ℓ < ji and 2ℓ matches the
last six digits of 2ji. Then, by part (ii) of the lemma, ji − ℓ is a positive multiple of u6,
but this is impossible because ji = iu5 + j < 2u5 + u5 = u6. Therefore, no such ℓ exists
and consequently 2
ji is the smallest possible power of two whose trailing six digits match
those of 2
ji.

• Last, by part (iii), the sixth ternary digit of 2
ji is equal (modulo 3) to the sixth digit of 2
j

plus 0, 1, or 2 multiples of the last digit of 2
j. The latter digit is either 1 or −1 (modulo
3), which means that, irrespective of what the sixth digit of 2
j is, we shall always obtain
some arrangement of 0abcde, 1abcde, and 2abcde for the last six digits of 2
ji, as i iterates
over {0, 1, 2}.

In general, we observe that adding multiples of uk to a number j < uk allow us to explicitly
construct powers of two whose last k digits match those of 2j and whose (k + 1)st digit
is controlled; moreover, the recursive approach builds powers of two in the smallest order
possible. As an example application, we may then use this approach to test the conjecture
of Erd˝os, by starting with 20 (whose least signiﬁcant digit is 1), then generate the smallest
powers of two whose trailing two digits are 01 and 11, then generate the smallest powers of
two whose trailing three digits are 001, 101, 011, and 111, etc. If any of these powers of two
end up containing solely 0s and 1s in their ternary representation, then a counterexample
to the conjecture has been discovered (provided it is not one of the trivial cases, of course);
moreover, any such counterexample must be constructable by this process.

1In fact, uk = ϕ(3
k), where ϕ is the Euler totient function; Euler’s theorem implies that a
uk ≡ 1 (mod 3
k)
for any positive integer a coprime to 3.
 3

Algorithm 1 Gχ(k, uk, 2uk , j, 2j).

1: Determine the ﬁrst occurrence of digit χ in 2j.
2: if digit χ not found and j > 16 then
3: output j (nontrivial counterexample found)
4: if dk(2j) = χ then
5: return
6: if k ≥ K then
7: return
8: Compute 2
uk+1 = (2
uk )3.
9: Execute Gχ(k + 1, 3uk, 2
uk+1, j, 2j).
10: Execute Gχ(k + 1, 3uk, 2
uk+1, j + uk, 2j · 2uk ).
11: Execute Gχ(k + 1, 3uk, 2
uk+1, j + 2uk, 2
j · (2uk )2).

Figure 1: Recursive generation of powers of two whose trailing k ternary digits are required
to satisfy particular conditions.

An algorithm implementing this strategy is given in algorithm 1. The input is k, the number
of so-far-constructed trailing digits, the unit uk deﬁned by lemma 1 and its corresponding
power of two, along with an integer j and its corresponding power of two. The parameter
χ speciﬁes the digit controlling the recursive construction: if χ = 2 (resp., χ = 0), then
algorithm 1 generates powers of two whose trailing k digits contain only 0s and 1s (resp.,
only 1s and 2s), thereby examining the conjecture of Erd˝os (resp., Sloane). In particular, for
χ = 2, the recursion is initiated with the ﬁrst power of two having k = 1 valid digits, i.e.,
G2(k = 1, uk = 2, 2uk = 4, j = 0, 2j = 1). Meanwhile, for χ = 0, the recursion is initiated
via two base cases, G0(k = 1, uk = 2, 2uk = 4, j = 0, 2j = 1) and G0(k = 1, uk = 2, 2uk =
4, j = 1, 2j = 2). By construction, the recursive algorithm is depth-ﬁrst, with a maximum
depth controlled by the user-deﬁned parameter K. A straightforward calculation shows that
the total number of powers of two constructed by the recursive algorithm is Θ(2K), and
that every such power is less than 2uK . On the other hand, the total number of powers of
two less than 2uK is Θ(3K). In that sense, and in the context of testing the conjectures,
the recursive approach exponentially reduces the search space versus the more elementary
method of simply testing every power of two in increasing order.
Our implementation of algorithm 1 includes the following aspects, mainly targeting its
eﬃcient execution:

• Except for line 1, all powers of two are computed in the cyclic group modulo 3
κ for a ﬁxed
κ. In particular, we have used a tailor-made, ﬁxed precision integer type representing
a κ = 54 digit ternary number. It is implemented as a three-digit number in base 318,
with each such digit represented by a conventional 64-bit unsigned integer (uint64_t in
C++). This approach is particularly fast at computing the cubes and multiplications in
algorithm 1.

• On line 1, we ﬁrst query for the occurrence of digit χ in the ﬁxed-precision 54-ternary digit

4

number representing 2
j. (Here, the “ﬁrst occurrence” essentially means min{i : di(j) = χ}.)
Although suﬃciently rare, it can happen that no such digit occurs in these 54 digits,
in which case we switch over to an alternative algorithm. The alternative algorithm
computes 2j (via exponentiation-by-squaring) in the cycling group modulo 3ℓ (using a
similar ternary digit implementation as above), in progressively increasing lengths ℓ, until
χ is found. In essence, this method tries to compute as few of the trailing digits of 2
j as
possible in order to ﬁnd the digit χ; owing to the nature of the distribution of ternary
digits of powers of two, it is usually the case that not many additional digits are required.
(We note that a nontrivial counterexample to the conjectures would require ℓ to reach
the full digit length of the ternary representation of 2
j, however this circumstance never
occurred in our computational study.)

4 Results

Running on a modest 64-core compute server for a few days, the computational study in
this work applied a maximum recursion depth of K = 46. This corresponds to testing the
conjectures of Erd˝os and Sloane against all powers 2
n such that n ≤ u46 = 2·3
46−1 ≈ 5.9×10
21.
No counterexamples were found.
As part of this study, trailing digit count “record breakers” were tracked. Speciﬁcally, for
χ ∈ {0, 1, 2}, we deﬁne ρχ : N → N such that

ρχ(k) = min{n ∈ N : 2
n ≥ 3
k−1 and χ occurs nowhere in the last k ternary digits of 2
n}.

(In particular, the powers of two must have at least k ternary digits, i.e., 2
n ≥ 3
k−1.) As an
example, ρ2(100) = 710982592620911336; the last 110 ternary digits of 2710982592620911336 are
(
0102020002100100100110011100110101011111010101010110010
←↩
1000111001000101110010101011111010001110110001110111011)

3.

As another example, ρ0(100) = 388128961376647359; the last 110 digits of 2388128961376647359

are (
2021120020121121111112111222212121111112222122221212212
←↩
1122111112221212212211111121221222222111222122221212122)

3.

It is straightforward to show that ρ1(k) = ρ2(k) + 1 for all k. This is because 2n ends in
a sequence of 0s and 2s if and only if 2n−1 ends in a sequence of 0s and 1s; moreover, the
maximal number of trailing non-1 digits (for the former) and non-2 digits (for the latter) are
exactly the same. As a result, we only consider ρ0 and ρ2 in the following analysis.
Fig. 2 plots ρ0 and ρ2 as a function of k. We observe that ρχ(k) grows approximately
exponentially with k. The longer horizontal steps correspond to the record breakers which
have, roughly speaking, an uncharacteristic number of trailing non-χ digits. One notable

5

Figure 2: Plots of ρ0 (resp., ρ2), deﬁned as the smallest integer n such that the digit 0 (resp.,
2) occurs nowhere in the last k ternary digits of 2
n. The arrow points to the instance where
ρ2(k) = 201015414581294 for all 82 ≤ k ≤ 98.

Figure 3: Length of the ternary representation of 2ρχ (being approximately ρχ log3 2) as a
fraction of the expected number of rolls of three-sided die required to generate an uninterrupted
sequence of k non-χ digits (that average roll count being 3( 3
2)k − 3).

example is n = 201015414581294, which corresponds to the smallest power of two having
82 trailing non-2 digits; this same example has, in fact, 98 trailing non-2 digits. On the
other hand, the total number of ternary digits of this power of two is about 1.3 × 1014, far
exceeding this 98 digit count.
An alternative analysis comes from the heuristic that the ternary digits of powers of two
are essentially random. Imagining the digits of 2n, reading from right-to-left, are a random
number generator implementing the rolls of a three-sided die, we may ask how many rolls
are necessary to generate an uninterrupted sequence of k non-χ digits. Each non-χ digit
has a probability of 2
3, and a routine calculation shows that we need, on average, 3( 3
2)
k − 3
total rolls to generate such a sequence. Of course, this is only an approximation given that
the digits of powers of two are entirely deterministic; in particular, the ﬁrst and last digit
of 2n is never a 0, so this heuristic analysis could be slightly improved. Nevertheless, the
expected roll count serves as an estimate of what the total ternary digit length is expected to

6

be. Corresponding to the record breakers, Fig. 3 plots the ternary digit length of 2n (being
approximately n log3 2) as a fraction of the expected roll count. We observe that, within zero
to four of orders of magnitude, the digit counts of record breakers roughly match the expected
roll count. The example of n = 201015414581294, mentioned in the previous paragraph, is
uncharacteristic in the sense that for k = 98, we expect to require about 5.4 × 1017 rolls,
yet 2201015414581294 has only 1.3 × 1014 ternary digits. Nevertheless, we observe in Fig. 3 that
there is no reasonable indication of ﬁnding any counterexamples to the conjectures: even the
outlier record breakers are nowhere close to having the entire string of digits devoid of χ.

5 Proof of Lemma 1

We begin with a few elementary observations:

(a) Suppose the last k ≥ 2 ternary digits of an integer x are (a[0]
k−21)3 with a ∈ {0, 1, 2}.
(Here and in the following, the notation [ · ]ℓ means ℓ copies of the indicated digit.)
Then, for some exponent i ∈ N, we have that xi ≡ (a·3
k−1 +1)
i ≡ ai·3
k−1 +1 (mod 3
k),
as shown by a simple application of the binomial theorem.

(b) For a positive integer k, the last k + 1 ternary digits of 2uk are (1[0]k−11)3. A simple
inductive proof is as follows. Suppose the result holds for some k ≥ 2 (the base cases
with k ∈ {1, 2} are trivial to verify). Then 2
uk − 1 = (3x + 1)3
k for some non-negative
integer x, and so

2
uk+1 = (2
uk)3 = ((2
uk − 1) + 1)3 = (2
uk − 1)
3 + 3(2uk − 1)
2 + 3(2uk − 1) + 1

≡ 3
k+1 + 1 (mod 3
k+2),

as required.

Applying these observations, the proof of Lemma 1 is as follows.

(i) For k ≥ 2, assume by induction that uk−1 is the smallest positive integer j such that
2j ≡k−1 1, and let ℓ be the smallest positive integer such that 2ℓ ≡k 1. This number
clearly satisﬁes 2ℓ ≡k−1 1, and so if ℓ = auk−1 + b with a, b ∈ N and 0 ≤ b < uk−1,
we see that (2uk−1)a2b ≡k−1 1. This linear congruence problem has a unique solution,
namely 2b ≡k−1 1, which by the inductive hypothesis implies b = 0, and so ℓ is a
multiple of uk−1. By observation (b) above, ℓ cannot equal uk−1 because the kth digit of
2
uk−1 is 1. Further, ℓ cannot equal 2uk−1 because the square of 2
uk−1 has kth digit equal
to 2. The next multiple of uk−1 satisﬁes all requirements, and so ℓ = 3uk−1 = uk, as
claimed. (Note: the base cases of the inductive argument trivially hold by elementary
computation.)

(ii) Suppose i, j ∈ N are such that 2i ≡k 2j. Without loss of generality, suppose i < j.
Then 2i2j−i = 2j yields a linear congruence (2i mod 3k)(2j−i mod 3k) ≡ 2j (mod 3k).
Since the gcd of (2
i mod 3
k) and 3
k is unity, there is exactly one solution to the linear

7

congruence, namely 2j−i ≡k 1. Now suppose j − i = auk + b with a, b ∈ N and
0 ≤ b < uk; since 2j−i = (2uk)a2b ≡k 1 and 2uk ≡k 1, again by uniqueness of the linear
congruence problem, we ﬁnd that 2b ≡k 1. Part (i) then implies b = 0, and so i and j
diﬀer by a multiple of uk, as claimed.

(iii) Suppose i, j ∈ N. Note that 2iuk+j ≡k+1 (2uk mod 3k+1)i2j (mod 3k+1). By observa-
tions (a) and (b), the trailing k +1 ternary digits of the ﬁrst term are ([i mod 3][0]
k−11
)

3.
It is then a straightforward application of long multiplication to show that, modulo
three, the (k + 1)
st digit of 2
iuk+j is equal to the sum of the (k + 1)
st digit of 2
j plus i
times the ﬁrst digit of 2
j, as claimed.

6 Conclusions

By way of a recursive algorithm and extensive computation, we studied here the two con-
jectures of Erd˝os and Sloane. These conjectures essentially state that, except for small
number of trivial cases, every power of two has all possible digits somewhere in its ternary
representation. The recursive algorithm explicitly constructs powers of two such that their
trailing digits satisfy a certain requirement, e.g., consist solely of 0s and 1s. Testing these
conjectures against all powers 2n with n ≤ 2 · 345 ≈ 5.9 × 1021, no counterexamples were
found. This extends an earlier study by Vardi [6] which considered n ≤ 2 · 3
20 ≈ 7 × 10
9. As
part of the analysis, two “record breaking” integer sequences were deﬁned: these record the
smallest powers of two having no 0 (resp., 2) in the last k digits of its ternary representation,
for k = 1, 2, . . .. These integer sequences have been entered into the OEIS as A351927 and
A351928.

7 Acknowledgments

The author thanks an anonymous reviewer for suggesting reﬁnements to the proof of Lemma 1.
Some computations used resources made possible by the Applied Mathematics Program of
the U.S. Department of Energy Oﬃce of Advanced Scientiﬁc Computing Research under
contract number DE-AC02-05CH11231.

References

[1] Vassil S. Dimitrov and Everett W. Howe, Powers of 3 with few nonzero bits and a
conjecture of Erd˝os, preprint, 2021. Available at https://arxiv.org/abs/2105.06440.

[2] Paul Erd¨os, Some unconventional problems in number theory, Math. Mag. 52 (1979),
67–70.
 8

[3] Hansraj Gupta, Powers of 2 and sums of distinct powers of 3, Univ. Beograd Publ.
Elecktrotehn 602–633 (1978), 151–158.

[4] Jeﬀrey C. Lagarias, Ternary expansions of powers of 2, J. Lond. Math. Soc. 79 (2009),
562–588.

[5] N. J. A. Sloane, The persistence of a number, J. Recreational Math. 6 (1973), 97–98.

[6] Ilan Vardi, Computational Recreations in Mathematica, Addison Wesley Longman Pub-
lishing Co., Inc., 1991.

2020 Mathematics Subject Classiﬁcation: Primary 11A63; Secondary 11Y55, 11D61, 11Y50.

Keywords: power of two, ternary expansion, number theory conjecture, exponential Diophan-
tine equation.

(Concerned with sequences A351927 and A351928.)

Received February 26 2022; revised versions received March 19 2022; March 21 2022. Published
in Journal of Integer Sequences, March 23 2022.

Return to Journal of Integer Sequences home page.

9
