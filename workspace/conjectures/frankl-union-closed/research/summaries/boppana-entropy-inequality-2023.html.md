# Boppana, "A Useful Inequality for the Binary Entropy Function" — arXiv:2301.09664 (2023)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2301.09664 (also arxiv.org/pdf/2301.09664).
> Full text: `research/sources/boppana-entropy-inequality-2023.html.full.md`.

The clean, elementary proof of the one-variable entropy inequality that
underpins the whole `(3−√5)/2` barrier.

## What it establishes

- **Lemma (the entropy inequality).** If `0 ≤ x ≤ 1`, then
  `h(x²) ≥ φ·x·h(x)`, where `h` is the binary entropy and
  `φ = (√5+1)/2` is the golden ratio.
- **History recorded in-paper.** Boppana first used this (or a two-variable
  generalization) in the 1980s to prove lower bounds on Boolean formulas. The
  same inequality was later the analytic core of the union-closed progress:
  AHS proved it by computer; Chase–Lovett cited AHS; Pebody wrote "to be
  proven"; Sawin gave a symbolic proof; this note gives a simple proof by
  elementary differential calculus.
- The proof technique: basic differential calculus (base-e logs in the paper,
  but the inequality is base-independent).

## Relation to the barrier

The constant `φ = (√5+1)/2` is the reciprocal of `1−φ = (√5−1)/2 = (3−√5)/2`.
The inequality `h(x²) ≥ φ x h(x)` with `φ = (√5+1)/2` is equivalent (by the AHS
reduction) to the `1 − φ = (3−√5)/2` lower bound for the union-closed
conjecture. Its equality case `x ∈ {φ,1}` is exactly the sharpness described in
AHS's Claim 3 and Chase–Lovett's optimality example.

## Hypotheses and holds-here

- `x ∈ [0,1]`, `h` the binary entropy, `φ = (√5+1)/2`. **Holds-here:** this is
  the analytic inequality that the union-closed bound reduces to; no extra
  hypotheses on `ℱ`.

## What it lets the run do

- Gives an *elementary, checkable* statement of the key inequality, independent
  of the computer-assisted proof in AHS. Useful for any symbolic/interval
  verification of the barrier in `code/`.
- The equality case `x ∈ {φ,1}` is the extremal input to any attempt to prove
  that the iid method is capped.

```claim
id: boppana-entropy-inequality
statement: For 0≤x≤1, h(x²) ≥ φ·x·h(x) with φ=(√5+1)/2 (golden ratio) and h the
  binary entropy; proved by elementary differential calculus. Equivalent, via
  the AHS reduction, to the (3−√5)/2 = 1−φ upper bound being attained by the
  iid-OR entropy method.
hypotheses: x∈[0,1]
holds-here: yes
status: proved (elementary proof in-paper)
bearing: the exact analytic inequality bounding the iid entropy method at
  (3−√5)/2; its equality case is the extremal test object
anchor: research/sources/boppana-entropy-inequality-2023.html.full.md
follows-from: ahs-barrier-3-minus-rt5-over-2
```
