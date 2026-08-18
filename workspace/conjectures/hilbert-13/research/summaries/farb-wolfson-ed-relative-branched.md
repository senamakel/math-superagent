> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/farb-wolfson-ed-relative-branched.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2510.22786 | converted from PDF -->

## What it claims

Abstract. We prove for various finite groups G and integers n ≥ 1 that there are families
of equations with Galois group G that cannot be simplified to a one-parameter family even
after adjoining a root of a polynomial of degree at most n. In more geometric language,
there are G-varieties X with the following property: for any G-equivariant branched cover
̃X → X of degree ≤ n, there is no dominant rational G-map ̃X 99K C to any G-curve C.
The method of proof is new, and applies in cases where previous methods do not.

1. Introduction

Let k be a perfect field. A G-variety over k is a k-variety X equipped with a faithful action
of a finite group G on X by birational automorphisms. A G-compression is a dominant
rational map f : X 99K Y

of G-varieties; equivalently, the G-action on X is the pullback via f of the G-action on Y .
In classical language, a G-compression is a simplification of equations via a rational change
of variables.

Example 1.1 (Kummer’s theorem). Suppose that char(k) ∤ n and that k contains a
primitive nth root of unity ζ ∈ k. Then every Z/nZ-variety compresses to…

## Statements it makes

Definition 1.2 (Essential dimension). Let k be a field. The essential dimension over
k of a faithful G-variety X, denoted edk(X 99K X/G) or edk(X), is the smallest d ≥ 1 so
that there is a G-compression X 99K Y over k to a d-dimensional faithful G-variety Y .

Theorem 1.3 (Klein’s Normalformsatz). Let k be a field of characteristic 0 with √
5 ∈
k. Let X be any A5-variety over k. Then X has an A5-equivariant branched cover
2 ̃X 99K X
of degree at most 2 such that there is an A5-compression

Theorem 1.6 (Main Theorem). Let k be a perfect field. Let n ≥ 2. Let G be a finite
group such that:

Theorem 1.6 is applicable because its three hypotheses are easy to check in examples.
Over C, we can apply it to give the following.

Corollary 1.7 (Sample results).

Theorem 2.1 (Castelnuovo’s Inequality). Let C be an irreducible algebraic curve over a
perfect field k. Let fi : C → Di be rational maps of curves of degree ni ≥ 1 for i = 1, 2.
Assume that the map (f1, f2) : C → D1 × D2 is birational onto its image. Then

Lemma 2.2. Let C be an algebraic curve of genus g(C) over a perfect field k. Let j ≥ 1 and
let fi : C → P1 (so fi ∈ k(C)) have degree n ≥ 1 for i = 1, . . . , j. If k(f1, . . . , fj) = k(C),
then
 g(C) ≤ (n − 1)2.

Corollary 2.3. Let G be a finite group. Assume that |G| ∤ n and that G does not act
nontrivially on an algebraic curve of genus at most (n − 1)2. Then no faithful irreducible
G-curve C admits a degree n rational function.

Lemma 2.4. Let C be an irreducible curve. Suppose there exists a dominant map H → C
and a degree n rational function h : H → P1. Then C has a degree n rational function
f : C → P1.

Lemma 3.1. Let G be a finite group. Let k be a perfect field. Suppose that:

*[digest of a 22320 character source; every section, statement, and proof in full at `research/sources/farb-wolfson-ed-relative-branched.full.md`]*
