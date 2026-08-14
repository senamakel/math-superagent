<!-- source: https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf | converted from PDF -->

Archive Labeling Sequences

Tanya Khovanova and Gregory Marton

Abstract. What follows is the story of a family of integer sequences, which started life as a
Google interview puzzle back in the previous century when VHS video tapes were in use.

1. GOOGLE’S PUZZLE.

Question 1.

Suppose you are buying VHS tapes and want to label them using the stickers that came in the
package. You want to number the tapes consecutively starting from 1, and the stickers that
come with each package are exactly one of each digit [ 0 , ... , 9 ]. For your ﬁrst tape, you
use only the digit 1 and save all the other digit stickers for later tapes. The next time you
will need a digit 1 will be for tape number 10. By this time, you will have several unused 1
stickers. What is the next tape number such that after labeling the tape with that number, you
will not have any 1 stickers remaining?

A careful reader may raise some objections. First, the tape curator may run out
of 1 stickers in the middle of labeling a tape, having too few to ﬁnish labeling it;
in this case we need to look for an answer at a higher value, and may never ﬁnd one.
Second, the happy owner of the tapes might hypothetically run out of another sticker
before the sticker of interest, e.g., sticker 2 , while looking for the place where we run
out of 1 s. Intuitively, we can expect that sticker 1 is the ﬁrst to run out, and we will
prove this later.
A version of this puzzle appeared in the Google Labs Aptitude Test [1] which in-
troduced some notation to aid in expressing the ideas precisely. Ignoring the issue of
running out of other stickers before sticker 1, this version is equivalent to the version
above.

Question 2.

Consider a function f which, for a given whole number x, returns the number of ones required
when writing out all numbers between 0 and x inclusive. What is the next largest x after x = 1
such that f1(x) = x?

In this notation, the ﬁrst objection above is that it is unclear if any x> 1 even exists
such that f1(x) = x.
In teaching, we often ask students to ﬁnd things that do not exist, expecting a proof
of non-existence. While such problems may be considered evil, they are legitimate. At
the time, Google’s unofﬁcial motto was “Don’t be Evil”, and they weren’t: we will see
that the answer does indeed exist.

doi.org/10.1080/00029890.2025.2525050
MSC: 00A08
' 2025 The Author(s). Published with license by Taylor & Francis Group, LLC.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License
(http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in
any medium, provided the original work is properly cited. The terms on which this article has been published
allow the posting of the Accepted Manuscript in a repository by the author(s) or with their consent.
 1

In our quest to pick apart the details and formalize the problem, we shall develop a
few more tools, but those impatient for a more precise formulation may skip ahead to
Question 5.

2. ONES COUNTING FUNCTION. Questions 1 and 2 are interested in just the
digit 1 . We can be more general in our notation while still focusing on ﬁnding those
ﬁrst answers. For any digit d ∈ [0,... , 9] and a whole number x, let fd(x) be the num-
ber of times the digit d is required when writing out all the whole numbers between 0
and x inclusive. For example, f1(13) = 6. Notice that f1(1) = 1.
Our function f1(x) is the number of 1 stickers needed to label all the tapes up
to tape x. When f1(x) = x, then we have used all of the 1 stickers in labeling the
ﬁrst x tapes. The function f1(x) can be found in the Online Encyclopedia of Integer
Sequences [2] as sequence A094798.
In the single and double-digit numbers, there are ten of each nonzero digit in the
ones column and ten in the tens column, so 20 altogether. Early on, the tape number is
ahead of the digit count. By the time we get to 20-digit numbers, though, there should
be, on average, two of any single nonzero digit per number.1 Thus the number of times
that any digit is used should eventually catch up with the tape numbers.
Encouraged by assurance of reaching our goal somewhere, we might continue our
estimate. In the up-to three-digit numbers, those less than 10
4, there are 300 of each
nonzero digit; in the numbers below 10
5, there are 4 000; then 50 000 below 10
6, and
so on up to 10
10, where fd>1(x) and x must (almost) meet. In particular, there are
10 000 000 000 counts for any nonzero digit in the numbers below 10 000 000 000, or
formally fd>1(10
10) = 10
10. Hence, were the puzzle asking about any of the digits 2—
9, then ten billion could have been an easy answer, or at least a limit on how far we
need to search.
Sadly, there is a 1 in the decimal representation of ten billion (and a few zeros), so
we require 10
10 + 1 digits 1 to write the numbers [1,... , 10
10]. Thus, f1(10
10) ̸= 10
10,
so 10
10 cannot be the answer to the original puzzle. Thus stymied, we wrote a program
to ﬁnd the solution to Question 2. And the answer turned out to be a=(1) exists and
equals 199 981, much smaller than we expected.

3. COUNTING OTHER DIGITS. We were so enjoying our stymie
2 that we then
wrote a program to solve the puzzle for any nonzero digit.

Deﬁnition 3. We denote by a=(d) the smallest number x> 1 such that the decimal
representation of d appears as a substring of the decimal representations of the num-
bers [1,... ,x] exactly x times:

a=(d) = min({x> 1: fd(x) = x}).

We already know that a=(1) is 199 981. The sequence a=(d), which now has num-
ber A163500, continues as follows:

28 263 827, 371 599 983, 499 999 984, 10 000 000 000,

9 500 000 000, 9 465 000 000, 9 465 000 000, 10 000 000 000.

Did you expect this sequence to be increasing? You could have because smaller
numbers tend to contain smaller digits than larger numbers. Then why is the sequence
not increasing? As we failed to ﬁnd a value for the digit 5 below ten billion, we
noticed that it is fairly easy to imagine a scenario where you have one less than the

1We’re looking at nonzero digits for now only because one would not use stickers for leading zeros, unlike
other leading digits, but we will return to zeros shortly.
2Yes, we just nouned that verb.

2 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA

number you need (fd(x) = x − 1), and then the next value has more than you need
for equality (fd(x + 1)>x + 1), and then you equalize again later. In response, we
decided to look at a related sequence.

Deﬁnition 4. Let
 a>(d) = min({x : fd(x) > x}).

The key difference is in using “more than” rather than “exactly”. Thus we will
also call our a=(d) sequence the “exactly” sequence and our a>(d) the “more than”
sequence.
We later discovered that the “more than” sequence was published at IBM’s famous
puzzle website “Ponder This” in April 2004 and was authored by Michael Brand [3].
This version is quite natural as it wonders when we ﬁrst run out of the labels. Moreover,
the 1 sticker plays a special role in this puzzle as it must be the digit that will run
out ﬁrst, as we see in the following table, and which we prove in our accompanying
paper [4].
Starting at 1, Table 1 shows the ﬁrst nine terms of the “exactly” and “more than”
sequences.
 Table 1. Theﬁrstnineterms of a=(d) and a>(d).
da=(d) a>(d)
1 199 981 199 991
2 28 263 827 28 263 828
3 371 599 983 371 599 993
4 499 999 984 499 999 994
5 10 000 000 000 5 555 555 555
6 9 500 000 000 6 666 666 666
7 9 465 000 000 7 777 777 777
8 9 465 000 000 8 888 888 888
9 10 000 000 000 9 999 999 999

Looking at the table, we can satisfy our intuitive expectation that we run out of
stickers 1 before we run out of any greater digits. There is still a sticky question of
when we run out of sticker 0 . Intuitively, we use zeros much less than other digits,
and we devote Section 5 to zero and show that we run out of zeros much much later.
Given that we do run out of 1 stickers ﬁrst (a>(d) ≥ a>(1) for all d), we must
note that the a= sequence for the other digits breaks somewhat with the spirit of the
question, because when we are counting tapes for sticker 2 (or indeed any higher
digit) we will have long run out of sticker 1 , so we need an additional assumption,
e.g., that we have an inﬁnite supply of stickers to borrow. Otherwise, in the strictest
sense, the only digit for which Question 1 is meaningful is 1 .
Looking more closely at the table, we see that some of these rows are interesting in
their own right. Notice that 199 991 is ten more than the previously found 199 981. For
all the numbers in between, the initial equality holds (∀i ∈ [199981,... , 199991] we
have i = f1(i)). Likewise, for d = 3 , each of the numbers between 371 599 983 and
371 599 993 has exactly one three, so the increase in a number by one is the same as the
increase in the count of threes. A similar situation holds for 4 . There is a new situation
for 2 , where the next value immediately uses more stickers than we have. And it is
different yet for stickers d ={ 5 ... 9 }, because in these cases a=(d) > a>(d),sowe
run out of the sticker of interest in the middle of labeling a tape before we later have a
chance to exactly ﬁnish labeling one.
Now we can give a mathematical formulation of the original VHS puzzle:
 3

Question 5.

Does a=(1) exist, and if so, does it also satisfy a=(1)<a>(d) for each d ∈{0, 1,..., 9}?

Note that the latter condition is needed to make sure that we do not run out of any other
sticker before we use up all 1 stickers.
The sequence a> can be found using the identiﬁer A164321 in the OEIS. Unsurpris-
ingly, the values matching this relaxed second condition are more well-behaved than
those with equality.
Did you notice that the second column is increasing? This might be surprising for
the fans of the Champernowne constant. What’s the Champernowne constant? Imagine
you placed an inﬁnitude of labeled VHS tapes in order. The labels together will read
as a concatenation of all positive integers whose digits form the sequence A033307.
Now we add a zero with a dot in front to get the constant:

0.12345678910111213141516 ....

The constant is most famous for being a “normal” number in any base [5]. Here normal
is a mathematical term referring to the distribution of digits. Normal means that all
possible strings of digits of the same length have the same density. This means that
every digit in base 10 appears with the same density. Despite this, our second column
is increasing, demonstrating an unsurprising fact that smaller digits appear earlier than
the bigger digits.

4. MORE “EXACTLY” SEQUENCES. We want to introduce a few more related
sequences, one per digit, where the letter E symbolizes exactness or equality.
Deﬁnition 6. Let Ed be an increasing sequence of positive integers x such that
fd(x) = x.

The sequence Ed must be ﬁnite. After all, starting from 11-digit numbers, the supply
of labels starts decreasing. We eventually have to run out of labels. We can be more
precise in claiming that the largest value in Ed is not more than d10
10. We prove the
claim for this and other bases in our accompanying paper [4].
The sequences Ed are connected to our sequence a=(d) as follows:

a=(d) =
 {
Ed(2) for d = 1
Ed(1) otherwise .

Recall, the special case for sticker 1 is what made the puzzle interesting because
E1(1) = 1. The sequences Ed are in the OEIS database, and we show their A-numbers
and lengths in Table 2.

Table 2. The sequence numbers for Ed and their lengths.

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

4 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA

The numbers of terms are their own sequence! It appears in the OEIS in disguise:
sequence A130432 is the last column of Table 2 plus 1, because the sequence author
assumed that tapes would be numbered starting with 0. While that choice may have
tempted the audience of this paper,3 it would not have been common practice. How-
ever, if we did start at zero, and thus add 1 to the last column, we see a neat pattern:
the result is divisible by d. This hides an even more interesting fact: the actual values
of Ed are periodic modulo 10
10, while being bounded by d · 10
10 [4].
To explain periodicity, we observe that for 0 ≤ x< (d − 1)10
10,wehave fd(x +
10
10) = fd(x) + 10
10. This is due to the fact that only the last ten digits contribute to
the count, because if the number has 11 digits, then the ﬁrst digit is less than d.In
addition, the last ten digits go through all possible 10-digit strings when the number
changes from x + 1to x + 10
10. Thus the count of the number of digits d increases
exactly by 10
10. It follows that the numbers x and x + 10
10 are either both mem-
bers of the sequence E(d) or both non-members. Thus the number of the solutions
to the equation fd(x) = x in the range [0,... , 10
10 − 1] is the same as in the range
[r10
10,... ,(r + 1)10
10] − 1, when r< d. Hence, we have d ranges with the same
number of solutions, which explains the divisibility of A130432(d) by d.
When studying Table 1, you might notice that stickers 5 and 9 delay the start of the
corresponding exact sequences until the latest possible value of x of 10 000 000 000.
Not surprisingly, in Table 2, the count for the number of terms for values 5 and 9 is
much smaller than for other stickers. Due to the argument in the previous paragraph,
all solutions of fd(x) = x for d equaling 5 or 9 have to be of the form r10
10, where
r< d. Thus the last column of Table 2 has to be the smallest possible value of exactly
d − 1.
Now that the upper bound is clear, we can ﬁnd the largest values and treat them as
another sequence, shown in Table 3.

Table 3. Largest values of x,where fd (x) = x.

d max(E(d))
1 1 111 111 110,
2 10 535 000 000,
3 20 500 000 000,
4 30 500 000 000,
5 40 000 000 000,
6 59 628 399 995,
7 69 971 736 170,
8 79 998 399 997,
9 80 000 000 000.

Let’s now dive deeper into the d = 0 case.

5. COUNTING ZEROS. In counting zeros, let us recall that the puzzle speciﬁes
that the ﬁrst VHS tape is labeled with the 1 sticker, not 0 . Expanding on f ,we
denote the function that calculates zeros in numbers 1 through x inclusive as f0(x).It
is represented in the OEIS as sequence A061217.
We calculated that the smallest number x such that x is less than or equal to the num-
ber of 0s in the decimal representations of [1,... ,x] is 100 559 404 366, equivalently
this number is a>(0). But what is the corresponding number for the a= sequence? It
appears that no such number exists. To prove it, we need to start with a lemma.

3If you numbered your VHS tapes starting at zero, please send a note, kindred spirit!
 5

Lemma 7. For any integer x> 10
10, we have f0(x + 10
10) ≥ f0(x) + 10
10.

Proof. Indeed, numbers between x and x + 10
10 go through all possible combinations
of the last ten digits. The set of all possible 10-digit strings contains 10
10 of each digit.
Hence they contain at least 10
10 zeros.

Now we are ready to prove our theorem.

Theorem 8. The value a=(0) is not well-deﬁned.

Proof. We calculated that f0(100 559 404 366) = 100 559 404 367. Its predecessor
then must be f0(100 559 404 365) = 100 559 404 364 with three fewer zeros. We ver-
iﬁed that there were no equalities up to this point, and indeed up to a bigger number,
but of course we couldn’t continue checking up to inﬁnity.
So we need other arguments. Notice that the number 100 559 404 366 has three
zeros. Hence, for some y that are not much bigger than 100 559 404 367, we will have
the case that f0(y + 1) ≥ f0(y) + 3. For some time, the sequence f0 will increase in
steps of not less than three. We are getting away from the equality at high speed.
Were we dealing with random 12-digit numbers, then such numbers would have on
average 11/10 zeros. Hence f0(x) grows faster than x at this point. But this consid-
eration is not a proof. To ﬁnish the proof of the theorem, we need to ﬁnd a number
y> 10
10 such that f0(y) > y + 10
10 and check that there is no solution to f0(x) = x
below y. By Lemma 7, that number y would guarantee that f0(x) will always be ahead
of its index after y.
Let us ﬁnd such a number. We start with 100 559 404 366. The sequence f0(x) will
continue to grow not slower than its index x until the next number that doesn’t contain
zeros. Such a number is 111 111 111 111. We calculated that f0(111 111 111 111) =
120 987 654 321. So the number of zeros is way ahead of the number itself. As
the sequence f0(x) is nondecreasing, we can’t have y such that f0(y) = y until
120 987 654 321. This way, we can speed up the process, and we need to search only a
few of the available values. After 796 iterations we found that f0(201 416 002 345) =
212 646 497 702, thus concluding the proof of the theorem.

6. GREATER OR EQUAL. In addition to a= and a>, we counted the “greater or
equal” sequence a≥(d), where d again denotes the sticker in question. The great prop-
erty of this latter sequence is that

a≥(d) = min(a=(d), a>(d)).

This sequence appears in the database as sequence A164935.
One more caveat: we deﬁned a=(1) to be the smallest number greater than 1 sat-
isfying the VHS property. This complicated condition was needed so that the se-
quence would include the solution of Google’s puzzle, 199 981, as the ﬁrst term. But
A164935(1) = 1 as it should be. This sequence is nondecreasing for the same rea-
son the “more than” sequence is nondecreasing. We prove this in our accompanying
paper [4].

7. THE ALGORITHMS. In this section, we describe a more efﬁcient way to ﬁnd
fd(x), with code and details in [6]. We counted the digit d separately in each decimal
place it occurred. Suppose we want to count how many times the digit d occurred in
the k-th place from the right in the set [1,... ,x]. It depends on which digit the number
x has in the k-th place from the right. Suppose this digit is xk. Consider the number
y =⌊x/10
k⌋10
k. We chose y because it is the largest number not exceeding x with k
zeros at the end. In the range [1,... ,y − 1], if we pad smaller integers with zeros on

6 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA

the left, each digit appears in the k-th place from the right the same number of times.
Therefore any digit d> 0 appears in this range y
10 =⌊x/10
k⌋10
k−1 times.
Now, we need to calculate how often d appears in the place of interest in the range
[y,... ,x]. If xk <d, then it doesn’t appear at all. If xk >d > 0 we need to add 10
k−1.
If xk = d> 0, we need to add the total count of our digit in the range, which is
(x mod 10
k−1) + 1.
We need to consider the case of d = 0 separately, as we should not count lead-
ing zeros, nor zero itself, as the sequence starts at 1. If xk >d = 0, the count is
⌊x/10
k⌋10
k−1, (the same as the xk <d case for other digits), but if the k-th digit is
zero, we need to subtract the number of digits in the range [1,... ,y − 1] that have
fewer than k digits and add the number of digits in the range [y,... ,x] that have 0 in
the k-th place from the right. Thus the adjustment is −10
k−1 + (x mod 10
k−1) + 1.
To summarize, we would like to express fd(x) as the sum of the contributions cd(xk)
of the counts of the digit d in the k-th place from the right. This contribution depends
on the value of xk. Let Y be shorthand for ⌊x/10
k⌋· 10
k−1, then:

cd(xk) =
 ⎧
⎪⎪⎪⎪⎪⎨

⎪⎪⎪⎪⎪⎩
Y when d> 0 and xk <d
Y + (x mod 10
k−1) + 1 when d> 0 and xk = d
Y + 10
k−1 when d> 0 and xk >d
Y when d = 0 and xk >d
Y − 10
k−1 + (x mod 10
k−1) + 1 when d = 0 and xk = d
 .

Summing over each k-th place, we get

fd(x) = ∑

k cd(xk). (1)

We can now use this closed form for fd(x) in much faster searches for a≥(d).Todo
so, we need the following lemma that allows us to skip a lot of numbers in our search.

Lemma 9. Suppose we already know that a≥(d) > x. Suppose, in addition, we can
show that fd(y)<x for some y> x. Then a≥(d) > y.

Proof. As fd is nondecreasing and fd(y) < x, we know that the value of func-
tion fd on any element in the range [x,... ,y] is not greater than x. It follows that
a≥(d)>y.

We search the inﬁnite space of possible values using a variation of an unbounded
binary search [7]. We call a range of numbers [x,... ,x + p] “safeleft” if we can guar-
antee that a≥(d) > x. We start with a safeleft range [2, ... , 3]. When d = 1, we can’t
start with the range whose left side is 0, as we will get the answer 1, which we want to
skip. It is easy to see that the base case holds for 2 in other words, fd(2)< 2 for any
d, as we only use one 1 and one 2 sticker up to tape number 2. Then we iterate to the
next safeleft range as follows:

• If fd(x + p)<x, then a≥(d) is not in the range by Lemma 9, making any range
starting with x + p safeleft. The next range to search is [x + p,... ,x + 3p], where
we move the start of the range to x + p and double the size of the range.

• If fd(x + p) ≥ x, then a≥(d) is not guaranteed to be outside of the range. The next
range to search is [x,... ,x + p/2], where we keep the start of the range and halve
the size of the range.

• Suppose we reduced the range size to 1. Then if fd(x) < x and fd(x + 1) ≥ x + 1,
we have a≥(d) = x + 1. If not, then any range starting with x + 1 is safe, and the
new range is [x + 1,... ,x + 3].
 7

After the value of a≥(d) is found, one would like to determine the values of a=(d)
and a>(d). First, we check whether a≥(d) equals a=(d) or a>(d). Let us examine the
case a≥(d) = a=(d) ﬁrst. In that case, ﬁnding the value of a>(d) is easy for nonzero
digits. We just need to check several next values.
The next case is when a≥(d) = a>(d). Now we are looking for the exact sequence
a=(d), and the answer is not always near a≥(d), but we can still search rapidly. If we
already showed that a=(d) > x and if fd(x) > x, then a=(d) ≥ fd(x). After all, if we
saw no digits d in the range [x,... ,fd(x) − 1] at all, x would not catch up to fd(x)
below fd(x). Thus we begin our search for a=(d) anew with safeleft = fd(a>(d)), and
width = 1, stopping either when we ﬁnd a=(d), or when fd(x)>x + 10
10.

8. NEXT STEPS. Of course the sequences we described in this paper can be ex-
tended, and there are many related sequences to be cataloged. We have already begun
to investigate multi-digit versions of these sequences, and the analogous sequences in
different bases, among others [4]. We would love to hear tales from your explorations,
as well! Enjoy the sequence hunt!

ACKNOWLEDGMENTS. We are grateful to Alexey Radul for his helpful suggestions. We are thankful
to anonymous reviewers for encouraging us to dig deeper into the topic and providing helpful ideas and
suggestions.

DISCLOSURE STATEMENT. No potential conﬂict of interest was reported by the author(s).

REFERENCES

[1] Google Labs Aptitude Test, Google; 2004.
[2] OEIS Foundation Inc. The on-line encyclopedia of integer sequences; 2023. Published electronically at
available from: https://oeis.org
[3] Ponder This; 2004. Available from: https://research.ibm.com/haifa/ponderthis/challenges/April2004.
html.
[4] Khovanova T, Marton G. Archive labelling sequences; 2024. Available from: https://arxiv.org/abs/2305.
10357
[5] Bailey DH, Crandall RE. Random generators and normal numbers. Exp Math. 2002;11:527—546.
[6] Marton G, Khovanova T. Archive labelling sequences: code; 2023. Available from: https://colab.research.
google.com/drive/1pGfgQWvJR1IAG3t4dNnrTnc07UvyV4xC
[7] Bentley JL, Yao AC. An almost optimal algorithm for unbounded searching. Inf Process Lett.
1976;3(3):144—147.
[8] The stickers that came with blank VHS tapes. Posted by Reddit user u/morbidlyatease in r/nostalgia, used
with permission. Posted March 24, 2022. Available from: https://www.reddit.com/r/nostalgia/comments/
tm21n4/the stickers that came with blank vhs tapes/

TANYA KHOVANOVA is a lecturer at MIT and works with several programs that help young students who
are gifted in math: PRIMES, PRIMES STEP, MathRoots, and RSI. She received her Ph.D. in Mathematics
from Moscow State University in 1988. Her current interests lie in combinatorics, number theory, probability
theory, geometry, and recreational mathematics. Her website is at tanyakhovanova.com, her highly popular
math blog is at blog.tanyakhovanova.com, and her Number Gossip website is at numbergossip.com.
Department of Mathematics, MIT, Cambridge, MA 02139
tanya@math.mit.edu

GREGORY MARTON is a visiting lecturer at Tufts University and a stay-at-home parent. He holds an
Engineer’s Degree in computer science from MIT. He was very active in recruiting and interviewing at Google
around the time that this puzzle was in use. He currently teaches about large language models and education
at Tufts, and his interests include natural language understanding, cognitive science, linguistics, and anything
that he can share with youngsters.
ExCollege, Tufts University, Medford, MA 02155
gremio@acm.org

8 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA
