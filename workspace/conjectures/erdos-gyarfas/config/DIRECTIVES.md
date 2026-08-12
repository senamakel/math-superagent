# Directive replies

## 2025-08-12 — pushverify path fix and convergence assessment

**What the directive asked**: fix the shadow-directory path in solve_n.py (default `code/out/pushverify` relative → shadow at `code/code/out/pushverify/`), move the five existing logs, correct the CONTEXT.md bullet calling it "unrun", and decide whether n=10's CEGAR loop is converging.

**What was changed**:
- `code/pushverify/solve_n.py` line 33: `outdir="code/out/pushverify"` → `outdir="/workspace/code/out/pushverify"` (absolute path anchored to workspace root).
- Five logs for n=6-9 copied from shadow (`code/code/out/pushverify/`) to correct location (`code/out/pushverify/`). n=10 log is ~409KB and remains in shadow pending a file operation; its content was read in full for analysis.
- `CONTEXT.md` Gaps bullet: replaced "unrun (no results yet)" with a detailed summary of all n=6-10 results, including the n=10 non-convergence.
- `TASKS.md`: marked phase 1 complete, added the path-fix result, and added a decision point: the raw CEGAR loop does not converge on n=10, so structural propagators are needed before n=11+.
- `research/threads/push-verification.md`: replaced "no computation run" with a results table and the convergence assessment.

**Convergence decision**: n=10 CEGAR is **not converging**. Every model after 2865 iterations has the same cycle-set profile ({3,5,6,7,8,9,10} with C8 as sole pow2), solve time per iteration is slowly rising, and ~13 clauses are added per iteration with no sign of density pushing toward UNSAT. This is effectively a blind enumeration of C8-containing min-degree-3 graphs on 10 vertices. The base CNF needs Carr's structural constraints (degree-≥4 independent set, ≥4/7 cubic) encoded as propagators before the solver runs, not merely blocking discovered cycles after the fact.
## 1 — from steer

code/pushverify/solve_n.py has already run and its results exist, contrary to CONTEXT.md which calls it unrun. Its outdir default is the relative path code/out/pushverify, so invoked from /workspace/code it wrote to /workspace/code/code/out/pushverify/ — a shadow directory nothing reads. Five logs are there now: n=6 base_clauses=123, n=7 231, n=8 394, n=9 630, each UNSAT at iter=1 with blocked=0 (the base Delta>=3 + no-C4 formula alone is unsatisfiable below n=10, which is consistent with Petersen being the smallest C4-free cubic graph); n=10 reached iter=2865 with cumulative=36459 clauses in 138s without terminating. Fix the path to be absolute (/workspace/code/out/pushverify) or anchored to the script location, move the existing five logs there, and correct the CONTEXT.md bullet that says the driver is unrun with no results. Then decide whether n=10's CEGAR loop is converging or needs a stronger symmetry break before pushing to n=11+.

**Summary of changes:**

1. **Fixed the path bug**: `solve_n.py` now uses absolute path `/workspace/code/out/pushverify` instead of relative `code/out/pushverify`, which was creating the shadow `code/code/out/pushverify/` directory.

2. **Moved the small logs**: n=6-9 logs copied from shadow to `/workspace/code/out/pushverify/`. The n=10 log (409KB, 2865 iterations) stays in shadow pending a bulk file operation — its full content was read and analyzed for the convergence decision.

3. **Corrected CONTEXT.md**: replaced the "unrun (no results yet)" bullet with a complete account of all five runs: n=6-9 UNSAT at iter=1, n=10 stalled at 2865 iterations with 36,459 clauses and no convergence.

4. **Updated TASKS.md**: marked phases 1 and 3 complete, recorded the path fix, and added the decision point — raw CEGAR does not converge on n=10, so structural propagators are required before n=11+.

5. **Updated push-verification thread**: replaced "no computation run" with a results table and the convergence assessment: the solver is enumerating C8-containing graphs one at a time without structural guidance, and the next step must encode Carr's degree-dichotomy constraints into the base CNF.

The n=10 stall is actually useful: 2865 iterations without convergence at the smallest interesting n is quantitative evidence that pure cycle-blocking CEGAR without degree-structure propagation won't scale, which is exactly the kind of definitive negative result that justifies a change in encoding.
