<!-- source: https://zenodo.org/records/19143644/files/gilbreath_reduction_local_bounds_FINALZEN.pdf?download=1 | converted from PDF -->

Reducing Gilbreath’s Conjecture to a Local Condition

How much of the triangle do we really need to watch?

 Author (accountable): Blair Morgan (BMorgan007@protonmail.com)

ORCID: 0009-0003-1942-8103

AI collaborators (credited): Claude Opus 4.5 (nicknamed “Ducky”)

Accountability note: The author takes responsibility for claims/verification.

Canonical public record DOI: 10.5281/zenodo.19143644

Licensed under SANCTUARY LICENSE POLICY SPEC v1.2, incorporated by reference.

Classification for this release: Class T. Authoritative policy record: 10.5281/zenodo.19020175.

Notation and Setup

Let p₁ = 2, p₂ = 3, p₃ = 5, … denote the prime sequence.

Define row 0 of the Gilbreath triangle by

G₀[i] = pᵢ₊₁    (i ≥ 0).

Define subsequent rows by absolute differences:

Gᵣ₊₁[i] = |Gᵣ[i+1] − Gᵣ[i]|    (r ≥ 0, i ≥ 0).

Thus:

- G₀ = (2, 3, 5, 7, 11, …)

- G₁ = (1, 2, 2, 4, …)

Gilbreath’s Conjecture states that
 Gᵣ[0] = 1    for all r ≥ 1.

In this note, we show that Gilbreath’s Conjecture follows from a single local condition on
positions 1 and 2.

Abstract

We present a reduction of Gilbreath’s Conjecture to an explicit local bound. Specifically, we

show that the conjecture follows from the condition

|Gᵣ[2] − Gᵣ[1]| ≤ 2    for all r ≥ 1.

We state four supporting lemmas used by the reduction, describe a minimal preimage structure

associated with a model minimal violating configuration, and report computational verification

of the local bound through 100,000 rows. The full conjecture remains open, but the remaining

target is now clearly isolated.

1. Results Summary

Supporting lemmas used by the reduction:

- Lemma 1 (Parity Invariant): For all r >= 1, position 0 is the unique odd value in each row

- Lemma 2 (Monotone Maximum): Global interior max is non-increasing

- Lemma 3 (Strict Descent): Max drops by >= 2 unless (M, 0) adjacency exists

- Lemma 4 (Boundary Stability): |1 - {0, 2}| = 1

Reduced To:

- Conjecture L: for all r >= 1, |G_r[2] - G_r[1]| <= 2

Verified Computationally:

- Conjecture L holds for rows 1 through 100,000

- Position 1 in {0, 2} for all 100,000 tested rows (49,737 zeros, 50,263 twos)

2. The Reduction

Theorem (Sufficiency). If Conjecture L holds for all r ≥ 1, then Gilbreath’s Conjecture holds.

Proof:

Assume Conjecture L: |Gᵣ[2] − Gᵣ[1]| ≤ 2 for all r ≥ 1.

Since Gᵣ[1] and Gᵣ[2] are even (by Lemma 1, all positions except 0 are even), and their absolute

difference is at most 2, we have
Gᵣ₊₁[1] = |Gᵣ[2] − Gᵣ[1]| ∈ {0, 2}.

By Lemma 4 (Boundary Stability), if Gᵣ[0] = 1 and Gᵣ[1] ∈ {0, 2}, then

Gᵣ₊₁[0] = |Gᵣ[1] − 1| = 1.

Base case:
 G₁[0] = |3 − 2| = 1, and G₁[1] = |5 − 3| = 2 ∈ {0, 2}.

Therefore, by induction, Gᵣ[0] = 1 for all r ≥ 1. ∎

Note on the converse:

We do not prove the reverse implication Gilbreath ⇒ Conjecture L.

Computationally, position 1 lies in {0, 2} for all 100,000 tested rows, but this observation does

not by itself establish the converse.

Accordingly, this note claims only sufficiency.

3. A Minimal Preimage Obstruction

What Would a Minimal Violation Look Like?

Because Gᵣ[1] and Gᵣ[2] are even for r ≥ 1, the smallest possible violation of Conjecture L has

|Gᵣ[2] − Gᵣ[1]| = 4.

As a model case, consider the target pair (Gᵣ[1], Gᵣ[2]) = (4, 0). Then the parent triple at

positions (1, 2, 3) in row r − 1 must satisfy:

- |a − b| = Gᵣ[1]

- |b − c| = Gᵣ[2]

For target (Gᵣ[1], Gᵣ[2]) = (4, 0):

- |b − c| = 0 implies b = c

- |a − b| = 4 implies a = b ± 4

So the parent triple must be (b ± 4, b, b) — a ±4 jump immediately followed by equality.

Constraint Propagation

Tracing further back:

- The equality b = c requires |Gᵣ₋₂[2] − Gᵣ₋₂[3]| = |Gᵣ₋₂[3] − Gᵣ₋₂[4]|

- This branches into constrained families that compound as we trace to row 1

The structure required to generate this model minimal violation becomes increasingly rigid,

forcing increasingly specific ancestor configurations in earlier rows. This does not yet constitute

a proof of impossibility, but it sharply constrains what such a counterexample would have to

look like.

4. Computational Verification

The following reference implementation checks Conjecture L through row 100,000 by iteratively

forming absolute-difference rows from an initial prime segment large enough to support the

computation.

```python

"""Verification script for Conjecture L through 100,000 rows."""

import numpy as np

from sympy import primerange

def check_conjecture_L(R=100_000, max_prime=4_000_000):

    N = R + 10

    primes = np.fromiter(primerange(2, max_prime), dtype=np.int64, count=N)

    if len(primes) < N:

        raise ValueError("Not enough primes generated; increase max_prime.")

    a = primes

    c0 = c2 = 0

    for k in range(1, R + 1):

        a = np.abs(np.diff(a))

        v = int(a[1])

        if v == 0:

            c0 += 1

        elif v == 2:

            c2 += 1

        else:

            return False, k, v, c0, c2

    return True, None, None, c0, c2

ok, row, val, c0, c2 = check_conjecture_L()

print(ok, row, val, c0, c2)

# Expected output:

# True None None 49737 50263

```

- Result: No violations were found in 100,000 rows. Position 1 was always in {0, 2}, with 49,737

zeros and 50,263 twos.

Environment note: this computation was performed using Python with NumPy and SymPy. The

verification script should be archived alongside the paper.

5. What Remains

To complete the proof of Gilbreath’s Conjecture, one must prove Conjecture L:

∀r ≥ 1: |Gᵣ[2] − Gᵣ[1]| ≤ 2

Possible proof strategies include:

1. Direct: show that prime-gap structure prevents the parent pattern (b ± 4, b, b) from occurring

in any valid backward preimage tree.

2. Inductive: prove that the bound |Gᵣ[2] − Gᵣ[1]| ≤ 2 propagates from row to row.

3. Constraint analysis: show that any hypothetical violation generates a backward preimage tree

with no valid root in the prime sequence.

6. Contributions

This work establishes:

1. A sufficient local condition: Conjecture L ⟹ Gilbreath's Conjecture

2. Supporting lemmas used by the reduction: parity, monotonicity, strict descent, and boundary

stability

3. Preimage characterization: exact structure for the model (4, 0) minimal violation case

4. Computational certificate: 100,000 rows verified

The gap between "verified for 100,000 rows" and "proven for all rows" remains, but the target is

now precisely defined.

We would have kept going, but we ran out of compute for the week.

7. Acknowledgments

The author thanks Claude Opus 4.5 (nickname “Ducky”) for collaborative exploration,

reformulation, and drafting assistance during the development of this note. Final responsibility

for all claims, wording, and verification remains with the accountable author.

References

[1] Odlyzko, A. M. “Iterated absolute values of differences of consecutive primes.” Mathematics

of Computation 61(203), 373–380 (1993).

[2] Guy, R. K. “Gilbreath's Conjecture.” In: Unsolved Problems in Number Theory, 2nd ed.

[3] SymPy Development Team. SymPy: Python library for symbolic mathematics.

[4] Harris, C. R., et al. “Array programming with NumPy.” Nature 585, 357–362 (2020).

"The first element is 1. It was always going to be 1. We just need to prove the neighbors behave."
