<!-- source: https://nntdm.net/papers/nntdm-29/NNTDM-29-3-474-485.pdf | converted from PDF -->

Copyright © 2023 by the Author. This is an Open Access paper distributed under the
terms  and  conditions  of  the  Creative  Commons  Attribution  4.0  International  License
(CC BY 4.0). https://creativecommons.org/licenses/by/4.0/

Notes on Number Theory and Discrete Mathematics
Print ISSN 1310–5132, Online ISSN 2367–8275
2023, Volume 29, Number 3, 474–485
DOI: 10.7546/nntdm.2023.29.3.474-485

Digits of powers of 2 in ternary numeral system

Yagub N. Aliyev

School of IT and Engineering, ADA University
Ahmadbey Aghaoglu str. 61, Baku, AZ1008, Azerbaijan
e-mail: yaliyev@ada.edu.az

Received: 23 November 2022  Revised: 22 June 2023
Accepted: 27 June 2022  Online First: 10 July 2023

Abstract: We study the digits of the powers of 2 in the ternary number system. We propose an
algorithm for doubling numbers in ternary numeral system. Using this algorithm, we explain the
appearance  of  “stairs”  formed  by  0s  and  2s  when  the  numbers  2
𝑛 (𝑛 = 0,1,2, … )  are  written
vertically so that for example the last digits are forming one column, the second last digits are
forming another column, and so forth. We use the patterns formed by the leftmost digits, and the
patterns formed by the rightmost digits to prove that the sizes of these blocks of 0s and 2s are
unbounded. We also study how this regularity changes when the digits are taken between the left
end and the right end of the numbers.
Keywords: Ternary numeral system, Benford’s law, Digits, Zeros, Twos, Powers of two.
2020 Mathematics Subject Classification: Primary: 11A63; Secondary: 11A07, 11B83.

1  Introduction

In 1979, Paul Erdős conjectured that there are only finitely many positive integers 𝑛 such that 2
𝑛
can  be  written  as  sum  of  distinct  powers  of  3.  This  is  equivalent  to  saying  that  its  ternary
representation does not contain the digit 2 (see p. 67 in [5], p. 80 in [6]). Neil Sloane  and Eric
Weisstein made similar conjectures for digits 0 and 1 ([13, 16, 17] and [20], p. 28). The digits of
powers  of  2  in  ternary  numeral  system  were  also  studied  in  [20],  p.  20–25.  The  encyclopedic
entries  [13]  and  [17]  contain  many  references  and  results  related  to  ternary  representations,
including connections with Collatz conjecture and cellular automaton. Similar questions for decimal

475

numeral system were asked and answered in [4, 19]. In the current paper we studied the patterns
formed by the ternary digits of 2
𝑛, when these numbers are taken together and individually.
Let us write first powers of two  (1,2,4, … , 2
18) in ternary numeral system so that all their
digits in the corresponding place values are aligned along vertical columns (see Table 1.1).
  1 1 1 0 2 2 1 2 1 0 0 1 = 2
18

  2 0 1 2 2 2 1 0 1 1 2 = 2
17

  1 0 0 2 2 2 2 0 0 2 1 = 2
16

    1 1 2 2 2 2 1 1 2 2 = 2
15

      2 1 1 1 1 0 2 1 1 = 2
14

      1 0 2 0 2 0 1 0 2 = 2
13

        1 2 1 2 1 2 0 1 = 2
12

          2 2 1 0 2 1 2 = 2
11

          1 1 0 1 2 2 1 = 2
10

            2 0 0 2 2 2 = 2
9

            1 0 0 1 1 1 = 2
8

              1 1 2 0 2 = 2
7

                2 1 0 1 = 2
6

                1 0 1 2 = 2
5

                  1 2 1 = 2
4

                    2 2 = 2
3

                    1 1 = 2
2

                      2 = 2
1

                      1 = 2
0

 1 1 2
0 2 1
1 2 2
2 1 1
1 0 2
2 0 1
2 1 2
2 2 1
2 2 2
1 1 1
2 0 2
1 0 1
0 1 2
1 2 1
0 2 2
0 1 1
0 0 2
0 0 1

  Table 1.1.  Table 1.2.
  In the future, we will refer to this infinite list simply as the table or the construction. We can
easily observe several interesting patterns from this table.

I Observation.  If we look only at the rightmost 𝑘 digits of each power of two, then, as we go
upwards along the table, we can see that all possible 𝑘-digit endings (of course,
except those which ends with 0) appear in the table and they repeat periodically
(see  [20],  p.  2025).  For  example,  if  𝑘 = 3,  then  there  are  2 ∙ 3
𝑘−1 = 18
possible 3-digit endings and all of them appear in the rightmost 3 columns of
the  above  table  and  will  appear  periodically  with  period  2 ∙ 3
𝑘−1 = 18  (see
Table 1.2).

II Observation.  If we look only at the leftmost  𝑘 digits, then we can see that all the possible
𝑘-digit headings (of course, excluding those which start with 0) appear but this
time not periodically (cf. Exercise 20.3.2 in [10, p. 502]). For example, if 𝑘 =
2,  then there are 2 ∙ 3
𝑘−1 = 6 possible 2-digit headings (10, 11, 12, 20, 21, 22)
and all of them appear in the table, although not with the same frequency. One
can notice that the numbers starting with smaller two-digit blocks such as 10 or
11,  appear  more  frequently  than  larger  two-digit  blocks,  say,  21  or  22  (see
Table 1.3).

 476

III Observation. The digits 0 and 2 (alternatively) appear in triangular blocks (see the red and
blue parts of Table 1.1, where each step is of height either 1 or 2 digits and of
length 1 digit). One such block is shown in Table 1.4 which is formed using
some of the digits of 2
15, 2
16, … , 2
20 (see also Table 2.1 below). The total height
of each of these blocks is greater than or equal to its total length, which can be
arbitrarily  large  as  𝑛  (i.e.,  the  exponent  of  2)  is  free  to  run  over  the  positive
integers. These blocks of twos are not touching each other except diagonally.
The same is true for the blocks of zeros.

𝟐 𝟎 0 2 2 2
𝟏 𝟎 0 1 1 1
  𝟏 𝟏 2 0 2
    𝟐 𝟏 0 1
    𝟏 𝟎 1 2
      𝟏 𝟐 1
        𝟐 𝟐
        𝟏 𝟏
          2
          1

         The total height is 6.
2       ← Step of height 1 and length 1.
2 2
2 2     ← Step of height 2 and length 1.
2 2 2   ← Step of height 1 and length 1.
2 2 2 2
2 2 2 2 ← Step of height 2 and length 1.
        The total length is 4.

  Table 1.3.  Table 1.4.

We will prove that both observations I and II are in general true. The observations I and II
will  be  expressed  as  Lemma  3.3  and  Lemma  4.1,  respectively,  which  are  used  to  prove
Theorem  5.1,  the  main  result  of  the  current  paper  that  generalizes  the  observation  III.  Some
formulae for the probability of occurrence of certain blocks of digits in between the first and last
digits of the number are proved. These formulae are then used to show that the probabilities for
different 𝑘-digit blocks are different but as these blocks of digits shift in the direction of the right
side of the numbers, the probabilities become more and more uniform.

2  The structure of the stairs

We need to determine the rules obeyed by the digits when the numbers are doubled. This will help
us to explain the patterns in Observation III above and prove the main result (Theorem 5.1) below.
Let us first describe the algorithm for doubling an arbitrary positive integer in ternary numeral

system. Consider the substitutions 𝐴 = (0 1 2
0 2 1
) = (0)(12) and 𝐵 = (0 1 2
1 0 2
) = (01)(2),

which we prefer to write as 𝐴 = (0 2 1
↑ ↑ ↑
0 1 2) and 𝐵 = (1 0 2
↑ ↑ ↑
0 1 2), because we go upwards as

we double the numbers and write the digits.

1)  Add an extra 0 to the left of the given number. Start with the rightmost digit of the number
and apply 𝐴. Write the result above this digit.

2)  If we obtained 0 or 2, then for the next digit of the number to the left, we use the last used

477

substitution, otherwise if we obtained 1 then we switch to the other substitution, and apply
it for the next digit on the left. Write the result above the digit.

3)  Return to Step 2) unless you already reached the extra 0 at the left end.

For example, we can use this algorithm to double 131072 = (20122210112)3.
    𝐵 𝐴 𝐵 𝐵 𝐵 𝐵 𝐴 𝐴 𝐵 𝐵 𝐵 𝐴
  1 1 1 0 2 2 1 2 1 0 0 1
Extra zero → 0 2 0 1 2 2 2 1 0 1 1 2

After completion of the algorithm, we erase the leftmost extra zero of the original number and, if
there is any, the leftmost extra zero of the resulting number. The proof of this algorithm is self-
evident, since each time the digit 1 appears as a result of the algorithm, there is a change in the
number carried over the next place value. Let us see how this algorithm is applied to a string of
twos in a number. Suppose that we have a string of twos as in the red part of the numbers in the
following Table 2.1.
  2
21 = ⋯ 1 1 2 2 0 2 …
2
20 = ⋯ 0 2 1 1 0 2 …
2
19 = ⋯ 1 2 2 0 1 2 …
2
18 = ⋯ 0 2 2 1 2 1 …
2
17 = ⋯ 1 2 2 2 1 0 …
2
16 = ⋯ 0 2 2 2 2 0 …
2
15 = ⋯ 1 2 2 2 2 1 …
2
14 = ⋯ 2 1 1 1 1 0 …

  Table 2.1.
  According to the described doubling algorithm, the digit 2 can be obtained only from 1 (the
substitution 𝐴) or from 2 (the substitution 𝐵). In both cases, we keep using the same substitution
until we run out of twos. Because of this, either
1.  all these twos are obtained from only ones (e.g., check above how the red digits of 2
15 are
obtained from 2
14),
2.  or all these twos are obtained from again the twos (e.g., check above how the red digits of
2
16 are obtained from 2
15).
On the other hand, it is not possible to have three or more vertical 2s or two or more horizontal
2s  on  one  step  of  the  construction.  One  can  put  all  possible  combination  of  digits  instead  of
asterisks (∗), which stands for a non-two digit, and, if necessary, instead of dots (…), which stands
for any digit, to check that the following two cases are not possible.
  … … … … … …
… 2 2 2 ∗ …
… 2 2 2 ∗ …
… 2 2 2 ∗ …
… 2 2 2 2 …

 … … … … … …
… 2 2 ∗ … …
… 2 2 2 2 …
… 2 2 2 2 …

478

This shows that each step of the triangular block of twos is of vertical height either 1 or 2
digits and of horizontal length of only 1 digit. This also proves that the total height of each of
these blocks is greater than or equal to its total length. The same method works for the triangular
blocks of zeros.

3  The last digits

In the present section we prove the main result of this paper by showing that Observation I is valid
for any arbitrarily large value of 𝑘, thanks to the following pair of lemmas.

Lemma 3.1. For any given 𝑘 ∈ ℤ
+, 3
𝑘| (2
3𝑘−1 + 1), and 3
𝑘+1 ∤ (2
3𝑘−1 + 1).

Proof.  Lemma  3.1  can  be  proved  using  the  method  of  mathematical  induction.  Denote

𝐴𝑘 = 2
3𝑘 + 1. For 𝑘 = 1 we have 3
1|𝐴0, but 3
2 ∤ 𝐴0. Suppose that it is true for 𝑘 = 𝑛, that is

3
𝑛+1|𝐴𝑛,  but  3
𝑛+2 ∤ 𝐴𝑛.  Then  𝐴𝑛+1 = 23𝑛+1 + 1 = (2
3𝑛)3 + 1 = (23𝑛 + 1)(2
2∙3𝑛 − 2
3𝑛 + 1)

= 𝐴𝑛(𝐴𝑛
2 − 3 ∙ (𝐴𝑛 − 1)) = 𝐴𝑛(𝐴𝑛
2 − 3𝐴𝑛 + 3).  Note  that  3|(𝐴𝑛
2 − 3𝐴𝑛 + 3)  but
3
2 ∤ (𝐴𝑛
2 − 3𝐴𝑛 + 3). Therefore, 3
𝑛+2|𝐴𝑛+1, 3
𝑛+3 ∤ 𝐴𝑛+1, and this completes the proof.  

Lemma 3.2. For any given 𝑘 ∈ ℤ
+, 3
𝑘|2
2∙3𝑘−1 − 1 and 3
𝑘+1 ∤ 2
2∙3𝑘−1 − 1.
Proof. The statement easily follows from Lemma 3.1 by observing that

  2
2∙3𝑘−1 − 1 = (23𝑘−1 − 1) (2
3𝑘−1 + 1)  and 3 ∤ (2
3𝑘−1 − 1).  

Note.  By  invoking  Lemma  3.1  and  Lemma  3.2,  we  could  also  use  the  special  case  of  Euler’s

Theorem, which says that 2
𝜑(3𝑛+1) ≡ 1 (mod 3
𝑛+1), and the fact that 𝜑(3
𝑛+1) = 2 ∙ 3
𝑛. Here 𝜑
is The Euler Phi-Function [14, Sec. 6.3 and 7.1]. Also note that ord3𝑛+12 = 2 ∙ 3
𝑛, which means
that  𝑥 = 2 ∙ 3
𝑛  is  the  least  positive  integer  such  that  2𝑥 ≡ 1(mod 3
𝑛+1).  Otherwise,
since  ord3𝑛+12|𝜑(3
𝑛+1)  and  𝜑(3
𝑛+1) = 2 ∙ 3
𝑛,  either  (I  option)  ord3𝑛+12 = 3
𝑘  or

(II option) ord3𝑛+12 = 2 ∙ 3
𝑘 for some 0 ≤ 𝑘 < 𝑛. But 3 ∤ (2
3𝑘 − 1), as mentioned earlier, so,

the  first  option  is  not  possible.  The  second  option  is  also  impossible,  because  in  this  case

2
2∙3𝑘 ≡ 1(mod 3
𝑛+1) for some 0 ≤ 𝑘 < 𝑛. But as proved in Lemma 3.2 above 3
𝑘+1 ∤ 2
2∙3𝑘 − 1,

therefore, 3
𝑛+1 ∤ 2
2∙3𝑘 − 1, too. The equality ord3𝑛+12 = 𝜑(3
𝑛+1) that we just proved means that
2 is  a primitive root modulo  3
𝑛+1. See [14, Sec. 9.1] for the definition of primitive roots, the
notation  ord𝑚𝑎  (order  of  𝑎  modulo  𝑚)  and  its  properties.  The  following  result  generalizes
Observation I above.

Lemma 3.3. Except those which ends by zero, any finite sequence of digits can appear infinitely
many times, at the end of a ternary numeral system representations of powers of 2.

Proof. If 𝑘 is a positive integer, then {1, 2, 2
2, 2
3, … , 2
𝜑(3𝑘+1)−1} gives the set of 𝜑(3
𝑘+1) integers

such that each element of the set is relatively prime to 3, and no two different elements of the set
are  congruent  modulo  3
𝑘+1,  i.e.,  the  set  forms  a  reduced  residue  set  modulo  3
𝑘+1  (see  [14],

sec. 6.3). So, the rightmost 𝑛 digits of the elements of the set {1, 2, 2
2, 2
3, … , 2
𝜑(3𝑘+1)−1} written

479

in radix-3, go through all the possible 𝑘-tuples without repetitions, except those ending with 0
(see [20], p. 20–25). By Lemma 3.2, the last 𝑘 digits of 2
𝑛 are periodic with period 2 ∙ 3
𝑘, and
this completes the proof of Lemma 3.3.  

4  The first digits

Let us now turn our attention to the first digits of the elements of the set {1, 2, 2
2, 2
3, … }, when
they are written in ternary numeral system. The following result generalizes Observation II above.

Lemma 4.1. Except those which start with zero, any finite sequence of digits can appear infinitely
many times, at the beginning of a ternary numeral system representation of powers of 2.
Proof.  Suppose  that  the  first  𝑚  digits  of  2
𝑛  are  (𝑎1𝑎2 … 𝑎𝑚̅̅̅̅̅̅̅̅̅̅̅̅̅)3 = 𝐴,  where  𝑎1 ∈ {1,2}  and
𝑎𝑖 ∈ {0, 1, 2} for 𝑖 = 2, … , 𝑚. Then

   𝐴 ∙ 3
𝑘 < 2
𝑛 < (𝐴 + 1) ∙ 3
𝑘,   (4.1)

for some nonnegative integer 𝑘. Taking base 3 logarithm of both sides of (4.1) gives

   𝑘 + log3 𝐴 < 𝑛 log3 2 < 𝑘 + log3(𝐴 + 1).   (4.2)

Since 𝑚 − 1 ≤ log3 𝐴 < 𝑚 and 𝑚 − 1 < log3(𝐴 + 1) ≤ 𝑚, we obtain that

  𝑘 + 𝑚 − 1 < 𝑛 log3 2 < 𝑘 + 𝑚.   (4.3)

This means that 𝑘 + 𝑚 − 1 is simply the integer part of 𝑛 log3 2. So,

  log3 𝐴 − 𝑚 + 1 < 𝑛 log3 2 − ⌊𝑛 log3 2⌋ < log3(𝐴 + 1) − 𝑚 + 1.   (4.4)

Note that [log3 𝐴 − 𝑚 + 1, log3(𝐴 + 1) − 𝑚 + 1] ⊆ [0,1]. By the well-known result of Bohl [3],
Sierpinski [15], and Weyl [21] (see also [11], Chapter 1, Example 2.1; [2, 9, 22]) the sequence
{𝑛 log3 2}(𝑛 = 1,2, … ) is uniformly distributed modulo 1. In particular, this means that there are
infinitely many 𝑛 such that the difference 𝑛 log3 2 − ⌊𝑛 log3 2⌋ is in the interval [log3 𝐴 − 𝑚 +
1, log3(𝐴 + 1) − 𝑚 + 1]. This completes the proof of Lemma 4.1.  

Note. Suppose that  𝑚 is  a positive integer  and  𝑛 = 𝑛0  is  the least  integer such that  2
𝑛 > 3
𝑚.
Then, the first 𝑚 digits of {2
𝑛}𝑛=𝑛0,𝑛0+1,…, give all of possible 2 ∙ 3
𝑚−1 sequences of digits at the
beginning of these numbers. The frequency with which 𝑎1𝑎2 … 𝑎𝑚̅̅̅̅̅̅̅̅̅̅̅̅̅ = 𝐴 appears at the beginning
when 𝑛 → ∞, is equal to the length of the interval [log3 𝐴 − 𝑚 + 1, log3(𝐴 + 1) − 𝑚 + 1], which

is log3 𝐴+1

𝐴 = log3(𝐴 + 1) − log3 𝐴. For example, the frequency of 1 and the frequency of 2 as

the leftmost digit of 2
𝑛, are log3 2

1 = log3 2 ≈ 0.63 and log3 3

2 = 1 − log3 2 ≈ 0.37, respectively.

In contrast to the case of rightmost digits described above, where the frequency is the same for all
combinations, the frequency of the first digits shows preference for smaller 𝐴, when 𝑚 is fixed.
This  phenomenon  is  generally  known  as  Benford’s  law  or  The  Significant-Digit  Phenomenon
(see, e.g., [7, 8]). See also Exercise 20.3.2 in [10, p. 502] for a version of this law similar to ours.
See [1], the recent paper [4], and the references therein for more details about Benford’s law.

480

5  Main result

We can now use the stated results for the first and last digits in order to prove the main result of
the present paper, which generalizes Observation III in Section 1. If the powers of 2 are written
so that each next power of 2, in ternary number system notation, is written on top of the previous
power of 2, and the digits corresponding to the same place values are all on the same vertical lines,
then arbitrarily large triangular blocks of zeros (twos) can appear in this infinite triangular table.
In a more formal way this can be expressed in the following way. Our proof strategy arises from
the fact that an arbitrary large number of consecutive zeros and twos appear infinitely many times
in a ternary representation of 2
𝑛.

Theorem 5.1. Let radix-3 be given. Then, we define the sequence given by 𝑎𝑛   =   2
𝑛 (𝑛 ≥ 0),
with  radix-3  representation  𝑎𝑛   = (𝑎𝑛
(𝑘𝑛) … 𝑎𝑛
(1)𝑎𝑛
(0))3.  Consider  numbers  𝑎𝑚, 𝑎𝑚+1, … , 𝑎𝑚+𝑟,

such that for some positive integer 𝑗, and integers 𝑙0 ≥ 𝑙1 ≥ ⋯ ≥ 𝑙𝑟−1 ≥ 𝑙𝑟 = 0,

𝑎𝑚
(𝑗), 𝑎𝑚+1
(𝑗) , … , 𝑎𝑚+𝑟
(𝑗) = 2, 𝑎𝑚
(𝑗+1), 𝑎𝑚+1
(𝑗+1), … , 𝑎𝑚+𝑟
(𝑗+1) ≠ 2, 𝑎𝑚+𝑟+1
(𝑗) = 1,

𝑎𝑚−1
(𝑗) = 𝑎𝑚−1
(𝑗−1) = ⋯ = 𝑎𝑚−1
(𝑗−𝑙0) = 1, 𝑎𝑚
(𝑗−1) = 𝑎𝑚
(𝑗−2) = ⋯ = 𝑎𝑚
(𝑗−𝑙0) = 2,

𝑎𝑚+1
(𝑗−1) = 𝑎𝑚+1
(𝑗−2) = ⋯ = 𝑎𝑚+1
(𝑗−𝑙1) = 2, … , 𝑎𝑚+𝑟−1
(𝑗−1) = 𝑎𝑚+𝑟−1
(𝑗−2) = ⋯ = 𝑎𝑚+𝑟−1
(𝑗−𝑙𝑟) = 2,

𝑎𝑚
(𝑗−𝑙0−1), 𝑎𝑚+1
(𝑗−𝑙1−1), … , 𝑎𝑚+𝑟−1
(𝑗−𝑙𝑟−1−1), 𝑎𝑚+𝑟
(𝑗−𝑙𝑟−1) ≠ 2 (See Table 5.1).

Then the natural numbers 𝑟 and 𝑙0 can be made arbitrarily large, provided that 𝑚 is sufficiently
large. The same is true when digit 2 in the above relationships is replaced by digit 0.

 2
𝑚+𝑟+1 = ⋯   𝑎𝑚+𝑟+1
(𝑗)           …

2
𝑚+𝑟 = ⋯ 𝑎𝑚+𝑟
(𝑗+1) 𝑎𝑚+𝑟
(𝑗−𝑙𝑟) 𝑎𝑚+𝑟
(𝑗−𝑙𝑟−1)         …
⋮          = ⋯ ⋮ ⋮ ⋮         …
⋮          = ⋯ ⋮ ⋮ ⋮         …

2
𝑚+2 = ⋯ 𝑎𝑚+2
(𝑗+1) 𝑎𝑚+2
(𝑗) 𝑎𝑚+2
(𝑗−1) … 𝑎𝑚
(𝑗−𝑙2) 𝑎𝑚
(𝑗−𝑙2−1)   …

2
𝑚+1 = ⋯ 𝑎𝑚+1
(𝑗+1) 𝑎𝑚+1
(𝑗) 𝑎𝑚+1
(𝑗−1) … 𝑎𝑚+1
(𝑗−𝑙1+1) 𝑎𝑚+1
(𝑗−𝑙1) 𝑎𝑚+1
(𝑗−𝑙1−1) …

2
𝑚      = ⋯ 𝑎𝑚
(𝑗+1) 𝑎𝑚
(𝑗) 𝑎𝑚
(𝑗−1) … 𝑎𝑚
(𝑗−𝑙0+1) 𝑎𝑚
(𝑗−𝑙0) 𝑎𝑚
(𝑗−𝑙0−1) …

2
𝑚−1 = ⋯   𝑎𝑚−1
(𝑗) 𝑎𝑚−1
(𝑗−1) … … 𝑎𝑚−1
(𝑗−𝑙0)   …

  Table 5.1.

Proof. By Lemma 3.3 and Lemma 4.1, for sufficiently large 𝑛, we can obtain any sequence of the
digits 0, 1, 2, including arbitrary large number of consecutive zeros (00 … 0) or twos (22 … 2).
Because of the doubling algorithm described above, any such block of zeros (or twos) is included
in a triangular block of zeros (or twos). This proves that the dimensions (height 𝑟 + 1 and width
𝑙0 + 1) of these blocks are unbounded. The proof is complete.  

 481

Note.  It would be interesting to know how frequently such blocks with given dimensions appear
in  Table  1.1  or  how  fast  the  dimensions  of  the  largest  blocks  of  zeros  and  twos  formed  by
radix-3 representations of {2
0, 2
1, … , 2
𝑛} grow as 𝑛 approaches infinity.

In view of these results, it would also be interesting to study the question of frequency for the
intermediate digits of the powers of two and how this frequency changes when the block of digits
𝐴 shifts from left endpoint, where the frequencies are different and obey Benford’s law, to the
right endpoint, where all the frequencies are equal. We determined that the probability of an 𝑚-
digit number 𝐴, which cannot start with zero digit, appearing at the beginning (after 0th position

from  left)  of  3-base  representations  of  2
𝑛,  is  𝑝0(𝐴) = log3 (1 + 1

𝐴).  Let  us  now  find  the

probability 𝑝𝑘(𝐴) of an 𝑚-digit number 𝐴, which can start with zero or zeros now (it can even be
only  zeros  00…0),  appearing  after  𝑘th  position  from  left  of  3-base  representations  of  2
𝑛.  By
adding the probabilities of 𝐴 appearing after 3
𝑘, after 3
𝑘 + 1, …, after 3
𝑘+1 − 1, we obtain

 𝑝𝑘(𝐴) = log3 ∏ (1 + 1

3𝑚𝑖+𝐴)
3𝑘+1−1
𝑖=3𝑘 .       (5.1)

See  [10,  11]  for  the  discussion  of  the  case  𝑚 = 1  in  decimal  number  system.  For  simplicity,
we will give examples only about the case 𝑚 = 1. We already mentioned that 𝑝0(1) = log3 2 ≈

0.63 and 𝑝0(2) = log3 3

2 ≈ 0.37. Let us find corresponding probabilities for some 𝑘 > 1. Using

the above formula, we calculate that

 𝑝1(0) = log3 (
67925
45927) ≈ 0.36,

 𝑝1(1) = log3 (2737
1900) ≈  0.33,

𝑝1(2) = log3 (
78732
55913) ≈  0.31.

  Similarly,  𝑝2(0) ≈ 0.341,  𝑝2(1) ≈  0.333,  𝑝2(2) ≈  0.326  and  𝑝3(0) ≈ 0.336,  𝑝3(1) ≈
0.333,  𝑝3(2) ≈  0.331,  etc.  We  can  observe  that  for  each  𝑘  the  sum  of  the  probabilities  is
𝑝𝑘(0) + 𝑝𝑘(1) + 𝑝𝑘(2) = 1 and 𝑝𝑘(0), 𝑝𝑘(1), 𝑝𝑘(2) approach each other. We can prove these
in more general 𝑚-digit case. For the sum of the probabilities, we can write

 𝑝𝑘(0) + 𝑝𝑘(1) + ⋯ + 𝑝𝑘(3
𝑚 − 1) = log3 ∏ 3
𝑚𝑖 + 1
3𝑚𝑖 ∙ 3
𝑚𝑖 + 2
3𝑚𝑖 + 1 ∙ … ∙ 3
𝑚𝑖 + 3
𝑚

3𝑚𝑖 + 3𝑚 − 1

3𝑘+1−1

𝑖=3𝑘

               = log3 ∏ 3
𝑚(𝑖 + 1)
3𝑚𝑖

3𝑘+1−1

𝑖=3𝑘

       = log3 ∏ 𝑖 + 1
𝑖

3𝑘+1−1

𝑖=3𝑘

= log3 3
𝑘+1

3𝑘

= log3 3 = 1.

482

For the difference of the probabilities, note that 𝑝𝑘(𝐴) decreases as 𝐴 increases. So, we will
estimate the difference of the largest 𝑝𝑘(0) and smallest 𝑝𝑘(3
𝑚 − 1):

  𝑝𝑘(0) − 𝑝𝑘(3
𝑚 − 1) < 𝑝𝑘(0) − 𝑝𝑘(3
𝑚)

= log3 ∏ 3
𝑚𝑖 + 1
3𝑚𝑖 ∙ 3
𝑚(𝑖 + 1)
3𝑚(𝑖 + 1) + 1

3𝑘+1−1

𝑖=3𝑘

= log3 3
𝑚+𝑘 + 1
3𝑘 ∙ 3
𝑘+1

3𝑚+𝑘+1 + 1

= log3 3
𝑚+𝑘+1 + 3
3𝑚+𝑘+1 + 1

= log3 1 + 3−𝑚−𝑘

1 + 3−𝑚−𝑘−1

< 2
(1 + 3𝑚+𝑘+1) ln 3.

  The last inequality can be easily proved by applying The Mean Value Theorem to function
𝑓(𝑥) = log3(1 + 𝑥) in the interval (3
−𝑚−𝑘−1, 3−𝑚−𝑘). Indeed, there is 𝑐 ∈ (3
−𝑚−𝑘−1, 3
−𝑚−𝑘)
such that

                     𝑓(3
−𝑚−𝑘) − 𝑓(3
−𝑚−𝑘−1) = log3(1 + 3
−𝑚−𝑘) − log3(1 + 3
−𝑚−𝑘−1)

                                𝑓′(𝑐)(3
−𝑚−𝑘 − 3
−𝑚−𝑘−1) = 2
3𝑚+𝑘+1(1 + 𝑐) ln 3.

It remains to note that since 𝑐 > 3
−𝑚−𝑘−1,

 log3(1 + 3
−𝑚−𝑘) − log3(1 + 3−𝑚−𝑘−1) < 2
3𝑚+𝑘+1(1 + 3−𝑚−𝑘−1) ln 3

                                                            = 2
(1 + 3𝑚+𝑘+1) ln 3
.

This expression approaches zero exponentially if 𝑚 is fixed and 𝑘 → ∞. Since ∑ 𝑝𝑘(𝐴)3𝑚−1
𝐴=0 = 1,
this proves that (cf. [7], p. 355)

 lim
𝑘→∞ 𝑝𝑘(𝐴) = 1
3𝑚   (𝐴 = 0,1, … , 3
𝑚 − 1).

  We can also show that as 𝑘 increases (𝑘 ≥ 0), 𝑝𝑘(0) decreases and 𝑝𝑘(3
𝑚 − 1) increases,
that is 𝑝𝑘(0) > 𝑝𝑘+1(0)  and 𝑝𝑘(3
𝑚 − 1) < 𝑝𝑘+1(3
𝑚 − 1) for 𝑚 > 0. For this let us write these
probabilities differently:

𝑝𝑘(0) = log3 ∏ (1 + 1
3𝑚𝑖)

3𝑘+1−1

𝑖=3𝑘 ,

𝑝𝑘+1(0) = log3 ∏ (1 + 1
3𝑚𝑖)

3𝑘+2−1

𝑖=3𝑘+1
 483

= log3 ∏ (1 + 1
3𝑚 ∙ 3𝑖)

3𝑘+1−1

𝑖=3𝑘 (1 + 1
3𝑚 ∙ (3𝑖 + 1)) (1 + 1
3𝑚 ∙ (3𝑖 + 2)),

𝑝𝑘(3
𝑚 − 1) = log3 ∏ 1

1 − 1
3𝑚(𝑖 + 1)

3𝑘+1−1

𝑖=3𝑘 ,

𝑝𝑘+1(3
𝑚 − 1) = log3 ∏ 1

1 − 1
3𝑚(𝑖 + 1)

3𝑘+2−1

𝑖=3𝑘+1

= log3 ∏ 1

1 − 1
3𝑚(3𝑖 + 1)
 ∙ 1

1 − 1
3𝑚(3𝑖 + 2)
 ∙ 1

1 − 1
3𝑚(3𝑖 + 3)

3𝑘+1−1

𝑖=3𝑘 .

For the monotonicity of 𝑝𝑘(0) and 𝑝𝑘(3
𝑚 − 1), it sufficient to show that

      1 + 1
3𝑚𝑖 > (1 + 1
3𝑚 ∙ 3𝑖) (1 + 1
3𝑚 ∙ (3𝑖 + 1)) (1 + 1
3𝑚 ∙ (3𝑖 + 2)),

1 − 1
3𝑚(𝑖 + 1) > (1 − 1
3𝑚(3𝑖 + 1)) ∙ (1 − 1
3𝑚(3𝑖 + 2)) ∙ (1 − 1
3𝑚(3𝑖 + 3)),

which  can  be  easily  proved.  Similarly,  if  𝑘  is  fixed  and  𝑚  increases,  then  the  probabilities
𝑝𝑘(0), 𝑝𝑘(1), … , 𝑝𝑘(3
𝑚 − 1) become more uniform. In particular, this means that a sequence of
𝑚 zeros 00…0 is more likely to appear towards the left side of the construction than a sequence
of 𝑚 twos 22…2, but as the block of 𝑚 digits approach the right side of the construction then the
probabilities become closer to each other. It would be interesting to study the effect of this on the
probability of appearance and the sizes of triangular blocks of zeros and twos discussed above.
We can now return to the mentioned question asked by Erdős [5, 6]: How frequently do the
powers of 2 have ternary expansions that omit the digit 2? He conjectured that this holds only for
finitely many powers of 2. See [12] for the detailed discussion of this problem. In view of the
results of the current paper, Erdős’ conjecture can be interpreted in the following way. There are
only finitely many powers of 2 which do not intersect the triangular blocks containing only twos.
In Table 1.1 the numbers 2
0, 2
2 and, 2
8 do not cross any of the regions with digits 2. One could
prove, using these elementary methods, that 2 appears in the ternary expansion of 2
𝑛 for “almost
all” 𝑛, in the sense of asymptotic density. But there is a large gap between “almost all” and “all
but finitely many”, and this is the real difficulty of Erdős’ problem. A similar observation can be
made about the powers of two which miss the regions of zeros. A better understanding of these
structures of zeros and twos may be helpful in the future for attempting to solve Erdős’ problem.

6  Conclusion

In  the  present  paper  we  have  focused  our  attention  on  the  regularities  occurring  in  base  3
representation of powers of 2, so we have shown that (I) every string of ending digits appears
infinitely often, by assuming that the string itself is not congruent to 0 modulo 3, (II) every string

484

of starting digits (not beginning with 0) appears infinitely often, (III) if the powers of 2 are all
written in base 3 as one column so that the digits of the same place value are on top of each other,
then the size of the triangular blocks of zeros and twos grow indefinitely. Part (I) was proved
using  elementary  number  theory  methods,  but  it  can  also  be  proved  using  the  fact  that  2  is  a
primitive  root  modulo  each  power  of  3.  Part  (II)  was  proved  using  the  fact  that  for  irrational
number 𝛼, the sequence 𝑥𝑛 = {𝑛𝛼}, where {𝑥} = 𝑥 − ⌊𝑥⌋ is the fractional part of 𝑥, is uniformly
distributed in [0,1], but it can also be interpreted in the context of “Benford’s law”. Part (III),
which is the main objective of the current paper, is shown to be a direct consequence of the Parts
(I) and (II). Also, the change of the distribution of probabilities of these combination of digits
when they are taken in between the left and right endpoints, is studied.

Acknowledgements

I thank the reviewers for their critical comments and suggestions which resulted in a much clearer
and rigorous presentation of the results.

References

[1]  Benford,  F.  (1938).  The  law  of  anomalous  numbers.  Proceedings  of  the  American
Philosophical Society, 78(4), 551–572.

[2]  Birkhoff, G. D. (1931). Proof of the ergodic theorem, Proceedings of the National Academy
of Sciences USA, 17, 656–660.

[3]  Bohl, P. (1909). Über ein in der Theorie der säkutaren Störungen vorkommendes Problem,
Journal für die reine und angewandte Mathematik, 135, 189–283.

[4]  Chang, S. (2023). Unlikely leading digits of powers of 2. Elemente der Mathematik, 78(2),
77–81.

[5]  Erdős, P. (1979). Some unconventional problems in number theory. Mathematics Magazine,
52(2), 67–70.

[6]  Erdős, P., & Graham, R. L. (1980). Old and New Problems and Results in Combinatorial
Number  Theory.  Geneva,  Switzerland:  L’Enseignement  Mathématique  Université  de
Genève, Vol. 28.

[7]  Hill, T. (1995). A statistical derivation of the significant-digit law. Statistical Science, 10(4),
354–363.

[8]  Hill, T.P. (1995). The significant-digit phenomenon. The American Mathematical Monthly,
102(4), 322–327.

[9]  Khintchine, A. (1933). Zu Birkhoffs Lösung des Ergodenproblems. Mathematische Annalen,
107, 485–488.
 485

[10]  Klenke, A. (2020). Probability Theory, A Comprehensive Course, Universitext, 716 p.

[11]  Kuipers,  L.,  &  Niederreiter,  H.  (1974).  Uniform  Distribution  of  Sequences.  John  Wiley;
Russian translation: Nauka, 1985.

[12]  Lagarias,  J.  C.  (2009).  Ternary  expansions  of  powers  of  2.  Journal  of  the  London
Mathematical Society, 79, 562–588.

[13]  Origlio,  V.,  &  Weisstein,  E.W.  Ternary.  From  MathWorld  –  A  Wolfram  Web  Resource,
Available online at: https://mathworld.wolfram.com/Ternary.html

[14]  Rosen, K. H. (2000). Elementary Number Theory and its Applicatons (4th ed.). Addison-
Wesley-Longman.

[15]  Sierpinski,  W.  (1910).  Sur  la  valeur  asymptotique  d'une  certaine  somme.  Bulletin
International  de  l'Academie  Polonaise  des  Sciences  et  des  Lettres  (Cracovie)  series  A,
9–11.

[16]  Sloane, N. J. A. (1973). The persistence of a number. Journal of Recreational Mathematics,
6(2), 97–98.

[17]  Sloane, N. J. A. (ed.), Powers of 2 written in base 3, The On-Line Encyclopedia of Integer
Sequences (OEIS), A004642. Available online at: https://oeis.org/A004642

[18]  Sobol,  I.  M.  (1985).  Points  uniformly  filling  a  high-dimensional  cube.  Znaniye,
Mathematics, Cybernetics series, 2, 1–32 (in Russian).

[19]  Strzelecki,  P.  (2004).  On  powers  of  2.  EMS  Newsletter,  52,  7–8;  translated  from  Polish
journal Delta 7 (1994).

[20]  Vardi,  I.  (1991).  Computational  Recreations  in  Mathematica.  Reading,  MA:  Addison-
Wesley.

[21]  Weyl, H. (1910). Über die Gibbs'sche Erscheinung und verwandte Konvergenzphänomene.
Rendiconti del Circolo Matematico di Palermo, 330, 377–407.

[22]  Weyl, H. (1916). Über die Gleichverteilung von Zahlen mod. Eins. Mathematische Annalen,
77, 313–352.
