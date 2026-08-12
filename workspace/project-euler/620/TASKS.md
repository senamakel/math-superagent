# Tasks

- [ ] **Diagnose the overcount.** Run `code/pattern/fast_g.py`'s `G_sum(20)`
  (already implemented, just execute it) with verbose per-tuple output and
  for each of the 22 tuples print: g(c,s,p,q), the oracle-per-tuple g if
  available (see below), and for any tuple where the model disagrees with
  the grid-enumeration oracle, print each offending d value and the four
  planet positions (centre coordinates). The oracle per-tuple values come
  from running `code/pattern/tangency_enum.py` generalized to arbitrary
  (c,s,p,q) — or, simpler, from a small brute-force grid enumeration of the
  winning residue form at high resolution on each tuple. Save output to
  `code/out/G20_diagnostic.txt`.
- [ ] **Identify the spurious arrangements.** From the diagnostic output,
  determine which kind of degeneracy each overcount corresponds to:
  d=d_min (1/(2π), p-planets coincide), d at f(DL) or f(DU) (endpoint
  crossing), planets landing on top of each other, or some other spurious
  geometry.
- [ ] **Fix the admissibility rule.** Modify `g_fast()` in
  `code/pattern/fast_g.py` to exclude the spurious arrangements, keeping
  the sign convention (sigma=-1, eta=-1, theta=-1) and the f-crossing
  structure unchanged. The fix is in the counting rule — which integer
  crossings are admissible — not in the residue.
- [ ] **Validate.** Confirm the fixed model gives G(16)=9, G(20)=205, and
  per-tuple agreement with the grid oracle on every G(20) tuple.
- [ ] **G(500).** Once validated, compute G(500) with the fixed model.

## Do NOT do

- Write new approaches or new models. Six exist; three were added in the
  last ten minutes; zero are tested beyond the one being diagnosed.
- Re-derive the sign convention. (sigma, eta, theta) = (-1, -1, -1) is
  settled and correct — it gives g(16,5,5,6)=9.
- Re-derive the residue formula or the f-crossing monotonicity.
- Compute G(500) with the unfixed model — it is wrong by construction.
