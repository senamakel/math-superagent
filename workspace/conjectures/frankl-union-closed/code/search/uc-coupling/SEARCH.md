# Search — uc-coupling

Derived from `scores.jsonl`; do not edit, the next candidate re-derives it. Every row is a program in `candidates/` that was executed against `score.py` — a candidate that was not executed is not here, because nothing can record one.

15 candidates scored, 14 discarded.

| Candidate | Island | Score |
| --- | --- | --- |
| `candidates/c0000.py` | 0 | `0.3823435642` |
| `candidates/c0001.py` | 1 | `0.3823435642` |
| `candidates/c0002.py` | 2 | `0.3823435642` |
| `candidates/c0005.py` | 1 | `0.3823435642` |
| `candidates/c0006.py` | 2 | `0.3823435642` |
| `candidates/c0007.py` | 3 | `0.3823435642` |
| `candidates/c0009.py` | 1 | `0.3823435642` |
| `candidates/c0016.py` | 0 | `0.3823435642` |
| `candidates/c0017.py` | 1 | `0.3823435642` |
| `candidates/c0018.py` | 2 | `0.3823435642` |
| `candidates/c0019.py` | 3 | `0.3823435642` |
| `candidates/c0020.py` | 0 | `0.3823435642` |
| `candidates/c0021.py` | 1 | `0.3823435642` |
| `candidates/c0022.py` | 2 | `0.3823435642` |
| `candidates/c0023.py` | 3 | `0.3823435642` |

## Why candidates were discarded

- All rows above the proved ceiling `t_hat_max=0.3823455334` that would have carried a numeric score are INVALID (missing-inf artifacts), and the degenerate-atom candidate is INVALID — per the scorer's STEP 2 guards and STEP 4 re-score; none certifies anything. The believable result is the Yu-witness plateau at 0.3823435642.
- 2× INVALID: legacy in-module main(), no module-path params, rejected
- 2× INVALID: certified score 0.3823610000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: diagnostic probe, no readable params
- 1× INVALID: malformed (IndentationError), not a candidate
- 1× INVALID: certified score 0.3824280000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: certified score 0.3825300000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: certified score 0.3826835000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: certified score 0.3828830000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: certified score 0.3838000000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: certified score 0.3859550000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: certified score 0.3937600000 above proved ceiling t_hat_max (missing-inf artifact)
- 1× INVALID: degenerate-atom a=0.01 < A_FLOOR=0.1 (small-a hole)
