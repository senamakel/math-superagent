> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/berthe-automatic-sturmian-sequences-course.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.irif.fr/~berthe/Articles/chili.pdf | converted from PDF -->

## What it claims

The complexity function is a classical measure of disorder for se-
quences with values in a ﬁnite alphabet: this function counts the
number of factors of given length. We introduce here two charac-
teristic families of sequences of low complexity function: automatic
sequences and Sturmian sequences. We discuss their topological and
measure-theoretic properties, by introducing some classical tools in
combinatorics on words and in the study of symbolic dynamical sys-
tems.

1 Introduction

The aim of this course is to introduce two characteristic families of sequences
of low “complexity”: automatic sequences and Sturmian sequences (complex-
ity is deﬁned here as the combinatorial function which counts the number of
factors of given length of a sequence over a ﬁnite alphabet). These sequences
not only occur in many mathematical ﬁelds but also in various domains as
theoretical computer science, biology, physics, cristallography...
We ﬁrst deﬁne some classical tools in combinatorics on words and in the
study of symbolic dynamical systems: the complexity function and frequen-
cies of…

36

## Statements it makes

Proposition 2.5 We have Hn ≤ logd(p(n))
n , for all n ≥ 1.

Theorem 3.5 Let u be a sequence on A = {1, . . . , d}. Consider a family of
maps (pn)n≥1, where pn is a map from An to R, such that

Lemma 4.6 Let U and V be two vertices linked by an edge such that U + = 1
and V − = 1. Then the two factors U and V have the same frequency.

Theorem 4.7 For a recurrent sequence of complexity function p(n), the fre-
quencies of factors of given length, say n, take at most 3(p(n + 1) − p(n))
values.

Theorem 4.9 If the complexity p(n) of a sequence on a ﬁnite alphabet is
sub-aﬃne, i.e., ∃(a, b), ∀n, p(n) ≤ an + b,

Corollary 4.10 If a sequence has a sub-aﬃne complexity then the frequen-
cies of its factors of given length take a ﬁnite number of values.

Theorem 6.3 (Hedlund and Morse) A sequence u is Sturmian if and
only if there exists an irrational α in ]0, 1[ and x on the unit circle such
that u is the coding of the orbit of x under the rotation by angle α with
respect to one of the partitions {[0, 1 − α[, [1 − α, 1[} or {]0, 1 − α], ]1 − α, 1]}.

Theorem 6.4 The frequencies of factors of given length of a Sturmian se-
quence take at most three values.

Theorem 6.4 implies that the lengths of the intervals I(w1, . . . , wn), and
thus the lengths of the intervals obtained by placing the points 0, {1 −
α}, . . . , {n(1−α)} on the unit circle, take at most three values. We thus have
proved the following classical result in Diophantine approximation, called the
three-distance theorem (see the survey [3]). In fact, this point of view and
more precisely, the study of the evolution of the graphs of words with respect
to the length n of the factors, allows us to give a proof of the most complete
version of the three distance theorem, i.e., to express the exact number of
factors having each of the three frequencies and the frequencies themselves…

Theorem 6.5 Let 0 < α < 1 be an irrational number and n a positive
integer. The points {iα}, for 0 ≤ i ≤ n, partition the unit circle into n + 1
intervals, the lengths of which take at most three values, one being the sum
of the other two.
More precisely, let ( pk
qk )k∈N and (ck)k∈N be the sequences of the convergents
and partial quotients associated to α in its continued fraction expansion (if
α = [0, c1, c2, . . .], then pn
qn = [0, c1, . . . , cn]). Let ηk = (−1)
k(qkα − pk). Let n
be a positive integer. There exists a unique expression for n of the form

Theorem 7.1 (Christol, Kamae, Mend`es France and Rauzy)
Let u = (u(n))n∈N be a sequence with values in Fq. The following condi-
tions are equivalent:

Theorem 7.5 The Hadamard product of two algebraic formal power series
with coeﬃcients in a ﬁnite ﬁeld is algebraic.

Theorem 7.6 Let u be a sequence which is both k-automatic and k′-automatic.
If k and k′ are multiplicatively independent (i.e., if log(k)
log(k′) is irrational), then
the sequence u is ultimately…

Theore…


*[further statements in the full text]*

*[digest of a 68169 character source; every section, statement, and proof in full at `research/sources/berthe-automatic-sturmian-sequences-course.full.md`]*
