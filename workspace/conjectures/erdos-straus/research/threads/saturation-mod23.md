# Saturation of modulus 23

**Deferred by directive 7.** The operator has directed: "Do NOT generate more
families at new primes." The saturation question is being resolved at M=11
first — it is the smallest modulus, and if it cannot be saturated, no modulus
can. If M=11 saturates, M=23 is the natural next target; if M=11 has an
obstruction, the method is bounded away from 100% and the run must change
mechanism.

```thread
question: Can the Salez seven-equation generator produce polynomial identity
  families for all 23 residue classes t mod 23 (where t = (n−1)/840,
  n = 840·23·k + (840s+1) with s = t)?
status: deferred (directive 7 — resolve M=11 first)
rests-on: subprogression-families-verified-and-coverage,
  subprogression-coverage-positive-limit,
  seven-equations-complete
next: wait for M=11 result. If M=11 saturates: run search_subprogression.py
  focused on a = 840×23 = 19320, enumerating b ≡ 1 (mod 840) that are
  QNR mod 19320. If M=11 has an obstruction: this thread is moot — the method
  has a hard ceiling.
```

## Current state

- Modulus 23: 9/23 residues covered: [5, 9, 12, 13, 15, 17, 18, 19, 20]
- Missing 14 residues: [0, 1, 2, 3, 4, 6, 7, 8, 10, 11, 14, 16, 21, 22]
- Schinzel analysis: only 11 residues are QNR-allowed, of which 9 are
  realised — gap is [3, 8]. The other 12 are QR-blocked or non-unit.

## Reference

- Salez seven equations: `research/sources/salez-seven-modular-equations.full.md`
- Coverage summary: `code/out/coverage_update_extended.md`