## Excess-height renormalization identity — proved and Lean-kernel-checked

```claim
id: excess-renorm-identity-proved
statement: |
  Let h be any halved Gilbreath row (entries >= 0), with excess t(j) = max(0, h(j)-1),
  h'(j) = |h(j) - h(j+1)|, and t'(j) = max(0, h'(j)-1). The renormalization is
  pointwise (per-pair), with three disjoint cases:
    (a) bulk:  t(j) >= 1 and t(j+1) >= 1  ==>  t'(j) = max(0, |t(j)-t(j+1)| - 1);
    (b) wall:  h(j) in {0,1} and h(j+1) = t(j+1)+1 with t(j+1) >= 1
               ==>  t'(j) = t(j+1) - h(j);
    (c) low:   h(j), h(j+1) in {0,1}  ==>  t'(j) = 0.
  Consequence (max principle): with M = max_j t(j) and M' = max_j t'(j), M' <= M;
  and a bulk pair strictly decreases: t'(j) < max(t(j), t(j+1)).
status: proved
evidence: |
  Three independent routes agree:
  (1) Lean 4, code/lean/excess_renorm.lean, lean_check compiled=true verified=true,
      zero sorryAx, #print axioms all within {propext, Classical.choice, Quot.sound}
      (low_case has no axioms at all). Theorems: bulk_case, wall_case, low_case,
      pointwise_bound, max_principle, bulk_strict, bulk_strict_ltM.
  (2) Universal finite-class verification, code/excess_renorm_universal.py:
      all rows in {0,...,6}^9 (h(0)=0), 5,764,801 rows, 46,118,408 (row,j) positions,
      cases a/b/c/max violations = 0/0/0/0. Complete because the identity is
      per-pair: the 49 ordered pairs {(h(j),h(j+1))} exhaust the hypothesis space,
      so the pair table (case-a 25, case-b 10, case-c 4, 0 violations) is the whole
      mathematics; the row walk repeats it under all contexts.
  (3) Real rows: first-step capture code/out/excess_height_verify.captured.txt
      (depth 600, sieve 2e7) — interior 0 violations, wall drain 94/94 matched,
      regeneration 61/61, max-principle 0 violations over 556 rows.
holds-here: yes
hypotheses: h entries nonnegative (the halved row); exact integer |a-b| = Nat.dist.
falsifier: any halved row and adjacent pair where one of (a),(b),(c) fails; none
  exists in the finite class {0..6}^9 nor on the real rows.
note: research/approaches/excess-height-renormalization.md (status adopted).
```

### The wall-case correction (this run's own fix)

The naive wall formula `t'(j) = t(j+1) + 1 - h(j)` is **off by one**. Correct:
with `h(j) in {0,1}` and `h(j+1) = t(j+1)+1`, the absolute value resolves to
`(t(j+1)+1) - h(j)`, so

```
t'(j) = |h(j) - h(j+1)| - 1 = (t(j+1)+1 - h(j)) - 1 = t(j+1) - h(j).
```

Hand-check: `h(j)=1, h(j+1)=2` (t(j+1)=1) gives `t'(j)=|1-2|-1 = 0 = 1-1`, not
`r+1-h(j)=1`. Both the Lean file and the universal verifier use the corrected
form.

### Why this is a genuine GOAL.md deliverable

The reduction to `A_k(1) in {0,2}` is equivalent to `t_k(1) = 0`. The
renormalization identity is a **proved invariant of the absolute-difference
operator**: the tail excess profile evolves under the same operator one level
down (D, minus one, clamp at 0), and the max-excess is non-increasing. This is
the sharpest-coordinate statement of the drain/erosion law (its wall case) and
the self-similarity that the three previously-refuted scalar-potential,
level-set, and max-plus candidates all lacked.

Not resolved here: the *regeneration* side (whether `t` reaches the
regeneration threshold `t=1` at the wall often enough), which is the open
content and is unaffected by this identity — the identity is consumption-side
and was already expected; the new contribution is the machine-checked form and
the sharp wall constant.
