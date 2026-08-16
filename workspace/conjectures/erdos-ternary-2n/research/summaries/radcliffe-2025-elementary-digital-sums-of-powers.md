# Radcliffe, "Elementary bounds on digital sums of powers, factorials, and LCMs"

Source: arXiv:2511.15850 (2026), expository. Full text: `research/sources/radcliffe-2025-elementary-digital-sums-of-powers.full.md`.

## What it establishes

**Theorem 6 (Stewart's theorem, with Baker–Wüstholz):** if `log a / log b` is irrational, then the number of nonzero digits
```
c_b(a^n) > log n / log log n + C   for all sufficiently large n,
```
with `C` an effectively computable constant depending only on a, b. (Senge–Straus 1973 gave the weaker `c_b(a^n) → ∞ ⇔ log a/log b ∉ ℚ` with no rate; Stewart's theorem 2 made it `> log n/log log n + C − 1` for n > 4.)

**Application to Erdős.** Take a = 2, b = 3; `log 2/log 3 ∉ ℚ`. So the number of nonzero ternary digits of `2^n` (i.e. digits that are 1, since omitting 2 leaves only 1s and 0s) grows at least like `log n/log log n`. Combined with Dimitrov–Howe's ≥26 ones, this is a genuinely quantitative statement about counterexamples: a counterexample needs infinitely many digits, all of which are 0s and 1s, with the number of 1s growing like `log n/log log n` while `n` grows.

Also gives elementary bounds: `c_10(a^n) ≥ log_4 n` for a divisible by 2 not 10 (Theorem 1); general `c_b(a^n) > C log n` under an irrationality condition (remarks Section 4, elementary, improving the constant 1 but not the logarithmic growth).

**The blind spot (crucial).** The arguments in Section 4 apply equally to `a^n` and to any multiple of `a^n`; but every `3^n` has a multiple of the form `10^k + 8` with only two nonzero digits. So any approach that does not distinguish `a^n` from its multiples cannot prove `c_10(3^n) → ∞`. Lucid statement of why "count of nonzero digits" alone is insufficient — the same caveat transfers to base 3 / powers of 2: showing the count of nonzero digits grows does not force a digit 2 specifically, because the nonzero digits could all be 1s.

## What it does NOT settle

The constant is effectively computable but huge (from Baker–Wüstholz); not a route to excluding finitely many `n`. The theorem guarantees the *number* of nonzero digits grows; it does not force a 2 among them. So it supports but does not prove Erdős.

## Status

Sourced, arXiv preprint (recent, 2026). Stewart's theorem is classical (proved); the effective constant is not computed here.

```claim
id: STEWART-DIGITAL-SUM-POWERS
statement: If log a / log b is irrational, the number of nonzero base-b digits of
  a^n is > log n / log log n + C for all sufficiently large n (effective C from
  Baker–Wüstholz). For a=2, b=3 this means the number of 1s in (2^n)_3 grows at
  least like log n / log log n.
hypotheses: log a / log b irrational (holds for 2,3).
holds-here: yes — an effective quantitative lower bound on the nonzero-digit
  count of 2^n. But "nonzero digits" could all be 1s; it does not force a digit 2.
status: proved (Stewart 1980; expository proof in Radcliffe §6)
bearing: quantitatively supports the belief, and combined with
  DIMITROV-HOWE-26-ONES bounds counterexample sizes structurally; does not
  force digit 2 among the nonzero digits.
anchor: research/sources/radcliffe-2025-elementary-digital-sums-of-powers.full.md
```
