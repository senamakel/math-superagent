# Final requested sequence audit — 2026-08-18

I read the existing `code/out/pattern_hunt` reports/index and all compact integer-token files under `code/out`, then ran:

```sh
python code/pattern_hunt/final_new_sequence_audit.py
python code/pattern_hunt/check_run_sequence_exact.py
```

The first program tested exact rational homogeneous recurrences of orders 1–12 and the already-recorded structural formulas. The second parsed the specially formatted run-start file and checked its displayed long start sequence with integer arithmetic. Output:

```text
starts=60 first_bad=none
gaps= {2: 22, 3: 37}
```

The file itself records the full check `Wythoff (A): OK, all j to 1146`; the new parser independently checked the displayed 60-term prefix.

## New exact findings

**NOTHING FURTHER.** No genuinely new exact regularity beyond the already recorded findings was found.

The fresh audit reproduced known finite results: `counts(k)=k+1` (`k=1..400`), `c1(k)=1+floor(k/phi^2)` (`k=1..400`), and `Lmin(k)=k+NextFib_strict(k)-1` (`k=1..400`). It found no exact homogeneous recurrence of order ≤12 for `c1`, `Lmin`, exact Ψ, Ψ residues, extension columns, `d_j`, or Toeplitz defects. The trivial order-2 recurrence for `counts` is merely the affine identity and is not new.

Existing candidate attacks remain as recorded: Ψ mod 1000 and mod 8 fail at `k=2`; the general Toeplitz conjecture fails at `k=3`; the proposed Fibonacci-additive `d_j` law fails at `j=3`; decimal-length and leading-block conjectures fail at `k=24` and `k=138`.

No larger run was made: the supplied ranges already had exact recurrence searches and independent formula checks, while extending the same bounded tests would add evidence but no new structural conclusion.
