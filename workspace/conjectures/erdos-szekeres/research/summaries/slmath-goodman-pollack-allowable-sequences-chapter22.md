# Hagit Last, "Two Proofs for Sylvester's Problem Using an Allowable Sequence" (MSRI/SLMath 2005)

<!-- source: https://library.slmath.org/books/Book52/files/22last.pdf | full text at research/sources/slmath-goodman-pollack-allowable-sequences-chapter22.full.md -->

**Publication.** Hagit Last, *Two Proofs for Sylvester's Problem Using an Allowable
Sequence of Permutations*, in *Combinatorial and Computational Geometry*, MSRI
Publications Vol. 52 (2005), pp. 433–436. Free PDF at the SLMath (formerly MSRI)
library. This is **not** the Goodman–Pollack 1980/1993 originals, but it contains a
precise, self-contained, published statement of the allowable-(circular-)sequence
definition that the run's live `allowable-sequence` thread had flagged as
*unsourced on disk* (`gp80-not-held-circular-sequence-unsourced`).

## Why this closes a genuine library gap

The thread `research/threads/allowable-sequence.md` rests on the Goodman–Pollack
allowable (circular) sequence as the finite combinatorial encoding of an order
type — convexity/staircase structure is read off the sequence — but its `next`
block records that the load-bearing **definition** was not on disk: "*fetch GP80 /
GP93 survey or verify against the oracle before that claim becomes load-bearing.*"
The 1980 JCTA paper (DOI 10.1016/0097-3165(80)90011-4) and the 1993 Springer survey
chapter "Allowable Sequences and Order Types in Discrete and Computational
Geometry" (in *New Trends in Discrete and Computational Geometry*, Springer 1993,
pp. 103–134) are both paywalled. This MSRI chapter provides the same definition,
freely, and attributes it to GP80/GP93.

## The definition (verbatim content, Section 1)

Given a set S of n points, L the set of lines spanned by S, and {k_1,…,k_m} the m
distinct slopes. Choose a directed line ℓ with a point P on it, such that ℓ
contains no point of S and is orthogonal to no line in L.

**Construction of A_{ℓ,P}(S).** Label the points of S by their orthogonal
projection onto ℓ → first permutation π₀ = 1,…,n. Rotate ℓ counterclockwise about
P through 180°, tracking the projections of the labeled points. A new permutation
arises each time ℓ passes a direction orthogonal to one of the slopes k_i, giving
permutations π₁,…,π_m. Define A_{ℓ,P}(S) = {π₀,π₁,…,π_m}. At each critical
direction the new permutation differs from the previous by reversing the
consecutive elements whose points lie on a line of that slope — a *reversed
substring*; a reversed substring of length 2 is a *simple switch* (corresponds to a
*simple line*).

**Three properties.**
1. A_{ℓ,P}(S) is a sequence of permutations of {1,…,n}.
2. First permutation π₀ = 1,…,n; last π_m = n,…,1.
3. Every pair i<j switches exactly once across the sequence, and each consecutive
   pair of permutations differs by reversing a single increasing substring. (The
   digest confirms: "Each pair i<j switches exactly once across the entire
   sequence, and each consecutive pair of permutations differs by reversing a
   single increasing substring, i.e. a single reversed substring that is
   increasing in the previous permutation.")

This matches the notion the run's `allowable_encoder.py` implements: C(N,2) events,
each an adjacent reversal in the simple case, with the last permutation the reverse
of the first; exactly the "circular sequence" object the thread is measuring
convexity and ES block-depth against.

## Cautions

- This is a *source for the definition and its standard properties*, not for the
  GP80 classification theorem (n ≤ 5 order types) nor the full GP93 survey. Those
  remain paywalled; if a precise statement of either becomes load-bearing it
  should be fetched separately (MaRDI portal holds the records).
- Convexity-from-sequence (staircase/extreme-in-projection) is **not** stated in
  this chapter; the run's `staircase-convexity-unsourced` flag therefore still
  stands, and that characterization must be verified against the exact oracle
  (which the captures began doing) rather than cited from here.
- The chapter is about Sylvester's problem/Gallai's theorem as application; the ES
  connection is not in it. It is acquired for the definition alone.

```claim
id: gp-allowable-sequence-definition
statement: The Goodman–Pollack allowable (circular) sequence of a point set S (after GP80) is the sequence of permutations A_{l,P}(S) obtained by orthogonally projecting S onto a directed line l rotating counterclockwise 180° about a point P; a new permutation arises at each critical direction orthogonal to a slope of a line spanned by S, by reversing the points collinear on that slope (a reversed substring). Properties: it is a sequence of permutations of {1..n}; it runs from 1..n to n..1; each pair of labels switches exactly once over the period; each consecutive pair of permutations differs by reversing a single increasing substring. Each pair of labels thus reverses exactly once per half-period, giving C(n,2) switch events for a simple configuration.
hypotheses: S in the plane, no three collinear, no two sharing an x-coordinate (the general-position/configuration convention); l not orthogonal to any spanned line.
holds-here: true — this is the object the run's allowable_encoder.py builds (C(N,2) events, adjacent reversals, last permutation = reverse of first); the thread's convexity-from-sequence checks are measured against this exact object.
status: sourced (published MSRI chapter, free full text; definition attributed to Goodman–Pollack 1980, survey 1993, both of which remain paywalled here).
bearing: fixes the load-bearing definition the allowable-sequence thread previously lacked on disk; removes the gp80-not-held-circular-sequence-unsourced gap (definition part). The composition-of-permutations reversal rule (single switching pair per adjacent step, exactly once per half-period) is the mechanism the reversible-depth = ES block statistic and the staircase-convexity characterization are computed from.
anchor: research/sources/slmath-goodman-pollack-allowable-sequences-chapter22.full.md
```
