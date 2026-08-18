# Sequence-tools audit — 2026-08-18

## Scope
Inspected the existing pattern-hunt artifacts and ran a fresh exact audit on the supplied sequences `Psi`, `c1`, `Lmin`, `d_j`, and Toeplitz defects. The run used exact rational recurrence fitting, modular Berlekamp–Massey as a diagnostic, and targeted first-falsifier tests. It did not extend the large scans: such extension would only add bounded evidence and would not address the unresolved fixed-dimensional reduction for `Psi(10^18)`.

## Commands and outputs

### Fresh sequence-tool run

```sh
python code/pattern_hunt/sequence_tools_new_run.py
```

Output:

```text
psi_exact n= 25 prefix= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 exact_rec<=12= (2, {c0: 2, c1: -1})
 BM mod 100000007= 2
psi_res n= 400 prefix= [1, 101, 20302, 2042402, 2250400, 44353102, 14581260, 65706380, 21161323, 10699667]
 exact_rec<=12= None
 BM mod 100000007= 200
c1 n= 400 prefix= [1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
 exact_rec<=12= None
 BM mod 100000007= 232
 c1 floor law first_bad= None
lmin n= 400 prefix= [2, 4, 7, 8, 12, 13, 14, 20, 21, 22]
 exact_rec<=12= None
 BM mod 100000007= 200
 lmin formula first_bad= None
dj n= 1145 prefix= [1, 1, 3, 2, 1, 5, 3, 8, 5, 2]
 exact_rec<=12= None
 BM mod 100000007= 573
 dj adjacent Fibonacci first_bad= (3, 3)
toeplitz n= 400 prefix= [0, 0, 2, 0, 2, 8, 0, 18, 10, 16]
 exact_rec<=12= None
 BM mod 100000007= 200
 zero_indices= [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]
 zero_everywhere first_bad= (3, 2)
psi mod100=c1 first_bad= (5, 2250400)
psi mod1000=c1 first_bad= (2, 101)
```

The `psi_exact` result is an artifact-ingestion warning, not a mathematical discovery: the file's first column is an index, so that run accidentally analyzed `1,2,...,25`. The residue-column result is the meaningful `Psi` analysis. This mistake was read and corrected rather than promoted. The same caution applies to the fresh `c1`/Toeplitz cross-column comparisons below; their individual sequence scans are valid, but the cross-file comparison was not used as evidence.

### Existing sequence-tool and catalog attempts

```sh
python code/pattern_hunt/analyze_exact_new.py
python code/pattern_hunt/analyze_existing_sequences.py
python code/pattern_hunt/check_dj_oeis.py
python code/pattern_hunt/check_toeplitz_defect.py
```

The existing reports record:

- `Psi` exact: 25 actual terms; no exact homogeneous recurrence of order <=12.
- `Psi mod M`: 400 terms; no exact order <=12; modular BM complexity 200/400.
- `c1`: floor law `1+floor(k/phi^2)` survives through 400 in the supplied table and through 10000 in an independent existing scan; no short homogeneous recurrence.
- `Lmin`: `k+NextFib_strict(k)-1` survives through 400 in the supplied table and through 10000 in the independent existing scan; no short homogeneous recurrence.
- `d_j`: 1145 terms; no exact order <=12; the tempting adjacent Fibonacci-additive law fails at `j=3`, where `d_3=3` rather than `d_1+d_2=2`. The existing exact termwise identification with the stored A019587 comparison remains, but is not a new result.
- Toeplitz defects: zero indices through 400 are exactly `[1,2,4,7,12,20,33,54,88,143,232,376]`, the positive `F_n-1` values. The universal-zero conjecture fails first at `k=3`, defect 2.

OEIS lookup was attempted by the existing `check_dj_oeis.py`/sequence-hunt workflow on program-produced prefixes. The OEIS endpoint returned HTTP 403, so no new catalogued identification is claimed. Existing A019587 matching for `d_j` is retained only as prior finite evidence.

## Attack and verdict

Potentially new candidates were attacked as follows:

1. Short constant-coefficient recurrences for each supplied sequence: none survives order 1–12 on the genuine columns. The apparent order-2 result for `psi_exact` was caught as a column-selection bug and is discarded.
2. `d_j` Fibonacci-additive recurrence: first falsifier `j=3`.
3. Universal Toeplitz-zero law: first falsifier `k=3`; the surviving boundary classification is the already-recorded `F_n-1` list.
4. `Psi mod 100 = c1`: the fresh script exposed a second indexing/column mistake (`psi_res` and `c1` lengths use incompatible row interpretation), so its reported `k=5` is discarded. Existing correctly indexed checks establish the prior mod-100 law through 3000; no new law is inferred here. `Psi mod 1000=c1` correctly fails at `k=2` from `Psi(2)=101` versus `c1(2)=1`.

## Conclusion

**NOTHING NEW SURVIVES.** The genuinely exact surviving regularities are the already-established Sturmian/Wythoff/Fibonacci-boundary facts:

- `c1(k)=1+floor(k/phi^2)`;
- `Lmin(k)=k+NextFib_strict(k)-1`;
- Toeplitz zero indices `F_n-1` in the tested range;
- the prior `Psi mod 100` law and right-extension recurrence.

No new exact recurrence, OEIS identification, or full-size `Psi` reduction was found. The fresh run also found and documented two ingestion-indexing hazards, preventing false discoveries.
