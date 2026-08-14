> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/archive-labeling-amm-published.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf | converted from PDF -->

## What it claims

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
out of 1 s. Intuitively, we can expect that sticker 1 is the ﬁrst to run…

## Statements it makes

Lemma 7. For any integer x> 10
10, we have f0(x + 10
10) ≥ f0(x) + 10
10.

Theorem 8. The value a=(0) is not well-deﬁned.

Lemma 9. Suppose we already know that a≥(d) > x. Suppose, in addition, we can
show that fd(y)<x for some y> x. Then a≥(d) > y.

*[digest of a 25072 character source; every section, statement, and proof in full at `research/sources/archive-labeling-amm-published.full.md`]*
