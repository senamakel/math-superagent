# Tasks

## Background

Two models exist. `code/pattern/n_integer_count.py` (grid-enumeration, O(N)
scan) reproduces all three oracle values: g(16,5,5,6)=9, G(16)=9, G(20)=205
(see `code/out/n_integer_model.txt`). `code/pattern/fast_g.py` (monotone
f-crossing, no grid, the efficient candidate) also gets g(16,5,5,6)=9 but
overcounts G(20) as 213 vs oracle 205 — an overcount of 8 (see
`code/out/G20_overcount.md`). The sign convention (sigma,eta,theta)=(-1,-1,-1)
is settled and correct. The goal is to fix the overcount in the crossing model
so we have an efficient method for G(500) that does not scan d.

- [ ] **1. Run the G(20) per-tuple diagnostic.** Extend `code/pattern/fast_g.py`
  (or write a short driver that calls `g_fast` with `verbose=True`) to print
  per-tuple g(c,s,p,q) for all 22 G(20) tuples alongside the n_integer_count
  oracle values (already in `code/out/n_integer_model.txt`). For any tuple
  where the two disagree, print each offending d value and the planet centre
  positions (x,y for p and q). Save output to `code/out/G20_diagnostic.txt`.
- [ ] **2. Identify the spurious arrangements.** Compare the d values from
  fast_g.py against those from n_integer_count.py. The overcount is 8 across
  22 tuples — find which tuples contribute how many spurious d's and what
  makes them invalid: d=d_min (p-planets coincide at 1/(2π)), d at an endpoint
  where f crosses an integer exactly at DL or DU, planet positions that
  coincide (y≈0 for either type), or some other degeneracy.
- [ ] **3. Fix the admissibility rule in fast_g.py.** Modify `g_fast()` to
  exclude the spurious arrangements. The fix is in the counting — which
  integer crossings are admissible — not the residue formula, the sign
  convention, or the monotonicity. Possible changes:
  - exclude d values where y_p or y_q < epsilon (planets coincide)
  - exclude integer m where the crossing d is within epsilon of DL or DU
  - or a different endpoint treatment in the strict inequality
- [ ] **4. Validate.** Confirm the fixed model gives G(16)=9, G(20)=205, and
  per-tuple agreement with n_integer_count.py on every G(20) tuple.
- [ ] **5. G(500).** Compute G(500) with the fixed fast_g model. The method
  counts integer levels of f(d)=Q_p−Q_q on (DL,DU) by bisection, O(g log ε⁻¹)
  per tuple — independent of the bound 500.
- [ ] **6. Independent verification.** Verify G(500) against the grid-enumeration
  model at reachable sizes, or by a second derivation.

## Do NOT do

- Write new approaches/models. The crossing-model structure is correct; only the
  admissibility rule needs fixing.
- Re-derive the sign convention. (-1,-1,-1) is settled.
- Re-derive the residue formula or the f-crossing monotonicity.
- Compute G(500) with the unfixed model — it is wrong by construction.
