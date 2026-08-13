# The Modulo-k Gilbreath Family — Li, Zenodo preprint, March 2026

<!-- source: https://doi.org/10.5281/zenodo.19522976 | full text: sources/li-2026-modulo-k-gilbreath-family.full.md -->

The strongest generalisation in the library. For odd k, take the sequence of all primes of
the form `kn + 2` and iterate absolute differences; the claim is that the leading entry
eventually stabilises to **k**, with the classical conjecture (k=1, all primes) as the
degenerate case.

## What it claims

- For any odd k, the primes of the form `kn + 2` produce a difference triangle whose
  leading entry stabilises to k from the second row onward (modulo-k Gilbreath family;
  classical case k=1).
- Mechanism offered: **modular invariance** — the parity argument that the run's reduction
  uses (2 is the only even prime) generalises: for primes `p ≡ 2 (mod k)`, differences of
  consecutive such primes are `0 mod k`, so rows have the shape
  `(k, 0 mod k, 0 mod k, ...)` and `|k - m| = k` iff `m ∈ {0, 2k}`... (the exact residue
  closure needs the paper's own statement; the abstract only guarantees stabilisation).
- Computational verification: all odd k < 100,000.
- Studies inadmissible residue classes causing localised collapses, and fault tolerance in
  higher-order entries.

## How to read it

This is the **general-class direction the run's ROOT.md commits to**, taken an order of
magnitude further: the structural fact is not "leading entry is 1" but "leading entry
stabilises to the modulus k". If the modulo-k stabilisation ever gets a proof for the
general class, the k=1 case is the corollary. As it stands it is a **preprint with
computational verification** (odd k < 100,000), not a peer-reviewed theorem; its modular
invariance discussion is the part worth mining for the k=1 argument.

## Bearing on this run

- Strengthens the "not about primes" framing with a second independent generalisation
  family (alongside Chase's random model).
- The k-generalisation is a natural falsifier/consistency check: any invariant that proves
  the k=1 case via "2 is the only even prime" must be examined to see whether it would
  wrongly also force the k>1 stabilisation (which is only verified, not proved) — if a
  proposed invariant proves too much too cheaply, that is evidence it is vacuous.
- A concrete oracle extension: compute the modulo-k triangles **for small odd k and small
  depths** and check the k-stabilisation numerically; record as a checked claim. (Not yet
  done — a natural small task for the run's own oracle, since it is computable here and
  needs no outside source.)

## Source status

Zenodo preprint v2 (9 Mar 2026), single author (Dong Li, TH Fire Test Company — h-index 0,
0 citations). Not peer-reviewed. Treat all theorem-level claims as **asserted-by-source,
unverified**; the verification data (odd k < 100,000) is computational and could be
spot-checked by this run's oracle.