# State-vector linear-recurrence test for PE1006 (negative result)

Test question: does the exact state vector evolve under a constant-coefficient
*linear* recurrence mod M = 101001001 across k? Tested on the 200 saved states
in `psi_state_1_200.txt`.

## Data and verification

Columns of `psi_state_1_200.txt`: `k, P_mod, S_mod, N1, N0, P1_mod, vR_mod`
(P = Psi mod M, S = sum of values mod M, N1/N0 counts of factors extending by
1/0, P1 = sum of values of '1'-extending factors mod M, vR = value of the
unique right-special length-k factor mod M).

Before testing, I re-verified the exact extension formula against the file:

    Psi(k+1) = 100(Psi(k) + vR(k)^2) + 20 P1(k) + N1(k)   (mod M)

Held for **all 199 transitions** (columns P,S,N1,P1,vR — note the file has N0
as the 4th column, so P1 is column 5, vR column 6). 0 mismatches.

## Method

For order d and state dimension m, seek a fixed matrix C (m x m·d) over F_M

    u(k) = C * [u(k-1); ... ; u(k-d)]     (mod M)   for all k past some point.

Decided by modular Gaussian elimination (consistency of C·A = B over F_M), then
any found C is verified to reproduce the whole window. Affine variants add a
constant feature. All exact integer arithmetic mod the prime M. No floats.

Validated the tester on a synthetic constant-recurrence sequence: it correctly
reported `consistent` with 0 verify-errors, so "INCONSISTENT" on real data is
meaningful.

## Results — every tested configuration is INCONSISTENT

Orders d = 1..6, both with the full window and skipping the first 30 states,
both linear and affine, all fail:

| state | linear | affine |
| --- | --- | --- |
| 5-dim [P,S,N1,P1,vR] | INCONSISTENT (all d) | INCONSISTENT (all d) |
| 6-dim [P,S,N1,N0,P1,vR] | INCONSISTENT (all d) | INCONSISTENT (all d) |
| enriched [P,S,vR,V2,P1,N1,N0] (vR² kept) | INCONSISTENT (all d) | INCONSISTENT (all d) |
| enriched [P,vR,V2,P1,N1] | INCONSISTENT (all d) | — |

Individual components (P, P1, vR, N1, S, and V2 = vR²) have NO low-order linear
recurrence mod M in their own past (d = 1..6 all INCONSISTENT).

## Independent cross-check (Berlekamp–Massey over F_M)

Running BM on the first half of each component gives order ≈ n/2 = 50 and the
derived coefficients fail to reproduce the very first untrained term (k = 101).
On the full 200 terms BM returns order ≈ n/2 = 100 for every component (P, S,
P1, N1: 100; vR, N1: 90). This is the degenerate ceiling for a non-recurrent
sequence — the same signature as the prior
`PE1006-no-loworder-linear-recurrence` finding for Psi(1..150).

## Structural reason

The (verified) extension recurrence is nonlinear in the natural state:

    P(k+1) = 100 P(k) + 100 vR(k)² + 20 P1(k) + N1(k).

It needs the square vR(k)². Even explicitly carrying V2 = vR² as an extra state
component does not close the evolution as a constant linear map, because how V2
itself advances (V2(k+1) = vR(k+1)²) is not linear in the state. So no
constant-coefficient linear (or affine) recurrence of any tested small order
describes the state vector — consistent with the broader conclusion that the
closed recurrence lives in the Fibonacci/Zeckendorf structure of k, not in a
fixed matrix in k.

```claim
id: PE1006-state-vector-no-linear-recurrence
statement: No constant-coefficient linear (or affine) recurrence mod 101001001 of order 1..6 fits the state vector [P,S,N1,N0,P1,vR] (or the enriched [P,S,vR,vR^2,P1,N1,N0]) across k=1..200; individual components P, P1, vR, N1, S, vR^2 likewise have no low-order constant linear recurrence (BM order = n/2 degenerate ceiling on full 200 terms).
hypotheses: exact states k=1..200 in code/out/psi_state_1_200.txt; M prime; extension formula P(k+1)=100(P+vR^2)+20P1+N1 verified for all 199 transitions.
holds-here: yes.
status: checked
bearing: rules out matrix-exponentiating a fixed constant-order linear recurrence in k for the state vector; reinforces that the closed recurrence for Psi(k) is piecewise in the Fibonacci/Zeckendorf structure of k.
anchor: code/out/state_vector_linear_recurrence.md (state_recurrence_test.py, state_recurrence_enriched.py, state_component_bm.py)
```

## Files

- `code/pe1006/state_recurrence_test.py` — Gaussian-elimination consistency
  tester (orders 1..6, linear + affine, any column subset, skip-window).
  Validated on a synthetic constant-recurrence sequence.
- `code/pe1006/state_recurrence_enriched.py` — tests the enriched
  extension-formula state [P,S,vR,vR²,P1,N1,N0].
- `code/pe1006/state_component_bm.py` — independent Berlekamp–Massey
  cross-check per component.
- This note.
