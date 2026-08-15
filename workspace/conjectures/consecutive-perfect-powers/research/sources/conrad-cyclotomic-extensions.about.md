# Keith Conrad, "Cyclotomic Extensions" (Galois theory notes, cyclotomic.pdf)

**Primary source URL:** https://kconrad.math.uconn.edu/blurbs/galoistheory/cyclotomic.pdf
**Type:** University course notes, Keith Conrad (UConn).
**How obtained:** server-side readout via `read_sources`.

## What this source establishes

Introductory material on cyclotomic extensions: definition of cyclotomic fields, Galois group `Gal(Q(ζ_n)/Q) ≅ (Z/nZ)^×`, cyclotomic polynomial `Φ_n`, separability, and Kronecker–Weber. It is the *entry-level* tier of the problem's machinery — the Galois-theoretic foundation. It does **not** reach the ring of integers, ramification, cyclotomic units, or class numbers (those are in the Stanford 676 `factorize.pdf` and unit-theorem handouts, also captured).

Section on `Φ_n` irreducibility and Galois conjugacy of primitive roots of unity that this text establishes:
- `Gal(K_n/Q) ↪ (Z/nZ)^×` is an isomorphism, where `K_n = Q(ζ_n)`.
- All primitive `n`-th roots of unity are Galois conjugate over `Q` (share the minimal polynomial `Φ_n`).
- `Φ_n` is monic in `Z[X]`, divides `X^n - 1` in `Z[X]`, and (Gauss's lemma) any monic factorisation over `Q` descends to `Z[X]`.

## Status

Sourced, asserted-by-source. This is background; the load-bearing ring-of-integers and ramification facts live in `conrad-factorization-cyclotomic.primary.md`.
