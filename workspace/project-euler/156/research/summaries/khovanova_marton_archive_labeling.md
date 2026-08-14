> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/khovanova_marton_archive_labeling.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2305.10357 | converted from PDF -->

## What it claims

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
f (1)…

## Statements it makes

Definition 3.1. We denote by a=(d) the smallest number x > 1 such that
the decimal representation of d appears as a substring of the decimal rep-
resentations of the numbers [1,. . . , x] exactly x times:

Definition 3.2. Let
 a>(d) = min({x : fd(x) > x}).

Definition 4.1. Let Ed be an increasing sequence of positive integers x such
that fd(x) = x.

Lemma 5.1. For any integer x > 10
10, we have f0(x + 10
10) ≥ f0(x) + 10
10.

Theorem 5.2. The value a=(0) is not well-defined.

Lemma 7.1. Suppose we already know that a≥(d) > x. Suppose, in addition,
we can show that fd(y) < x for some y > x. Then a≥(d) > y.

Proposition 8.1. The “more than” sequence a> and the “greater or equal”
sequence a≥ are non-decreasing after the first terms a>(1) and a≥(1).

Theorem 8.2. The value a=(d) is well-defined for any d > 0.

Proposition 9.1. For any digit d > 0 in base b > d the maximum possible
value of a=(d, b) is bb and all x such that fd(x, b) = x must be ≤ d · bb.

Theorem 9.2. The value a=(d, b) is well-defined for any b > 2 and any
d > 0. For b = 2, it is well-defined when d > 0 is not a power of 2.

Proposition 9.3. For digit 0 in base b > 1, the value of a=(0, b), if it is
well-defined, must be less than bb+3.

*[digest of a 35226 character source; every section, statement, and proof in full at `research/sources/khovanova_marton_archive_labeling.full.md`]*
