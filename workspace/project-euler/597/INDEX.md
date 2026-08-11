# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method and evidence rules for the whole run: restate the problem, test small cases, prefer theory over enumeration, keep sourced facts separate from deductions, keep files described. |
| `CONTEXT.md` | _(undescribed)_ |
| `GOAL.md` | _(undescribed)_ |
| `MEMORY.md` | _(undescribed)_ |
| `README.md` | Folder-layout note pointing newcomers to AGENTS.md, `prompts/`, and the goal/tasks/scratchpad/memory working files. |
| `SCRATCHPAD.md` | Provisional work: the diagnosis of the parity-comparator bug, its fix, and the corrected MC run output. |
| `TASKS.md` | _(undescribed)_ |
| `race_spec.md` | Exact chronological race-dynamics specification for implementation: event simulation, bump/OUT/FINISH treatment, and the bump-chain parity definition. Reference contract for any race solver. |
| `test_treap.py` | Deterministic test of the Cartesian-tree (min-heap treap) hypothesis for PE 597: compares tree-parity (count of ancestor/descendant index pairs in the min-w treap) against the true oracle outcome_parity on many random Exp(1) speed vectors, and Monte-Carlos the tree model's implied p(3,160), p(4,400), p(13,1800). Reports total mismatches and concrete failing cases. |
