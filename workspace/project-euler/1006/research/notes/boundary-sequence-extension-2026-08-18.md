# Boundary sequence extension (2026-08-18)

Using the verified mechanical evaluator `code/mech/mech_psi.py`, the exact boundary values
`Psi(k)` were extended at `k=|q_n|-1=F_{n+1}-1` through `n=18`, i.e. `k=4180`.

Residues modulo `M=101001001`, in order for
`k = 1,2,4,7,12,20,33,54,88,143,232,376,609,986,1596,2583,4180`, are:

```text
1 101 2042402 14581260 50567341 78244245 35684836 53101262
81475026 47327343 56074264 41973743 89635420 99069783 83233380
56603180 79637523
```

The cyclic-window identity was checked exactly at every `n=2..18`: the `k+1` factors at
`k=|q_n|-1` equal the cyclic windows of the standard Fibonacci word `q_n`, and their
squared decimal values sum to the mechanical `Psi(k)`.

`analyze_sequence` found no low-degree polynomial pattern. `find_linear_recurrence` found
no constant-coefficient recurrence of order <=8 over all 17 terms. `oeis_lookup` found no
matching entry. These are finite exact negative results; no extrapolation is justified.

An attempted recursion for this boundary subsequence was refuted. Although the individual
cross-boundary window formulas are exact, the aggregate expansion requires prefix/suffix
cross-moments because the recursive block is inserted in the middle of each cyclic window;
ordinary `Psi` and first moment do not close. This is another instance of the existing
joint-observable obstruction, not a new solver.
