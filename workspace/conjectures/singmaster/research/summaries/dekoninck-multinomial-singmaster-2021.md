# Repetitions of multinomial coefficients and a generalization of Singmaster's conjecture

Source: J.-M. De Koninck, N. Doyon, W. Verreault, arXiv:2107.09107 (2021).
Full text: `research/sources/dekoninck-multinomial-singmaster-2021.full.md`.

## What it establishes

Generalizes Singmaster's binomial-count to multinomial coefficients. For fixed
`k >= 2`, let `N_k(a)` be the number of `k`-term multinomial coefficients equal
to `a` (entries of the Pascal `k`-simplex; `k=2` is the classical binomial
triangle).

- **Average and normal order**: `N_k(a) = k(k-1)` for almost all `a`. (For the
  binomial case `k=2`, this gives normal order 2, matching the Abbott–Erdős–
  Hanson result that almost all `a` occur only as the value and its trivial
  partner.)
- **Upper bound**: `N_k(a) = O( (log a / log log a)^{k-1} )`.
- Propositions constructing large values of `N_k(a)`: infinitely many `a` with
  `N_k(a) >= 2·k! + k(k-1)` for `k >= 4`.

## Relevance to this run

The `k=2` case is exactly our problem. The paper's introduction restates the
known binomial history (Singmaster `O(log a)`, AEH `O(log a / log log a)`,
Kane record) and the known high-multiplicity values, listing up to `10^60`:
the infinite Fibonacci family members `120, 210, 1540, 3003, 7140, 11628,
24310, 61218182743304701891431482520`. It confirmes `N(3003)=8` is the highest
known. This is a *secondary* confirming source (an adjacent-problem paper that
reproduces the binomial record), useful as cross-check but not the primary
source for any binomial claim.

Two further cross-checks this run can use:
- The **`k`-term normal-order result** generalizes the binomial average-order
  fact and so corroborates that the small-column/high-`k` boundary (not the
  typical values) is where any bound is hard.
- The bound `N_k(a)=O((log a/log log a)^{k-1})` for binomial-adjacent
  multinomial coefficients is a genuinely different shape from the binomial
  record and could be a comparison point for a uniform-in-`k` claim.

Evidence class: sourced (full text read). Not load-bearing for any new binomial
claim beyond corroborating the record.

```claim
id: dekoninck-multinomial-average-and-bound
statement: De Koninck-Doyon-Verreault 2021 (arXiv:2107.09107): for fixed k>=2,
  N_k(a) (number of k-term multinomial coefficients equal to a) has average and
  normal order k(k-1); N_k(a) = O((log a / log log a)^{k-1}); and for k>=4
  there are infinitely many a with N_k(a) >= 2*k! + k(k-1). The k=2 case is the
  binomial problem: normal order 2 (matching Abbott-Erdos-Hanson) and the
  binomial record (N(3003)=8 highest, Fibonacci family N>=6 infinitely often)
  is restated as context up to 10^60.
hypotheses: k fixed >= 2; a integer; multinomial coefficients in the k-simplex.
holds-here: yes for k=2 (exactly Singmaster); the paper is a secondary
  cross-check of the binomial record, not a primary source for any binomial
  theorem.
status: asserted (full text read; statements quoted, not re-derived)
bearing: independent corroboration that N(3003)=8 is the highest known and the
  family N(a)>=6 is infinite; the k-term normal-order result corroborates that
  the small-column/high-k boundary (not typical values) is where a uniform
  bound is hard. Does not provide a binomial bound or method.
anchor: research/sources/dekoninck-multinomial-singmaster-2021.full.md
```

## Relationship to recalled memory

The prior durable memory held this paper as "multinomial generalization"
carrying the same record corroboration and the same hypothesis check (k=2
restriction is exactly Singmaster). This digest agrees and adds the exact
quantitative statements (average/normal order k(k-1), bound
O((log a/log log a)^{k-1}), construction N_k(a) >= 2k!+k(k-1) for k>=4). No
contradiction.
