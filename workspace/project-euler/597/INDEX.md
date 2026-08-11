# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method and evidence rules for the whole run: restate the problem, test small cases, prefer theory over enumeration, keep sourced facts separate from deductions, keep files described. |
| `CONTEXT.md` | Shared standing brief for the run: the PE 597 model, what the research library establishes (rate-ratio products, relative-speed clocks, treap recursion, parity accumulation), known limits (w-order and treap hypotheses refuted), and MC pinning p(13,1800)≈0.5002. |
| `GOAL.md` | Run goal for PE 597: restated problem with every symbol defined, the n=3/L=160 worked-example table and p(4,400) value as the test oracle, and completion criteria for brute/solution agreement. |
| `MEMORY.md` | Durable working memory: established results, the parity-comparator and multi-bump edge-loss bug fixes, refuted hypotheses (w-order, treap), MC ballpark of p(13,1800)≈0.5002±0.00007, and the open exact-method gap. |
| `README.md` | Folder-layout note pointing newcomers to AGENTS.md, `prompts/`, and the goal/tasks/scratchpad/memory working files. |
| `SCRATCHPAD.md` | Provisional work: the diagnosis of the parity-comparator bug, its fix, and the corrected MC run output. |
| `TASKS.md` | Run task checklist with status: oracle verification, both bug fixes, MC ballparking of p(13,1800), and the remaining exact-solution task. |
| `exact_small_backup.py` | Independent from-scratch second engine for PE 597 race dynamics (race_parity, mc_estimate) written without reference to code/brute.py, used as a ground-truth cross-check: differentially compares against brute.outcome_parity across n=2..6, and MC-anchors p(3,160)=56/135, p(4,400), and p(13,1800). This is the independent-verification route for the final answer. Lives at root because its import path (os.path.dirname(__file__)+"/code") assumes it sits one level above code/. |
| `pattern_study.py` | Empirical structural study (Q1/Q2/Q3) of PE 597: correlates race parity with three candidate scalar-priority treaps (w_i = v_i/(L-40i), finish time, raw speed) counted mod 2 against the oracle, searches for any scalar treap matching parity, and characterizes the bump directed graph (out-degree, index monotonicity, and distinct chronological edge sets with frequencies vs. the n=3,L=160 probability table). Assumes it lives in the workspace root (imports code/brute via a path relative to its own directory). |
| `problem.md` | Official Project Euler 597 statement downloaded from projecteuler.net/minimal=597 — the run's source document with the n=3/L=160 worked examples and the stated p(4,400) value. |
| `race_spec.md` | Exact chronological race-dynamics specification for implementation: event simulation, bump/OUT/FINISH treatment, and the bump-chain parity definition. Reference contract for any race solver. |
| `test_treap.py` | Deterministic test of the Cartesian-tree (min-heap treap) hypothesis for PE 597: compares tree-parity (count of ancestor/descendant index pairs in the min-w treap) against the true oracle outcome_parity on many random Exp(1) speed vectors, and Monte-Carlos the tree model's implied p(3,160), p(4,400), p(13,1800). Reports total mismatches and concrete failing cases. |
