> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/bank_barysoroker_rosenzweig_1302.0625.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1302.0625 | converted from PDF -->

## What it claims

In this paper we establish function ﬁeld versions of two classical conjectures
on prime numbers. The ﬁrst says that the number of primes in intervals
(x, x + x
ǫ] is about x
ǫ/ log x. The second says that the number of primes
p < x in the arithmetic progression p ≡ a (mod d), for d < x
1−δ, is about
π(x)
φ(d) , where φ is the Euler totient function.
More precisely, for short intervals we prove: Let k be a ﬁxed integer. Then

πq(I(f, ǫ)) ∼ #I(f, ǫ)
k , q → ∞

holds uniformly for all prime powers q, degree k monic polynomials f ∈ Fq[t]
and ǫ0(f, q) ≤ ǫ, where ǫ0 is either 1
k , or 2
k if p | k(k − 1), or 3
k if further
p = 2 and deg f ′ ≤ 1. Here I(f, ǫ) = {g ∈ Fq[t] | deg(f − g) ≤ ǫ deg f },
and πq(I(f, ǫ)) denotes the number of prime polynomials in I(f, ǫ). We show
that this estimation fails in the neglected cases.
For arithmetic progressions we prove: Let k be a ﬁxed integer. Then

πq(k; D, f ) ∼ πq(k)
φ(D) , q → ∞,

holds uniformly for all relatively prime polynomials D, f ∈ Fq[t] satisfying
∥D∥ ≤ qk(1−δ0), where δ0 is either 3
k or 4
k if p = 2 and (f /D)′ is a constant.
Here…

∗S…

## Statements it makes

Conjecture 1.1. If Φ(x) > x
ǫ then (1) holds.

Conjecture 1.2. For every δ > 0, (2) holds in the range d1+δ < x.

Conjecture 2.1. There exists a function ǫ0(f, q) > 0 deﬁned on f ∈ Fq[t] such that
lim
deg f →∞ ǫ0(f, q) = 0 and such that for any ﬁxed ǫ the asymptotic formula

Conjecture 2.2. There exists a function δ0(f, D, q, k) deﬁned over relatively prime
f, D ∈ Fq[t] such that lim
k→∞ δ0(f, D, q, k) = 0 and such that for any ﬁxed δ the asymptotic

Theorem 2.3. Let k be a positive integer. Then there exists a constant c(k) > 0
depending only on k such that for any

Corollary 2.4. Let k > 0 be ﬁxed. The asymptotic formula

Theorem 2.5. Let k be a positive integer. Then there exists a constant c(k) > 0
depending only on k such that for any

Corollary 2.6. Let k be a ﬁxed integer. Then

Proposition 3.1. Let k, m, and B be positive integers, let λ be a partition of k, let
F be an algebraic closure of Fq, and let F ∈ Fq[A0, . . . , Am, t] be a polynomial that is
separable in t with deg F ≤ B and degt F = k. Assume that

Lemma 3.2. Let F be an algebraically closed ﬁeld, A = (A0, . . . , Am) an m-tuple of
variables with m ≥ 1, and f, g ∈ F [t] relatively prime polynomials. Then F (A, t) =
f (t) + g(t) · (∑m
i=0 Ait
i) is separable in t and irreducible in the ring F (A)[t].

Lemma 3.3. Let F be an algebraically closed ﬁeld, A = (A0, . . . , Am) an m-tuple of
variables with m ≥ 2, and f, g ∈ F [t] relatively prime polynomials with deg f > deg g.
The Galois group G of F (A, t) = f (t) + g(t) · (∑m
i=0 Ait
i) over F (A) is doubly transitive
(with respect to the action on the roots of F ).

Lemma 3.2 then gives that f0(t)+g(t)·( ∑m−1
i=1 Ait
i−1) is separable and irreducible. This
means that the stabilizer of the root t = 0 in the Galois group of ¯F acts transitively
on the other roots. But since ¯F is separable, its Galois group embeds into G, so the
stabilizer of a root of F in G is transitive. Thus G is doubly transitive.

Lemma 3.4. Let ψ(t) ∈ F (t) be a rational function with ψ[2] nonzero and A1 a variable.
Then ψ′(t) + A1 and ψ[2](t) have no common zeros.

Lemma 3.5. Let F be an algebraically closed ﬁeld of characteristic p ≥ 0, m ≥ 2,
A = (A1, . . . , Am), f, g ∈ F [t] relatively prime polynomials and put ψ = f /g and Ψ =
ψ + ∑m
i=1 Ait
i. Assume deg f > deg g + m. Further assume that ψ′ is not a constant if
p = m = 2. Then the system of equations

Proposition 3.6. Let F be a ﬁeld of characteristic p ≥ 0, let 1 ≤ m < k, let
A = (A0, . . . , Am) an (m + 1)-tuple of variables, and let f, g ∈ F [t] be relatively prime
polynomials with deg g + m < k = deg f . Assume

Proposition 6.1. For k > 1 and 0 < ǫ < 1
k we have

Proposition 6.2. For q = p2n, k = p2, and 1
k ≤ ǫ < 2
k we have

Proposition 6.3. For q = p2n, f = t
p2+1, k = p2 + 1, and 1
k ≤ ǫ < 2
k we have

*[digest of a 31480 character source; every section, statement, and proof in full at `research/sources/bank_barysoroker_rosenzweig_1302.0625.full.md`]*
