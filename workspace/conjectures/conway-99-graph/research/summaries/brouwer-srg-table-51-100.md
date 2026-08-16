# Brouwer's parameters of strongly regular graphs — table 51 ≤ v ≤ 100 (canonical reference)

<!-- source: https://aeb.win.tue.nl/graphs/srg/srgtab51-100.html -->
<!-- full text: research/sources/brouwer-srg-table-51-100.full.md -->

The standard authoritative feasibility table. Marking conventions: `+` = exists,
`!` = exists (unique or distinguished), `-` = does not exist, `?` = open.

## The (99,14,1,2) row — the object of this run

```
? | 99 | 14 | 1 | 2 | 3 54 | -4 44 |
```
- status **`?` — open** (no construction, no nonexistence).
- spectrum **3⁵⁴, −4⁴⁴**, matching the run's exact integrality computation
  (claim `integrality-five-members`, checked) and Brouwer–Neumaier 1988.

## What the table does and does not establish

- Confirms (99,14,1,2) is feasible by every standard test that the table
  applies (integrality, Krein, absolute bounds): it is listed `?` not `-`.
- Two existing members of the same λ=1,μ=2 family adjacent elsewhere: the
  rook's graph (9,4,1,2) in table 1–50 and BvLS (243,22,1,2) in table 101–150.
  Neither appears here (v≤100), but both are the negative controls for any
  argument against 99.
- Neighbour rows give the closest *settled* μ=2 / λ=1 context:
  - `- | 57 | 14 | 1 | 4 | 2 38 | -5 18 |` (Wilbrink–Brouwer) — k=14, λ=1, μ=4, **does not exist** (see wilbrink-brouwer-57141 summary).
  - `- | 85 | 14 | 3 | 2 | 4 34 | -3 50 |` (Shpectorov–Zhao) — k=14, μ=2, λ=3, **does not exist** (see shpectorov-zhao summary).
  Both are k=14 like 99 and are the closest nonexistence precedents.

## The complement row (noted for completeness, not used)

`+ | 99 | 48 | 22 | 24 | 4 54 | -6 44 | pg(8,5,4) does not exist` — this is
(half of) the complemented pair of the 99 line: the second row of the 99 block
is the complement `84 71 72 | 3 44 | -4 54`. The existence of a (99,14,1,2)
would give a (99,84,71,72) complement. Neither is decided.

## Implication for this run
This is the citation to reach for whenever open-status or the spectrum of
(99,14,1,2) is asserted. It is a **reference table** (`status: catalogued`),
not a proof: the `?` means the problem is open in the field's standard ledger.

```claim
id: brouwer-table-99-open
statement: Brouwer's canonical table marks (99,14,1,2) with status '?'
  (open), spectrum 3^54,-4^44, complement (99,84,71,72). It is feasible by
  the standard tests the table applies (it is '?' not '-'). The two settled
  k=14 neighbours are (57,14,1,4) and (85,14,3,2), both marked '-' (do not
  exist).
hypotheses: none — a reference-table statement.
holds-here: yes — the exact object.
status: catalogued (Brouwer's web parameter table; the spectrum matches the
  run's own exact integrality computation, checked).
bearing: the canonical citation for (99,14,1,2) being open and feasible; and
  confirms the two k=14 nonexistence precedents that frame the run's structural
  attack.
anchor: research/sources/brouwer-srg-table-51-100.full.md
contradicts: none; confirms existence-status-open, integrality-five-members
```

[[brouwer-srg-table-51-100.full]]
