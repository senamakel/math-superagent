# Follow-up sequence audit (2026-08-18)

## Prior reports read

Read `sequence_audit_report.md`, `direct_sequence_hunt_report.md`, `sequence_analysis_report.md`, `final_targeted_investigation.md`, `adopted_diagonal_closure_attack_2026-08-18.md`, and `fib_block_state_attack_report.md` before computing. Those reports already classify the c1/Lmin laws, Toeplitz Fibonacci-boundary zeros, low-order recurrence failures, and the three-moment/block-summary obstruction.

## Exact computation

Ran:

```text
python code/pattern_hunt/fresh_sequence_tool_audit.py
```

This reads the current exact artifact rows, tests rational homogeneous recurrences of orders 1--12, and computes a prime-field Berlekamp--Massey diagnostic. It is finite evidence only; it does not extrapolate to `10^18`.

The run used 400 terms for `c1`, `Lmin`, Toeplitz defect, and `Psi mod M`; 153 run-gap terms and 154 run-start terms. Results:

- `c1(k)=1+floor(k(3-sqrt(5))/2)`: no falsifier in 1..400; no exact recurrence of order <=12; BM complexity 232.
- `Lmin(k)=k+NextFib_strict(k)-1`: no falsifier in 1..400; no exact recurrence of order <=12; BM complexity 200.
- Toeplitz zero set is `[1,2,4,7,12,20,33,54,88,143,232,376]`; universal zero fails first at `(k,defect)=(3,2)`; no exact recurrence <=12.
- Run gaps after the initial marker are exactly `{2,3}` over all 152 checked gaps; no exact recurrence <=12; BM complexity 88. This is already recorded, not new.
- Run starts likewise show no exact recurrence <=12 (BM complexity 89); no new exploitable law.
- `Psi mod 100 = c1 mod 100` is falsified at `k=5`; `Psi mod 1000 = c1 mod 1000` is falsified at `k=2`.
- `Psi mod M` has no exact recurrence of order <=12; BM complexity 200 on 400 terms.

## Audit conclusion

No new exact regularity survived. Every surviving finite pattern is already recorded and does not supply the missing fixed-dimensional joint-intercept/Fibonacci-block aggregation. The new checks either re-confirm settled laws or give negative falsifiers. No larger run was made because it would only extend already-concluded finite scans and would not settle the structural gap.

**NOTHING FURTHER.**
