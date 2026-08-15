# Scholar digest — Pach, Raz, Solymosi 2026, "Erdős's Unit Distance Problem and Rigidity"

<!-- source: https://doi.org/10.4230/lipics.socg.2026.83 (arXiv lead) -->

**P. Pach, O. E. Raz, J. Solymosi** (2026), SoCG 2026 / arXiv. Filed by a
citation-graph lookup (abstract only; no reference or citing rows in OpenAlex).

## What the abstract actually establishes

Spencer–Szemerédi–Trotter 1984: the max number of unit distances among n plane
points is `u_2(n) = O(n^{4/3})`, far above Erdős's lower bound
`n^{1 + O(1/log log n)}` (conjectured optimal). This paper:

1. proves a **structural result**: a well-chosen strict subset of the points of
   a point set with nearly `n^{4/3}` unit distances must have a complementary
   point set with many "unit-distance-free" pairs — the precise dichotomy is
   in the abstract's "structural result" phrase, restated as a reduction.
2. **reduces the problem** of improving the `O(n^{4/3})` bound to a **conjecture
   on rigid frameworks**; the conjecture, if true, yields the first improvement
   over Spencer et al.
3. the conjectured rigidity statement has **a weaker version already established
   by Raz and Solymosi**.

## What it means for THIS problem

This is another entry in the "density cannot be bought" tier
(`unit-distance-upper-bound`, `szemeredi-trotter-*`): it is about the extremal
*count* of unit distances, i.e. the edge-density side, **not** about chromatic
number. Its bearing is:

- Reinforces that near-extremal unit-distance configurations are **rigid /
  algebraically structured** — the same algebraic-structure message as
  `maehara-algebraic-rigid-distances` and the `szemeredi-trotter-algebraic-extremal`
  family. This supports the run's exact-algebraic-field universe
  (`Q(sqrt3, sqrt11, sqrt33)`) but does not change it.
- It is a **reduction to a conjecture**, not a theorem about chromatic number.
  Even the conjecture, if true, only tightens `u_2(n)`, which the run's
  chromatic problem already treats as "density cannot be bought".
- **No constructive or chromatic leverage** for the forced-pair crux
  (`G-forced-pair-exists`) or the size-bound or the upper bound. It does not
  help build anything.

## Verification status

`asserted` — abstract only, not machine-checked, not relevant enough to
justify fetching the full text (and the evidence boundary screens the
published extremal/answer tier anyway). It agrees with, and does not
contradict, the existing `unit-distance-upper-bound` and the
`szemeredi-trotter-algebraic-extremal` claims.

```claim
id: pach-raz-solymosi-2026-rigidity-reduction
statement: Point sets in the plane with nearly n^{4/3} unit distances admit a structural decomposition whose extremal bound O(n^{4/3}) (Spencer-Szemeredi-Trotter 1984) can be improved only by a conjecture on rigid frameworks, a weaker form of which (Raz-Solymosi) is already proved.
hypotheses: finite plane point sets; u_2(n) unit-distance count; truth of a rigidity conjecture to obtain the improvement.
holds-here: partial — it is about extremal edge counts, not chromatic number; consistent with (and no bearing beyond) the existing density/rigidity tier.
status: asserted (abstract only)
bearing: reinforces the exact-algebraic/rigidity discipline of the run's universe; provides no construction and no chromatic statement.
anchor: research/summaries/citations_w4416841415.md
contradicts: nothing on disk; agrees with unit-distance-upper-bound and szemeredi-trotter-algebraic-extremal.
answers: none of the open REQUESTS rows.
```

## Does not help, read-once

Same class as Braun–Vega, Roth, de Bruijn–Erdős cited-by: an abstract-graph /
extremal-count source that corroborates the run's algebraic-rigidity framing
but gives the construction engine nothing to run. Do not re-read.
