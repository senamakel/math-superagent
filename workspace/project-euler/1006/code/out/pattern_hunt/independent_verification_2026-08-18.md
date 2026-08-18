# Independent verification of strongest finite regularities

## Definitions and method

`c1(k)` is the number of length-k Fibonacci factors beginning with `1`; `Lmin(k)` is the least prefix length containing every length-k factor; the Toeplitz defect compares pair-correlation matrices of factor digits with a lag-only (translation-invariant) matrix. The governing theory is characteristic Sturmian/mechanical-word theory: the Fibonacci fixed point has slope `alpha=1/phi^2=(3-sqrt(5))/2`, balanced factors, and complexity `k+1`. The computations below use exact integer arithmetic and independent finite scans; they are evidence for the stated finite ranges, not proofs of infinite extensions.

## c1 slope law

Command: `python code/pattern_hunt/fresh_c1_lmin_check.py` and `python code/pattern_hunt/check_c1_weight.py`.

Output:

```text
c1 slope law: exact for k=1..10000
c1(k)=1+floor(k/phi^2), k=1..100: HOLDS
weight dist = {floor,ceil(k/phi^2)}, k=1..100: HOLDS
c0=(k+1)-c1 (complement identity): HOLDS
```

No falsifier through `k=10000` for the slope law. The independent weight-distribution check reaches `k=100`. This is consistent with the Sturmian balance theorem; the finite scan does not itself prove the theorem.

## Lmin formula

Command: `python code/pattern_hunt/fresh_c1_lmin_check.py` and `python code/pattern_hunt/verify_lmin_formula_f20.py`.

Output:

```text
Lmin Fibonacci law: exact for k=1..10000
mismatches of Lmin(k) = k + NextFib(k) - 1 for k=1..6764: 0
first failing k: none -- zero mismatches
```

Additional exact boundary values:

```text
k=1596: Lmin=3192, NextFib=1597
k=1597: Lmin=4180, NextFib=2584
k=2583: Lmin=5166, NextFib=2584
k=2584: Lmin=6764, NextFib=4181
k=4181: Lmin=10945, NextFib=6765
k=6764: Lmin=13528, NextFib=6765
k=6765: Lmin=17710, NextFib=10946
k=10000: Lmin=20945, NextFib=10946
```

No falsifier through `k=10000` in the fresh check; the bit-mask verifier independently reaches `6764` with zero mismatches. A third stored verifier reaches the same formula through `6764`; these are finite checks, not a proof of the global first-occurrence theorem.

## Toeplitz zero-defect indices

Command: `python code/pattern_hunt/check_toeplitz_defect.py`.

Exact output for `k=1..400`:

```text
max |Toeplitz defect| over all k, all cells = 1
k with any |d| >= 2: NONE
fully-Toeplitz k: [1,2,4,7,12,20,33,54,88,143,232,376]
predicted F_n-1: [0,1,2,4,7,12,20,33,54,88,143,232,376]
```

Thus, for the positive-index scan, the first missing predicted index is `0`, outside the tested domain. After removing that boundary artifact, every tested zero-defect index equals `F_n-1`, and there is no extra zero-defect index through `400`. The first nonzero-defect length is `k=3` if one asks for any defect cell; the first reported nonzero-defect cell in the separate extension diagnostic is at `k=6` under its indexing/criterion. The zero-defect list is the reliable invariant here.

The strongest attack against the overgeneralized Toeplitz conjecture is therefore a counterexample: full translation invariance does **not** hold for arbitrary k. The zero-defect phenomenon survives exactly at the tested positive Fibonacci-boundary indices `F_n-1`.

## Additional sequence tools and attacks

`analyze_exact_new.py` tested exact rational homogeneous recurrences through order 12 and Berlekamp–Massey modulo several moduli. Results:

- `Psi` exact prefix (25 terms): no order <=12; BM complexity 13 modulo `M`.
- `Psi mod M` (400 terms): no order <=12; BM complexity 200 modulo `M`.
- `d_j` (1145 terms): no order <=12; BM complexity 573 modulo `M`.
- `Lmin` (400 stored terms): no order <=12; this is expected because the NextFib staircase is the stronger description.

The Wythoff run-start attack independently verified `floor(j phi^2)` for all recorded `j=1..1146`; gaps were only 2 or 3, with gap counts `{2:437,3:708}` over gaps from starts 2 through 1146. The script’s final density print has an unrelated `mpf` formatting exception; the exact comparisons completed before that exception and were not used as proof.

## Conclusions

- `c1(k)=1+floor(k/phi^2)`: no falsifier through 10000; independently supported by exact factor scans and Sturmian balance theory.
- `Lmin(k)=k+NextFib_strict(k)-1`: no falsifier through 10000 in the fresh scan, and zero mismatches through 6764 in the independent bit-mask verifier.
- Toeplitz zero-defect indices: exactly `[1,2,4,7,12,20,33,54,88,143,232,376]` through 400, i.e. positive `F_n-1`; no extra index in range. The all-k Toeplitz conjecture is falsified (nonzero defects occur, with maximum absolute defect 1 through 400).
- No new low-order scalar recurrence or stronger finite pattern survived the sequence-tool attacks.
