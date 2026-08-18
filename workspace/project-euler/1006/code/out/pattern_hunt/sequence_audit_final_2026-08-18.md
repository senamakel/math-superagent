# PE1006 integer-sequence audit — 2026-08-18

## Scope and method

Audited the stored exact tables under `code/out/` and reran the existing exact tooling:

```text
python code/pattern_hunt/analyze_existing_sequences.py
python code/pattern_hunt/sequence_audit_requested.py
python code/pattern_hunt/analyze_exact_new.py
python code/pattern_hunt/check_dj_structure.py
python code/pattern_hunt/check_small_moduli.py
```

The programs parse stored `(index,value)` rows, test exact rational homogeneous linear recurrences through order 12, run Berlekamp–Massey over selected moduli, and test the stored structural identities. This is bounded evidence, not a proof of nonexistence of any global recurrence.

## Exact outputs

- `counts.txt`: 400 terms; `count(k)=k+1` with no mismatch. A schema-aware scan reports the trivial affine recurrence `a_n=2a_{n-1}-a_{n-2}`; this is not useful for Ψ.
- `c1_terms.txt`: 400 terms; `c1(k)=1+floor(k/phi^2)` with no mismatch. Prefix: `[1,1,2,2,2,3,3,4,4,4]`; suffix: `[153,153,153]`. No exact homogeneous recurrence of order ≤12.
- `lmin.txt`: 400 terms; `Lmin(k)=k+NextFib_strict(k)-1` with no mismatch. Prefix: `[2,4,7,8,12,13,14,20,21,22]`; suffix: `[1007,1008,1009]`. No exact homogeneous recurrence of order ≤12.
- `psi_exact.txt`: 25 terms; prefix `[1,101,20302,2042402,204252402,30445654403,3054587854503,407470828064704]`; no exact homogeneous recurrence of order ≤12. BM over `M=101001001` has finite-prefix complexity 13.
- `psi_residues.txt`: 400 terms; prefix `[1,101,20302,2042402,2250400,44353102,14581260,65706380,21161323,10699667]`; no exact homogeneous recurrence of order ≤12. BM over M has complexity 200.
- `ext_recurrence.txt` (40 terms) and `extrecur_res.txt` (400 terms): no exact homogeneous recurrence of order ≤12.
- `dj_raw.txt`: 1145 terms, beginning `[1,1,3,2,1,5,3,8,5,2,9,5,1,10,5,15,9,3,15,8]`, ending `[471,35,743]`; no exact homogeneous recurrence of order ≤12. BM over M has complexity 573/1145. It agrees term-for-term with the stored A019587 comparison for all 1145 terms.
- `toeplitz_defects.txt`: 400 terms; no exact homogeneous recurrence of order ≤12. Zero indices are `[1,2,4,7,12,20,33,54,88,143,232,376]`; the proposed universal-zero pattern is first falsified at `(k, defect)=(3,2)`.

## OEIS lookup

Attempted exact OEIS web lookups for the extracted prefixes of `c1`, `lmin`, and `dj` using the OEIS JSON endpoint. All three returned HTTP 403 in this container. Therefore no OEIS identification is claimed here. The local stored A019587 comparison for `dj` was independently verified, but that local comparison is not a fresh external lookup.

## Conjecture attacks and first falsifiers

- `d_j` Fibonacci-additive conjecture fails first at `j=3`: `d_3=3` but `d_1+d_2=2`.
- `Psi(k) mod 1000 = c1(k)` fails first at `k=2`: `Psi(2)=101`, `c1(2)=1`.
- `Psi(k) mod 8 = c1(k)` fails first at `k=2`: `101 mod 8=5`, while `c1(2)=1`.
- The stored Toeplitz/general lag-translation conjecture fails first at `k=3`, defect 2; only Fibonacci-boundary lengths in the listed finite scan vanish.
- No low-order constant-coefficient recurrence was found for Ψ, residues, `c1`, `Lmin`, `d_j`, extension data, or Toeplitz defects under the stated finite order bound. This does not prove that no recurrence exists globally.

## Assessment

No new exploitable sequence or recurrence was found. The verified positive descriptions remain the prior floor/Fibonacci-block identities for `c1` and `Lmin`, the factor count `k+1`, and the stored run decomposition of `d_j`; none supplies the missing fixed-dimensional aggregation needed for `Psi(10^18)`.

No larger run was made: extending the same scans would add only bounded evidence and would not settle the structural gap.
