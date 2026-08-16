# Sums of products of binomial coefficients mod 2 are 2-regular — Wu (2023)

Source: https://arxiv.org/pdf/2309.04012 (arXiv:2309.04012)
Full text: [[run-length-transform-binmod2-wu.full]]

## What it establishes

Shows that the **run length transforms** (binary-expansion run-length transform, as
defined in the 2022 INTEGERS companion) of famous linear recurrence sequences — the
positive integers, Fibonacci, extended Lucas, Narayana's cows — are **2-regular
sequences**. This is proved using the computer program **Walnut** (automated proof for
automatic/regular sequences), eliminating long technical proofs.

- Run length transforms of recurrence sequences are 2-regular.
- Gives a method (Walnut) for verifying such identities automatically.

## Bearing for this problem

Confirms the 2-regularity vocabulary around run-length transforms of binomial-mod-2
sums — the same family as the run-count statistics this run computes. **Weak bearing**:
the object studied (run length transform of a recurrence sequence, indexed by binary
runs of `n`) is again *not* this problem's maximal-consecutive-integer runs inside
`M_d`, nor the symmetric-difference multiset. It supplies vocabulary and an automated
verification style, not new structure for the crux.

## Contradiction / non-bearer note

The name "run length transform" is shared with item 5's "runs of `M_d`" but the two are
**different objects**. Do not cite this paper as establishing the run structure of `M_d`.
