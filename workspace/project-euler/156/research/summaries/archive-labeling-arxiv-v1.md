> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/archive-labeling-arxiv-v1.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2305.10357v1 | converted from PDF -->

## What it claims

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
tape x. When f (x) = x, then we have used all of…

## Statements it makes

Lemma 5.1. For any integer x > 1010, we have z(x + 1010) ≥ z(x) + 1010.

Theorem 5.2. The value a=(0) is not well-deﬁned.

Lemma 6.1. Suppose we already know that a≥(0) > x. Suppose, in addition,
we can show that z(y) < x for some y > x. Then a≥(0) > y.

*[digest of a 15443 character source; every section, statement, and proof in full at `research/sources/archive-labeling-arxiv-v1.full.md`]*
