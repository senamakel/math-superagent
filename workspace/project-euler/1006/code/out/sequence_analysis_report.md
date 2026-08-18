# Exact sequence-analysis run (2026-08-18)

## Established prior inputs

`GOAL.md` defines PE1006: `S_0=0`, `S_1=01`, `S_n=S_{n-1}S_{n-2}`; `F_k` is the distinct length-k factor set and `Psi(k)` is the sum of squared decimal values. The stated anchors are `Psi(3)=20302` and `Psi(10) mod 101001001=10699667`.

The workspace already records the governing Sturmian/Fibonacci-word theory and prior checks. The current linear evaluator is explicitly only an O(k) evaluator; the O(log k) fixed-dimensional collapse is unresolved. No published answer was searched.

## Commands and exact outputs

### Brute oracle: `python code/brute.py`

```text
psi(3)= 20302
psi(10) mod M= 10699667
1 1
2 101
3 20302
4 2042402
5 2250400
6 44353102
7 14581260
8 65706380
9 21161323
10 10699667
11 77738268
12 50567341
13 60501668
14 39049712
15 54716955
16 44184356
17 24648269
18 91059589
19 53059648
20 78244245
```

This is the required bounded exponential oracle (`k<=20`), and its output reproduces both examples exactly. The stored oracle notes also record the corrected prefix bound and factor counts.

### Existing evaluator: `python code/solution.py`

```text
window evaluator vs mech_psi k=1..150: PASS
Psi(1) mod 101001001 = 1
Psi(2) mod 101001001 = 101
Psi(3) mod 101001001 = 20302
Psi(10) mod 101001001 = 10699667
Psi(10^18): NOT RUN; this certified evaluator is O(k), not the requested O(log) method
```

### Existing transfer diagnostic: `python code/directive9_transfer.py`

```text
directive9 finite transfer checks k=1..150: PASS
summary composition checks k=1..150: PASS
3 5 20302 20302
10 13 10699667 10699667
```

These are checks of the finite transfer implementation against the independent mechanical-word evaluator, not a proof of the missing full-size reduction.

### Sequence analyzer: `python code/out/analyze_sequences.py`

The analyzer reads stored exact integer rows from `code/out`; Berlekamp–Massey orders are modular diagnostics modulo `101001001`, not integer-recurrence proofs.

```text
psi_exact.txt terms=25 first10=[1, 101, 20302, 2042402, 204252402, 30445654403, 3054587854503, 407470828064704, 40849095449084804, 4085011557551094804]
BM modulus 101001001 order= 13
psi_residues.txt terms=400 first10=[1, 101, 20302, 2042402, 2250400, 44353102, 14581260, 65706380, 21161323, 10699667]
BM modulus 101001001 order= 200
c1_terms.txt terms=400 first10=[1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
BM modulus 101001001 order= 232
first differences= [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
lmin.txt terms=400 first10=[2, 4, 7, 8, 12, 13, 14, 20, 21, 22]
BM modulus 101001001 order= 200
first differences= [2, 3, 1, 4, 1, 1, 6, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ext_recurrence.txt terms=40 first10=[0, 10, 10, 10, 10010, 10010, 1010010, 1010010, 1010010, 1001010010]
BM modulus 101001001 order= 20
```

## Interpretation

- The brute examples and the existing evaluator agree exactly; this validates the required oracle/example layer.
- `c1` has the established prior interpretation as the count of factors beginning with `1`; its first differences match the stored Fibonacci/Sturmian density pattern. The workspace's prior formula claim is `c1(k)=1+floor(k/phi^2)` (with indexing as stored); the sequence output alone is evidence, not a new proof.
- `lmin` has the established prior exact formula `Lmin(k)=k+NextFib(k)-1`, verified in the workspace through `k=6764`. Its difference spikes are consistent with Fibonacci block boundaries.
- The high BM orders for `psi_residues`, `c1`, and `lmin` do not support a short fixed-order linear recurrence over this modulus. BM is only a finite modular fit: order 200 on 400 terms, for example, is not evidence of a useful recurrence. The 25 exact `psi` values yielding order 13 is likewise too short to establish anything and should not be extrapolated.
- No exact value of `Psi(10^18) mod 101001001` was computed. The remaining obstruction is structural: the missing joint intercept/Fibonacci-block collapse, not lack of finite sequence data.
