> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/perrin-restivo-note-sturmian-words.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://hal.science/hal-00828351/file/noteSturmianWords.pdf | converted from PDF -->

## What it claims

We describe an algorithm which, given a factor of a Sturmian word, computes the next
factor of the same length in the lexicographic order in linear time. It is based on a combinatorial
property of Sturmian words which is related with the Burrows-Wheeler transformation.

1 Introduction

Sturmian words are inﬁnite words over a binary alphabet that have exactly n + 1 factors of length
n for each n ≥ 0. Their origin can be traced back to the astronomer J. Bernoulli III. Their ﬁrst
in-depth study is by Morse and Hedlund [11]. Many combinatorial properties were described in
the paper by Coven and Hedlund [5]. Sturmian words, also called mechanical words, are used in
computer graphics as digital approximation of straight lines. See [8] for a general exposition on
Sturmian words.
In this note, we describe an algorithm which, given a factor of a Sturmian word, computes the
next factor of the same length in the lexicographic order in linear time. It may be used to generate
the set of factors of a Sturmian word of given length in lexicographic order.
This algorithm is based on a…

1

is…

2…

W…

## Statements it makes

Theorem 1 An inﬁnite word s is Sturmian if and only if it is mechanical of irrational slope.

Proposition 1 Let s be a Sturmian word with slope α. Then w ∈ F (s) if and only if for any
factor u of w one has |u|b − 1 < α|u| < |u|b + 1. (1)

Corollary 1 Let F be a Sturmian set. If ra, rba ∈ F , then rab ∈ F .

Corollary 2 Let F be a Sturmian set. If rabsa, rbasb, bsb ∈ F , then rabsb ∈ F .

Theorem 2 Let F be a Sturmian set. Two words u, v of F of the same length are consecutive in
the lexicographic order if and only if u = rabs and v = rbas or if u = ra and v = rb.

Corollary 3 Let F be a Sturmian set and let n ≥ 1. For any word u in F ∩ A
n which is not
maximal for the lexicographic order in F ∩ A
n, there is a preﬁx r of u such that

Proposition 2 Let F be a Sturmian set and let n ≥ 1. The ﬁrst and the last elements of F ∩ A
n

Proposition 3 For n ≥ 1, the right border of the set F ∩ A
n is conjugate to a word in a∗b∗.

Proposition 3 is related with another result proved in [10] that we introduce now.

Theorem 3 One has T (w) = bpaq with p, q relatively prime if and only if w is a conjugate of a
standard word.

Proposition 4 The function PrincipalPrefix(u) returns the principal preﬁx of u if u is not
maximal in the set of elements of F of the same length and −1 otherwise.

Proposition 5 The algorithm Sturm generates the elements of length n of a Sturmian set in
lexicographic order in quadratic time O(n2).

*[digest of a 26559 character source; every section, statement, and proof in full at `research/sources/perrin-restivo-note-sturmian-words.full.md`]*
