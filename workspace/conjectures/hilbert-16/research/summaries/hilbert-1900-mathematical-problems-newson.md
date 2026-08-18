# Hilbert (1900), "Mathematical Problems" — Problem 16, original wording

<!-- source: https://www.gutenberg.org/files/71655/71655-h/71655-h.htm (Newson 1902 trans., Bull. AMS 8 (1902) 437-479). Full text: [[hilbert-1900-mathematical-problems-newson.full]]. Claim `h16-hilbert-1900-canonical-statement`. -->

## What it establishes — the canonical statement of H16

For a first-order differential equation `dy/dx = Y/X`, where X, Y are **rational
integral functions of degree n** (polynomial vector fields), determine:

> "the relative position of the cycles consisting of the integral curves in the
> neighbourhood of which the integral curves form a spiralling motion" — i.e.
> **the maximum number and relative position of Poincaré's "cycles limites"
> (boundary cycles / limit cycles).**

Two load-bearing facts in the original:

1. **Uniformity is the content.** Hilbert frames H16 as answerable by the same
   method of "continuous variation of coefficients" as the algebraic part. So
   H(N) is defined as a **uniform bound over the whole family of degree-n
   fields** (max over all fields, all locations) — not a pointwise bound. This is
   the reading the run's Lean statement `h16_2` implements (`∃N`, every degree-≤n
   field has ≤ N limit cycles), and it is what separates H16.2 from the
   (settled-but-contested) Écalle–Ilyashenko individual finiteness.
2. The two halves (real algebraic curves; limit cycles of a differential
   equation) share a number and are posed together. Part I — real schemes — is
   out of scope for this run (per GOAL), but the shared-number framing is why the
   two parts are historically linked.

## Hypotheses / holds here

Polynomial vector fields (X,Y rational integral of degree n). **Holds here:
yes** — anchors the uniform-bound reading of H16.2 used throughout.

**Evidence class: sourced** (Hilbert 1900, Newson 1902 translation, full text
held from Project Gutenberg #71655).

## Bearing / implication

Fixes the definition of H(n) the whole run computes against: a uniform bound
over the family. Any claimed upper bound must be uniform over degree-n fields
(test 2 in problem.md); the local/small-amplitude bounds (M(n)) are the weaker
local version.
