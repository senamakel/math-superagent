> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/berstel-karhumaki-combinatorics-words-tutorial.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://www-igm.univ-mlv.fr/~berstel/Articles/2003TutorialCoWdec03.pdf | converted from PDF -->

## What it claims

1Institut Gaspard-Monge, Universit´e de Marne-la-Vall´ee, 77454 Marne-la-Vall´ee
Cedex 2, France, email: jean.berstel@univ-mlv.fr
2Department of Mathematics and Turku Centre for Computer Science, University of
Turku, 20014 Turku, Finland, email: karhumak@cs.utu.ﬁ

Table of Contents

1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.1 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Notions and notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1 To matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 To algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 To algorithmics . . . . . . . . . . . . . . . . . . . . . . . . . .…

## Statements it makes

Theorem 2.1. The following questions are undecidable:

Theorem 2.2. The Burnside Problem for semigroups has a negative answer.

Theorem 3.1. Let x and y be nonempty words. The following properties are
equivalent:

Theorem 3.2. (Fine and Wilf’s Theorem) Let w be a word of length n. If w
has two periods p and q and n ≥ p + q − gcd(p, q), then also gcd(p, q) is a period
of w.

Lemma 3.3. Let x and y be nonempty words. If xy• = yx
•, then xy = yx.

Theorem 3.4. (Critical Factorization Theorem.) Every word of length at least 2
has a critical factorization.

Theorem 3.5. Let X be a ﬁnite set of nonempty words, and let p be the max-
imum of the periods of the words in X. Every word w with the period strictly
greater than p has at most Card(X) disjoint X-interpretations.

Theorem 3.6. (i) Each ϕ
2-legal word is periodic.
(ii) The Fibonacci word is (ϕ
2 − ε)-legal for any ε > 0.

Theorem 3.7. (i) Each (2, 4)-legal inﬁnite word is ultimately periodic.
(ii) For any ε > 0, each (2 + ε, 5)-legal inﬁnite word is ultimately periodic.
(iii) There exists nondenumerably many (2, 5)-legal inﬁnite words, including
the Fibonacci word.

Theorem 3.8. An inﬁnite word w = a1a2 · · · is ultimately periodic if and only
if, for any large enough i, there exists a square centered at position i.

Theorem 4.1. For any ﬁnite X ⊆ A
+ we have

Theorem 4.2. Let X ⊆ A
+ be ﬁnite. Then we have

Theorem 4.3. Let X ⊆ A
+ be ﬁnite. If there exists a nonperiodic two-way
inﬁnite word with two disjoint X-factorizations, then

Theorem 4.4. Let u = v be a constant-free equation over variables Ξ and A
an alphabet such that card(A) ≥ card(Ξ). The following numbers coincide

Theorem 4.5. Each system S of equations with a ﬁnite number of variables Ξ
over free monoid A
∗ is equivalent to some of its ﬁnite subsets S0.

Fact 5.1. The inﬁnite word z is cube-free.

Theorem 5.2. Let h : A
∗ → B∗ be a nonerasing morphism. If h preserves
square-free words of length K(h) = max (3, 1 + ⌈(M (h) − 3)/m(h)⌉) , then h is
square-free.

Theorem 5.3. A ternary endomorphism h is square-free if h preserves square-
free words of length 5.

Theorem 5.4. A binary morphism h is cube-free if h preserves cube-free words
of length 10.

Theorem 5.5. A morphism h is power-free if h preserves square-free words and
if the words h(a2) for a a letter, are cube-free.

Theorem 5.6. (i) The number of cubefree words of length n over a binary al-
phabet is exponential, i.e., there exist constants A, B > 0 and α, β > 1 such
that Aα
n ≤ 2 − F3(n) ≤ Bβn

Theorem 5.7. (i) The number of 2+-free words of length n over a binary al-
phabet is polynomial, i.e., there exist constants A, B > 0 and α, β > 1 such
that Anα ≤ 2+ − F2(n) ≤ Bnβ

Theorem 5.8. The cardinality of 21/3−F2(n) is polynomial while that of 21/3
+−
F2(n) is exponential.

Theorem 5.9. Let h be an overlap-free binary endomorphism. Then there is an
integer n such that h = µ
n…


*[further statements in the full text]*

*[digest of a 142737 character source; every section, statement, and proof in full at `research/sources/berstel-karhumaki-combinatorics-words-tutorial.full.md`]*
