<!-- source: https://arxiv.org/pdf/2305.10357 | converted from PDF -->

Archive Labeling Sequences

Tanya Khovanova, Gregory Marton

Abstract

What follows is the story of a family of integer sequences, which
started life as a Google interview puzzle back in the previous century
when VHS video tapes were in use.

1 Google’s Puzzle

Suppose you are buying VHS tapes and want to label them using
the stickers that came in the package. You want to number the
tapes consecutively starting from 1, and the stickers that come
with each package are exactly one of each digit [ 0 , . . . , 9 ].
For your first tape, you use only the digit 1 and save all the
other digit stickers for later tapes. The next time you will need a
digit 1 will be for tape number 10. By this time, you will have
several unused 1 stickers. What is the next tape number such
that after labeling the tape with that number, you will not have
any 1 stickers remaining?

2 Ones Counting Function

The puzzle appeared in Google Labs Aptitude Test [3] in the following for-
mulation.

Consider a function f which, for a given whole number x, returns
the number of ones required when writing out all numbers be-
tween 0 and x inclusive. For example, f (13) = 6. Notice that
f (1) = 1. What is the next largest x such that f (x) = x?

1arXiv:2305.10357v2  [math.HO]  16 Feb 2024
One might notice that it is unclear that the two questions above are
equivalent since the happy owner of the tapes might hypothetically run out
of another sticker, say sticker 2 first, thus not reaching a point where all
stickers 1 are used. Intuitively, we can expect that sticker 1 is the first to
run out, and we will prove this shortly.
It is also unclear if any x even exists such that f (x) = x. In teaching, we
often ask students to find things that do not exist, expecting a proof of non-
existence. While such problems may be considered evil, they are legitimate.
At the time, Google’s unofficial motto was “Don’t be Evil”, and they weren’t:
we will see that the answer does indeed exist.
But we digress. Our function f (x) is the number of 1 stickers needed to
label all the tapes up to tape x. When f (x) = x, then we have used all of
the 1 stickers in labeling the first x tapes. The function f (x) can be found
in the Online Encyclopedia of Integer Sequences [5] as sequence A094798.
In considering the other non-zero digits, let fd(x) count the number of d
stickers needed to number the first x tapes (and of course let f (x) henceforth
be f1(x)). In the single and double-digit numbers, there are ten of each non-
zero digit in the ones column and ten in the tens column, so 20 altogether.
Early on, the tape number is ahead of the digit count. By the time we get
to 20-digit numbers, though, there should be, on average, two of any single
non-zero digit per number.
1 Thus, the number of times that any digit is used
should eventually catch up with the tape numbers.
Encouraged by assurance of reaching our goal somewhere, we might con-
tinue our estimate. In the up-to three-digit numbers, those less than 10
4,
there are 300 of each non-zero digit; in the numbers below 105, there are
4000; then 50000 below 10
6, and so on up to 1010, where fd>1(x) and x must
(almost) meet. In particular, there are 10000000000 counts for any non-zero
digit in the numbers below 10000000000. Hence, were the puzzle asking
about any of the digits 2–9, then ten billion could have been an easy answer
or, at least a limit on how far we need to search.
Sadly, there is a 1 in the decimal representation of ten billion (and a few
zeroes), so we require 1010 + 1 digits 1 to write the numbers [1,. . . , 10
10].
Thus, f1(10
10) ̸= 10
10, so 10
10 cannot be the answer to the original puzzle.
Thus stymied, we wrote a program to find the solution to the original Google
puzzle. And the answer turned out to be 199981, much smaller than we

1We’re looking at non-zero digits for now only because one would not use stickers for
leading zeroes, unlike other leading digits, but we will return to zeroes shortly.

2

expected.

3 Counting Other Digits

We were so enjoying our stymie
2 that we then wrote a program to solve the
puzzle for any non-zero digit.

Definition 3.1. We denote by a=(d) the smallest number x > 1 such that
the decimal representation of d appears as a substring of the decimal rep-
resentations of the numbers [1,. . . , x] exactly x times:

a=(d) = min({x > 1 : fd(x) = x}).

We already know that a=(1) is 199981. The sequence a=(d), which now
has number A163500, continues as follows:

28263827, 371599983, 499999984, 10000000000,
9500000000, 9465000000, 9465000000, 10000000000.

Did you expect this sequence to be increasing? You could have because
smaller numbers tend to contain smaller digits than larger numbers. Then
why is the sequence not increasing? As we failed to find a value for the digit
5 below ten billion, we noticed that it is fairly easy to imagine a scenario
where you have one less than the number you need, and then the next value
has more than you need for equality, and then you equalize again later. In
response, we decided to look at a related sequence.

Definition 3.2. Let
 a>(d) = min({x : fd(x) > x}).

The key difference is in using “more than” rather than “exactly”. Thus,
we will also call our a=(d) sequence the “exactly” sequence and our a>(d)
the “more than” sequence.
We later discovered that this related sequence was published at IBM’s
famous puzzle website “Ponder This” in April 2004 and was authored by
Michael Brand [6]. This version is quite natural as it wonders when we first

2Yes, we just nouned that verb.
 3

run out of the labels. Moreover, the 1 sticker plays a special role in this
puzzle as it must be the digit that will run out first, as we see in the following
table and shall prove theoretically in Proposition 8.1.
Starting at 1, Table 1 shows the first nine terms of the “exactly” and
“more than” sequences.

d a=(d) a>(d)
1 199981 199991
2 28263827 28263828
3 371599983 371599993
4 499999984 499999994
5 10000000000 5555555555
6 9500000000 6666666666
7 9465000000 7777777777
8 9465000000 8888888888
9 10000000000 9999999999

Table 1: The first nine terms of a=(d) and a>(d).

Some of these rows are interesting in their own right. Notice that 199991
is ten more than the previously found 199981. For all the numbers in be-
tween, the initial equality holds (∀i ∈ [199981,. . . , 199991] we have i = f1(i)).
Likewise, for d = 3 , each of the numbers between 371599983 and 371599993
has exactly one three, so the increase in a number by one is the same as the
increase in the count of threes. A similar situation holds for d = 4 .
The sequence a> can be found using the identifier A164321 in the OEIS.
Unsurprisingly, the values matching this relaxed second condition are more
well-behaved than those with equality.
Did you notice that the second column is increasing? This might be
surprising for the fans of the Champernowne constant. What’s the Cham-
pernowne constant? Imagine you placed an infinitude of labeled VHS tapes
in order. The labels together will read as a concatenation of all positive in-
tegers, whose digits form the sequence A033307. Now we add a zero with a
dot in front to get the constant:

0.12345678910111213141516 . . . .

The constant is most famous for being a “normal” number in any base [1].

4

Here normal is a mathematical term referring to the distribution of digits.
Normal means that all possible strings of digits of the same length have the
same density. This means that every digit in base 10 appears with the same
density. Despite this, our second column is increasing, demonstrating an
unsurprising fact that smaller digits appear earlier than the bigger digits.

4 More “Exactly” Sequences

We want to introduce a few more related sequences, one per digit, where the
letter E symbolizes exactness or equality.

Definition 4.1. Let Ed be an increasing sequence of positive integers x such
that fd(x) = x.

The sequence Ed must be finite. After all, starting from 11-digit numbers,
the supply of labels starts decreasing. We have to run out of labels. We can
be more precise in claiming that the largest value in Ed is not more than
d10
10, which we prove in a more general setting in Proposition 9.1.
Sequences Ed are connected to our sequence a=(d):

a=(d) =
 {
Ed(2) for d = 1
Ed(1) otherwise .

Recall, the special case for 1 is what made the puzzle interesting because
E1(1) = 1. The sequences Ed are in the OEIS database, and we show their
A-numbers and lengths in Table 2.
The numbers of terms are their own sequence! It appears in the OEIS
in disguise: sequence A130432 is the last column of Table 2 plus 1, because
the sequence author assumed that tapes would be numbered starting with 0.
While that choice may have tempted the audience of this paper3, it would
not have been common practice. However, if we did start at zero, and thus
add 1 to the last column, we see a neat pattern: the result is divisible by d.
This hides an even more interesting fact: the actual values of Ed are periodic
modulo 10
10, while being bounded by d · 10
10; the latter fact is proven in
Proposition 9.1.
To explain periodicity, we observe that for 0 ≤ x < (d − 1)10
10, we have
fd(x + 10
10) = fd(x) + 10
10. It follows that the numbers x and x + 10
10, are

3If you numbered your VHS tapes starting at zero, please send a note, kindred spirit!

5

d OEIS ref. for Ed Number of terms
1 A014778 83
2 A101639 13
3 A101640 35
4 A101641 47
5 A130427 4
6 A130428 71
7 A130429 48
8 A130430 343
9 A130431 8

Table 2: The sequence numbers for Ed and their lengths.

either both members of the sequence E(d) or both non-members. Thus the
number of the solutions to the equation fd(x) = x in the range [0,. . . , 10
10−1]
is the same as in the range [r10
10,. . . , (r + 1)1010] − 1, when r < d. Hence,
we have d ranges with the same number of solutions, which explains the
divisibility of A130432(d) by d.
When studying Table 1, you might notice that stickers 5 and 9 delay
the start of the corresponding exact sequences until the latest possible value
of x of 10000000000. Not surprisingly, in Table 2 the count for the number
of terms for values 5 and 9 is much smaller than for other stickers. Due to the
argument in the previous paragraph, all solutions of fd(x) = x for d equaling
5 or 9 have to be of the form r10
10, where r < d. Thus, the last column of 2
has to be the smallest possible value of exactly d − 1.
Now that the upper bound is clear, we can find the largest values and
treat them as another sequence, shown in Table 3.
Let’s now dive deeper into the d = 0 case.

5 Counting Zeroes

In counting zeroes, let us recall that the puzzle specifies that the first VHS
tape is labeled with the 1 sticker, not 0 . Expanding on f , we denote the
function that calculates zeroes in numbers 1 through x inclusive as f0(x). It
is represented in the OEIS as sequence A061217.
We calculated that the smallest number x such that x is less than or

6

d max(E(d))
1 1111111110,
2 10535000000,
3 20500000000,
4 30500000000,
5 40000000000,
6 59628399995,
7 69971736170,
8 79998399997,
9 80000000000.

Table 3: Largest values of x, where fd(x) = x.

equal to the number of 0s in the decimal representations of [1,. . . , x] is
100559404366, equivalently this number is a>(0). But what is the corre-
sponding number for the a= sequence? It appears that no such number
exists. To prove it, we need to start with a lemma.

Lemma 5.1. For any integer x > 10
10, we have f0(x + 10
10) ≥ f0(x) + 10
10.

Proof. Indeed, numbers between x and x + 1010 go through all possible com-
binations of the last ten digits. Hence, they contain at least 10
10 zeroes.

Now we are ready to prove our theorem.

Theorem 5.2. The value a=(0) is not well-defined.

Proof. We calculated that f0(100559404366) = 100559404367. Its predeces-
sor then must be f0(100559404365) = 100559404364 with three fewer zeros.
We verified that there were no equalities up to this point, and indeed up to
a bigger number, but of course we couldn’t continue checking up to infinity.
So we need other arguments. Notice that number 100559404366 has three
zeroes. Hence, for some y that are not much bigger than 100559404367, we
will have that f0(y + 1) ≥ f0(y) + 3. For some time, the sequence f0 will be
increasing in steps not less than three. We are getting away from the equality
at high speed.
Were we dealing with random 12-digit numbers, then such numbers would
have on average 11/10 zeroes. Hence, f0(x) grows faster than x at this point.

7

But this consideration is not a proof. To finish the proof of the theorem, we
need to find a number y > 10
10 such that f0(y) > y + 1010 and check that
there is no solution to f0(x) = x below y. By Lemma 5.1, that number y
would guarantee that f0(x) will always be ahead of its index after y.
Let us find such a number. We start with 100559404366. The sequence
f0(x) will continue to grow not slower than its index x until the next number
that doesn’t contain zeroes. Such a number is 111111111111. We calculated
that f0(111111111111) = 120987654321. So the number of zeroes is way
ahead of the number itself. As the sequence f0(x) is non-decreasing, we
can’t have y such that f0(y) = y until 120987654321. This way, we can
speed up the process, and we need a small number of iterations to get to
such a number. We performed appropriate calculations, thus concluding the
proof of the theorem.

6 Greater or Equal

In addition to a= and a>, we counted the “greater or equal” sequence a≥(d),
where d again denotes the sticker in question. The great property of this
latter sequence is that
 a≥(d) = min(a=(d), a>(d)).

This sequence appears in the database as sequence A164935. How can we
define such a sequence for multi-digit stickers? The idea is to ignore stickers
and consider multi-digit strings; for which we give proper definitions in a
later section.
One more caveat: we defined a=(1) to be the smallest number greater
than 1 satisfying the VHS property. This complicated condition was needed
so that the sequence would include the solution of Google’s puzzle, 199981,
as the first term. But A164935(1) = 1 as it should be. This sequence is non-
decreasing for the same reason the “more than” sequence is non-decreasing.
We prove this in Proposition 8.1.

7 The Algorithms

So that you may easily check the facts we have described, we would like to
share the algorithms we used [4]. In this section, we describe a more efficient

8

way to find fd(x). We counted the digit d separately in each decimal place it
occurred. Suppose we want to count how many times the digit d occurred in
the k-th place from the right in the set [1,. . . , x]. It depends on which digit
the number x has in the k-th place from the right. Suppose this digit is xk.
Consider the number y = ⌊x/10
k⌋10
k. We chose y because it is the largest
number not exceeding x with k zeros at the end. In the range [1,. . . , y − 1], if
we pad smaller integers with zeros on the left, each digit appears in the k-th
place from the right the same number of times. Therefore, any digit d > 0
appears in this range y
10 = ⌊x/10
k⌋10
k−1 times.
Now, we need to calculate how often d appears in the place of interest in
the range [y,. . . , x]. If xk < d, then it doesn’t appear at all. If xk > d > 0
we need to add 10
k−1. If xk = d > 0, we need to add the total count of our
digit in the range, which is (x mod 10k−1) + 1.
We need to consider the case of d = 0 separately, as we should not count
leading zeros, nor zero itself, as the sequence starts at 1. If xk > d = 0, the
count is ⌊x/10
k⌋10
k−1, (the same as the xk < d case for other digits), but if
the k-th digit is zero, we need to subtract the number of digits in the range
[1,. . . , y − 1] that have fewer than k digits and add the number of digits in
the range [y,. . . , x] that have 0 in the k-th place from the right. Thus the
adjusment is −10
k−1 + (x mod 10k−1) + 1.
To summarize, we would like to express fd(x) as the sum of the con-
tributions cd(xk) of the counts of the digit d in the k-the place from the
right. This contribution depends on the value of xk. Let Y be shorthand for
⌊x/10
k⌋ · 10
k−1, then:

cd(xk) =
 




Y when d > 0 and xk < d
Y + (x mod 10k−1) + 1 when d > 0 and xk = d
Y + 10k−1 when d > 0 and xk > d
Y when d = 0 and xk > d
Y − 10
k−1 + (x mod 10k−1) + 1 when d = 0 and xk = d
 .

Summing over each k-th place, we get

fd(x) = ∑

k cd(xk). (1)

We can now use this closed-form for fd(x) in much faster searches for
a≥(d). To do so, we need the following lemma that allows us to skip a lot of
numbers in our search.
 9

Lemma 7.1. Suppose we already know that a≥(d) > x. Suppose, in addition,
we can show that fd(y) < x for some y > x. Then a≥(d) > y.

Proof. As fd is non-decreasing and fd(y) < x, we know that the value of
function fd on any element in the range [x,. . . , y] is not greater than x. It
follows that a≥(d) > y.

We search the infinite space of possible values using a variation of un-
bounded binary search [2]. We call a range of numbers [x,. . . , x+p] “safeleft”
if we can guarantee that a≥(d) > x. We start with a safeleft range [2, . . . ,
3]. When d = 1, we can’t start with the range whose left side is 0, as we
will get the answer 1, which we want to skip. It is easy to see that the base
case holds for 2 in other words, fd(2) < 2 for any d, as we only use one 1
and one 2 sticker up to tape number 2. Then we iterate to the next safeleft
range as follows:

• If fd(x + p) < x, then a≥(d) is not in the range by Lemma 7.1, making
any range starting with x + p safeleft. The next range to search is
[x + p,. . . , x + 3p], where we move the start of the range to x + p and
increase the size of the range twice.

• If fd(x + p) ≥ x, then a≥(d) is not guaranteed to be outside of the
range. The next range to search is [x,. . . , x + p/2], where we keep the
start of the range and halve the size of the range.

• Suppose we reduced the range size to 1. Then if fd(x) < x and fd(x +
1) ≥ x + 1, we have a≥(d) = x + 1. If not, then any range starting with
x + 1 is safe, and the new range is [x + 1,. . . , x + 3].

After the value of a≥(d) is found, finding the value of a>(d) is easy for
non-zero digits. One may need to check several next values. For zero it is
not as easy, but see Section 5. When looking for the exact sequence a=(d),
the answer is not always near a≥(d), but we can still search rapidly. If we
already showed that a=(d) > x and if fd(x) > x, then a=(d) ≥ fd(x). After
all, if we saw no digits d in the range [x,. . . , fd(x) − 1] at all, x would not
catch up to fd(x) below fd(x).
 10

8 Multiple Digits

There is no reason that we should be constrained to single digits. The formal
statement of the problem provides a generalization, where we consider sub-
strings of each of the numbers [1,. . . , x] rather than digits in those numbers.
We should note that we count every occurrence of a substring separately.
Thus 11 will be counted twice as a substring of 1113 even though an actual
sticker with “11” printed on it could be used in either position, but not in
both positions simultaneously.
Now that we defined the “more than” sequence a> for any positive integer,
we can prove the statement we promised before, along with a corresponding
statement about the a≥ sequence.

Proposition 8.1. The “more than” sequence a> and the “greater or equal”
sequence a≥ are non-decreasing after the first terms a>(1) and a≥(1).

Proof. For two strings i and j, if i < j, then for every occurrence of j in a
number x, we can get a smaller number with an occurrence of i by replacing
j with i. It follows that for 0 < i < j, and any x,

fi(x) ≥ fj(x).

It follows that fi(a>(j)) ≥ fj(a>(j)) = a>(j), and fi(a≥(j)) ≥ fj(a≥(j)) =
a≥(j) implying that a>(i) ≤ a>(j) and a≥(i) ≤ a≥(j).

Inspired, we wrote an even fancier program to find values of the “more or
equal” sequence a≥ for multi-digit numbers. As before, we start by calculat-
ing fd(x), where d is an n-digit number. As a warm-up, we have an exercise
for the reader to check that for k ≥ n

fd(10
k − 1) = k10
k−n.

To calculate fd(x), we count d’s contribution separately in each decimal
place it occurred, parametrized by the placement of its last digit. Suppose
we want to count how many times the n-digit string d occurred so that its
last digit is in the k-th place from the right in the range [1,. . . , x]. It depends
on which n-digits the number x has in the corresponding place. Suppose
this n-digit number is xk. Consider the number y = ⌊x/10
k+1⌋10
k+1. In the
range [1,. . . , y − 1], if we pad smaller integers with zeros on the left, each

11

n-digit number appears in the k-th place from the right the same number of
times. Therefore, d appears in this range y
10n = ⌊x/10
k+n−1⌋10
k−1 times.
Now, we need to calculate how often d appears in the place of interest in
the range [y,. . . , x]. If xk < d, then it doesn’t appear at all. If xk > d we
need to add 10k−1. If xk = d, we need to add the total count of appearance
d in the given spot in the range [y,. . . , x], which is (x mod 10k−1) + 1.
To summarize, we would like to express fd(x) as the sum of the contribu-
tions cd(xk) of the counts of the n-digit sticker d in the k-th place from the
right. Here we assume that n > 1, and, consequently, d > 0, which makes the
following formula simpler than the one for a single digit. This contribution
depends on the value of xk. Let Y be shorthand for ⌊x/10
k−n+1⌋·10
k−1, then:

cd(xk) =
 



Y when xk < d
Y + (x mod 10k−1) + 1 when xk = d
Y + 10k−1 when xk > d .

After working out the case d = 0, we were not immediately sure that
a=(d) is defined for every d > 0. However, it is.

Theorem 8.2. The value a=(d) is well-defined for any d > 0.

Proof. If d is an n-digit sticker that is not a power of 10, then fd(10
k − 1) =
fd(10
k). From the exercise above, it follows that fd(10
k) = k10
k−n. Plugging
in k = 10n, we get fd(10
10n) = 10n10
10n−n = 1010n. Thus, 1010n is always a
solution for fd(x) = x. Therefore, for an n-digit sticker d that is not a power
of 10, the function a=(d) is well-defined and a=(d) ≤ 10
10n.
Now we need to check the case when an n-digit sticker d is a power of 10,
that is d = 10
n−1. Consider x = 2 · 10
10n−6+n, then Y = 2 · 10
10n−6. We count
the contribution of the sticker d, where the last digit is in the k-th place from
the right, where k must be in the range [1,. . . , 10
n − 4].
If k < 10
n − 4, then xk is a string of 0s and d > xk, and the contribution
for this k is Y = 2 · 10
10n−6. If k = 10
n − 4, then xk is a 2 followed by n − 1
zeros, so d < xk, and the corresponding Y is 0, and the contribution for this
k is 10k−1 = 2 · 10
10n−6 + 1010n−5. Summing up, we get

2 · 10
10n−6(10
n − 5) + 1010n−5 = 2 · 10
10n−6+n,

implying that fd(x) = x, which concludes the proof.

12

Below is the smallest number x for which the number of 10 s as substrings
of the numbers in the range [1,. . . , x] is more than or equal to x. And by
a lucky strike, the equality holds. The number has 93 digits and doesn’t fit
on a line. Fortunately, the middle part of the number consists of a long run
of nines, namely 88 of them. So we replaced some of the nines with dots
without losing information. The number is:

a≥( 10 ) = 109999999999999999999999 · · · 999999999999999999999810.

Now the reader can do an exercise and find the corresponding number for
the “more than” sequence, a>( 10 ).
The value of a≥( 11 ) miraculously has 93 digits with a middle run of 88
nines:

a≥( 11 ) = 119999999999999999999999 · · · 999999999999999999999811.

Note how strikingly similar it is to the tenth element of the sequence! Can
you explain that similarity between a≥( 10 ) and a≥( 11 )?
Sadly, a≥( 12 ) is not so pretty, though it still has a middle run of 68
nines allowing us to display it on the line using dots. The total number of
digits is 94:

a≥( 12 ) = 1296624070230872986615199999999 · · · 999999999999812.

It appears that we are lucky again, that the a= sequence is the same as the
a≥ sequence for 11 and 12 . Our luck runs out at 21 .
We have calculated the values up to d= 113 so far, but please feel free
to contribute more compute!
The values for a=(50) and a=(99) are the same nice, round number: 10
101.
Similarly, a=(999) = 10
1002. It turns out that and a>(99) = a=(99) − 1 and
a>(999) = a=(999) − 1, but there is no such pretty relationship for 50
or 500 . There are, however, 6 two-digit values for which the difference is
100. There are also 8 two-digit values that share an a= value of 9465 · 10
97,
reminiscent of the a= values for 7 and 8: 9465 · 10
6. And would you have
guessed, there are corresponding three-digit values whose a= values are 9465·
10
998! There are other tantalizing patterns; for details please see the code [4],
and share what you find!
One would expect three-digit stickers to occur ten times less frequently
than two-digit stickers, and indeed the corresponding values in this sequence

13

that we’ve computed are in the neighborhood of a thousand digits. Each
answer for a three-digit sticker has taken about an hour of compute to find,
compared to a few seconds for two-digit numbers, so we haven’t checked them
all. Now that we defined our sequence for any sticker d, we get some natural
sequences. The first one is the sequence of stickers d for which a>(d) = a≥(d).:

5, 6, 7, 8, 9, 21, 24, 29, 33, 39, 50, 52, 55, 56, 58, 59, 63, 66, 67, . . . .

Another lens on this sequence is those d for which a=(d) exists and a=(d) <
a>(d), which is almost the complement, except that 0 still does not appear:

1, 2, 3, 4, 10, 11, . . . .

We can also extend Table 3, with the value for 10 being 5352172560
followed by 90 zeroes, but the value for 11 is again not so pretty: values up
to 94 are given in the supplementary materials [4].
Finally, we extend A130432 to the multi-digit case. Starting with the
value for the 10 sticker, these are:

3167, 9043, 7485, 1305, 5299, 297, 4659, 1019, 37, 2019, 617, 621, . . . .

Sadly, this sequence has lost the divisibility property: A130432(d) + 1 is
guaranteed to be divisible by d only for d < 10.

9 All Your Base

Of course the sticker sheets that came with VHS tapes had letters too. In-
terestingly, some sticker sheets (e.g., Figure 1) had letters A through F, that
seemed to beg for hexadecimal numbering, though other sheets included the
full alphabet. The algorithms generalize straightforwardly to any base, sub-
stituting base b where we previously wrote 10.
Let us add base b as the second parameter of our functions. For example,
we denote by fd(x, b) the number of times the sticker d is used in the writing
of numbers in the range [1,. . . , x] in base b. Similarly, we add the base to
functions a: a>(d, b), a=(d, b), and a≥(d, b), where we assume that sticker d
is also written in base b.
The unary base, where b = 1, is a special case, as only stickers containing
ones are relevant, and the function fd(x, 1) can be calculated explicitly. For

14

Figure 1: One of the sticker sheets that came with early VHS tapes, with
gratitude to an r/nostalgia user [7].

example, f1(x, 1) = x(x+1)
2 . We leave it for the reader to investigate multi-
digit cases in this base, and from now on, we will assume that b > 1.
Two sequences related to different bases are already in the database.

• Sequence A092175(b) represents our sequence a>(1, b). Starting from
base 1, the sequence a>(1, b) progresses as follows:

2, 3, 13, 29, 182, 427, 3931, 8185, 102781, 199991, 3179143, . . . .

Comfortingly, A092175(10) = 199991, which we already knew from
Table 1.

• Sequence A165617(b) counts the number of solutions to f1(x, b) = x.
Sequence A165617 starts from b = 2 as

2, 4, 8, 4, 21, 5, 45, 49, 83, 10, 269, 11, 202, 412, 479, 15, . . . ,

and, not surprisingly, the ninth term is 83, which we already knew from
Table 2.

By the way, sequence A165617 is easy to calculate, because the largest
possible number such that f1(x, b) = x is known. This number is the con-
catenation of b − 1 ones followed by a single zero written in base b, see the
comment in sequence A165617. Expressed in base 10, these largest numbers
are (starting from index 2):

2, 12, 84, 780, 9330, 137256, 2396744, 48427560, 1111111110, . . . ,

15

and they are in the database as sequence A226238.
We promised to show that the solution to fd(x) = x for a one-digit nonzero
sticker d in base 10 doesn’t exceed d · 10
10. We waited for this moment to
do the proof for any base b.

Proposition 9.1. For any digit d > 0 in base b > d the maximum possible
value of a=(d, b) is bb and all x such that fd(x, b) = x must be ≤ d · bb.

Proof. Similar to base 10, we can calculate that fb(bb) = bb, proving that
a=(d, b) ≤ bb. If x = d · bb, then fd(x, b) = x + 1. All numbers in the
range [d · bb,. . . , (d + 1)bb] have d for the first digit, implying that there are
no solutions to fd(x, b) = x in this range. Then fd((d + 1)bb) = (d + 2)bb.
Converting Lemma 5.1 to base b, we see that no solution can appear among
the next bb numbers, while the next bb numbers use at least bb digits d. By
repeating this ad infinitum, the conclusion follows.

We can generalize Theorem 8.2 to any base b > 2.

Theorem 9.2. The value a=(d, b) is well-defined for any b > 2 and any
d > 0. For b = 2, it is well-defined when d > 0 is not a power of 2.

Proof. By changing 10 to base b in all the right places, the Theorem 8.2 can
be adjusted for any b and d, except when b = 2, and d is a power of b.

As you might have noticed, the theorem above excludes cases when b = 2
and d is a power of 2. We ran our program for those cases, with findings
shown in Table 4, and confirmed that indeed not all seem to exist. We have
not proven an upper bound, but checked for 7 up to 1200 decimal digits, far
larger than the solutions found for larger powers.
We now turn our attention to d = 0. Many of the values a=(0, b) are
undefined. To be sure, we need to check to some upper bound, and it need
not be tight, but how far do we need to check?

Proposition 9.3. For digit 0 in base b > 1, the value of a=(0, b), if it is
well-defined, must be less than bb+3.

Proof. Similar to base 10, it is enough to find a number y > bb, such that
f0(y, b) > y + bb. We are then guaranteed that there are no solutions to
f0(x, b) = x, for x > y.
 16

d {x : fd(x, 2) = x} bits in a=(d, 2)
2 10 21 5
4 100 610 10
8 1000 283187 19
16 10000 35609822115 36
32 100000 300185978028231432373 69
64 1000000 unique value 134
128 10000000 not found!
256 100000000 unique value 520
512 1000000000 unique value 1033
1024 10000000000 1023 consecutive values 2058

Table 4: Solutions for fd(x, 2) = x for stickers d being the binary stickers
corresponding to powers of 2. Larger values are too long to show here.

The number of zeros used in range [bp−1,. . . , b
p − 1] is (p − 1)(b − 1)bp−2.
When p = b+3, then the range contains (b+2)(b−1)bb+1 = bb+3+(b−2)bb+1 ≥
bb+3 + bb zeros, whenever b > 2.
If b = 2, then bb+3 = 32. The number of zeros used in the range [1,. . . , 32]
is 54, which is greater than 32 + 4.
Thus, for b > 1, and y = bb+3, we have f0(y, b) > y + bb, implying that
a=(0, b) < y.

Those bases in which a=(0, b) does not exist are now A364972:

3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 20, . . .

The first few values of a=(0, b) where it does exist are shown in Table 5.

10 Future research

We have stretched the notion of a sticker with the multi-digit case, because
although our definition has nice mathematical properties it uses stickers that
are counted as overlapping, and excludes multi-digit stickers that begin with
a zero. These are of course both decisions that one can relax to explore fresh
possibilities.
 17

base b a=(0, b)
2 8
11 3152738985031
13 3950024143546664
16 295764262988176583799
24 32038681563209056709427351442469835
26 160182333966853031081693091544779177187
28 928688890453756699447122559347771300777482
29 74508769042363852559476397161338769391145562
31 529428987529739460369842168744635422842585510266

Table 5: Values of the “exactly” sequence for the zero sticker in the first few
bases where it exists.

The common inclusion of letter stickers on these VHS sticker sheets invites
not only generalization to other bases, but also generalization to, dare we
say it, textual labels? But this is still a math paper, so let’s not get carried
away: we can restrict ourselves by imagining textual labels that correspond to
spelled-out versions of the numbers! Thus, for some English-like convention
c, a=(“o”, c) = 2 “One”, “twO”),
a=(“e”, c) = 3 (“onE”, “two”, “thrEE”)
a>(“j”, c) undefined “J” does not appear.
Of course there are a jillion variations by language, locale, etc.
Throughout the paper we’ve noted phenomena that seemed interesting
but bear further investigation. Examples include the many solutions to a= in
base 10 that begin with “9465”, what governs whether a= is smaller or greater
than a>, what happens in unary base, whether the sequences are well-defined
for all powers of 2 in base 2, and whether all of those have unique solutions.
We encourage you to look at the tables in the supplementary materials, as
there are many more patterns begging for attention.
One such pattern we see in the data, but have not proven anything about
is that the number of digits in a=(b, b) equals b2 + b + 3, for b > 2. The
solutions, expressed in their respective bases in Table 6, all have a similar
form for b > 2: the first digits are 1, then 0, then digits b − 1, finishing with
b − 2, 1, 0.
And of course the sequences we described in this paper can be extended,

18

base length a=(b, b) or equivalently, a=( 10 , b)
2 5 101012,
3 9 1022221103,
4 15 1033333333332104,
5 23 104444444444444444443105,
6 33 1055555555555555555555555555554106.

Table 6: Lengths and values of a=( 10 , b) for the first few bases b.

and there are many related sequences to be cataloged. We would love to hear
tales from your explorations. Enjoy the sequence hunt!

11 Acknowledgments

We are grateful to Alexey Radul for his helpful suggestions. We are also
thankful to the anonymous reviewers of the American Mathematical Monthly
for encouraging us to dig deeper into the topic and providing helpful ideas
and suggestions.

References

[1] David. H. Bailey and Richard E. Crandall, Random Generators and Nor-
mal Numbers. Exper. Math. 11, 527–546, 2002.

[2] Jon L. Bentley and Andrew C. Yao. An Almost Optimal Algorithm
for Unbounded Searching. Information Processing Letters, 3(3):144–147,
1976.

[3] Google Labs Aptitude Test, Google, 2004.

[4] Gregory Marton and Tanya Khovanova. Archive Labelling Se-
quences: Code. 2023. https://colab.research.google.com/drive/
1pGfgQWvJR1IAG3t4dNnrTnc07UvyV4xC

[5] OEIS Foundation Inc. (2023), The On-Line Encyclopedia of Integer Se-
quences, Published electronically at https://oeis.org

19

[6] Ponder This, (2004), available at https://research.ibm.com/haifa/
ponderthis/challenges/April2004.html.

[7] The stickers that came with blank VHS tapes. Posted by Reddit user
u/morbidlyatease in r/nostalgia, used with permission. Posted March 24,
2022. https://www.reddit.com/r/nostalgia/comments/tm21n4/the_
stickers_that_came_with_blank_vhs_tapes/

20
