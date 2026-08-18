# Direct sequence hunt (2026-08-18)

No published Project Euler answers were consulted. All claims below are finite exact computational findings.

## Commands

`python code/pattern_hunt/analyze_sequences.py` (existing analyzer):
- `psi_exact.txt`: 25 terms; BM order 13 modulo M.
- `psi_residues.txt`: 400 terms; BM order 200 modulo M.
- `c1_terms.txt`: 400 terms; BM order 232 modulo M.
- `lmin.txt`: 400 terms; BM order 200 modulo M.
- `ext_recurrence.txt`: 40 terms; BM order 20 modulo M.

`python code/pattern_hunt/direct_sequence_hunt.py` (new direct run):

```text
psi_exact.txt ... linear_recurrence_order<=12 None
after exact terms: no homogeneous rational recurrence of order <=12
psi_residues.txt ... linear_recurrence_order<=12 None
c1_terms.txt ... distinct_diffs [0, 1] ... linear_recurrence_order<=12 None
lmin.txt ... distinct_diffs [1,2,3,4,6,9,14,22,35,56,90,145,234] ... linear_recurrence_order<=12 None
dj_raw.txt ... linear_recurrence_order<=12 None
topelitz_defects.txt ... linear_recurrence_order<=12 None
c1_floor_formula_first_bad None
lmin_formula_first_bad None
toeplitz_zero_indices_first [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]
toeplitz_zero_all_fib_minus1_through_400 True
```

The output's `None` means no exact rational homogeneous linear recurrence of order at most 12 fits every supplied term. Modular BM orders are finite diagnostics, not proofs of absence of higher-order recurrences.

## Exact regularities found or re-confirmed

1. `c1(k)=1+floor(k/phi^2)` holds for every stored `k=1..400`; the direct scan has no falsifier. Its first differences are exactly `{0,1}`.
2. `Lmin(k)=k+NextFib_strict(k)-1` holds for every stored `k=1..400`; no falsifier. The difference spikes in the stored range are exactly the listed values and occur at Fibonacci-boundary changes.
3. Toeplitz zero-defect indices through `k=400` are exactly
   `[1,2,4,7,12,20,33,54,88,143,232,376]`.
   These equal `F_n-1` for the Fibonacci indexing used in the workspace. First nonzero defects after the initial zeros are: `k=3 -> 2`, `k=5 -> 2`, `k=6 -> 8`, `k=8 -> 18`.
4. `d_j` has no order-12 exact homogeneous recurrence on all 1145 supplied terms. No new exact closed form was inferred; the existing report's exact identification with the stored run-jump sequence remains the relevant result.

## First falsifiers / negative results

- No short exact homogeneous linear recurrence (orders 1–12) for any supplied candidate sequence listed above.
- The residue sequence `Psi(k) mod M` has BM order 200 on 400 terms, and exact `Psi` has BM order 13 modulo M on only 25 terms; neither is a usable structural recurrence.
- Toeplitz zero defect is not universal: first falsifier to “zero for every k” is `k=3`, defect `2`; first non-Fibonacci-boundary zero gap after `k=2` is `k=4`, while the zero set through 400 remains precisely the displayed `F_n-1` list.

No newly generated larger terms were needed: the supplied records already reach 400 for Psi residues/c1/Lmin/Toeplitz and 1145 for d_j, while exact Psi reaches 25. The only surviving exact findings are the already structural c1/Lmin laws and the finite Fibonacci-boundary Toeplitz-zero pattern; no new recurrence or full-size Psi reduction was discovered.
