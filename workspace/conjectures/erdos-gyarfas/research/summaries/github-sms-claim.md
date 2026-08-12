# GitHub SMS verification claim — ArjunBalaji79/erdos-gyarfas-min-degree-3

**Verdict: the repository EXISTS and matches the CONTEXT.md description in its essentials,
but the claim is `asserted-by-source`, NOT reproduced or audited by this run.** Its own
docs concede there is no end-to-end machine-checkable proof certificate and no independent
third-party reproduction. There is also an internal off-by-one inconsistency between the
repo's GitHub "About" description and its README/results.

```claim
id: EG-github-sms-n32
statement: A repository ArjunBalaji79/erdos-gyarfas-min-degree-3 uses SAT-Modulo-Symmetries
  (Kirchweger–Szeider's SMS, CaDiCaL + SMS canonicity propagator + the Glasgow Subgraph Solver
  as a complete forbidden-subgraph propagator) to claim that no minimum-degree-≥3 graph on
  17 ≤ n ≤ 31 vertices avoids all of C4, C8, C16 as (non-induced) subgraphs (UNSAT by SMS at
  every n = 17..31, contiguous), which together with the n ≤ 16 baseline would put any
  general min-degree-3 counterexample at ≥ 32 vertices. An independent pure-Python CEGAR-SAT
  solver (PySAT/glucose42 re-check + its own DFS power-of-two cycle detector + lex symmetry
  break) independently reaches n = 19 and agrees with SMS there. Cross-corroboration claimed:
  nauty (geng+labelg) ground-truth = 5 at n=10 (C4-only), n≤16 baseline = 0, totalizer
  cardinality encoding at n∈{17,20,22,25} = 0, colex ordering at n∈{17,20} = 0 (n=22,25
  timed out at 55 min — inconclusive), and positive controls (forbid only C4) yield a graph
  (SAT) at n∈{17,20,25,30}.
hypotheses: finite simple graph, δ ≥ 3, no cycle of length in {4,8,16} (the powers of two
  ≤ 31; C32 first fits at n = 32); general (non-regular) case, which contains the cubic case.
holds-here: yes — this is precisely the run's verification-bound gap (general case past n=15,
  cubic past n=29).
status: asserted-by-source (not reproduced, not refereed, no third-party reproduction, no
  end-to-end machine-checkable certificate).
bearing: If correct, this is by two orders of magnitude the strongest published-or-otherwise
  computational frontier for BOTH the general min-degree-3 case (16→31, bound 17→32) and the
  cubic case (29→31, bound 30→32), and it is the FIRST SAT/SMS attack on the conjecture. It
  would push the run's verification oracle beyond the raw n≤15-general / n≤29-cubic bounds.
anchor: research/sources/arjunbalaji-sms-github.full.md; research/sources/arjunbalaji-sms-raw-readme.full.md;
  research/sources/arjunbalaji-sms-results.full.md; research/sources/arjunbalaji-sms-verification.md
  (stored whole, no .full companion); research/sources/arjunbalaji-sms-cegar-results.md;
  research/sources/arjunbalaji-modal-sms.py.full.md; research/sources/arjunbalaji-cegar-sat.full.md
falsifier: (i) a min-degree-3 graph on n ≤ 31 avoiding C4/C8/C16 — the repo's own positive-control
  pipeline (returncode 10) is designed to surface exactly this as a witness and would junk the
  claim; (ii) an independent third-party reproduction finding SAT at any n = 17..31; (iii) the
  repo's own admitted gap — the smsg --lrat-output LRAT proof is NOT RUP/RAT-derivable from the
  min-degree-3 CNF alone (the Glasgow propagator adds forbidden-cycle clauses during search), so
  a generic lrat-check cannot validate it, and the certified-SMS clause-logging machinery
  (Kirchweger et al.) that would make it machine-checkable is listed as future work — until that
  lands, the UNSAT verdicts rest on trusting SMS + Glasgow + the min-degree CNF.
```

## What was searched and found

Searched: GitHub search (`ArjunBalaji79/erdos-gyarfas-min-degree-3`), Exa `github` category for
SMS/SAT verification of the Erdős–Gyárfás conjecture, and a general web search for a 17–31
vertex computational check. The repository IS present: `https://github.com/ArjunBalaji79/erdos-gyarfas-min-degree-3`
(3 stars, 0 forks, 34 commits, MIT, sole author Arjun Balaji, Bangalore IN, last activity
2026-06-17). I read the raw README, the GitHub HTML page, `sms_results.md`, `verification.md`,
`results.md` (CEGAR), the Modal SMS driver `modal_sms.py`, the CEGAR loop, the file tree, and
`pyproject.toml`. All stored under `research/sources/` (see anchor).

## Key findings

- **Method (main, SMS):** one `smsg` call per n asks "is there a min-deg-3 graph on n vertices
  with no C4/C8/C16?"; SMS's isomorph-free exhaustive generation + Glasgow (complete)
  forbidden-subgraph propagator + a min-degree cardinality CNF (`GraphEncodingBuilder.minDegree(3)`).
  Soundness anchored (per the repo) at n=10 (C4-only → 5, matches nauty) and n≤16 (→ 0,
  published baseline). Pinned commits recorded but **not** checked out in the build script
  (commented as a reproducibility note): SMS `464f12f…` (v2.0.0-3-g464f12f), Glasgow
  `abd331a…`, CaDiCaL `rel-2.1.2-38-gb023aaf`.
- **Results table (from `sms_results.md`), all UNSAT = count 0:** n 17→2.9s, 18→7.8s, 19→24.1s,
  20→27.8s, 21→19.3s, 22→101.1s, 23→202.9s, 24→148.3s, 25→339.8s, 26→414.8s, 27→1000.3s,
  28→1892.0s, 29→2342.8s, 30→6888.9s, 31→7351.4s (1 core/size, Modal). Contiguous UNSAT through
  31 → claimed bound ≥ 32.
- **Independent cross-check (CEGAR-SAT):** own PySAT/cadical + DFS power-of-two cycle detector +
  lex symmetry break; verified contiguous UNSAT through n=19 (bound ≥ 20), each refinement
  cycle re-checked, each final UNSAT re-proven by a second solver (glucose42). n=20 hit the
  55-min wall (~719k refinements). This is the "cross-checked with CEGA-SAT to n≤19" of
  CONTEXT.md — CONFIRMED.
- **Reproduction status:** the repo's local "validation gates" (Gates 0,1,3,4,5) run fast with
  `pip install -e '.[dev]'` + nauty and `pytest -q`, and the local CEGAR `run_frontier
  --start 17 --end 19` runs without Modal, so the CEGAR cross-check (n≤19) and the soundness
  gates are independently runnable from the repo. The **SMS frontier itself (n=17..31) requires
  a Modal cloud account** and the SMS/Glasgow/CaDiCaL builds — reproducible only with that infra,
  and not reproducible here. I did NOT re-run any of it; the numbers below are quoted from the repo.
- **Honest-scope statements in the repo:** "Fresh computational result, **not yet independently
  reproduced or refereed**"; "bound ≥ 31 is well corroborated, with a formal proof certificate
  (§7) as the remaining step toward a fully machine-checked claim". This supports status
  `asserted-by-source`.
- **Important internal inconsistency (off-by-one):** the GitHub repository "About" description
  and the `verification.md` headline say "every min-degree-3 graph on **≤30** vertices has a
  power-of-two cycle (counterexample **≥31**)", whereas the README body and `sms_results.md`
  say "at most **31** vertices" / bound **≥32**, with the n=31 row listed as UNSAT. The
  stronger number (≤31/≥32) is the one the README, the results table, and the fetch logic
  actually support. Flagged so a later reader does not silently adopt either figure.
- **DOI:** README cites Zenodo DOI 10.5281/zenodo.21190438 ("Verifying the Erdős–Gyárfás
  Conjecture up to 31 Vertices with SAT Modulo Symmetries", 2026) and says the work is "under
  review in the Learning on Graphs Conference 2026". The DOI's resolution was NOT verified in
  this run; treat the citation as self-reported.
- **Closest other real artifacts (not this claim):** `rbsandeep/Erdos-Gyarfas` (the Hegde–
  Sandeep–Shashank P_k-free backtracking code for arXiv:2410.22842, a genuinely different
  method — P_k-free restricted class, not SAT/SMS), `markirch/sat-modulo-symmetries` (SMS
  itself), `leansolving/leansms` (a Lean front-end for SMS). A MathOverflow post
  (mathoverflow.net/q/512914, ~2026-07) reports an independent exhaustive census of all
  connected min-deg-3 graphs showing the C4-or-C8 dichotomy holds through n=19 (n=19:
  22,816,929,306 graphs → 0) — an independent n≤19 agreement with this repo's UNSAT range.
