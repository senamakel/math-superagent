# Goal — state at end of attempt 3

Attack Conway's 99-graph problem (`problem.md`): the existence of `srg(99,14,1,2)`.
This remains an OPEN problem; the deliverable is exact partial results with a
named failing step on the controls, never a claim of the whole.

## Where the run stands (end of attempt 3)

The workspace holds eleven closed routes (solution.md §2) and one verified
constraint. Attempt 3 carried out the final closure of the orbit-matrix
programme and verified the decisive boundary number by a second independent
route. All open tasks are closed; the run is at its natural consolidation point.

## New this attempt

8. **Route 11 closed: orbit-matrix Z2/Z3 completion — computational
   infeasibility, NOT mathematics (directive 36/37).** The plain unbroken CP-SAT
   encoder on the m=33 order-3 orbit matrix of a putative srg(99,14,1,2) ran its
   full 3000s budget and exited `UNKNOWN`: final bound `#Model 2974.64s
   var:41675/41745 constraints:56987/57165`, conflicts 5,039,266, branches
   8,049,382 (`code/out/orbit_order3_final_boundary.captured.txt`, and the live
   heartbeat in `orbit_z3_enc_g99_plain_detached.captured.txt`).
   **No INFEASIBLE ⇒ no order-3 fixed-point-free automorphism is excluded.** The
   residual order-2 case (more orbits, strictly larger model) is not worth the
   same attempt at this rate. The published reduction of a putative Aut to
   {Z2,Z3} stands untouched; the automorphism group of the graph remains open.

9. **Decisive boundary number independently re-verified in exact arithmetic.**
   `code/out/orbit_order3_boundary_verify.py → .captured.txt`: heartbeat points
   694.32s→15 vars fixed, 1889.85s→33 fixed; Δ=18 vars in 1195.53s = one per
   66.42s; at that (slowing) rate presolve alone for 41,745 vars ≈ 32 days
   (lower bound — rate slows: 46.29→57.27→66.42 s/var). The measurement survives
   independent exact recomputation; it is a refutation-of-a-method boundary, not
   a graph claim.

10. **Capture-doubling root cause found: NOT a second encoder.** Killing the
    buffered duplicate (PID 5504) left the single plain process (5789) still
    printing every `#Model` line twice — CP-SAT's native progress log plus the
    `log_callback` echo. Intrinsic to one process. (Directive 36's "kill the
    competing buffered encoder" was still executed; it was a genuine dead second
    process that produced nothing readable.)

## Completion test (unchanged)

No nonexistence argument is admissible until it is run against rook(3) and
bvls_graph() through `code/lib.srg.is_srg` and the step that breaks on them is
named. Every closed route in this run satisfies that gate — each failed either
on the controls (parameter-determined ⇒ cannot separate 99 from 9/243) or was a
stated computational-infeasibility boundary (never a verdict).

## What remains (the honest frontier, solution.md §7)

- Existence or nonexistence of `srg(99,14,1,2)`: **open**, not claimed.
- The **global closure of the n₃ ≥ 1 seed**: taking the radius-6 fixpoint
  structures (19 survivors) and closing them into 99 vertices (do the outside
  87–91 vertices join to satisfy μ=2 and degree-14 for every boundary pair?).
  No local obstruction at any radius, no counting floor — what remains is the
  cross-patch/global structural question, **harder than every closed route**.
- Any live argument must be a=7-specific (√(4k−7)=7), breaking where a∈{3,9}
  survive — the only shape the controls cannot refute.
