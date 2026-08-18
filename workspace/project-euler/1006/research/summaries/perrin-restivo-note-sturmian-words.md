> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/perrin-restivo-note-sturmian-words.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture1/slides1.pdf | converted from PDF -->

## What it claims

A Sturmian word is an inﬁnite word x such that P(x, n) = n + 1
for any integer n ≥ 0.
A word u ∈ F (x) is right-special if u0, u1 ∈ F (x). The word x is
Sturmian if and only if there is exactly one right-special word of
each length.
 Dominique Perrin Sturmian words, Lecture 1

Complexity of an inﬁnite word
Balance
Slope of a word

Theorem (Coven, Hedlund,1973)

The following conditions are equivalent for an inﬁnite word x.

1 x is eventually periodic.

2 P(x, n) = P(x, n + 1) for some n.

3 P(x, n) < n + 1 for some n ≥ 1.

4 P(x, n) is bounded.

1⇒ 4. If x = uv ω, then P(x, n) ≤ |uv |.
4⇒ 3.
3⇒ 2. If P(x, m − 1) < P(x, m) for m = 0, . . . , n, then
P(x, n) ≥ n + 1, a contradiction.
2⇒ 1. Uses the factor graph Gn(x). The edges are the words in
Fn(x) and the edges the words in Fn+1(x). The edge aub goes
from au to ub.
If P(x, n) = P(x, n + 1), the strongly connected components are
simple circuits.
 Dominique Perrin Sturmian words, Lecture 1

Complexity of an inﬁnite word
Balance
Slope of a word
The Fibonacci word

The Fibonacci word

x = 0100101001001010010100100101001001 · · ·

is…

u…

## Statements it makes

Theorem (Coven, Hedlund,1973)

Proposition

Theorem (Morse,Hedlund,1940)

Proposition

Proposition

*[digest of a 6162 character source; every section, statement, and proof in full at `research/sources/perrin-restivo-note-sturmian-words.full.md`]*
