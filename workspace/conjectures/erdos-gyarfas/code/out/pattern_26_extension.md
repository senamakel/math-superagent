# Pattern-finder pass over the run's computed sequences (n=26 extension)

Tool-exact checks over every term on disk. All results below are exact over the
terms supplied; none is a proof that the pattern extends.

## An 9th term for avoidsC4, and the C16-cliff survives its first falsifier

The n=26 census (`code/out/expansion_census_26/level_26_results.txt`, verified
byte-for-byte by `recount_26.py`):
    total=321776= A027610(12) EXACT, avoidsC4=3408, avoidsC4C8=0,
    avoidsC4C16=0, avoidsC4C8C16=0.

This adds the **9th term 3408** to the avoidsC4 sequence and, more
importantly, tests the run's standing conjures at a level n=26 that was
explicitly uncomputed in the prior note (`pattern_26_notes.txt`).

- **avoidsC4C16** = [1,1,2,0,0,0,0,0,0] over n=10..26 (9 levels, step 2).
  The C16-cliff statement "every C4-free member of the family at n>=16
  contains a C16" **SURVIVED its first falsifying level**: n=26 has
  avoidsC4C16 = 0, as predicted. It now holds for 6 consecutive levels
  (16..26). Its **first falsifier is n=28** — the next level, uncomputed.
  (The census is the cubic Apollonian-dual family = planar 3-trees, A027610;
  n=28 is infeasible — the family size explodes super-exponentially.)

## avoidsC4: still no closed form, now at 9 terms

avoidsC4 = [1,1,2,5,15,50,202,807,3408] (n=10..26).
- `analyze_sequence`: no constant-difference row → not a low-degree polynomial.
- `find_linear_recurrence(max_order=6)`: **none** fits all 9 terms.
- `oeis_lookup`: **0 strict-prefix matches** — not catalogued, nothing to lift.
- Growth ratios a_n/a_{n-1} at the tail: 3.995 (n=22->24), 4.223 (n=24->26)
  — creeping flat ~4 per +2 vertices, no settled growth law. This is a
  curve-fit heuristic (the 8-term data nudged ~15% between the last two),
  NOT an exact regularity; do not report it as structure.

## Lobe-probe sequences (cut-vertex (2,2) shape), 8 terms n_H=4..18

From `code/out/cutvertex/lobe_probe/lobe_probe.log`:
  constructions (6,18,60,285,1530,10689,97440,1115127),
  with-C4       (6,18,59,250,1387,9826,89834,1025689),
  with-C8       (0,0,60,265,1467,10559,96798,1112200).
- The `constructions` sequence satisfies the bookkeeping identity
  constructions(n_H) = #cubic(n_H) × (3n_H/2): 1×6, 2×9, 5×12, 19×15,
  85×18, 509×21, 4060×24, 41301×27 — each cubic graph on n_H vertices has
  3n_H/2 edges and one is removed. **Exact, but definitional bookkeeping** —
  it is the census machinery, not structure relevant to the EG conjecture;
  not a finding.
- with-C4 and with-C8: no clean exact regularity (spurious order-4 rational
  fits over 8 noisy terms arise for any such data — not reportable), no OEIS
  match findable, and the structural negative is the real content: **pow2-free
  lobes = 0 at every n_H=4..18** (every lobe of a connected-cubic H on ≤18
  vertices contains a C4 or a C8), so no (2,2)-glued or (1,2)-shaped cut-vertex
  counterexample candidate exists below order 20. That negative is already a
  verified-numerically result; the sequences carry no further structure.

## NO4 sequence, 8 terms

NO4 = [5,9,57,503,6059,91433,1655659,34758006] (n=10..17).
- `oeis_lookup`: 0 strict-prefix matches (fresh, this pass). Confirms the
  existing growth-law record (≈K·3^n·(n-10)!, tail ratio ≈3(n-10)).
- No exploitable closed form; already recorded in CONTEXT.md.

## Bottom line

The n=26 extension adds real confirmatory weight: the C16-cliff conjecture
survived its stated first falsifier (n=26), and avoidsC4 extended to a 9th
term still yields neither an OEIS match nor a low-order recurrence. No new
exact, exploitable regularity emerged in any family sequence. The only open
confirmation left is n=28, which the census cannot reach.
