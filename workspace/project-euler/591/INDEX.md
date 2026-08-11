# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you
create it, and refresh this index after adding, renaming, or deleting files.
Subfolders have their own indexes: `research/INDEX.md`, `toolkits/INDEX.md`,
`prompts/INDEX.md`.

## Problem

| File | Purpose |
| --- | --- |
| `problem.url` | The Project Euler 591 URL (https://projecteuler.net/minimal=591). |
| `problem.html` | The PE591 statement (quadratic integers BQA_d(pi,n), worked examples, find Σ|I_d(BQA_d(pi,10^13))|, d non-square < 100). |
| `README.md` | Generic workspace header: keep the run reproducible, start with AGENTS.md. |
| `config.toml` | Run configuration: workspace kind, solver flags (exact arithmetic, verify with code, forbid exponential time/space), artifact file paths. |
| `goal.md` | The objective: the Ostrowski/CF-based O(log B) reduction of PE591, and its completion criteria. |
| `tasks.md` | Task checklist for the run (understand → brute → theory → derive → implement → run full size → report). |
| `scratchpad.md` | Provisional reduction notes: DE591 → per-b best a, circular-distance subproblem for both signs of b. |
| `memory.md` | Working memory: problem restatement, established results (reduction, O(log B) candidate algorithm), failed approaches, open questions. |

## Programs (oracle + verification)

| File | Purpose |
| --- | --- |
| `brute.py` | Naive brute-force oracle for the PE591 quadratic-integer problem and for the per-b reduction; reproduces the statement's worked examples and records small reachable cases. The oracle the fast solver must match. |
| `verify_ostrowski.py` | Harness that checks the Cabanillas-López & Labbé best left/right α-approximation candidate algorithm (Props 9/10, Alg 3(ii)) against a brute-force oracle on many random small beta/B cases across many d. Not run in this environment (no exec tool); kept for the solver agent to execute. |
| `verify_big.py` | High-precision (mpmath, 60-digit) check of the d=2, n=10^13 candidate and the statement's upper-bound candidate: recomputes |a+b·sqrt(2)−π| where double precision cannot resolve 1e-13 closeness. |

## Subfolders

| Folder | Purpose |
| --- | --- |
| `research/` | Externally sourced mathematics — see `research/INDEX.md`. Two sources (Berthé–Imbert; Cabanillas-López–Labbé) each stored as a summary + `.full.md`, plus the final research report `report_pe591_inhomogeneous_approx.md`. |
| `toolkits/` | Reusable one-function-per-file helpers — see `toolkits/INDEX.md`. Currently empty. |
| `prompts/` | Role-specific agent guidance — see `prompts/INDEX.md`. |
