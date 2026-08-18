# Independent exact finite-range hunt: non-Psi sequences

## Method and scope

I read the stored artifacts and reran independent exact-integer programs. The
new script `code/pattern_hunt/independent_nonpsi_hunt.py` directly extracts
factors from a Fibonacci-word prefix and checks c1 and first-occurrence Lmin
through k=1000. Existing scripts were rerun for c1 through 400, Lmin through
2583/6764, and the extension recurrence through 400. These are finite checks;
all statements below are conjectures unless explicitly described as a direct
finite identity in the output.

## Exact regularities surviving the supplied terms

1. **Leading-1 factor count (conjecture).**
   `c1(k) = 1 + floor(k/phi^2)`, where `phi=(1+sqrt(5))/2`, equivalently
   `1 + floor(k*(3-sqrt(5))/2)`. It survived direct factor extraction for
   k=1..1000 in the new run and the existing independent routes for k=1..400.
   The first 30 exact terms are
   `1,1,2,2,2,3,3,4,4,4,5,5,5,6,6,7,7,7,8,8,9,9,9,10,10,10,11,11,12,12`.
   No counterexample was found in the checked range. The complementary count
   is exactly `k+1-c1(k)` over the same range.

2. **Least prefix length (conjecture).**
   `Lmin(k) = k + F_{m+1} - 1` whenever `F_m <= k < F_{m+1}`, i.e.
   `Lmin(k)=k+NextFib_strict(k)-1`. Direct first-occurrence extraction found
   no counterexample for k=1..1000 in the new run; existing independent
   implementations found none for k=1..2583 and none for the complete range
   k=1..6764. Selected exact values include
   `(1,2),(2,4),(3,7),(5,12),(8,20),(13,33),(21,54),(34,88),
   (55,143),(89,232),(144,376),(233,609),(377,986),(610,1596),
   (987,2583),(1597,4180),(2583,5166),(4181,10945),(6764,13528)`.
   A standalone independent route also checked all Fibonacci-boundary
   neighbours in its supplied range. No counterexample was found.

3. **Right-extension recurrence (conjecture, exact modulo M).**
   For the stored definitions of `V(R_k)`, `S1(k)`, and `J(k)`, the exact
   recurrence
   `Psi(k+1)=100 Psi(k)+100 V(R_k)^2+20 S1(k)+J(k) (mod M)`
   holds for every k=1..400 in `check_ext_recurrence_400.py`. In the same
   range `J(k)` equals the number of length-(k+1) factors ending in `1`, and
   equals `c1(k+1)`. This is a checked finite regularity, not a proof for all k.

4. **V-run structure (conjecture).**
   In the stored run through K=3000, proper V-runs have starts
   `s_j=floor(j phi^2)` for j=1..1146 and all gaps are 2 or 3; the histogram
   is 437 gaps of 2 and 708 gaps of 3 (with the terminal bookkeeping entry
   reported separately). The run-value increment rule for S1,
   `S1(s_j+1)-S1(s_j)=d_j 10^{s_j}`, with S1 flat within a run, survived all
   1145 proper recorded runs, and the extracted d_j agrees with the stored
   A019587 comparison. This is only a finite conjecture. The direct sequence
   report also found all S1-runs contained in V-runs (2292/2292).

## Regularities explicitly falsified

- The general Toeplitz pair-correlation identity is false: the exact rerun gives
  a first nonzero defect at k=6 (8 of 25 cells); further defects occur at
  k=8,10,13,16,21. It happens to have zero defects at k=12 and k=20 in the
  checked output, so Fibonacci-boundary successes do not extend it globally.
- `Psi(k) mod 1000 = c1(k)` already fails at k=2 (`Psi(2)=101`, `c1(2)=1`).
- No constant-coefficient linear recurrence was found for the stored exact Psi
  prefix at orders 1..10; this is a negative finite search, not a theorem.
- The stored pattern hunt found no new recurrence for the non-Psi sequences
  beyond the floor/Fibonacci-block descriptions above.

## Reproducibility

Commands executed:

```text
python code/pattern_hunt/independent_nonpsi_hunt.py
python code/pattern_hunt/check_ext_recurrence_400.py
python code/pattern_hunt/verify_c1_formula.py
python code/pattern_hunt/verify_lmin_formula.py
```

The outputs cited above are the outputs of those commands, not floating-point
numerical evidence for exact equality: the independent checks use direct
factor sets, integer Fibonacci arithmetic, and exact prefix scans. The formula
notation involving phi is only a compact conjectural description of the exact
integer floor sequence.
