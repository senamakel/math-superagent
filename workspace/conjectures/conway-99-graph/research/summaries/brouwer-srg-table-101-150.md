# Brouwer's parameters of strongly regular graphs — table 101 ≤ v ≤ 150 (canonical reference)

<!-- source: https://aeb.win.tue.nl/graphs/srg/srgtab101-150.html -->
<!-- full text: research/sources/brouwer-srg-table-101-150.full.md -->

## Relevance to this run

The Berlekamp–van Lint–Seidel graph srg(243,22,1,2) — the second positive
control — is **not** in this table (v≤150); it lives in the 201–300 table. This
table's role for the run is narrower: it records the nearby **λ=1, μ=3** member

```
? | 115 | 18 | 1 | 3 | 3 69 | -5 45 |
```
status `?` = **open**. This is the (115,18,1,3) set that Makhnev 1988 Theorem 2
also rules out under condition (*), and it shows the λ=1 family extends past 99
with higher-k open members. (By way of orientation: (115,18,1,3) and
(99,14,1,2) are the two sets Theorem 2 treats together.)

## What the table does not contain
- Not the 99 row (that is in the 51–100 table).
- Not the 243 BvLS control (201–300 table).

## Implication
This table's main contribution to the run is confirming (115,18,1,3) is open
and λ=1 — reinforcing that Makhnev's Theorem 2's two excluded-under-(*) sets
(99 and 115) are both currently `?` in the standard table. No new 99 weapon;
a reference consistency check.

```claim
id: brouwer-table-115-open
statement: Brouwer's table marks (115,18,1,3) with status '?' (open), spectrum
  3^69,-5^45, complement (115,96,80,80). It is the lambda=1, mu=3 member that
  Makhnev 1988 Thm 2 rules out under condition (*) together with
  (99,14,1,2).
hypotheses: none — canonical reference table.
holds-here: yes (context for the family and Makhnev Thm 2).
status: catalogued (Brouwer's web table; the Makhnev-Thm-2 relation is from
  the Russian full-text summary).
bearing: confirms the lambda=1 family extends beyond 99 with open members, and
  that Makhnev THM 2's two excluded-under-(*) sets are both '?' in the table.
anchor: research/sources/brouwer-srg-table-101-150.full.md
contradicts: none.
```

[[brouwer-srg-table-101-150.full]]
