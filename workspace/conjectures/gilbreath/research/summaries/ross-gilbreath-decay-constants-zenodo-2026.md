# Empirical Structure of the Gilbreath Decay Constants — Ross, Zenodo, July 2026

**Full text:** `research/sources/ross-gilbreath-decay-constants-zenodo-2026.full.md`
**Source URL:** https://zenodo.org/records/21326026/files/Empirical_Structure_of_the_Gilbreath_Decay_Constants.pdf
(record page https://zenodo.org/records/21326026; DOI 10.5281/zenodo.21326026)
**Author:** Michael M. Ross, independent; code + rational certificates at
https://github.com/michaelmross/Gilbreath, archived DOI 10.5281/zenodo.21536390.

## What it establishes

Empirical study of the CHT stationary continuous Gilbreath model (top row i.i.d.
standard exponentials, `c_i = E a(i,j)` at depth i). Nothing here is a theorem
about the primes; every asymptotic-looking statement except the exact values
below is explicitly empirical — the author states the figures "identify
theorem-shaped targets, not substitute for proofs".

1. **Exact rational values for `c_4, c_5, c_6`** (CHT had `c_0..c_3`):
   `c_4 = 778959731701/1447295850000 = 0.5382173463...` (hand-checked by this
   run to ~7 digits), `c_5 = 14008668886481596262550223816901 /
   25320304994525128311856832700000 = 0.5532582996...`, `c_6 = 0.448388672133...`
   (150-digit denominator, deposited with data). Method: exact rational
   sign-cone decomposition of the simplex (homogeneity `c_i = (i+1)E b(i,1)`),
   certified by partition-of-unity identities (cone volumes sum to exactly 1),
   by reproducing CHT's `c_2=7/9, c_3=227/288`, and by Monte Carlo agreement at
   2e8–5e8 samples. Largest primes in denominators: 17, 47, 331. Weave
   `c_2<c_3>c_4<c_5>c_6` tracks binary digit sum `s_2(i)`. First infeasible
   cones appear at depth 5.

2. **Digit-sum law (Monte Carlo, depth 8192, 768 pyramids):** `c_i ≈ C·λ^{s_2(i)}/i`,
   effective `λ ≈ 1.14–1.20` (drifting). Conditioned on digit-sum class, data
   are consistent with pure `1/i` decay; pooled data show a dyadic sawtooth with
   pooled exponent about −0.90…−0.86 `(α(λ) = log₂((1+λ)/2) ≈ 0.098–0.138)`.
   The terminal crescendo near `2^13 = 8192` follows `s_2`, but saturates below
   geometric extrapolation (concave `log g(k)`), with severe sample-size loss in
   the last octave.

3. **Finite-depth growth thresholds:** for `a_j ∼ Unif[0, R(j)]`, `p_n(R) =
   P(a(n−1,1) > 1)` trends down for every tested polynomial `R` (even `j⁴`) and
   up for exponential rates. Open question (author): is the threshold exactly at
   polynomial-vs-exponential in this family?

4. **Transient laws:** full-row grind-down time `τ(G) ≍ G^β`, `β ≈ 0.63–0.66`
   (not logarithmic — geometric start, linear "chipping" end); a spike of
   amplitude G at distance d from the wall loses ≈1 unit of wall amplitude per
   column of separation, with survival distance `d*(G)/G → 1`
   (observed 0.79, 0.85, 0.93, 0.96, 0.98, 0.99). Slope-one law = cleanest
   candidate for a direct theorem. Constant `{0,d}`-valued and constant-mod-4
   backgrounds can conserve disturbances (consistent with the `{0,d}` closure
   and the CHT inverse theorem's long zero-blocks / long shallow `{0,d}`-blocks
   obstructions).

## Two theorem-shaped targets the author names

- prove a digit-sensitive comparison `c_i ≤ A·B^{s_2(i)}/i` for absolute
  constants A, B (no asymptotic constant needed), or the dyadic averaged form;
- prove the propagation law `d*(G) ≈ G + O(1)` in a sufficiently mixing bounded
  background — a quantitative "light-cone" statement.

The author's close: none of these averages remove the deterministic obstruction
relevant to primes. The parity wave guarantees only oddness at the left edge;
"equal to one" requires suppressing rigid 0 and 2 structures. "That remains a
separate arithmetic problem."

## Bearing on this run

- Independent confirmation that the Pascal/mod-2 (digit-sum, `s_2`) structure is
  the right microscope — same Rule-90/Sierpinski structure as the run's
  mod-4 linearization.
- The averaged decay rate of the array is itself open (`c_i` bounded vs not);
  a claimed regeneration mechanism for the primes has this quantified
  still-open shadow to be consistent with.
- Consistent with (and cites) Ross's own parity note, CHT 2026, and Chase 2024 —
  all already in the library.

## Status

Empirical (author's label); exact `c_4..c_6` asserted-by-source with deposited
certificates. Not a theorem about primes. Full text on disk; claim ledger
updated (see `research/notes/library-state.md`, id `ross-2026-decay-constants`).