> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/stewart-2013-divisors-lucas-lehmer-arxiv.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1008.1274 | converted from PDF -->

## What it claims

Abstract. Let un be the n-th term of a Lucas sequence or a Lehmer sequence.
In this article we shall establish an estimate from below for the greatest prime
factor of un which is of the form n exp(log n/104 log log n). In so doing we are
able to resolve a question of Schinzel from 1962 and a conjecture of Erd˝os from
1965. In addition we are able to give the ﬁrst general improvement on results
of Bang from 1886 and Carmichael from 1912.

1. Introduction

Let α and β be complex numbers such that α + β and αβ are non-zero coprime
integers and α/β is not a root of unity. Put

un = (α
n − βn)/(α − β) for n ≥ 0.

The integers un are known as Lucas numbers and their divisibility properties have
been studied by Euler, Lagrange, Gauss, Dirichlet and others (see [11, Chapter
XVII]). In 1876 Lucas [24] announced several new results concerning Lucas se-
quences (un)
∞
n=0 and in a substantial paper in 1878 [25] he gave a systematic treat-
ment of the divisibility properties of Lucas numbers and indicated some of the
contexts in which they appeared. Much later Matijasevic [26] appealed to these…

## Statements it makes

Theorem 1. Let α and β be complex numbers such that (α + β)
2 and αβ are
non-zero integers and α/β is not a root of unity. There exists a positive number C,
which is eﬀectively computable in terms of ω(αβ) and the discriminant of Q(α/β),
such that for n > C,
 P (Φn(α, β)) > n exp(log n/104 log log n). (7)

Theorem 2. Let a and b be integers with a > b > 0. There exists a number C1,
which is eﬀectively computable in terms of ω(ab), such that if p is a prime number
which does not divide ab and which exceeds C1 and n is an integer with n ≥ 2 then

Lemma 1. Suppose that (α + β)
2 and αβ are coprime. If n > 4 and n ̸= 6, 12 then
P (n/(3n)) divides Φn(α, β) to at most the ﬁrst power. All other prime factors of
Φn(α, β) are congruent to ±1 (mod n).

Lemma 2. Let d be a square-free integer diﬀerent from 1, θ be an algebraic integer
of degree 2 over Q in Q(
√
d) and let θ′ denote the algebraic conjugate of θ over Q.
Suppose that p is a prime which does not divide 2θθ′. Let ℘ be a prime ideal of the
ring of algebraic integers of Q(
√
d) lying above p. The order of θ/θ′ in (Q(
√
d)℘)
×

Lemma 3. If 1 ≤ n < x and (n, ℓ) = 1 then

Lemma 4. Let d be a squarefree integer with d ̸= 1 and let pk denote the k-th
smallest prime of the form N πk = pk where N denotes the norm from Q(
√
d) to Q
and πk is an algebraic integer in Q(
√
d). Let ε be a positive real number. There is
a positive number C, which is eﬀectively computable in terms of ε and d, such that
if k exceeds C then
 log pk < (1 + ε) log k.

Lemma 5. Let p be a prime with p ≥ 5 and let ℘ be an unramiﬁed prime ideal of
OK lying above p. Let α1, . . . , αn be multiplicatively independent ℘-adic units. Let
b1, . . . , bn be integers, not all zero, and put

Lemma 6. There exists an eﬀectively computable positive number c such that if
n > 2 then |α|
ϕ(n)−cq(n) log n ≤ |Φn(α, β)| ≤ |α|ϕ(n)+cq(n) log n, (25)

Lemma 7. There exists an eﬀectively computable positive number c1 such that if
n exceeds c1 then
 log |Φn(α, β)| ≥ ϕ(n)
2 log |α|. (26)

Lemma 8. Let n be an integer larger than 1, let p be a prime which does not
divide αβ and let ℘ be a prime ideal of the ring of algebraic integers of Q(α/β)
lying above p which does not ramify. Then there exists a positive number C, which
is eﬀectively computable in terms of ω(αβ) and the discriminant of Q(α/β), such
that if p exceeds C then

*[digest of a 42351 character source; every section, statement, and proof in full at `research/sources/stewart-2013-divisors-lucas-lehmer-arxiv.full.md`]*
