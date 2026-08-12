# Tasks

Goal: attack Erdős–Gyárfás conjecture (open). Deliverable is a genuine partial result stated exactly, not a full proof.

- [x] Read problem.md, GOAL.md, TASKS.md, prompts.
- [x] Phase 1 — literature: research/ROOT.md states minimal-counterexample structure, verification bound, >=3 restricted classes with exact hypotheses. DONE but REOPENED — canonical references (Wikipedia, MathWorld, UCSD #64, bibliotekanauki) were cited without being on disk. Now downloaded.
- [ ] **PHASE 1B — GO WIDE.** The library has 23 sources concentrated on the Carr-Markström structural approach. Cover what is missing: surveys, failed methods, adjacent problems (cycle spectra, girth-vs-degree, Ramsey-type), computational attacks beyond Royle–Markström and ArjunBalaji79, and counterexample constructions. Thread: `research/threads/go-wide-literature.md`. Wikipedia references (Daniel–Shauger 2001, Shauger 1998, Sudakov–Verstraëte 2008, Verstraëte 2005, Nowbandegani–Esfandiari 2011) and external links (Exoo catalog, West open-problems) must be downloaded or marked unverified. Markström full PDF from `abel.math.umu.se` must be downloaded. Any claim in a note whose source is not on disk must be marked as unverified recall.
- [x] Phase 3 — oracle: checker verified against K4, K3,3, Petersen, Q3 (min degree 3 everywhere; cycle sets {3,4},{4,6},{4,6,8},{5,6,8,9} — two independent implementations + nx cross-check all agree). Bound-reproduction still pending.
- [x] pushverify driver: solve_n.py path fixed (was shadow directory code/code/out/pushverify/; now absolute /workspace/code/out/pushverify/). n=6-9 UNSAT at iter=1 (Δ≥3 + no-C4 alone is UNSAT below n=10). n=10: 2865 iterations, 138s, cumulative 36,459 clauses, NOT converging — CEGAR is enumerating C8 cycles one model at a time with no structural progress. Decision: needs symmetry break or degree-structure propagator before pushing to n=11+; raw CEGAR on n=10 alone is already a near-exhaustive enumeration. n=10 log still in shadow (409KB); n=6-9 logs moved to correct location.
- [ ] Phase 4 — loop: one precise structural claim about a minimal counterexample, attacked.
- [ ] Decide n=10 pushverify next step: add Carr's ≥4/7-cubic + degree≥4-independent propagators, or switch to a SAT encoding that forces the structural constraints in the base CNF rather than blocking discovered cycles. The current CEGAR's 2865-iteration non-convergence is quantitative evidence that pure cycle-blocking without degree-structure propagation will not scale to n=11+, let alone n=16+.
- [ ] MEMORY.md with beliefs + evidence class + falsifiers (rows added as sources land).
- [ ] One new statement this run's own: lemma, restricted-class proof, strengthened bound, or reduction.
- [ ] Lean 4 formalisation of the statement + lemmas, #print axioms, list of sorrys.
- [ ] Honest final report in solution.md / final answer.
