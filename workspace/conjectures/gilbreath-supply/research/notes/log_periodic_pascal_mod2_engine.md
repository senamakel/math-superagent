# Log-periodic fluctuations in Pascal-mod-2 counting functions — the local source for the operator's structural test

**Author:** librarian (post-directive-45). **Purpose:** give the write-up a citable
local source for the operator's structural hypothesis — that the oscillation in the
fitted threshold exponent `0.5568` (per-doubling slopes 0.5406..0.5712, oscillating
not drifting) is the *log-periodic* signature of a Pascal-mod-2 counting function,
i.e. `w*(n) = n^E · G(log₂(n))` with `G` bounded and period-1 in `log₂(n)`, rather
than a badly-fitted closed form.

## The canonical model, held locally

OEIS **A006046** — "Total number of odd entries in first n rows of Pascal's
triangle" — is the classical Pascal-mod-2 counting function that *genuinely*
carries the `n^E · G(log₂ n)` structure:

```
a(n) = Σ_{k<n} 2^wt(k)          (each k contributes 2^wt(k) odd entries on its row)
a(2k)   = 3·a(k)
a(2k+1) = 2·a(k) + a(k+1)
a(2^n)  = 3^n
a(n)    = n^(log₂ 3) · G(log₂ n),   G period-1      (Cloitre / Finch comment)
```

- `a(n) = n^(log₂3)·G(log₂n)` with `G` period-1 in `log₂ n` is *exactly* the
  bounded-oscillation-of-period-1-in-log₂(n) signature the operator asked to test.
- The exponent here is `log₂ 3 ≈ 1.585`; the threshold-weight exponent `E ≈ 0.557`
  is a *different* constant of the same *form*. The analogy is structural (same
  self-similar recursion shape ⇒ same log-periodic fluctuation form), NOT a claim
  that the constants match.
- The row engine `2^wt(k)` (odd entries on row k) is independently held via the
  Meštrović Lucas survey, Remark 35.
- Cross-references for the asymptotics: Stolarsky 1977 (cited on the OEIS page);
  Flajolet–Golin / Flajolet–Régnier–Sedgewick Mellin-asymptotics (cited on the page).
  **The Mellin stream is now held.** The Flajolet–Sedgewick report
  (`research/sources/flajolet_sedgewick_mellin_transform_asymptotics.full.md`)
  is the foundational method source; more decisively, the *exact* log-periodic
  representation for the p=2 case is now a **proved theorem, not an OEIS
  comment**: Hwang–Janson–Tsai 2024 (arXiv:2408.06817), Theorem 2.2,
  `F_2(n) = n^ρ·P(log₂n)` with `ρ = log₂(3/2) = log₂3 − 1 = 0.58496` and an
  explicit 1-periodic P. Stolarsky 1977 itself (SIAM J. Appl. Math 32 (1977)
  717–730, DOI 10.1137/0132060) is paywalled behind SIAM and not obtainable;
  its asymptotics are reproduced in the OEIS entry and the HJT theorem. See
  `research/summaries/hwang_janson_tsai_periodic_minimum_binomial_modp.md`.
- Sloane's comments also note the **Takagi / blancmange** appearance of A006046's
  graph — the canonical bounded-fractal-oscillation picture.

## What this buys the write-up

The operator's structural test ("tabulate `w*(n)/n^0.5568` against `log₂(n)`, look
for a bounded oscillation of period 1 rather than a trend") is not an ad hoc
suggestion: it is the *generic* behaviour of Pascal-mod-2 counting functions, of
which A006046 is the textbook example. If the run's tabulation shows a bounded
period-1-in-log₂(n) oscillation in `w*(n)/n^0.5568`, the phenomenon is classical
and nameable, with a local source to cite; if not, this note bounds what the data
can be claimed to show.

**Status:** sourced (OEIS catalogued entry, `a(2k)=3a(k)` etc.); the *exactness* of
the forms is authoritative from the OEIS record; the *transfer* to `w*(n)`'s
exponent `0.557` is a structural analogy to be tested by the run's own tabulation,
not a proved identity. The hypothesis-falsifier for the analogy: a tabulation of
`w*(n)/n^0.5568` vs `log₂(n)` that shows a monotone trend instead of a bounded
oscillation would refute the log-periodic reading and leave the 0.5568 a straight
fitted power with no periodic correction. That decision belongs to the run's own
computation (pattern_finder/coder), not to the library.

**Files:** `research/summaries/oeis_a006046.md` (the catalogued entry, filed by an
OEIS lookup), held alongside the Lucas survey `research/sources/mestrovic_lucas_theorem_survey_html.full.md`.

```claim
id: hjt-p2-log-periodic-representation-proved
statement: The log-periodic representation F_2(n) = n^ρ · P(log_2 n) for the
  number of odd entries in the first n rows of Pascal's triangle (OEIS A006046)
  is a proved theorem, not an OEIS-comment conjecture: Hwang–Janson–Tsai 2024
  (arXiv:2408.06817), Theorem 2.2, in the general form F_p(n) = n^ρ·P(log_p n)
  with ρ = ρ_p = log_p((p+1)/2), A=(p+1)/2, P(t)=A^{1−{t}}·φ(p^{{t}−1}), φ given
  by the explicit digit formula (2.11). For p=2 this gives
  ρ_2 = log_2(3/2) = log_2 3 − 1 = 0.58496, the 'natural candidate' exponent of
  directive 48, with P a continuous 1-periodic function.
hypotheses: p prime (p=2 for A006046); F_p(n) = #{binomial coefficients (m,k),
  0≤k≤m<n, not divisible by p}; the recurrence (2.1) holds; no number-theoretic
  input beyond the recurrence is used.
holds-here: yes — p=2 is exactly A006046, the Pascal-mod-2 counting function the
  run's log-periodic-oscillation-test-d47 uses as the prototype.
status: proved (primary source, Theorem 2.2)
bearing: Grounds in a theorem the log-periodic hypothesis for w*(n): if w*(n) is
  a Pascal-mod-2 counting function of the same self-similar recursion shape, it
  should carry w*(n) = n^E·G(log_2 n) with G period-1. Does NOT transfer the
  specific exponent log_2 3 − 1 to w*(n) — that is a structural analogy the run's
  own tabulation of w*(n)/n^0.5568 vs w*(n)/n^0.58496 against log_2(n) must
  decide; if neither residual is flat, keep E = 0.557 as fitted.
falsifier: a tabulation of w*(n)/n^E against log_2(n) showing a monotone trend
  rather than a bounded oscillation for both candidate exponents would refute the
  log-periodic reading of w*(n) (it would not refute HJT's Theorem 2.2, which is
  about A006046 itself).
anchor: research/notes/log_periodic_pascal_mod2_engine.md
```
