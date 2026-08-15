# Keith Conrad, "The unit theorem" (gradnumthy/unittheorem.pdf)

**Primary source URL:** https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf
**Type:** University course notes, Keith Conrad (UConn).
**How obtained:** server-side readout via `read_sources`.

## Exact statements captured

1. **Dirichlet's unit theorem:** For the ring of integers `O` of a number field, `O^× ≅ W × Z^r`, where `W` is the finite group of roots of unity and `r = r_1 + r_2 - 1` (one less than the total number of embeddings `r_1 + 2r_2 = [K:Q]`). For cyclotomic fields `Q(ζ_p)`, `r_1 = 0` and `r_2 = (p-1)/2`, giving rank `r = (p-1)/2 - 1 = (p-3)/2`.

2. **Minkowski bound → class number control:** The Minkowski convex-body bound gives a *finite* set of prime ideals to check for principality; if no prime ideal of small norm exists (e.g. the defining polynomial stays irreducible mod those `p`), the class number is 1 and `O` is a PID. Example in source: `T^3 - 3T - 1` irreducible mod 2, Minkowski bound exactly 2 → the cubic ring is a PID.

## Relation to the problem

- For `Q(ζ_p)`, `r_2 = (p-1)/2`, so the unit rank is `(p-3)/2`. This is the free-rank of the unit group that sits *inside* `Z[ζ_p]^×`; the cyclotomic units form a finite-index subgroup of it, and the index `[E:C]` is the plus-part class number machinery (Sinnott). This is the exact structural fact the `circular-units-index-plus-part` claim rests on.
- Minkowski bound is how one shows *small* `p` cyclotomic fields are PIDs (class number 1); it is why regularity (p ∤ h) is checkable for many p.

## Status

Sourced, asserted-by-source. Standard theorem.

## Claim

```claim
id: dirichlet-unit-theorem-cyclotomic-rank
statement: For the ring of integers O of a number field, O^× ≅ W × Z^r with W the roots of unity and r = r_1 + r_2 - 1 (one less than the number of embeddings). For K = Q(zeta_p), p odd prime, r_1 = 0 and r_2 = (p-1)/2, so the unit rank is (p-3)/2; the cyclotomic units form a finite-index subgroup of O^× (in the real subfield, index [E : C] is the plus-part class number machinery).
hypotheses: K a number field; p an odd prime for the cyclotomic rank.
holds-here: yes — this is the structural basis of the circular-units-index-plus-part claim and the h^+ obstruction.
status: asserted (Conrad unit theorem handout, and standard).
bearing: fixes the free rank of the unit group inside Z[zeta_p]^×; the circular-units index [E:C] = h^+ (the non-computable half of the class-number obstruction) is an index inside this Z^r.
anchor: research/sources/conrad-unit-theorem.about.md
follows-from: (none — fundamental theorem, not derived here)
```

The Galois tier in `conrad-cyclotomic-extensions.about.md`
(`Gal(Q(zeta_n)/Q) ≅ (Z/nZ)^×`, `Phi_n` monic irreducible, primitive roots
Galois-conjugate) is background only; it is covered by the ring/ramification
claims and adds nothing load-bearing beyond the Galois-group identification.
