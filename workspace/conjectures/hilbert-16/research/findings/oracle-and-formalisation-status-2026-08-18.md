# Oracle status note — this cycle

The workspace already contains `code/brute.py`, `code/problem_examples_and_i6b_report.py`, and captures under `code/out/`, including `naive-oracle-notes.md`, `naive_oracle.captured.txt`, and `problem_examples_and_i6b_report.captured.txt`. These are the existing naive/oracle evidence for the displacement/ECT questions and have already been run in prior workspace history. This cycle did not rerun them because the user request was reference-library construction and the source/library phase is already sufficient according to `research/ROOT.md`.

The formal H16 statement is present at `code/lean/Lib/Statement.lean`. It defines `PlanarPolyField`, `IsLimitCycle`, `LimitCycleSet`, and the uniform finite-cardinality claim, with the intended `:= by sorry`; the file itself documents Mathlib's missing flow/isolated-orbit packaging and prints axioms. Existing Lean outputs under `code/out/lean/` record prior compilation checks. No new numerical theorem is claimed here.

Complexity: the existing naive oracle is explicitly small-instance only and is not the method for H16.2; no full-size brute force was run in this cycle. The structural route remains displacement-function finite cyclicity, not enumeration of fields or cycles.
