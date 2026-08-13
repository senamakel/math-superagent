# The coverage figure is confirmed three independent ways

Eight programs had been written into `code/pattern_mining/` and **none had been
run** — captures were flat at 19 while `code files` climbed to 32. The operator
executed the four that need no sympy. `verify_current_coverage.py` could not run
on the host (it imports sympy); the other three did.

## The two figures were never in conflict

The run's `exact_union_density.py` reports `0.945305`. The operator's earlier
note reported `0.961127`. That looked like a disagreement and is not: the two
read **different input sets**.

| input | moduli | classes | covered |
| --- | --- | --- | --- |
| `extended_subprogression.full.txt` only (what the run's program reads) | 11…37 | 88 | `4552829/4816253` = **0.945305** |
| all three capture files (what the operator read) | 11…43 | 123 | `732719497/762354697` = **0.961127** |

Restricting the operator's CRT computation to the single file the run's program
reads reproduces `0.945305` **exactly**, to the last digit. The extra 1.58
points come only from the moduli `38, 39, 41, 43`, which live in the other two
capture files.

## Three routes, one answer

1. **Operator, CRT over independent prime groups** — `0.945305` on the matching
   input.
2. **Run's `exact_union_density.py`, factoring over `K mod 6` branches** —
   `0.945305`, with per-branch coverages from `0.92968` to `0.95898`.
3. **Run's `independent_density_check.py`, direct empirical count** over
   `K < N` with no CRT at all — `0.94530` at `N = 3·10⁶`, converging
   `0.92800 → 0.94180 → 0.94462 → 0.94514 → 0.94530`.

The third is the valuable one: it is a brute-force count, structurally unlike
the other two, and it lands on the same number. The density method is sound.

## The saturation question now has data

`aggregate_subprogression.py` answers directly what the previous note reduced
the problem to — whether any modulus can be saturated. It cannot, yet, and by a
wide margin:

| `M` | covered | missing |
| --- | --- | --- |
| 11 | 3 | 8 |
| 13 | 4 | 9 |
| 17 | 6 | 11 |
| 19 | 5 | 14 |
| 22 | 6 | 16 |
| 23 | 9 | 14 |
| 26 | 10 | 16 |
| 29 | 6 | 23 |
| 31 | 7 | 24 |
| 33 | 12 | 21 |
| 34 | 12 | 22 |
| 37 | 8 | 29 |

The best ratio is `M = 33` at 12 of 33, and `M = 11` — the smallest modulus —
has only 3 of 11 with residues `0,1,2,3,4,6,8,9` all missing. No modulus is
near saturation, and `M = 11` is the cheapest place to settle whether
saturation is even possible.

```claim
id: coverage-figure-triangulated
statement: The covered density of n congruent to 1 mod 840 by the identity
  families is confirmed by three independent computations. Restricted to
  extended_subprogression.full.txt (88 classes, moduli 11..37) the operator's
  CRT computation gives 4552829/4816253 = 0.945305, the run's
  exact_union_density.py gives 0.945305 by factoring over K mod 6 branches, and
  the run's independent_density_check.py gives 0.94530 by direct empirical
  count over K < 3*10^6 with no CRT. Over all three capture files (123 classes,
  moduli 11..43) the figure is 732719497/762354697 = 0.961127; the apparent
  discrepancy between 0.9453 and 0.9611 is entirely input scope, not
  mathematics. Per-modulus saturation is far off: the best is M=33 at 12 of 33
  residues covered, and M=11 has only 3 of 11, missing 0,1,2,3,4,6,8,9.
hypotheses: the families are exact identities in Z[k], established separately;
  a family for n = a*k + b covers n congruent to b mod a only for n >= b
holds-here: yes. Exact rational arithmetic in two routes and a direct count in
  the third, all on stated inputs
status: checked
bearing: removes any doubt about the density method by agreeing across a CRT
  computation and a brute-force count that share no structure. Confirms the two
  circulating figures differ only by which capture files were read. Supplies the
  missing residues per modulus, making the saturation question concrete: M=11,
  with 8 of 11 residues missing, is the cheapest test of whether any modulus can
  be saturated at all
anchor: code/out/exact_union_density.captured.txt;
  code/out/independent_density_check.captured.txt;
  code/out/aggregate_subprogression.captured.txt;
  code/out/coverage_triangulated.md
source: operator-computation
```
