> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/gasull-santana-note-h16-2024-arxiv.pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2407.13465 | converted from PDF -->

## What it claims

Abstract. Let H(n) be the maximum number of limit cycles that a planar
polynomial vector ﬁeld of degree n can have. In this paper we prove that H(n)
is realizable by structurally stable vector ﬁelds with only hyperbolic limit cycles
and that it is a strictly increasing function whenever it is ﬁnite.

1. Introduction and statement of the main results

Consider the planar polynomial system of diﬀerential equations X = (P, Q) given
by

(1) ˙x = P (x, y), ˙y = Q(x, y),

where the dot means the derivative in relation to the independent variable t and P ,
Q : R2 → R are polynomials. To system (1) corresponds a polynomial vector ﬁeld
X = P ∂
∂x + Q ∂
∂y in the phase plane of the variables x and y. In this paper we make
no distinction between system (1) and its respective vector ﬁeld. The degree of X
is the maximum of the degrees of P and Q. Given n ∈ N, let X n be the set of the
planar polynomial systems (1) of degree n, endowed with the coeﬃcients topology.
Given X ∈ X n, let π(X) ∈ Z⩾0 ∪ {∞} be its number of limit cycles (i.e. isolated
periodic orbits).
In his famous address to the…

H(n)…

## Statements it makes

Theorem 1. Given n ∈ N, it holds H(n + 1) ⩾ H(n) + 1.

Theorem 2. For n ∈ N, the following statements hold.

Theorem 3 ([5]). Let Xα be the family of rotated vector ﬁelds (2) and suppose
that Xα0 has a limit cycle γα0 . Then:

Proposition 1. Let Xα be the family of rotated vector ﬁelds (2) and suppose that
Xα0 has a limit cycle γα0 . Then, for |α − α0| > 0 small enough, all the limit cycles
detailed in Theorem 3 that bifurcate from γα0 are hyperbolic.

Proposition 2. Let X ∈ X n. Then the following statements hold.
(a) If π(X) < ∞, then there is Y ∈ X n such that πh(Y ) ⩾ π(X).
(b) If π(X) = ∞, then for each k ∈ N there is Yk ∈ X n such that πh(Yk) ⩾ k.

Lemma 1. Let X ∈ X n and B ⊂ R2 a closed ball centered at the origin. Then
there is an arbitrarily small perturbation Y of X having a regular point p ∈ R2\B
such that ℓ ∩ B = ∅, where ℓ is the straight line p + sY (p), s ∈ R.

Theorem 1 is not the ﬁrst known result about recurrence properties of H(n).
It follows from the proof of Christopher and Lloyd [4] that H(2n + 1) ⩾ 4H(n).
Roughly speaking, given X ∈ X n, the authors translate all the limit cycles of
X to the ﬁrst quadrant and thus apply the non-invertible transformation (x, y) ↦→
(u2, v2), followed by the rescaling of time dt/dτ = 2uv. Hence, obtaining Y ∈ X 2n+1

Proposition 3. Let X be a planar analytic vector ﬁeld. Then X has an enumerable
number of limit cycles. In particular, H(n) ⩽ ℵ0 for every n ∈ N.

*[digest of a 23112 character source; every section, statement, and proof in full at `research/sources/gasull-santana-note-h16-2024-arxiv.pdf.full.md`]*
