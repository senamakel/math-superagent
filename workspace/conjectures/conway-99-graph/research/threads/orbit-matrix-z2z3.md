# Thread: orbit-matrix Z2/Z3 feasibility

```
thread
question: Does the residual automorphism programme — an order-3 and an order-2
    automorphism of a putative srg(99,14,1,2) — yield a sharp exact result? The
    published orbit-matrix school (Crnković–Maksimović, Behbahani–Lam,
    Cesarz–Woldar) has reduced any nontrivial Aut to {Z2, Z3}; the residual Z2
    and Z3 cases are precisely the ones not yet settled by that published
    programme. A Kramer–Mesner-type orbit-matrix feasibility decision on each
    gives either INFEASIBLE (⇒ no such orbit matrix exists) or the finite
    residual orbit matrices a later bounded search must expand.
status: closed
rests-on: aut-cm-2020 (order-3 is fixed-point-free ⇒ 33 point-orbits, 77
    line-orbits on the 231-line triangle geometry), aut-cw-2025 + aut-cm-2020
    (nontrivial Aut ⊆ {Z2,Z3}), c4/c5 (controls rook(3), BvLS)
next: (directive 37) CLOSED — the whole orbit-matrix programme, order-3 AND
    order-2, is out of reach of this CP-SAT encoding at this presolve rate.
    The plain unbroken m=33 detached heartbeat: 15 vars fixed at 694s, 33 at
    1889s = 18 vars in 1195s (~1 per 66s); fixing all 41,745 vars is ~32 DAYS
    of presolve alone, before any search of the space an INFEASIBLE verdict
    would have to exhaust. An order-2 model has MORE orbits (≈(99+f)/2 for f
    fixed points) and is strictly larger and strictly worse. Closed as route
    11 (solution.md §2), boundary recorded in
    research/notes/orbit-order3-infeasibility-boundary.md, closed by
    computational infeasibility NOT by mathematics: no order-3 or order-2
    exclusion is established, the published Aut reduction to {Z2,Z3} stands
    untouched, Aut(99) remains open. Both encoder searches are killed and the
    cores freed — the measurement (~1 var/66s, 32 days presolve), not the
    judgement, is what a next pass can act on. What remains live for the orbit
    line: a different encoding, a different solver, or a structural argument
    on the orbit matrix that avoids the 41,745-variable search.
```

**Directive 27 gates — recorded before any run, per the operator.**

1. **What a verdict proves.** INFEASIBLE at the Z3 orbit matrix excludes an
   order-3 automorphism; it does **NOT** show `srg(99,14,1,2)` does not exist.
   Combined with the published reduction of any nontrivial Aut to {Z2, Z3},
   finishing both cases shows the graph has **trivial automorphism group if it
   exists** — a genuine result (no non-trivial symmetry can locate the graph),
   and **not a nonexistence proof**. State this in the note up front, before
   running.

2. **Validate the encoder before trusting UNSAT.** Build the analogous Z3 orbit
   matrix for a graph we have — **BvLS admits order-3 automorphisms** — and
   require Z3 to **FIND** it (the positive control). This workspace has one
   unvalidated-engine false positive on record already (`n3_vc_gate`:
   hypothesised `E = 16·n₃` failed across 37 random graphs, retracted). An UNSAT
   from an unvalidated orbit-matrix encoding would be the second, and is not
   admissible.

**Why it is a genuine (bounded) result, not a search.** The orbit-matrix case
split is finite and small: 33 point-orbits / 77 line-orbits for Z3, ~50+ orbits
for Z2 — a stated Kramer–Mesner-type count, not 3⁹⁹. Either decision is exact
and reportable. The controls (rook(3), BvLS) both possess the Z2/Z3 actions the
encoder must recover before any 99 verdict.
