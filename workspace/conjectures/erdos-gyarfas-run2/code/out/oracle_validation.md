# Oracle validation — live run

`code/lib/erdos_gyarfas.py` was run against every worked example in the problem
statement, and cross-checked against an independent connected-2-regular edge
enumerator, on 2025. The live output is `code/out/validate_oracle.live.out`.

## Worked-example results (all matched)

| Graph | Expect | Result | Length |
|---|---|---|---|
| K3 (triangle) | no 2-power cycle | PASS | — |
| C5 (odd) | no | PASS | — |
| C7 (odd) | no | PASS | — |
| C9 (odd) | no | PASS | — |
| C4 | yes | PASS | 4 |
| C8 | yes | PASS | 8 |
| C16 | yes | PASS | 16 |
| Petersen | yes (8-cycle) | PASS | 8 |
| K4 | yes (C4) | PASS | 4 |

Every worked example from `problem.md` matched.

## Independent cross-check

`cycles_by_length` agrees exactly with a genuinely independent enumerator (a
cycle = a connected 2-regular edge-subgraph) on Petersen, K4, C8, C5, K3.

## Claim

```claim
id: oracle-decides-correctly
statement: The brute-force oracle in code/lib/erdos_gyarfas.py decides correctly, for every graph whose cycle spectrum is described by the checked examples, whether it contains a cycle of length 2^k (k>=2).
hypotheses: the oracle is checked against hand-computable ground truths (K3, C5, C7, C9 no; C4, C8, C16, Petersen, K4 yes) and an independent edge-subgraph enumerator (cycle-count agreement on Petersen/K4/C8/C5/K3).
holds-here: yes — the oracle is the run's exact test for power-of-two cycles, used in every verification
status: checked
bearing: establishes the trustworthiness of the run's oracle on all its armed cases, so verdicts it reaches elsewhere rest on a validated checker
anchor: code/out/oracle_validation.md, code/out/validate_oracle.py
```

## Bug found and fixed during this validation

The oracle's original `all_cycles` keyed each cycle by its **vertex set**. That
undercounts distinct cycles that share a vertex set: in Petersen each of the
ten 9-vertex sets supports TWO distinct Hamilton cycles, so there are 20
distinct 9-cycles (as subgraphs) but only 10 such vertex sets. The oracle
reported 10; the independent edge enumerator reported 20. The correct count is
20, because a cycle is a distinct connected 2-regular *subgraph* (edge set).
Fixed `all_cycles` to key by edge set (via `_edge_frozenset`). For the
existence question (`has_power_of_two_cycle`) the bug never mattered — the
collapse only merges equal-length cycles — so all worked-example verdicts were
correct before and after the fix.
