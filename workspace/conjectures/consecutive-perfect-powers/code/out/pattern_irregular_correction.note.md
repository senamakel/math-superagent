# Irregularity correction: 2903 and 911 are REGULAR, not irregular

## The contradiction found

Claim `dw-pairs-regular-minor-torsion-free` (note `code/out/pattern_findings.note.md`)
and the earlier `pattern_dw_structure.py` output asserted:

- 2903 is irregular, `2903 | B_2386`
- 911 is irregular, `911 | B_60`

## The refutation (exact arithmetic)

`code/pattern_irregular_conflict.py` computes the exact Bernoulli numerators:
`num(B_60) % 911 = 859 != 0`, `num(B_2386) % 2903 = 1170 != 0`. Both are
non-zero, so **911 and 2903 are regular** (index of irregularity 0).

`code/pattern_irregular_locbug.py` locates the bug: the old
`OLD_bernoulli_even_modp` recurrence (a modular computation of Bernoulli-like
terms mod p) reported `0` at those indices where the exact integer numerator is
nonzero. A modular Bernoulli recurrence is NOT a valid irregularity test.

## Corroboration (all exact, mutually agreeing)

| script | result |
| --- | --- |
| `pattern_irregular_conflict.py` | num(B_60)%911=859, num(B_2386)%2903=1170 (both nonzero) |
| `pattern_irregular_locbug.py` | OLD indices=[60]/[2386] vs exact indices=[] |
| `pattern_irregular_cross.py` | 4871,18787,83,911,2903 all regular (rec1=rec2=[]) |
| `pattern_irregular_via3.py` | 83,911,2903,4871,18787 all regular |
| `pattern_irregular_decide.py` | 911,2903 regular (AGREE=True) |

Outputs: `code/out/pattern_irregular_conflict.captured.txt`,
`pattern_irregular_locbug.captured.txt`, `pattern_irregular_cross.captured.txt`,
`pattern_irregular_via3.captured.txt`, `pattern_irregular_decide.captured.txt`,
`pattern_irregular_dw.captured.txt`, `pattern_irregular_dw2.captured.txt`,
`pattern_irregular83.captured.txt`.

## Consequence

All five double-Wieferich primes {83, 2903, 4871, 911, 18787} are **regular**:
none divides an even Bernoulli numerator, so by Kummer's criterion none divides
h^-(Q(ζ_p)) of its own field. This **strengthens** the ledger's finding — a
descent whose obstruction is the minus-class-group torsion of the exponent prime
cannot be the mechanism at ANY of the small double-Wieferich pairs, not just at
(83,4871).

```claim
id: dw-pairs-all-regular-corrected
statement: >
  All five double-Wieferich primes {83, 2903, 4871, 911, 18787} are regular:
  exact Bernoulli-numerator arithmetic gives num(B_2386)%2903=1170!=0 and
  num(B_60)%911=859!=0, so neither 2903 nor 911 divides an even Bernoulli
  numerator (and 83, 4871, 18787 are regular by the same exact test). By
  Kummer's criterion none divides its own field's minus class number. This
  corrects the earlier claim that 2903|B_2386 and 911|B_60, which came from a
  buggy modular Bernoulli recurrence.
hypotheses: p an odd prime (one of the double-Wieferich primes); "regular"
  means p divides no numerator of B_2,...,B_{p-3}.
holds-here: yes — the double-Wieferich pairs are exactly where the both-odd
  descent must run, so their regularity bounds the mechanism.
status: checked — exact integer arithmetic on sympy.bernoulli().p, five
  independent agreeing scripts.
anchor: code/out/pattern_irregular_conflict.captured.txt; code/out/pattern_irregular_correction.note.md
bearing: removes a false irregularity label from the ledger; the minus-class-
  group torsion obstruction is absent at all small double-Wieferich pairs.
contradicts: dw-pairs-regular-minor-torsion-free (as first filed, in its 2903/911 clause)
```
