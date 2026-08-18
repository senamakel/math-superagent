> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/mousavi-schaeffer-shallit-fibonacci-automatic-decision-algorithms-numdam.pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.numdam.org/item/10.1051/ita/2016010.pdf | converted from PDF -->

## What it claims

Abstract. We implement a decision procedure for answering questions about a class of inﬁnite words
that might be called (for lack of a better name) “Fibonacci-automatic”. This class includes, for example,
the famous Fibonacci word f = f0f1f2 ··· = 01001010 ·· · , the ﬁxed point of the morphism 0 → 01 and
1 → 0. We then recover many results about the Fibonacci word from the literature (and improve some
of them), such as assertions about the occurrences in f of squares, cubes, palindromes, and so forth.

Mathematics Subject Classiﬁcation. 11B85, 68R15, 11A67, 11B39, 03D05, 68Q45.

1. Decidability

As is well-known, the logical theory Th(N, +), sometimes called Presburger arithmetic, is decidable [51, 52].
B¨uchi [11] showed that if we add the function Vk(n)= ke, for some ﬁxed integer k ≥ 2, where e =max{i : ki | n},
then the resulting theory is still decidable. This theory is powerful enough to deﬁne ﬁnite automata; for a survey,
see [9].
As a consequence, we have the following theorem (see, e.g., [58]):

Theorem 1.1. There is an algorithm that, given a proposition phrased using only…

## Statements it makes

Theorem 1.1. There is an algorithm that, given a proposition phrased using only the universal and existential
quantiﬁers, indexing into one or more k-automatic sequences, addition, subtraction, logical operations, and
comparisons, will decide the truth of that proposition.

Theorem 2.2. There is an algorithm that, given a proposition phrased using only the universal and existential
quantiﬁers, indexing into one or more Fibonacci-automatic sequences, addition, subtraction, logical operations,
and comparisons, will decide the truth of that proposition.

Theorem 3.1. The word f is not ultimately periodic.

Theorem 3.2. f contains no fourth powers.

Theorem 3.3. All squares in f are of order Fn for some n ≥ 2. Furthermore, for all n ≥ 2,there exists a
square of order Fn in f .

Theorem 3.4. The language

Theorem 3.5. The cubes in f are of order Fn for n ≥ 4, and a cube of each such order occurs.

Theorem 3.6. The language

Theorem 3.7. The Fibonacci word f contains exactly four antisquare factors: 01, 10, 1001, and 10100101.

Theorem 3.8. There exist nonempty palindromes of every length ≥ 1 in f .

Theorem 3.9. The Fibonacci word f has exactly one palindromic factor of length n if n is even, and exactly
two palindromes of length n if n is odd.

Theorem 3.10. The preﬁx f [0..n − 1] of length n> 0 is a palindrome if and only if n = Fi − 2 for some i ≥ 4.

Theorem 3.11. The word f is mirror invariant.

Theorem 3.12. The only nonempty antipalindromes in f are 01, 10, (01)
2,and (10)
2.

Theorem 3.13. The automaton depicted below in Figure 8 accepts the language

Theorem 3.14. The unique special factor of length n is f [0..n − 1]
R.

Theorem 3.15. If a word w is a nonempty factor of the Fibonacci word, then the least period of w is a Fibonacci
number Fn for n ≥ 2. Furthermore, each such period occurs.

Theorem 3.16. Let n ≥ 1, and deﬁne ℓ(n) to be the smallest integer that is the least period of some length-n
factor of f .Then ℓ(n)= Fj for j ≥ 1 if Lj − 1 ≤ n ≤ Lj+1 − 2,where Lj is the j’th Lucas number deﬁned in
Section 2.

Theorem 3.17. The factor f [i..i + n − 1] is a maximal repetition of f iﬀ (i, n)F is accepted by the automaton
depicted in Figure 10.

Theorem 3.18. A nonempty length-n preﬁx of f is a quasiperiod of f if and only if n is not of the form Fk − 1
for k ≥ 3.

Theorem 3.19. The only unbordered nonempty factors of f are of length Fn for n ≥ 2, and there are two for
each such length. For n ≥ 3 these two unbordered factors have the property that one is a reverse of the other.

Theorem 3.20. Every Lyndon factor of f is of length Fn for some n ≥ 2, and each of these lengths has a
Lyndon factor.

Theorem 3.21. For n ≥ 2, every length-n Lyndon factor of f is a conjugate of f [0..n − 1].

Theorem 3.22. The word f is recurrent, uniformly recurrent, and linearly recurrent.

Theorem 3.24. The critical exponent of f is 2+ α,where α =(1 + √
5)/2.

Theore…


*[further statements in the full text]*

*[digest of a 66836 character source; every section, statement, and proof in full at `research/sources/mousavi-schaeffer-shallit-fibonacci-automatic-decision-algorithms-numdam.pdf.full.md`]*
