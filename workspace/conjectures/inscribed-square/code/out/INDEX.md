# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `lean-formalisation.md` | Claim blocks for the Lean formalisation: `lean-toeplitz-statement` (conjecture stated as a type, asserted — proof open, sorry), `lean-stromquist-locally-monotone` (Stromquist's theorem as Cited axiom, asserted-by-source until a theorem is proved from it), `cited-stromquist-1989` (the source row). Records the lean_check verdicts. |
| `lean-statements-list.json` | JSON list of mathematical statements from the gathered square-peg sources that could be stated in Lean 4 against Mathlib, with name/statement/source/cited fields; cited=true marks statements the material merely quotes or asserts, cited=false marks statements the material proves. |
| `oracle_check.txt` | _(undescribed)_ |
| `sequence_provisional.md` | Pattern-finder pass record: only extractable artifact sequence is the 3-term sanity list [1,0,1] (too short for an exact claim); the boundary oracle on rationalized regular polygons returns all zeros while an independent rounded-vertex test returns [1,2,3,4,5,6,8] — disagreeing at n=4, so neither is a regularity. Also records that check_oracle.py's ellipse loop hangs because the boundary oracle finds no squares on those rationalized polygons (never wrote oracle_check.txt). Verdict: NOTHING FURTHER until new exact counts are computed. |
| `sequence_review_2026-08-18.md` | Executed sequence-extraction and exact sequence-tool review of existing computation artifacts; records why no structural conjecture is warranted. |
| `verify_symmetric.txt` | Saved stdout from verify_symmetric.py, containing exact PASS/FAIL results and Fraction-coordinate squares. |
