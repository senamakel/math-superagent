# Pattern-finder report — round 22: the two artifacts newer than round 21, closed

## What I did

Round 21 (mtime 00:36, `pattern_finder_report21.md`) declared the sequence line
closed. Two `code/out` artifacts landed **after** that report and had not been
run through the exact tools:

- `c3_spectrum_closed_form.captured.txt` (00:37)
- `c3_spectrum_exact_verify.captured.txt` (00:39, 0 bytes)

I read the closed-form capture and its generating script
(`c3_spectrum_closed_form3.py`). It holds the **C3 triangle-graph spectrum
family** — the exact same family round 19 sequenced. Round 19 ran the `rt`,
`st`, and `-3`-multiplicity (`nT-v`) columns through the tools. The one column
never tooled is the **eigenvalue multiplicity pair** `m_r, m_s` that the
closed-form script computes. I tooled them this round with exact integer
arithmetic.

## The multiplicity columns, changed this round

From the graph's own spectral multiplicities (the C3 spectrum at eigenvalue
`r = k/2 + u - 3` and `s = k/2 - (u+1) - 3`):

| u | m_r | m_s |
| --- | --- | --- |
| 1 | 4 | 4 |
| 3 | 54 | 44 |
| 4 | 132 | 110 |
| 10 | 3280 | 2992 |
| 31 | 250914 | 243104 |

Exact closed forms (sympy, derived from the standard SRG multiplicity formula
`m = ((v-1) ± top/a)/2` with `top = 2k-(v-1)`, `a = 2u+1`):

    m_r = u(u²+u+2)(u²+2u+3) / (2(2u+1))
    m_s = (u+1)(u²+2)(u²+u+2) / (2(2u+1))

## Why this adds nothing that separates 99 from its controls

These are the **parameter-determined eigenvalue-multiplicity polynomials** in `u`
— exactly the same `a = 2u+1 | 63`-governed closed-form class that every count
in the catalogue (rounds 1-17) belongs to. Integrality is guaranteed by the
divisor-63 integrality characterisation already proven on disk. At the two
existing `(1,2)`-family members they are u=3 (99): 54/44 and u=4 (243): 132/110
— both integral, and there is no index at which the value could fall below a
constraint one way for 99 and not for 243.

## Verdict

- The multiplicity columns are the same family-count class, confirmed once more.
- No artifact newer than round 21 carries a new sequence-bearing result: the
  two post-round-21 files are the C3 spectrum family, now exhaustively tooled
  (rt, st, nT-v in round 19; m_r, m_s this round).
- The only 99-specific structural values remain the **coclique bound 22** and the
  **forced n₃ ≥ 3** (Makhnev conditional) — neither a sequence the tools extend.

The sequence line is fully closed (rounds 1-22). Genuinely new exploitable
structure, if any, is in construction/search: the 99-vertex lift of the
super-simple 2-(22,4,2) design, and the k=14 local triangle geometry.

**NOTHING FURTHER** is available from the sequence tools.

## Files
- `code/out/c3_spectrum_closed_form.captured.txt`, `c3_spectrum_closed_form3.py` — the source artifacts.
- `code/out/pattern_finder_report19.md` — prior sequencing of this family.
- `code/out/pattern_finder_report22.md` — this report.
