<!-- source: https://arxiv.org/pdf/2305.10357v1 | converted from PDF -->

arXiv:2305.10357v1  [math.HO]  25 Apr 2023Archive Labeling Sequences

Tanya Khovanova, Gregory Marton

2009

Abstract
What follows is the story of a pair of integer sequences, which
started life as a Google interview puzzle back in the previous century
when VHS video tapes were in use.

1 Google’s Puzzle

Suppose you are buying VHS tapes and want to label them using
the stickers that came in the package. You want to number the
tapes consecutively starting from 1, and the stickers that come
with each package are exactly one of each digit [“0”, . . . , “9”].
For your ﬁrst tape, you use only the digit “1” and save all the
other digit stickers for later tapes. The next time you will need a
digit “1” will be for tape number 10. By this time, you will have
several unused “1” stickers. What is the next tape number such
that after labeling the tape with that number, you will not have
any “1” stickers remaining?

2 Ones Counting Function

The puzzle appeared in Google Labs Aptitude Test [2] in the following for-
mulation.

Consider a function f which, for a given whole number x, returns
the number of ones required when writing out all numbers be-
tween 0 and x inclusive. For example, f (13) = 6. Notice that
f (1) = 1. What is the next largest x such that f (x) = x?

1

Thus f (x) is the number of “1” stickers needed to label all the tapes up to
tape x. When f (x) = x, then we have used all of the “1” stickers in labeling
the ﬁrst x tapes. Function f (x) can be found in the Online Encyclopedia of
Integer Sequences [1] as sequence A094798.
Let’s consider any non-zero digit. In the single and double-digit numbers,
there are ten of each digit in the ones column, and ten of each digit in the
tens column, so 20 altogether. Early on, the tape number is ahead of the
digit count. By the time we get to 20-digit numbers, though, there should
be, on average, two of any single non-zero digit per number.1 Thus, the
number of times that any digit is used should eventually catch up with the
tape numbers.
Encouraged by assurance of reaching our goal somewhere, we might con-
tinue our estimate. In the up-to three-digit numbers, those less than 104,
there are 300 of each non-zero digit; in the numbers below 105, there are
4000; then 50000 below 106, and so on up to 1010, where f (x) and x must
(almost) meet. In particular, there are 10000000000 counts for any non-zero
digit in the numbers below 10000000000. Hence, were the puzzle asking
about any of the digits 2–9, then ten billion could have been an easy answer
or, at least a limit on how far we need to search.
Sadly, there is a 1 in the decimal representation of ten billion (and a
few zeroes), so we require 1010 + 1 of the digit “1” to write the numbers [1,
. . . , 1010]. Thus, f (1010) ̸= 1010, so 1010 cannot be the answer to the original
puzzle. Thus stymied, we wrote a program to ﬁnd the solution to the original
Google puzzle. And the answer turned out to be 199981, much smaller than
we expected.

3 Counting Other Digits

We were overstymied, so we actually wrote a program to solve the puzzle for
any non-zero digit. We calculated the beginning of the sequence a(n), where
a(n) is the smallest number x > 1 such that the decimal representation of n
appears as a substring of the decimal representations of the numbers [1, . . . ,
x] exactly x times.
We already know that a(1) is 199981. The sequence, which now has

1We’re looking at non-zero digits for now only because one would not use stickers for
leading zeroes, unlike other leading digits, but we will return to zeroes shortly.

2

number A163500, continues as follows:

28263827, 371599983, 499999984, 10000000000,
9500000000, 9465000000, 9465000000, 10000000000, . . . .

Did you expect this sequence to be increasing? You could have because
smaller numbers tend to contain smaller digits than larger numbers. Then
why is the sequence not increasing? As we failed to ﬁnd a value for the digit
5 below ten billion, we noticed that it is fairly easy to imagine a scenario
where you have one less than the number you need, and then the next value
has more than you need for equality, and then you equalize again later. In
response, we decided to look at a related sequence.
Let a>(n) be the smallest number x > 1 such that the decimal repre-
sentation of n appears as a substring of the decimal representations of the
numbers [1, . . . , x] more than x times. The key diﬀerence being “more than”
rather than “exactly”. Thus, we will also denote our “exactly” sequence as
a=(n).
We later discovered that this related sequence was published at IBM’s
famous puzzle website “Ponder This” in April 2014 and was authored by
Michael Brand [3]. This version is quite natural as it wonders when we ﬁrst
run out of the labels. Moreover, digit 1 plays a special role in this puzzle as
it must be the digit that will run out ﬁrst.
But we digress. Starting at 1, Table 1 shows the ﬁrst nine terms of each
sequence:
 n a=(n) a>(n)
1 199981 199991
2 28263827 28263828
3 371599983 371599993
4 499999984 499999994
5 10000000000 5555555555
6 9500000000 6666666666
7 9465000000 7777777777
8 9465000000 8888888888
9 10000000000 9999999999

Table 1: The ﬁrst nine terms of a=(n) and a>(n).

3

Some of these pairs are interesting in their own right. Notice that 199991
is ten more than the previously found 199981. For all the numbers in between,
the initial equality holds. Likewise, for n = 3, each of the numbers between
371599983 and 371599993 has exactly one three. Hence, the increase in a
number by one is the same as the increase in the count of threes. A similar
situation holds for n = 4.
The sequence a> can be found using the identiﬁer A164321 in the OEIS.
Unsurprisingly, the values matching this relaxed second condition are more
well-behaved than those with equality. Do you think the second sequence is
always increasing?

4 More on the “exactly” sequence

Let’s get back to sequence a=(n). This sequence must be ﬁnite. Think about
it, starting from 11-digit numbers, the supply of labels starts decreasing. We
have to run out of labels.
Sequences a=(n) are in the OEIS database, and we show their numbers
in Table 2.
 n Sequence number Number of terms
1 A014778 83
2 A101639 13
3 A101640 35
4 A101641 47
5 A130427 4
6 A130428 71
7 A130429 48
8 A130430 343
9 A130431 8

Table 2: Sequence numbers and the number of terms for a=(n).

The last column is its own sequence. It appears in the OEIS in disguise:
sequence A130432 is the last column of Table 2 plus 1, because the author
assumed that tapes would be numbered starting with 0. While that choice
may have tempted the audience of this paper, it would not have been common
practice. Let’s now dive deeper into the n = 0 case.”

4

5 Counting Zeroes

In counting zeroes, let us recall that the puzzle speciﬁes that the ﬁrst VHS
tape is labeled one, not zero. We denote the function that calculates zeroes
in numbers 1 through x inclusive as z(x). It is represented in the OEIS as
sequence A061217.
We calculated that the smallest number x such that x is less than or
equal to the number of 0s in the decimal representations of [1, . . . , x] is
100559404366. But what is the corresponding number for the “=” sequence?
It appears that no such number exists. To prove it, we need to start with a
lemma.

Lemma 5.1. For any integer x > 1010, we have z(x + 1010) ≥ z(x) + 1010.

Proof. Indeed, numbers between x and x + 1010 go through all possible com-
binations of the last ten digits. Hence, they contain at least 1010 zeroes.

Now we are ready to prove our theorem.

Theorem 5.2. The value a=(0) is not well-deﬁned.

Proof. We calculated that z(100559404366) = 100559404367. Obviously,
z(100559404365) = 100559404364. We wrote a program and checked that
a=(0) > 100559404366. We actually checked up to a bigger number, but
obviously, we couldn’t continue checking up to inﬁnity.
So we need other arguments. Notice that number 100559404366 has three
zeroes. Hence, for some y that are not much bigger than 100559404367, we
will have that z(y + 1) ≥ z(y) + 3. For some time, the sequence z will be
increasing in steps not less than three.
Were we dealing with random 12-digit numbers, then such numbers would
have on average 11/10 zeroes. Hence, z(x) grows faster than x at this point.
But this consideration is not a proof. To ﬁnish the proof of the theorem, we
need to ﬁnd a number y > 1010 such that z(y) > y + 1010 and check that
there is no solution to z(x) = x below y. That number y would guarantee
that z(x) will always be ahead of its index after y.
Let us ﬁnd such a number. We start with 100559404366. Clearly, the
sequence z(x) will continue to grow not slower than its index x until the
next number that doesn’t contain zeroes. Such number is 111111111111. We
calculated that z(111111111111) = 120987654321. So the number of zeroes
is way ahead of the number itself. As the sequence z(x) is non-decreasing,

5

we can’t have y such that z(y) = y until 120987654321. This way, we can
speed up the process, and we need a small number of iterations to get to
such a number. We performed appropriate calculations, thus concluding the
proof of the theorem.

In addition to a= and a>, we counted the “greater or equal” sequence
a≥(n), where (n) denotes the digit we use, not the term of a sequence. The
great property of this latter sequence is that

a≥(n) = min(a=(n), a>(n)).

This sequence appears in the database as sequence A164935. Actually, this
is not quite true. Sequences a= and a> are only deﬁned for digits 1 through
9. However, A164935 is deﬁned by any nonnegative number. Moreover,
we deﬁned a=(1) to be the smallest number greater than 1 satisfying the
VHS property. This complicated condition was needed so that the sequence
would include the solution of Google’s puzzle, 199981, as the ﬁrst term. But
A164935(1) = 1 as it should be.

6 The Algorithms

So that you may easily check the facts we have described, we would like to
share the algorithms we used, so in this section, we describe how we counted
the total count of a particular digit in the set [1, . . . , x]. Let us denote the
digit of interest as d. We counted the digit d separately in each decimal place
it occurred. Suppose we want to count how many times the digit d occurred
in the k-th place from the right in the set [1, . . . , x]. It depends on which
digit the number x has in k-th place from the right. Suppose this digit is a,
then

• If a > d, then the count is (⌊n/10k⌋ + 1)10k−1.

• If a < d, then the count is ⌊n/10k⌋10k−1.

• If a > d, then the count is ⌊n/10k⌋10k−1 + (n mod 10k−1) + 1.

For starters, we describe our algorithm for ﬁnding a≥(0). To speed up our
algorithm, we didn’t want to count z(x) for every x. We need the following
lemma.
 6

Lemma 6.1. Suppose we already know that a≥(0) > x. Suppose, in addition,
we can show that z(y) < x for some y > x. Then a≥(0) > y.

Proof. The proof follows from the fact that sequence z is non-decreasing.

So we used a sort of binary search on ranges of numbers. We call a range
of numbers [c, . . . , d] safe if we can guarantee that a≥(0) > c. We start with
a safe range [c, . . . , d] whose length is a power of 2, then iterate it to the
next safe range as follows:

• If z(d) ≤ x, then the next range is [c, . . . , (c + d)/2]

• If z(d) > x, then the next range is [d, . . . , d + 2(d − c)].

We just described the algorithm for ﬁnding the value of a≥(0). In a similar
manner, we can ﬁnd the value a≥(d) for any d. After the value of a≥(d) is
found, ﬁnding the value of a>(d) is often easy. You just need to check several
next values.

7 Multiple Digits

There is no reason that we should be constrained to single digits. The for-
mal statement of the problem provides an obvious generalization, where we
consider substrings of each of the numbers [1, . . . , x] rather than digits in
those numbers. We should note that we count every occurrence of a substring
separately. Thus 11 will be counted twice as a substring of 1113.
We can prove that the “more than” sequence is increasing after the ﬁrst
term. Indeed, for two integers i and j, if i is less than j, then for every
occurrence of j, by replacing j with i, we get a smaller number with an
occurrence of i.
Inspired, we wrote another fancier and faster program to ﬁnd values of the
“more or equal” sequence for two-digit numbers. Here is the smallest number
x for which the number of “10”s as substrings of the numbers [1 . . . x] is more
than or equal to x. And by a lucky strike, the equality holds. The number
has 93 digits and doesn’t ﬁt on a line. Luckily, the middle part of the number
consists of a long run of nines, namely 88 of them. So we replaced some of
the nines with dots without losing information. The number is:

109999999999999999999999 · · · 99999999999999999999810.

7

Now the reader can do an exercise and ﬁnd the number for the “more than”
sequence.
The value of a≥(11) miraculously has 93 digits with a middle run of 88
nines:
 119999999999999999999999 · · · 99999999999999999999811.

Note how strikingly similar it is to the tenth element of the sequence! Can
you explain that similarity between a≥(10) and a≥(11)?
Sadly, a≥(12) is not so pretty, though it still has a middle run of 68 nines
allowing us to display it on the line using dots. The total number of digits
is 94:
 1296624070230872986615199999999 · · · 9999999999999812.

8 Further Research

We cannot leave oﬀ without at least mentioning that the sequence function
should next take one more parameter: the base of representation. We know
about two results in this area.

• Sequence A092175(b) represents our sequence a>(1) in base b. That is,
it assumes that we want to number VHS in base b, and our labels are
also the digits in base b. Starting from base 1, the sequence progresses
as follows:

2, 3, 13, 29, 182, 427, 3931, 8185, 102781, 199991, 3179143, . . . .

Not surprisingly, A092175(10) = 199991, which we already knew from
Table 1.

• Sequence A165617(b) counts the number of values of x such that fb(x) =
x, where fb(x) is the total number of ones in all nonnegative numbers
not exceeding x when written in base b. In other words, fb(x) is the
analog of our function f (x) for other bases. The function f (x) can be
now viewed as f10(x). Sequence A165617 is

2, 4, 8, 4, 21, 5, 45, 49, 83.

The sequence starts from base 2, and, not surprisingly, the ninth term
is 83, which we already knew from Table 2.

8

By the way, sequence A165617 is easy to calculate as the largest possible
number such that fb(x) = x is known; see the comment in sequence A165617.
This number is the concatenation of b − 1 ones followed by a single zero.
Expressed in base 10, these numbers are (starting from index 2):

2, 12, 84, 780, 9330, 137256, 2396744, 48427560, 1111111110 . . . ,

and they are in the database as sequence A226238.
The sequences we described in this paper can be extended, and there are
many related sequences to be cataloged. We would love to hear tales from
your explorations. Enjoy the sequence hunt!

9 Acknowledgments

We are grateful to Alexey Radul for his helpful suggestions.

References

[1] N. J. A. Sloane, Online Encyclopedia of Integer Sequences (OEIS).
http://www.research.att.com/∼njas/sequences/

[2] Google Labs Aptitude Test, Google, 2004.

[3] Ponder This, (2004), available at https://research.ibm.com/haifa/ponderthis/challenges/April2004.html.

9
