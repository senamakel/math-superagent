# Empirical Structure of the Gilbreath Decay Constants — Ross, Zenodo, July 2026

<!-- source: https://zenodo.org/records/21326026 | full text: sources/ross-gilbreath-decay-constants-zenodo-2026.full.md -->

Empirical study of the continuous model's decay constants; anchors OEIS A397880 (numerators
of c_n). Not a proof of anything about primes, but the quantitative companion to the CHT
lower bound.

## What it establishes

- Model: top row independent standard exponential variables; `c_i = E[a(i,j)]` at depth i.
  CHT proved `Σ_{i≤n} c_i ≥ log(n+e)`, computed c_0..c_3 exactly, left boundedness of
  `(c_i)` open.
- New **exact rational values for c_4, c_5, c_6** (code + certificates in
  `github.com/michaelmross/Gilbreath`, exact rational arithmetic).
- Monte Carlo to depth 8192. Principal empirical law `c_i ≈ C·λ^{s_2(i)}/i` with effective
  λ drifting through ~1.14–1.20; conditioning on digit-sum classes reveals the 1/i decay;
  pooled data show a dyadic sawtooth.
- Finite-depth experiments: polynomial-vs-exponential growth transition for continuous
  uniform data; full-row relaxation ~ G^0.63–G^0.66; spike survival distance asymptotic to
  its amplitude.
- `c_i` is not monotone: `c_2 < c_3`, `c_3 > c_4 < c_5 > c_6`, tracking the binary digit
  sum A000120(n) (also in the OEIS A397880 summary already on disk).

## Bearing on this run

- The digit-sum structure of the *continuous* model is the same Pascal/mod-2 structure the
  run's `mod4-linearization` claim uses for the discrete prime rows — an independent
  confirmation that the {0,2}/Rule-90 structure is the right microscope.
- The open question "does c_i → 0, or even stay bounded?" is the averaged decay-rate
  version of the run's regeneration obstruction; a regeneration mechanism would imply
  something about this rate.

## Source status

Zenodo record v1 (12 Jul 2026), single author (M. Ross, ORCID 0009-0001-3428-5337), with
reproducible code and rational-arithmetic certificates. Empirical; record claims as
checked-empirical only. OEIS A397880 (already in library) documents c_0..c_6 and the CHT
lower bound.