# Phi universal set and no-triple claims — mirrored from code/out/

The claims below are computed facts from this run's own exact programs.
The evidence is in `code/out/phi_claim_blocks.md` and the captures it
references; this note exists because `research/CLAIMS.md` is derived from
notes under `research/` and claim blocks in `code/out/` alone are invisible
to it.

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
  membership tests)
bearing: the rational reduction of the four-AP obstruction; the no-triple conjecture
  is the current structural frontier
anchor: code/out/phi_claim_blocks.md;
  code/out/ap_structure2_output.txt;
  code/out/pattern_seq_output.txt
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
anchor: code/out/phi_claim_blocks.md; code/phi_extend.py
```