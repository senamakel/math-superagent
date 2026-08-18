> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/reichstein-algebraic-groups.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2204.13202 | converted from PDF -->

## What it claims

Abstract. The algebraic form of Hilbert’s 13th Problem asks for the resolvent degree
rd(n) of the general polynomial f (x) = x
n+a1x
n−1+. . .+an of degree n, where a1, . . . , an
are independent variables. The resolvent degree is the minimal integer d such that every
root of f (x) can be obtained in a ﬁnite number of steps, starting with C(a1, . . . , an)
and adjoining algebraic functions in ⩽ d variables at each step. Recently Farb and
Wolfson deﬁned the resolvent degree rdk(G) of any ﬁnite group G and any base ﬁeld k
of characteristic 0. In this setting rd(n) = rdC(Sn), where Sn denotes the symmetric
group. In this paper we deﬁne rdk(G) for every algebraic group G over an arbitrary ﬁeld
k, investigate the dependency of this quantity on k and show that rdk(G) ⩽ 5 for any
ﬁeld k and any connected group G. The question of whether rdk(G) can be bigger than
1 for any ﬁeld k and any algebraic group G over k (not necessarily connected) remains
open.
 1. Introduction

The algebraic forms of Hilbert’s 13th Problem asks for the resolvent degree rd(n), which
is the smallest integer d such…

## Statements it makes

Theorem 1.1. Let G be a connected algebraic group over a ﬁeld k. Then
(a) rdk(G) ⩽ 5.
(b) Moreover, if G has no simple components of type E8, then rdk(G) ⩽ 1.

Theorem 1.2. Let G be an algebraic group deﬁned over k. Then rdk(G) = rdk′(Gk′) for
any ﬁeld extension k′/k.

Theorem 1.3. Let G be a smooth aﬃne group scheme over Z. Denote the connected
component of G by G0. Assume that G0 is split reductive and G/G0 is ﬁnite over Z. Let
k be a ﬁeld of characteristic 0. Then rdk(Gk) ⩾ rdk(Gk0) for any other ﬁeld k0.

Conjecture 1.4. rdk(G) ⩽ 1 for any connected algebraic group G over any ﬁeld k.

Theorem 1.1(a) (or more precisely, Proposition 16.1(a)), may thus be viewed as a partial
answer to Tits’ question. Note that it is not known whether or not rdk(G) can be > 1 for
any ﬁeld k and any algebraic group G deﬁned over k (not necessarily connected).
The remainder of this paper is structured as follows. Sections 2 and 3 are devoted to
preliminary material on essential dimension of ﬁnite-dimensional algebras and ﬁeld exten-
sions. In Section 4 deﬁnes the level of a ﬁnite ﬁeld extension and explores its elementary
properties. Section 5 studies how the level changes under specialization. Section 6 in-
troduces the level d closure of a ﬁeld. The resolvent degree of a functor is…

Theorem 1.3 in Section 13, and the proof of Theorem 1.1 in Sections 14 - 16. In the last
section we show that Conjecture 1.4 follows from a positive answer to a long-standing
open question of Serre (Question 17.1).
The main focus of this paper is on the aspects of the subject which have not been pre-
viously investigated: resolvent degree of connected groups and dependence of resolvent
degree on the base ﬁeld. However, many of the preliminary results overlap with exist-
ing literature and some have classical roots. In particular, Section 4 overlaps with [16,
Section 2], Section 10 with [16, Section 3]. Section 6 elaborates on the short note of
Arnold and Shimura [6, pp, 45-46]; there is…

Lemma 2.1. Let k ⊂ K be a ﬁeld extension, A a ﬁnite-dimensional K-algebra, and S a
ﬁnite subset of A. Then A/K descends to A0/K0 such that K0 is ﬁnitely generated over
k, A0 is a K0-subalgebra of A, and S ⊂ A0.

Lemma 2.3. Let K be a ﬁeld containing k and A a ﬁnite-dimensional K-algebra. Then
edk(A) < ∞. Moreover, A/K descends to some A0/K0 such that K0 is ﬁnitely generated
over k and edk(A) = edk(A0) = trdegk(K0).

Lemma 2.4. Let k ⊂ k′ ⊂ K be ﬁelds and A be a ﬁnite-dimensional K-algebra. Then
(a) edk′(A) ⩽ edk(A).
(b) If k′ is algebraic over k, then edk′(A) = edk(A).
(c) There exists an intermediate ﬁeld k ⊂ l0 ⊂ k′ such that l0 is ﬁnitely generated over
k and edl(A) = edk′(A) for any l0 ⊂ l ⊂ k′.

Lemma 3.1. Let k ⊂ K ⊂ L be ﬁeld extensions such that [L : K] < ∞.
(a) If K sep is the separable closure of K in L, then edk(K sep/K) ⩽ edk(L/K) and
edk(L/K sep) ⩽ edk(L/K).
(b) If L is separable over K,…


*[further statements in the full text]*

*[digest of a 112012 character source; every section, statement, and proof in full at `research/sources/reichstein-algebraic-groups.full.md`]*
