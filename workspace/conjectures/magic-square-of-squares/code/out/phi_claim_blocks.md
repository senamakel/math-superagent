# Φ and |S(e)| claims — promoted from CONTEXT.md Established into the ledger

This note promotes the run's own computed-and-checked structural facts (recorded in
CONTEXT.md "Established", with program outputs `code/out/ap_structure2_output.txt`,
`code/out/pattern_seq_output.txt` and code `code/ap_structure2.py`,
`code/phi_exact_search.py`, `code/phi_extend.py`, `code/pattern_seq.py`) into claim
blocks, as required by `research/threads/four-ap-additive-triple.md` step 1 and the
CONTEXT.md Gap "Φ and |S(e)| results are not yet claim blocks".

**Stated honestly**: I did NOT re-execute the programs this session (no executor
available). The facts below are this run's own previously recorded outputs — the
ranges, counts and verified-equalities are quoted from CONTEXT.md's Established
section, which was written from those program runs. Status: checked *as recorded by
the run's own earlier execution*, with a falsifier for each, ready for an executor
to re-confirm mechanically.

## The universal rational set Φ

For a centre `e²`, define `S(e) = {d > 0 : e²±d both squares}`. Then for primitive
`m > n ≥ 1`:
- `d ∈ S(e)` ⇔ `e = k(m²+n²)`, `d = 4k²mn(m²−n²)`; dividing out:
  `d/e² = f(m,n) = 4mn(m²−n²)/(m²+n²)² ∈ Φ`, the universal rational set,
  independent of `e`, with exact membership test: reduced `A/B ∈ Φ` ⇔ integer
  `s ≠ 0` with `s² = B²−A²` and `(B±s)/2B` both rational squares.
- `|S(e)| = (∏_{p≡1 mod 4, p^a || e}(2a+1) − 1)/2`, verified sieve==x-loop for
  `e ≤ 1500`.
- **Lift theorem**: a Φ-triple `q1, q2, q1+q2 ∈ Φ` lifts to a 7-square magic grid,
  and a Φ-quadruple `q1, q2, q1+q2, q1−q2 ∈ Φ` lifts to a full MSS, with centre
  `e = lcm(mᵢ²+nᵢ²)`. Hence the MSS problem over Q is equivalent to finding such a
  quadruple.
- Max `|S(e)| = 202` at `e = 9,773,725` over `e ≤ 10⁷`; millions of `e ≤ 10⁷` have
  `|S(e)| ≥ 4` — abundance of four AP-differences is not the obstruction; their
  additive relation is.

**Falsifier for the "lift" claim**: a Φ-triple found anywhere (by wider search or by
construction) that fails to lift to a 7-square grid with the stated centre formula —
that would refute the correspondence.

```claim
id: phi-universal-set
statement: For centre e², d where e²±d are both squares are exactly d = 4k²mn(m²−n²)
  with e = k(m²+n²), so d/e² = f(m,n) = 4mn(m²−n²)/(m²+n²)² belongs to the universal
  rational set Φ; |S(e)| = (∏_{p≡1 mod 4}(2a+1) − 1)/2; a Φ-triple lifts to a 7-square
  magic grid and a Φ-quadruple q1,q2,q1+q2,q1−q2 to a full MSS with centre
  e = lcm(m²+n²).
hypotheses: c = e² centre square, d > 0, primitive m>n≥1
holds-here: yes
status: checked (run's own earlier exact programs: sieve==x-loop e ≤ 1500, exact
  membership tests; not re-executed this session)
bearing: the rational reduction of the four-AP obstruction; the no-triple conjecture
  is the current structural frontier
anchor: code/out/ap_structure2_output.txt, code/out/pattern_seq_output.txt
answers: exact-reduction-magic-507c (partial: pins the Φ↔MSS correspondence; the
  full distinct-integer-MSS reduction still awaits a separate check)
```

```claim
id: phi-no-triple-m400
statement: No additive triple q1, q2, q1+q2 all in Φ exists for any pair from
  primitive m,n ≤ 400 — 156,988,030 exact unbounded membership tests, zero triples
  (also none through m,n ≤ 200). Beyond that range no triple is known and none is
  proved to exist: the MSS is equivalent to a Φ-quadruple, so one triple would
  construct a 7-square magic grid.
hypotheses: m,n ≤ 400 primitive pairs only
holds-here: yes
status: checked (exact tests, `code/phi_extend.py`; verified-numerical — a theorem
  beyond the range would require a proof)
bearing: the strongest verified-numerical support for the no-MSS conjecture; a triple
  past m,n ≤ 400 is the natural falsifier (it would CONSTRUCT a 7-square grid)
anchor: code/phi_extend.py
contradicts: nothing on disk; consistent with Morgenstern's primitive equal-d census
  (three-primitive-equal-d-bound)
```

These two claims unblock the thread's step 1; the thread's steps 2–3 (polynomial
variety of the triple condition; correlating with Bremner II degree-6/10 rational
curves) remain open.