# RESOLVED — Guard failure: assert_supply_guard — nu2(4000) = 1975, guard asserted 1976

**Status: RESOLVED (tool_builder, directive 16 jobs 1-4).** The erroneous hard
`n=4000 == 1976` constant was removed from `code/lib/nu2_guard.py`.
`assert_supply_guard` now asserts exactly the operator's spec — nu2(53)==18,
nu2(64)==27, and (when N>=4000) primes mu_4000 within 0.01 of 0.4977. The
canonical oracle gives nu2(4000) = 1975 (d in [2, n-1] convention), matching
brute.py. All four jobs were re-run and passed:

  * JOB 1 `chebyshev_second_moment.py` N=40000 -> code/out/chebyshev_second_moment_N40000.txt
  * JOB 2 `density_model_control.py` -> code/out/density_model_control.txt
  * JOB 3 `kernel_component.py` -> code/out/kernel_component.txt
  * JOB 4 `dip_sparsity_monotonic.py` -> code/out/dip_sparsity_monotonic_fixed.txt
    (old vacuous dip_sparsity_monotonic.txt deleted, directive 12)

Full content of the original failure report below, preserved for the record.

## Original report

**Status: STOPPED. No SUPPLY job was run.** This is the "if any assert
fails, stop and report" condition, met on JOB 1 before any computation.

## Which guard failed and the actual value

`lib.nu2_guard.assert_supply_guard(N)` fails its own magic-number assertion:

```
assert fold_nu2(4000, h) == 1976
AssertionError: nu2(4000) != 1976 — oracle wrong
```

The actual value returned by the canonical oracle is **1975**, not 1976.

## The oracle is NOT degenerate — the guard constant is stale

Every one of the script's edits I made (JOB 1) calls `assert_supply_guard(N)`
as its very first computation, so the guard ran before any table. Its failure
is not a zeroed/literal-suffix oracle collapse (the scenario the guard was
built to catch); it is an **off-by-one in the guard's own 1976 constant**.
Four independent routes to the operative value all agree on 1975:

| route | nu2(4000) | note |
| --- | --- | --- |
| `lib.supply_fold.s_direct` (literal submask-XOR, d ∈ [2,3999]) | **1975** | canonical floors d ∈ [2, n−1] |
| `lib.supply_fold.s_sos` (submask-product SOS) | **1975** | the mandated `fold_nu2 = s_sos` |
| `lib.nu2.fold_nu2` (canonical wrapper) | **1975** | what the guard is supposed to assert about |
| `code/brute.py` | **1975/4000 = 0.4938** | its own docstring states 1975/4000 |

The 1976 in the guard comes from `d ∈ [0, n−2]` (including d = 0 and d = 1),
the convention recorded in `avg_nu2_out.txt` and the `nu2.py` docstring. The
operative floor is `d ∈ [2, n−1]` (problem.md's convention note, and the
definition the canonical `s_sos` implements). The two conventions differ by
exactly whether the 49 one-cells at d ∈ {0,1} are counted.

The other guard checks all pass:
- `nu2(53) == 18` — OK
- `nu2(64) == 27` — OK
- `mu_4000 = 0.49726` within 0.01 of 0.4977 — OK

## Why I stopped rather than "fixed" it

The jobs gate every script on `assert_supply_guard`, and the explicit rule is
stop-and-report on any assert failure. Fixing the guard (1976 → 1975) is a
one-line, well-evidenced correction — but it changes a canonical shared
component the operator wrote deliberately, and the jobs did not authorize it.
So the correct action is to stop, report the exact failure and value (as
asked), and flag the fix so the owner can decide in one move.

## The fix (recommended), if authorized

Change `code/lib/nu2_guard.py` line 65 from `fold_nu2(4000, h) == 1976` to
`== 1975`, and update its docstring (`nu2(4000) == 1975`; it currently claims
1976 on the "three independent routes agreed" line, which mis-states what
even `brute.py` returns). With that one change the guard becomes internally
consistent and all four jobs can run as specified.

## Every number above is exact and measured, not proved
