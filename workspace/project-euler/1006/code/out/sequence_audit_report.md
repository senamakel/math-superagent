# PE1006 sequence audit report (2026-08-18)

## Scope and method

I inspected the existing result artifacts and ledgers before running anything. The governing objects remain Fibonacci-word factor sequences and their exact derived integer summaries; prior ledgers already record the Sturmian/mechanical-word theory and the unresolved fixed-dimensional aggregation. I therefore audited only sequences not already conclusively classified, using exact integer comparisons and exact symbolic recurrence fitting on the stored finite rows. No target-bound brute force or extrapolation was performed.

The reproducible command is:

```text
python code/out/sequence_audit_workflow.py
```

Its output is an evidence check for the finite sequence claims below, not a proof of the unbounded statements.

## Exact output

```text
c1 floor law first bad: None
Lmin formula first bad: None
Toeplitz zero indices: [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]
Psi mod100=c1 first bad: (5, 2250400)
Psi mod1000=c1 first bad: (2, 101)
c1 exact recurrence <=12: []
Lmin exact recurrence <=12: []
Psi residues exact recurrence <=12: []
Toeplitz defect exact recurrence <=12: []
```

## Comparison with memory

- `c1(k)=1+floor(k(3-sqrt(5))/2)` was already recorded and is reproduced with no falsifier over all stored `k=1..400`; it is not new.
- `Lmin(k)=k+NextFib_strict(k)-1` was already recorded and is reproduced with no falsifier over all stored `k=1..400`; it is not new.
- Toeplitz zero indices are already recorded as the Fibonacci-boundary list `F_n-1` through 400; the audit reproduces exactly that list and the first failure of universal zero is `(k, defect)=(3,2)`; not new.
- The tempting congruence `Psi(k) ≡ c1(k) (mod 100)` is **not** a regularity: the exact first counterexample is `k=5`, where `Psi(5) mod 100 = 0` while `c1(5) mod 100 = 2`. Modulo 1000 already fails at `k=2`.
- No exact homogeneous rational recurrence of order at most 12 was found for any of `c1`, `Lmin`, `Psi mod M`, or the Toeplitz-defect sequence. This confirms the prior negative recurrence audit and yields no new recurrence.

## Verdict

No genuinely new exact regularity was identified. The only surviving laws are already present in memory/ledgers, and the new checks either reproduce them or falsify plausible congruence/recurrence candidates. The missing O(log k) joint-intercept aggregation remains unresolved.

**NOTHING FURTHER.**
