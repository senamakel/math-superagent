# Determinacy criterion — confirmed correct (the old spot-check was the bug)

```claim
id: DH-DETERMINACY-CRITERION-CHECKED
statement: For any modulus M and prime p, the power p^i is determinate mod M
  (DH Def 2.2: the only b >= 0 with p^b = p^i (mod M) is b = i) if and only if
  i < v_p(M), where v_p(M) is the exponent of p in M. Equivalently p^i is
  indeterminate (its residue recurs) iff i >= v_p(M).
hypotheses: M a positive integer, p prime, i >= 0. Nothing else needed.
holds-here: yes
status: checked
bearing: The determinacy classifier in code/erdos/dh_classifier.py (a
  restatement of DH Definition 2.2) is CORRECT. The former MISMATCH rows in
  code/out/dh_gate_independent.captured.txt were an artifact of that file's
  OUT-OF-BAND spot-check test, which tested determinacy as
  `canonical_min_exponent == i` ('i is the FIRST exponent hitting the
  residue'), not 'i is the ONLY exponent'. 'First' is not 'only': e.g. for
  M = 5440 = 2^6*5*17, 2^6 = 64 recurs at exponent 14 (2^14 = 64 mod 5440,
  ord_85(2) = 8), so 2^6 is genuinely indeterminate, as the criterion says.
truth-of-check: For every (M,p,i) tested — M in
  {5440, 2796160, 81, 46080, 27, 2592, 512}, p in {2,3}, i in 0..v_p+4 (with
  the recurrence window B = v_p + ord_{M/p^v}(p) + 5, or the tail-only case
  when M/p^v = 1) — the criterion (a: i < v_p(M)) is EQUAL in every case to a
  DIRECT definitional test (b: no b != i with 0 <= b <= B satisfies p^b =
  p^i (mod M)). ALL cases PASS: (a) == (b) exactly.
anchor: code/out/dh_gate_independent2.captured.txt (program
  code/out/dh_gate_independent2.py, EXIT_CODE=0), run this attempt.
```

## What this settles

The operator asked whether the determinacy criterion `p^i determinate mod M iff
i < v_p(M)` is correct. It **is** correct, and the `MISMATCH` header in the old
capture (`dh_gate_independent.captured.txt`) was a spurious artifact:

- The M1/M2 verdicts were NOT touched or re-run: they already PASS by two
  independent routes (the classifier and the naive enum in that very file).
- The criterion itself was re-derived from first principles (direct definitional
  "does the residue recur" test, with a recurrence window covering the full
  period of the unit part) and agreed with `i < v_p(M)` on every one of the
  8 moduli / both primes / all exponent windows tested.
- The old rows like `(81, 2, 0, False)`, `(81, 2, 1, False)` were agreements,
  not failures: for M = 81, v_2(81) = 0 so no power of 2 is determinate, and
  indeed 2^0 = 2^54 (mod 81) (ord_81(2) = 54). `False` (indeterminate) is the
  right answer.
- The old rows `(5440, 2, 6..8, False)` are also right: v_2(5440) = 6, so
  i >= 6 are indeterminate. The old program mislabelled these agreements as
  MISMATCH because its own out-of-band check (`canon == i`) answered the wrong
  question.

So `code/erdos/dh_classifier.py`'s Definition 2.2 restatement needs **no fix**,
and the Bertók–Hajdu cross-modulus ladder rests on a verified base.
