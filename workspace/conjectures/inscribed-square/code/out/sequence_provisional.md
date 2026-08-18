# Sequence extraction pass (executed 2026-08-18)

Executed `python code/extract_all_sequences.py`. Computation-bearing integer sequences in existing result artifacts are `[1,0,1]`, `[0,0,0,0,0,0,0]`, and `[1,2,3,4,5,6,8]` (the latter is rounded-rational vertex-only polygon output and conflicts with the exact boundary oracle).

`analyze_sequence` found no low-degree polynomial for `[1,2,3,4,5,6,8]`, with differences `[1,1,1,1,1,2]`; `find_linear_recurrence` found no constant-coefficient recurrence through order 6; OEIS lookup matched only unrelated sequences A269303, A215366, A051037, A000378.

The all-zero sequence is an artifact of a broken boundary oracle, contradicted already by unit-square sanity. The 3-term sanity sequence is too short. No exact exploitable regularity was found. Any conjecture suggested by the 7-term sequence is falsified at its first uncomputed term only if that term is actually computed; no such extension was warranted because the source sequence is not exact regular-polygon data.
