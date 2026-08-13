> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/hajdu-pinter-tengely-varga-equal-figurate-2014.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://shrek.unideb.hu/~tengely/hptvrevised.pdf | converted from PDF -->

## What it claims

Abstract. Some eﬀective results for the equal values of ﬁgu-
rate numbers are proved. Using a state-of-the-art computational
method for the small parameter values the corresponding Diophan-
tine equations are resolved.

1. Introduction

There are several results concerning arithmetical and Diophantine
properties of certain combinatorial numbers. Let k, m be integers with
k ≥ 3 and m ≥ 3, further, denote by

fk,m(X) = X(X + 1) . . . (X + k − 2)((m − 2)X + k + 2 − m)
k!
the Xth ﬁgurate number with parameters k and m. For some problems
and theorems related to these families of combinatorial numbers, we
refer to the books [11] and [10]. The power and equal values of special
cases of fk,m(X), including, for instance, binomial coeﬃcients (for m =
3), polygonal numbers (for k = 2) and pyramidal numbers (for k = 3)
have been studied intensively, see [1], [20], [4], [23], [8], [9], [14], [18],
[19], [17], [16] and references therein. Brindza, Pint´er and Turj´anyi [5]
conjectured that apart from the case (m, n) = (5, 4) the equation

f3,m(x) = f2,n(y)

has only ﬁnitely many solutions in…

201…

## Statements it makes

Theorem 2.1. Let m, n, k be integers with k ≥ 3 and (m, n, k) ̸=
(5, 4, 3), (6, 4, 4). If k is even, then assume further that k!D is not
of the form r2, 2r2, where D = gcd(k!(n − 4)
2, 8d(n − 2)) with d =
gcd(k, m − 2). Then equation (1) has only ﬁnitely many solutions in
x, y which can be eﬀectively determined.

Corollary 2.1. Let m, n, k be integers with k ≥ 4. If k is even, then
assume further that there exists a prime p with k/2 < p < k such that
p ∤ n − 2. Then equation (1) has only ﬁnitely many solutions in x, y
which can be eﬀectively determined.

Theorem 2.2. Suppose that k ≥ 3, m ≥ 3, n ≥ 3 are integers with

Theorem 2.3. The only solution of the equation

Theorem 2.4. The set of integral points (x, y) on the curve (3) with
(m, n) = (7, 5) is

Proposition 3.1. Let t ≥ 0 be an integer, and write Pt(x) = x(x +
1) . . . (x + t). Let f (x) ∈ Z[x] and v ∈ Z \ {0} such that g(x) :=
Pt(x)f (x) + v is a primitive polynomial.
• If t ≥ 3 and deg(g) is odd, then g(x) has at least three roots of
odd multiplicities.
• If t ≥ 2, deg(g) is even and v is not of the form ±r2, ±2r2,
then g(x) has at least three roots of odd multiplicities.
• Let ℓ ≥ 3. If t ≥ 3 and deg(f ) < (t + 1)(ℓ − 1), then g(x) has
at least two roots with multiplicities not divisible by ℓ.

Lemma 3.1. Let t(X) ∈ Q[X] and suppose that the polynomial t(X)
possesses at least three zeros of odd multiplicities. Then the equation
t(x) = y2 in integers x, y implies that max(|x|, |y|) < C, where C is an
eﬀectively computable constant depending only on the polynomial t(X).

*[digest of a 23232 character source; every section, statement, and proof in full at `research/sources/hajdu-pinter-tengely-varga-equal-figurate-2014.full.md`]*
