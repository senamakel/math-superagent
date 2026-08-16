> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2512.24061 | converted from PDF -->

## What it claims

The determination of ES(7) is the first open case of the planar Erdős–Szekeres problem,
where the general conjecture predicts ES(7) = 33. We present a SAT encoding for the 33-
point case based on triple-orientation variables and a 4-set convexity criterion for excluding
convex 7-gons, together with convex-layer anchoring constraints. The framework yields UN-
SAT certificates for a collection of anchored subfamilies. We also report pronounced runtime
variability across configurations, including heavy-tailed behavior that currently dominates
the computational effort and motivates further encoding refinements.

Keywords: Erdős–Szekeres problem, SAT solving, discrete geometry, convex layers, order
types, automated reasoning.

1 Introduction

In their seminal 1935 paper, Erdős and Szekeres investigated the smallest integer ES(k) such
that any set of ES(k) points in the plane in general position (no three collinear) contains k
points in convex position [1]. They conjectured the exact formula

ES(k) = 2k−2 + 1 (k ≥ 3).

This formula is verified for k ≤ 6. Moreover, the classical…

∗Faculty…

## Statements it makes

Definition 1 (3-cup / 3-cap (convention)). Fix a convention: χ(a, b, c) = + corresponds to a
3-cup and χ(a, b, c) = − corresponds to a 3-cap (or vice versa). The convention is arbitrary
but must be used consistently.

Proposition 1 (4-set criterion for convex position). Let S be a finite set of points in the plane
in general position. Then S is in convex position if and only if every 4-point subset of S is in
convex position.

*[digest of a 18286 character source; every section, statement, and proof in full at `research/sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`]*
