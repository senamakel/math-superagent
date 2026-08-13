> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kane-combinations2.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://cseweb.ucsd.edu/~dakane/combinations2.pdf | converted from PDF -->

## What it claims

Let N (t) denote the number of ways of writing t as a binomial coeﬃ-

cient. We show that N (t) = O  (log t)(log log log t)
(log log t)3  .

1 Introduction

As in [2] we deﬁne
 N (t) = ∣
∣
∣
∣
{
(n, m) ∈ Z
2 : ( n
m

) = t}∣
∣
∣
∣

to be the number of ways of writing an integer t > 1 as a binomial coeﬃcient.
N (3003) = 8, and N (t) ≥ 6 for inﬁnitely many t, but essentially no other
lower bounds on N (t) are known. Singmaster conjectured in [2] that N (t) =
O(1). Although no one has yet managed to achieve this bound (or even gotten
particularly close), there has been some work on bounding the size of N (t)
(see [1, 2, 3]). The record was that N (t) = O ( (log t)(log log log t)
(log log t)2 ) proved by the
author in [1]. Using a reﬁnement of this argument we improve this bound by a
factor of log log t.

2 Overview of Our Technique

We recall the basics of the argument from [1]. First we note that it suﬃces to
consider only solutions of the form t = ( n
m
) where n > 2m, since for any other
solution (n, m) with n < 2m, we have the solution (n, n − m) with n > 2m
(there is at most one…

## Statements it makes

Lemma 1. If F (x) : R → R is an inﬁnitely diﬀerentiable function and if F (x) =
0 for x = x1, x2, ..., xn+1 (where x1 < x2 < ... < xn+1), then F (n)(y) = 0 for
some y ∈ (x1, xn+1).

Proposition 2. If mi are integers where the largest and smallest diﬀer by at
most S,
 log(B(m1, . . . , mk)) = O (S max(1, log ( k2 log S
S
 ))
) .

*[digest of a 12618 character source; every section, statement, and proof in full at `research/sources/kane-combinations2.full.md`]*
