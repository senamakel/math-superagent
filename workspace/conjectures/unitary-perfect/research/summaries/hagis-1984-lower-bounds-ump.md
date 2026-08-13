<!-- source: https://www.mathstat.dal.ca/FQ/Scanned/22-2/hagis.pdf | converted from PDF -->

# Hagis (1984), *Lower bounds for unitary multiperfect numbers*, Fib. Quart. 22(2) 140–144

Full text: [[hagis-1984-lower-bounds-ump.full]]

**Setup.** `n` is unitary *multiperfect* (UMP) when `σ*(n) = k·n`, `k ≥ 2`
(Harris–Subbarao definition). No UMP is known at all.

## Statements (proved in the paper)

- **Theorem 1.** No odd unitary multiperfect number exists.
- **Theorem 2** (`n = 2^a·Π p_i^{a_i}`, `t` distinct odd primes, `σ*(n) = k·n`):
  - `k ≥ 8` ⇒ `n > 10^663`, `t > 247`;
  - `k = 4 or 6` ⇒ `n > 10^110`, `t > 51`, `2^49 | n`;
  - `k` odd, `k ≥ 5` ⇒ `n > 10^461`, `t > 166`, `2^166 | n`.
- **Theorem 3** (unitary triperfect, `k = 3`): `t > 45`, `n > 10^102`,
  `2^16 | n`; if `3^2 ∥ n` then `t > 237`, `n > 10^779`, `2^237 | n`; if
  `3^3 ∥ n` then `t > 544`, `n > 10^2026`, `2^545 | n`.

Mechanism: `k = σ*(n)/n = (1+2^{-a})·Π(1+p_i^{-1})` is bounded above by
monotone products over the smallest primes; a computer run shows the upper
envelope falls below `k` for small `a, t`. (The same envelope idea, at `k = 2`,
is Subbarao–Warren's Lemma 1.)

## Bearing on this run

**Does not bound a sixth UPN.** The theorem's `t ≤ a + 2`-type bounds come
from `2 | (1+p^{a_i})` and the requirement `k ≥ 4`; the `k = 2` (unitary
perfect) case is untouched, exactly because (3.2)/(3.6) allow `t ≤ a + 1` with
no analogous closure. This source is background for the 2-adic budget / `ω`
structure (`research/notes/parity-and-2-adic-budget.md`), not a constraint on
`H_even` or on a sixth UPN. It also documents that `k ≥ 3` UMPs must be
astronomically large, which is why the whole literature's open cases sit at
`k = 2`.

```claim
id: hagis1984-ump-lower-bounds-exact
statement: For a unitary multiperfect n = 2^a * prod p_i^{a_i} with
  sigma*(n) = k n: k >= 8 => n > 10^663 and t > 247; k = 4 or 6 => n > 10^110,
  t > 51, 2^49 | n; k odd >= 5 => n > 10^461, t > 166, 2^166 | n; unitary
  triperfect (k = 3): t > 45, n > 10^102, 2^16 | n, with 3^2 || n => t > 237
  and 3^3 || n => t > 544.
hypotheses: sigma*(n) = k n with k >= 3 (multiperfect); n even
holds-here: yes for the multiperfect background, but k = 2 (a sixth UPN) is
  NOT covered -- no implication for the UPN finiteness question
status: asserted
bearing: background for the 2-adic budget/omega structure; bounds k >= 3
  UMPs out of reach, leaving k = 2 as the only live case
anchor: research/sources/hagis-1984-lower-bounds-ump.full.md
answers: whether-hagis1984-bounds-sixth-upn
```