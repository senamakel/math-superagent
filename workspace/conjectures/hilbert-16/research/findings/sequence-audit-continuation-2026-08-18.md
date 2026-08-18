# Provisional: Bautin sequence audit continuation (2026-08-18)

Pattern pass. Every sequence finding on disk audited; sequence tools run on
the previously un-tool-checked sequences (denominators, valuations).

## Sequences and exact verdicts

- S_k family (S_k, S_{3j}, ceil(S_k)): fully derived from the Buzzi–Novaes/Li
  closed form; recurrences verified to large index; OEIS misses recorded.
  Nothing new to conjecture.
- a_d = [4, 30, 97, 236, 485, 890, 1505] (5-param Bautin focal monomial
  counts, d=4..16) and c(h) complements [7, 10, 16, 23, 31, 40, 50]:
  no low-degree polynomial, no constant-coefficient recurrence order<=6,
  OEIS miss — all documented.
- D_d = [8, 192, 18432, 1105920, 22295347200, 37456183296000]:
  analyze_sequence: no polynomial structure; leading ratios
  [24, 96, 60, 20160, 1680] irregular. find_linear_recurrence returned an
  order-3 rational-coefficient fit (coeffs 3427080/2093, 3207072000/2093,
  -84576384000/2093) — this is the DOCUMENTED exactly-determined
  false-positive trap (6 terms, 3 free coefficients, absurd coefficients,
  no verification beyond the given terms). NOT reported as a regularity.
- v2 = [3, 6, 11, 13, 19, 23] (irregular, no affine law), v3 = [0,1,2,3,5,6]
  (threshold observation only), v5, v7 (2-4 terms): not laws, per the
  provisional denoms file. Nothing to report.
- a6 = [6, 56, 220, 628, 1481], c6 = [9, 14, 22, 31, 41]: documented, no
  structure.

## The two living conjectures (both previously delegated, NEVER executed)

No agent-run-23/24 results exist anywhere on disk; both falsifier terms were
never computed.

1. 5-param complement conjecture c(h) = (h^2+14h+8)/8 for h>=4 even (h=2
   exceptional), equivalent a_d = (C(h+4,4) - c(h))/2 for d>=6.
   FALSIFIER: a_18 =? 2392 (h=16, c=61).
   COMMISSIONED: agent-run-38 runs `membership_d18.py 18`, nohup to
   code/out/.d18_final2.tmp.txt. Also settles L18 in <L4,L6,L8> (extends the
   Bautin-trick membership chain from d=16 to d=18).
2. 6-param complement conjecture c6(h) = (h^2+22h+8)/8 (h=2 exceptional).
   FALSIFIERS: a6_14 =? 3068 (h=12, c6=52); D6_14 =? 37456183296000
   (denominator identity D5 = D6).
   COMMISSIONED: agent-run-39 runs `focal_counts_6coeff.py --resume
   --max-degree 14 --deadline-min 120` (checkpoint at degree 12).

Both runs use exact sympy rational arithmetic, no floats. Results to be
recorded verbatim from captures.

## Cofactor monomial counts (from focal_denoms.captured.txt)

L10: q1,q2,q3 = [210, 70, 15], total 295; L12: [489, 204, 55], total 748;
L14: [969, 463, 133], total 1565. Deficits vs full degree-dimension:
q1/q2 = (0,0), (6,6), (32,32); q3 = (0, 15, 77). 3 data points only —
Groebner-reduction quotients are order-dependent (not canonical objects), so
no conjecture is warranted.

## Tool caveat (re-confirmed this pass)

find_linear_recurrence is unreliable on fast-growing/large-coefficient
sequences (documented false positive AND false negative in
sequence-tool-validation-sk.md). The D_d order-3 fit is another false
positive of the same kind.
