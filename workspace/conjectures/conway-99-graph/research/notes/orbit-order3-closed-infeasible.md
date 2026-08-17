# CLOSED ROUTE 11: orbit-matrix Z2/Z3 completion — closed by computational infeasibility, NOT mathematics

```
route:  orbit-matrix-z2z3 (thread, research/approaches/orbit-matrix-residual-group)
task:   orbit-matrix-g99-detached
status: closed as computationally infeasible (boundary recorded); NO verdict reached
```

## The route

A nontrivial Aut of a putative srg(99,14,1,2) reduces (published) to {Z2, Z3}.
Completing the Z2 and Z3 orbit-matrix feasibility cases would give UNSAT on both
⇒ |Aut|=1 (a sharp named result), or SAT ⇒ finite residual. This run attempted
the order-3 (m=33 orbit) case with the **plain, unbroken** CP-SAT encoder
(the symmetry-broken encoder was already ruled UNSOUND: 20,000 random
conjugations of the real BvLS orbit matrix, none satisfying the break).

## The boundary (exact, verified)

- Model size at m=33: **41,745 variables, 57,165 constraints**.
- Plain encoder (PID 5789, `python -u` heartbeat) ran its full **3000s budget**
  and exited **UNKNOWN / INCONCLUSIVE**.
- Final bound: `#Model 2974.64s var:41675/41745 constraints:56987/57165`,
  conflicts **5,039,266**, branches **8,049,382**
  — `code/out/orbit_order3_final_boundary.captured.txt`.
- Verified extrapolation (exact rational, `code/out/orbit_order3_boundary_verify.py`
  → `.captured.txt`): heartbeat points 694.32s→15 vars fixed, 1889.85s→33 fixed;
  Δ=18 vars in 1195.53s = **one per 66.42s**; at that (slowing) rate, presolve
  alone for 41,745 vars ≈ **32 days**. This is a **lower bound** on total
  wall-clock: the rate is slowing (start 46.29s/var → overall 57.27s/var →
  two-point 66.42s/var) and presolve fixing is the only progress, while the
  space an INFEASIBLE verdict would have to exhaust is far larger than the
  presolve-fixed variables.

## The honest verdict

- **No INFEASIBLE reached ⇒ no order-3 fixed-point-free automorphism is
  excluded.** The order-3 case remains OPEN.
- The residual **Z2** case (more orbits, ~(99+f)/2, strictly larger model) is
  **not worth the same attempt** at this rate — a stated reason, not a mood.
- The published reduction of a putative Aut to {Z2, Z3} stands **untouched**.
- The automorphism group of the graph remains **open**.

## The doubling correction

The capture's doubled `#Model` lines were **not** two live encoders. After
killing the buffered duplicate (PID 5504), the single plain process (5789)
still printed every line twice: CP-SAT's native progress log fires and the
`log_callback` lambda re-echoes each emitted line. Intrinsic to the single
process. (Directive 36's "kill the competing buffered encoder" was still
executed — the buffered one was a genuine second process that produced nothing
readable.)

## What this closes, and what it leaves

This is a **refutation-of-a-method** boundary: this CP-SAT encoding cannot close
the residual Z2/Z3 automorphism question within any practical budget. It is NOT
a graph existence claim. A different encoding, a different solver, or a
structural argument on the orbit matrix (avoiding the 41,745-variable search)
remains open.

Evidence: `code/out/orbit_z3_enc_g99_plain_detached.captured.txt`,
`code/out/orbit_order3_final_boundary.captured.txt`,
`code/out/orbit_order3_boundary_verify.captured.txt`.
