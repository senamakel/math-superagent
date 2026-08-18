# Independent Psi pattern test

I inspected `code/out/` and `code/pattern_hunt/`. Existing conclusions already rule out low-order scalar recurrences through order 10 (exact prefix) and 12 (residue prefix), and identify the genuine Wythoff/Fibonacci block structure of the right-special factor and `Lmin`; these are not claimed as new findings.

`code/pattern_hunt/independent_psi_patterns.py` parses stored exact terms (`psi_exact.txt`, k=1..25) and residues (`psi_residues.txt`, k=1..400), testing affine first differences, Fibonacci addition, decimal-shift scaling, repetition of first differences at Fibonacci boundaries, and constant-coefficient recurrences of orders 1..6. Exact integer arithmetic is used, with residues modulo 101001001.

Run:

```text
python code/pattern_hunt/independent_psi_patterns.py
```

Mechanical output:

- Exact affine first-difference rule: first falsifier k=3, Psi(3)=20302.
- Residue affine first-difference rule: first falsifier k=3, residue 20302.
- Exact Fibonacci addition Psi(k)=Psi(k-1)+Psi(k-2): first falsifier k=2, value 101.
- Residue Fibonacci addition: first falsifier k=2, residue 101.
- Exact decimal-shift Psi(k)=100 Psi(k-1): first falsifier k=2, value 101.
- Residue decimal-shift rule: first falsifier k=2, residue 101.
- Repeating first differences at Fibonacci boundaries: first falsifier k=3, both exact and residue tests.
- No constant-coefficient recurrence of order <=6 was identified from the stored exact or residue terms. The existing broader survey had already tested stronger bounds (<=10 and <=12 respectively).

The existing `survey_requested.py` rerun reports its fit-from-prefix procedure: order 1 first fits with coefficient 101 but fails at k=3 for both exact and residue Psi; orders 2..7 fail at k=5,7,9,11,13,15. This is consistent with, but not stronger than, the established negative result.

## Conclusion

No new recurrence, scalar Fibonacci rule, or fixed Fibonacci-block repetition survived. The only strong regularities remain those already recorded: right-special-factor Wythoff run starts/gaps, the mod-100 identity, and the `Lmin` Fibonacci-block formula. No new exploitable structure or stronger pattern was found.