# Thread — a finite-transducer statistic separating the {0,1}-digit set from the ×2 orbit

The live direction of the run (GOAL.md, problem.md, `research/backward/erdos-via-symbolic-invariant.md`).
Question: does there exist a statistic `Φ` on the orbit `{2^n}` — computable by a fixed
finite transducer along the base-2 → base-3 carry — that the digit-`{0,1}` set `S`
violates and `x ↦ 2x` preserves, with `Φ(0), Φ(2), Φ(8)` surviving and `Φ(n)` excluded for
`n > 8`?

```thread
id: erdos-symbolic-invariant
question: Is there a finite-transducer statistic Phi on the orbit {2^n : n>=0},
  evolved by one fixed step under x->2x, with Phi(0),Phi(2),Phi(8) in W, such that
  2^n in S (S = digit-{0,1} 3-adic set) => Phi(n) in W and n>8 => Phi(n) not in W?
  The whole difficulty is the MIDDLE ternary digits, unreached by the low-k sieve
  and by top-digit size arguments.
status: open
rests-on: SIEVE-EXACT-COUNT (verified), DIMITROV-HOWE-26-ONES (sourced),
  carry-count-zero-iff-digitfree (proved, a reformulation), ALBAYRAK-BELL
  (no decidability route), ABL-II-EXCEPTIONAL-SET-BOUND-PRIMARY (dimension bound
  gives no integer statement)
blocked-by: the statistic cannot be a continuous function of the 3-adic point --
  the {2^n} orbit is dense in Z_3^x, so a continuous ×2-invariant is constant on
  the closure and cannot separate S. Must be a transducer/carry statistic on digit
  strings, not a function of the limit point.
next: the concrete finite objects are the 3-adic path-set automata of ABL (C(1,2)
  is the relevant intersection for x->2x, with computable spectral-radius
  dimension); a candidate Phi must first pass the constraint family (i),(ii) of
  G-cong (c1 even; 2^n ≡ 0 mod 2^k for k<=n) and the falsification oracle n=0,2,8.
  SMT candidates were already refuted at n=0 (weighted polarity); Spencer's
  carry-packet proof is unsound at completeness.
```

## Recalled / recorded negatives on this thread

- **Weighted signed-digit sums** (`Σ(-1)^i a_i`) fail at n=0 under both mod 2 and mod 3
  (`research/approaches/smt-weighted-polarity-refuted.md`).
- **Carry-count under ×2** equals zero exactly on `{0,2,8}` (`carry-count-zero-iff-digitfree`),
  never separating the witnesses from each other — a zero carry is the zero-digit-free
  condition, not a new obstruction.
- **Continuous ×2-invariants** are constant on the orbit closure (dense) and cannot separate `S`.
- **Spencer 2026** carry-packet exhaustion is unsound at the completeness step.
- **Furstenberg-slicing/transversality line ruled out as a direct instrument**
  (`HAN-YU-2021-SLICING-DIM-SUM-LT-1`): the slicing theorems require
  dim_H A2 + dim_H A3 < 1; here dim S ≈ 0.6309 and the ×2 orbit closure is all of
  Z_3^× (dim 1), sum ≈ 1.63 > 1, so the hypothesis fails precisely in the regime this
  problem occupies. Adds to `ABL-II-EXCEPTIONAL-SET-BOUND-PRIMARY`: dimension/measure
  statements about S do not reach which integers lie in it.

## Next concrete step

Build the ×2 base-3 carry transducer (the only piece with a chance of being a theorem on its
own) and check the first finite-transducer statistics against n=0,2,8 and against the
constraint family `G-cong`. Any candidate must be shown machine-refutable or machine-holdable
with the falsification gate passed first.
