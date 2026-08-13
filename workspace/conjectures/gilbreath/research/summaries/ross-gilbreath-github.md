# Ross, "Empirical Structure of the Gilbreath Decay Constants" — companion code (GitHub)

<!-- source: https://github.com/michaelmross/Gilbreath | full text: sources/ross-gilbreath-github.full.md -->

Companion repository for the Zenodo note of the same name (zenodo.21326025/6, July 2026) on the
CHT stationary continuous Gilbreath model (top row i.i.d. Exp(1), `c_i = E a(i,j)` at depth i).

## What it establishes

- The repo is reproducible infrastructure, not a new theorem: exact rational `c_i` via
  sign-cone decomposition (`src/exact_ci.py`, needs pycddlib built with GMP) extends CHT's
  exact `c_0=1, c_1=7/9, c_2=?, c_3=227/288` — CHT's smoke-test values are
  `exact_ci.py 2 -> 7/9`, `exact_ci.py 3 -> 227/288`, and the new values are `c_4`,
  `c_5`, `c_6` (about 2M sign patterns for `c_6`), each certified by a partition-of-unity
  identity ("volume check: 1").
- Empirical laws (Monte Carlo, depth 8192): `c_i ≈ C·λ^{s_2(i)}/i` with λ drifting
  1.14–1.20; digit-sum classes reveal the 1/i envelope; dyadic sawtooth in pooled data;
  sublinear full-row grind-down `τ(G) ≈ G^{0.63–0.66}`; a spike of amplitude G survives to
  distance ≈ G.
- Cross-links: companion parity note "Is Gilbreath's conjecture garden-variety
  numerology?" (michaelmross.github.io), OEIS A397880 / A395556, arXiv:2607.08712.
- **Corrected Zenodo path:** the record's own API (sources/ross-gilbreath-decay-constants-zenodo-api.full.md)
  gives concept DOI 10.5281/zenodo.21326025 (parent) and version 10.5281/zenodo.21326026; the PDF
  is fetched at sources/ross-gilbreath-decay-constants-pdf.full.md.

## Bearing on this run

The digit-sum (A000120) modulation is the continuous-model mirror of the Pascal/mod-2
structure the run's mod-4 linearization uses on the discrete prime rows — independent
confirmation that the {0,2}/Rule-90 microscope is the right one. The still-open question
"is (c_i) bounded?" is the averaged shadow of the run's regeneration obstruction.

## Source status

Code repo, MIT licence, 21 commits, 0 stars; note author Michael M. Ross
(ORCID 0009-0001-3428-5337). Claims are empirical except the exact low-depth values and
their certificates. Not a proof about primes.