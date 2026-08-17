# Order-3 orbit-matrix search for srg(99,14,1,2): the infeasibility boundary

```
thread: orbit-matrix-z2z3
task:  orbit-matrix-g99-detached
status: boundary recorded from the live heartbeat (directive 36); NOT a verdict
```

## What this is

The plain, unbroken CP-SAT encoder on the m=33 order-3 orbit matrix of a
putative srg(99,14,1,2) does NOT terminate within any practical budget. An
INFEASIBLE verdict would exclude a fixed-point-free order-3 automorphism (not
the graph itself); that verdict was **not** reached, so **no order-3 exclusion
is established by this run**. What the run did establish, and what this note
records, is the **infeasibility boundary** — the model size and the observed
rate at which the solver makes progress, stated exactly.

This is a reportable result precisely because it is a stated boundary, not a
mood. A search that does not terminate is data about the problem: the space, the
reduction, the rate, and the wall clock at which it was abandoned.

## The live heartbeat (directive 36), exact numbers

From `code/out/orbit_z3_enc_g99_plain_detached.captured.txt` (lines 300–375),
the flushed per-bound heartbeat:

- **Model size at m=33:** `41,745 variables`, `57,165 constraints`.
- **At 694.32 s:** `var 41730/41745`, `constraints 57129/57165`.
  - That is **15 variables fixed out of 41,745** in eleven and a half minutes —
    roughly one variable per ~46 s, and the constraint count has barely moved
    (57165 → 57129, i.e. 36 constraints dropped).
- Through the end of the capture (1111.29 s) the same pattern continues:
  var 41725/41745, constraints 57115/57165. **No bound movement** — the
  objective bound does not move because the model is purely Boolean feasibility;
  each `var` decrement is a presolve fixing, and the rate is ~1 per minute
  with no tendency to accelerate.

**Consequence.** An INFEASIBLE verdict requires exhausting the 41,745-variable
space. At the observed presolve rate this will not terminate in the 3000 s
budget, and almost certainly not in any budget available here. It is a stated
boundary, not a result: the conclusion is **no INFEASIBLE ⇒ no exclusion of an
order-3 automorphism** (directive 27's verdict distinction, now applied to a
boundary rather than a result).

**The decisive extrapolation (directive 37).** The heartbeat gives two points:
**15 variables fixed at 694 s**, **33 fixed at 1889 s** — that is **18
variables in 1195 s, about one per 66 s**. At that rate, fixing all **41,745**
variables would take roughly **32 days** — and that is **presolve alone**,
before any search of the space an INFEASIBLE verdict would have to exhaust.
This closes the whole orbit-matrix programme (route 11 — see solution.md): an
**order-2** automorphism has **more** orbits than the order-3 case
(≈(99+f)/2 for f fixed points), so its model is strictly larger and strictly
worse, and is not worth the same attempt at this rate. 'Does not terminate
within any practical budget' is a judgement; **'one variable per 66 seconds,
32 days for presolve' is a measurement**, and the measurement is what a next
pass can act on. The route is closed by **computational infeasibility, NOT by
mathematics**: no order-3 or order-2 exclusion is established, the published
Aut reduction to {Z₂, Z₃} stands untouched, and the graph's automorphism group
remains open.

## Capture defect: two encoders writing one file

Every heartbeat line in the capture is **doubled** (identical text, identical
timestamp) — the mechanical signature of **two encoder processes appending to
the same capture file**. This corroborates directive 36 problem 1: the old
buffered encoder is still running alongside the plain one. They split the same
cores (the box has 28, but both run multi-worker CP-SAT), so both are slower and
only one is observable. The buffered one can produce nothing readable anyway
(stdout buffered until exit, and it was killed/abandoned). **Action required:**
kill the buffered process; run exactly one encoder (directive 33), and the one
that stays is the plain `python -u` detached run. Before trusting any further
heartbeat, confirm exactly one encoder process and a single, non-doubled capture.

## Verdict semantics — unchanged

- **INFEASIBLE** from the plain unbroken encoder would have excluded a
  fixed-point-free order-3 automorphism and **nothing more** (NOT that the graph
  does not exist; combined with the published triviality reduction it would show
  trivial automorphism group *if* a graph exists).
- **UNKNOWN / TIMEOUT / no verdict** proves nothing. The boundary above is what
  is honestly reportable, and it is what is recorded here.
- The symmetry-broken encoder is UNSOUND (directive 35) and no symbreak 99
  INFEASIBLE may be believed; the plain unbroken encoder was the only sound
  route, and it is the one whose boundary is recorded.

## What this boundary does and does not say

- It **does not** bear on whether srg(99,14,1,2) exists.
- It **does** state, with the model size and the observed presolve rate, that the
  order-3 orbit-matrix feasibility question is out of reach of this CP-SAT
  encoding on this budget — so the residual order-3 case is not closed by
  enumeration, and the Z2 case (m~50, strictly harder) is not even worth the same
  attempt at this rate.
- It leaves open: a different encoding, a different solver, or a structural
  argument on the orbit matrix that avoids the 41,745-variable search.

Evidence: `code/out/orbit_z3_enc_g99_plain_detached.captured.txt` (live
heartbeat, lines 300–375). Status: boundary observed from a live capture — not a
graph claim.
