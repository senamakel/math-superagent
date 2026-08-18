# Sequence survey (2026-08-18)

## Scope and method
Inspected `code/out/` and `code/pattern_hunt/`, then ran the existing exact sequence-analysis scripts. Integer sequences surveyed included Psi exact/residues, c1, counts, Lmin, ext-recurrence columns, d_j, V-run starts/gaps/lengths/values, S1 and transition data, and Toeplitz defects. Recurrence searches were exact rational homogeneous recurrences through order 12 where supported, plus Berlekamp–Massey modulo the stored modulus and small moduli. No OEIS network lookup tool is present; existing OEIS comparisons were rerun where scripts provide them.

## Exact regularities surviving the tested ranges

- `c1(k)=1+floor(k/phi^2)` for k=1..1000 by direct factor extraction; stored table checks k=1..400. No falsifier.
- Factor count `count(k)=k+1` for k=1..400. No falsifier.
- `Lmin(k)=k+NextFib_strict(k)-1` for k=1..1000 by independent extraction; stored independent checks extend to k=6764. No falsifier.
- `d_j` equals the existing OEIS A019587 comparison for j=1..1145. No falsifier in the recorded range.
- V-run starts equal `floor(j*phi^2)` for j=1..1146; gaps are exactly 2 or 3 there. This is a finite verification; no global claim made.
- The V-run/S1 extension recurrence remains valid for k=1..400 modulo M, as previously recorded. No new stronger relation found.
- Toeplitz-defect scan: maximum absolute defect is 1 through k=400; zero-defect k are exactly `1,2,4,7,12,20,33,54,88,143,232,376`, i.e. the positive recorded `F_n-1` values (with the indexing artifact 0 omitted). This is an exact finite pattern and agrees with the known Fibonacci-boundary route.

## Negative results / first falsifiers

- No exact homogeneous constant-coefficient recurrence of order <=12 was found for `psi_exact` (25 terms), `psi_residues` (400), `c1` (400), `d_j` (1145), `ext_recurrence` (40), `extrecur_res` (400), or `Lmin` (400).
- BM complexity is correspondingly high on the finite prefixes: Psi exact 13/25 modulo M; Psi residues 200/400; c1 232/400; d_j 573/1145; ext residues 200/400; Lmin 200/400. These are finite negative searches, not proofs of non-recurrence.
- `Psi(k) mod 1000 = c1(k)` first fails at k=2: Psi(2)=101 versus c1(2)=1.
- Corrected `Psi mod 100 == c1` first fails at k=5: residue 2250400 has mod-100 value 0 while c1(5)=2. (An older report's claim of no falsifier was due to comparing unreduced data.)
- The naive left-append rule for S1 holds only 23 of 1145 tested runs and fails first at the reported j=13 / s=34 example; it is not a regularity.
- `len(S1(s_j))=s_j` fails at the terminal truncated record (j=1146, s=3000, length 3002), a boundary artifact; similarly the shifted length rule fails at j=1145. No interior counterexample was established by this run.
- The existing `check_wythoff_gaps2.py` did not execute due to an `mpf` formatting TypeError; its exact integer outputs from other scripts were used instead.

## Commands and output

Commands run:

```sh
for f in code/pattern_hunt/analyze_existing_sequences.py code/pattern_hunt/analyze_exact_new.py code/pattern_hunt/independent_nonpsi_hunt.py code/pattern_hunt/sequence_report.py code/pattern_hunt/boundary_subseqs.py; do echo "=== $f ==="; python "$f"; done
for f in code/pattern_hunt/check_dj_oeis.py code/pattern_hunt/check_wythoff_gaps2.py code/pattern_hunt/check_run_density.py code/pattern_hunt/check_digit_excess.py code/pattern_hunt/check_s1_leftappend.py code/pattern_hunt/check_s1_runstructure.py code/pattern_hunt/check_toeplitz_defect.py; do echo "=== $f ==="; python "$f"; done
for f in code/pattern_hunt/extract_vr_runs.py code/pattern_hunt/check_directive1_big.py code/pattern_hunt/check_leading_counts.py code/pattern_hunt/check_weight_dist.py code/pattern_hunt/check_s1_inrun.py; do echo "=== $f ==="; python "$f"; done
```

Representative exact outputs:

```text
c1 formula first falsifier: None
Lmin formula first falsifier: None
count=k+1: True
loaded d_j count: 1145
d_j == A019587(j) for j = 1..1145: VERIFIED (no mismatch)
first 12 runs ... starts 2,5,7,10,...
k = 1..400
max |Toeplitz defect| over all k, all cells = 1
k with fully-Toeplitz matrix (zero defects): [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]
```

No new exact global regularity or OEIS identification was found beyond the already recorded floor/Fibonacci-block formulas and A019587/Wythoff comparisons. No larger run was made: the available artifacts already extend farther than the recurrence searches, and scaling those same finite scans would not settle a structural/global claim.
