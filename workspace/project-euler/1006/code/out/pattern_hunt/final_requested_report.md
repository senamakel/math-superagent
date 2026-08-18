# Pattern-hunt report (exact rerun)

Commands run:

```sh
python code/pattern_hunt/survey_sequences.py
python code/pattern_hunt/analyze_existing_sequences.py
python code/pattern_hunt/check_c1_weight.py
python code/pattern_hunt/check_ext_recurrence_400.py
python code/pattern_hunt/check_dj_structure.py
python code/pattern_hunt/check_dj_oeis.py
python code/pattern_hunt/check_runsum_increment.py
python code/pattern_hunt/check_small_moduli.py
python code/pattern_hunt/check_psi_digitlen.py
python code/pattern_hunt/sequence_report.py
```

`check_wythoff_gaps2.py` and `check_psi_leading_digits.py` were also attempted; both have unrelated Python-output issues in their existing scripts (`mpf` format specifier and Python's 4300-digit conversion limit respectively). Their exact stored outputs and independent exact checks below remain usable.

## Exact regularities

- `c1(k) = 1 + floor(k(3-sqrt(5))/2) = 1+floor(k/phi^2)` for `k=1..400`; no falsifier. The weight distribution is exactly `{floor(k/phi^2), ceil(k/phi^2)}` for `k=1..100`.
- Factor counts are exactly `k+1` for `k=1..400`; no falsifier.
- `Lmin(k) = k + NextFib_strict(k) - 1` for `k=1..400`; no falsifier.
- The right-extension recurrence
  `Psi(k+1)=100 Psi(k)+100 V(R_k)^2+20 S1(k)+J(k) (mod 101001001)`
  holds for `k=1..400`. Also `J(k)=c1(k+1)` throughout that range.
- For 1145 proper recorded V-runs, `S1(s_j+1)-S1(s_j)=d_j*10^{s_j}`, and `S1` is flat on the remainder of each run. The extracted `d_j` agrees with the existing A019587 comparison for all `j=1..1145`; no falsifier in the stored range.
- V-run starts satisfy `s_j=floor(j phi^2)` for the recorded `j=1..1146`; all recorded gaps are in `{2,3}`. This is an exact finite verification, not a claim about asymptotic frequencies.
- No constant-coefficient linear recurrence was found for exact `psi_exact` at orders 1..10 on its 25-term prefix.

## First falsifiers

- `Psi(k) mod 100 = c1(k)`: **none through k=400 in the stored residue table**. Note: the first run of `survey_sequences.py` printed a false positive because it compared the unreduced residue to a mod-100 value; `sequence_report.py` performs the correct comparison and prints no falsifier.
- `Psi(k) mod 1000 = c1(k)`: first falsifier `k=2`: `Psi(2)=101`, while `c1(2)=1`.
- `len(Psi(k))=2k-1`: first falsifier `k=24`; later excess transitions are `k=257` and `k=2569` in the checked range.
- `floor(Psi(k)/10^(2k-2))=c1(k)`: first falsifier `k=138`.
- The general Toeplitz pair-correlation conjecture is false; `check_ext_recurrence_400.py` reports a first nonzero defect at `k=6` (though some Fibonacci-boundary lengths have zero defect).

All claims above are computational finite-range results, except where explicitly marked as identities already established by the workspace's Sturmian theory. No published-answer search was used.
