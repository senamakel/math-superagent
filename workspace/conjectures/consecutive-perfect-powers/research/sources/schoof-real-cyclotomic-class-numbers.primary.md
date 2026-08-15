# Schoof, "Class numbers of real cyclotomic fields of prime conductor" — retrieved primary content

- Author: René Schoof.
- Source: Math. Comp. **72** (2003), 913–937. DOI 10.1090/S0025-5718-02-01432-1.
- Full text PDF (freely hosted): https://www.mat.uniroma2.it/~schoof/realcyc.pdf
- How obtained: retrieved **full-text readout via `read_sources`** (server-side) on
  `https://www.mat.uniroma2.it/~schoof/realcyc.pdf`. `download_document` on the same
  host is refused by the network boundary, so this is a captured readout, not a
  stored PDF. This file records the genuine primary content that readout returned.

## Content established (as retrieved)

### Setup

Let `l` be a prime and `ζ_l` a primitive `l`-th root of unity. The cyclotomic field
`Q(ζ_l)` has class group `Cl` of its ring of integers, with class number `h_l`. The
group naturally splits into two parts via the action of complex conjugation on
`Gal(Q(ζ_l)/Q) = (Z/lZ)^×`; there is a natural exact sequence

    0 -> Cl^+ -> Cl -> Cl^- -> 0

where:

- `Cl^+_l` is the class group of the **maximal real subfield** `Q(ζ_l + ζ_l^{-1})`
  (degree `(l-1)/2` over `Q`); its order is `h^+_l`, the **plus** or real class number.
- `Cl^-_l` is the **minus part** (kernel of the norm), of order `h^-_l`, the
  **relative** (minus) class number.
- `h_l = h^+_l · h^-_l`.

Both `Cl^-_l` and `Cl^+_l` are finite modules over `Z[G_l]`, `G_l = Gal(Q(ζ_l)/Q) ≈
(Z/lZ)^×`, and admit Jordan–Hölder filtrations whose simple factors are
1-dimensional spaces over the finite residue fields of `Z[G_l]`.

### Main computational results

- The paper computes all simple Jordan–Hölder factors of order **less than 80,000**
  that occur in `Cl^+_l` (equivalently `Bl` as they denote the plus part in the minus
  module) for all primes `l < 10,000`.
- For each such `l` it determines `h̃^+_l`, the order of the largest subgroup of
  `Cl^+_l` all of whose Jordan–Hölder factors have order `< 80,000`.
- It is **proved** that `h̃^+_l | h^+_l`, i.e. the computed proxy divides the true
  plus class number.
- Among all simple factors of order `< 80,000` occurring for some `l < 10,000`, only
  **354** distinct ones appear; the largest has order **1451**.
- The computation does **not** determine the full `l`-part of `h^+_l` for all
  `l < 80,000`; the true `h^+_l` could in principle be larger than `h̃^+_l` by a
  factor up to `80,000`.

### Why the run wants it

The obstacle for `x^p - y^q = 1` with `p, q` odd is the class group of `Q(ζ_p)`; the
library's structural fact is **minus computable, plus not**. This source is the
canonical statement of that asymmetry for the real (plus) side, and it fixes the
exact-sequence form `0 -> Cl^+ -> Cl -> Cl^- -> 0` and the `h = h^+ h^-`
factorisation. It also gives the strongest practical bound the reference library
holds on `h^+_p` for `p < 10,000`.

## Relation to the known solution

This is pure machinery: nothing here is a statement about the equation `x^p - y^q =
1`. The known solution `(3,2,2,3)` has exponent `p = 2` even, so no `Q(ζ_p)` with
`p` odd prime is involved. The content is the toolkit the run's own derivation must
use.

## Status

- **Primary research-paper content, retrieved server-side.** This is a genuine
  full-text readout, not an abstract, and it is technique (class-number structure),
  not the answer to Catalan's conjecture. Nothing here is screened.
- The Jordan–Hölder factor counts (`354`, `1451`) are the paper's computed results,
  quoted as reported; they have not been re-derived in this run.

## Claims

```claim
id: schoof-plus-minus-exact-sequence
statement: >
  The class group Cl of Q(zeta_l) (l prime) sits in the exact sequence
  0 -> Cl^+ -> Cl -> Cl^- -> 0, with Cl^+ the class group of the maximal real
  subfield Q(zeta_l + zeta_l^{-1}) and Cl^- the minus part (kernel of the norm);
  h_l = h^+_l * h^-_l.
hypotheses: l a prime.
holds-here: yes — the obstruction in the (p,q odd) case is the class group of Q(zeta_p), and the +/- split is its first structural fact.
status: proved in Schoof 2003; asserted here (source retrieved, not re-derived).
anchor: research/sources/schoof-real-cyclotomic-class-numbers.primary.md
bearing: fixes the exact-sequence h = h^+ h^- form the run's class-group control must respect.
```

```claim
id: plus-class-proxy-bounds-true
statement: >
  For every prime l < 10^4, h~^+_l (order of the largest subgroup of Cl^+_l all
  of whose Jordan-Hölder factors have order < 80,000) divides the true plus class
  number h^+_l; the computation establishes only h~^+_l, so true h^+_l may exceed
  it by a factor up to 80,000. Only 354 distinct simple factors of order < 80,000
  occur for all l < 10^4, largest 1451.
hypotheses: l a prime < 10,000.
holds-here: yes — the strongest practical bound the library holds on h^+_p for p < 10^4.
status: the divisibility h~^+ | h^+ is proven in the paper (asserted here); the 354/1451 counts are computed results quoted as reported, not re-derived.
anchor: research/sources/schoof-real-cyclotomic-class-numbers.primary.md
bearing: bounds what a computational check can establish for the plus part; a run-proof must not assume h^+ computed.
```
