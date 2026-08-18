# Requested exact-sequence inspection (2026-08-18)

## Method
`code/pattern_hunt/inspect_requested_sequences.py` parsed exact integer rows from `psi_exact.txt`, `c1_terms.txt`, `ext_recurrence.txt`, and raw binary strings from `vr_runvals.txt`. It tested exact homogeneous constant-coefficient recurrences of orders 1--12 using SymPy, Berlekamp--Massey where the modulus was usable, and the established exact c1 floor formula. This is a bounded diagnostic; it does not evaluate Euler 1006 at full size.

The program was executed successfully after fixing BM's non-unit-modulus edge case. Its output is the numerical evidence below.

## Exact extracted sequences

* `psi_exact.txt`, k=1..25 begins:
  `1, 101, 20302, 2042402, 204252402, 30445654403, 3054587854503, 407470828064704, 40849095449084804, 4085011557551094804, 508703259827952296805, 50970528087268072496905`.
* `c1_terms.txt`, k=1..12:
  `1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5`.
* Final numeric column of `ext_recurrence.txt`, k=1..12:
  `0, 10, 110, 110, 20210, 120210, 1130220, 31130220, 31130220, 3041140320, 23041140320, 23041140320`.
* `vr_runvals.txt` has 154 binary strings; first eight are `0, 10, 10010, 1010010, 1001010010, 1001001010010, 101001001010010, 100101001001010010`.

## Conjecture attacks and falsifiers

* Scalar exact homogeneous linear recurrence of order 1--12 for `psi_exact`: **none found**, so no surviving recurrence and hence no falsifying term. This is only a finite-prefix rejection, not a proof of no recurrence globally.
* Scalar exact homogeneous linear recurrence of order 1--12 for `c1`: **none found**. The actual floor/Sturmian formula `c1(k)=1+floor(k(3-sqrt(5))/2)` survives all 400 stored terms; **first falsifier: none through k=400**.
* Scalar exact homogeneous linear recurrence of order 1--12 for the final `ext_recurrence` column: **none found** through 40 terms.
* BM complexity over modulus 101001001: `psi_exact=13` on 25 terms, `c1=232` on 400 terms, `ext_final=20` on 40 terms. BM over 100 and 1000 was not applicable because the algorithm encountered non-invertible discrepancies; this is an algorithm/modulus limitation, not a sequence conclusion.
* No scalar recurrence conjecture was asserted for `vr_runvals`; its extracted prefix is visibly a family of Fibonacci-word binary blocks rather than decimal integers. No falsifier is applicable.

## OEIS lookup

The local source library identifies the Fibonacci word as OEIS A003849. No local exact OEIS match is established for the consecutive raw `Psi` values; the report does **not** claim an external OEIS hit. Existing notes already record that the raw Psi prefix was not catalogued.

## Additional-term attack

The available stored extensions are already beyond the prefixes that suggested the conjectures: c1 has 400 terms, ext-recurrence has 40, vr-runvals has 154, and Psi has 25 exact terms. The recurrence searches were rerun on those full stored ranges. No proposed scalar recurrence survived; the c1 floor formula survived with no falsifier through k=400. Generating further Psi exact terms would be a larger finite evaluator run and would not settle the structural O(log) gap, so it was deliberately not attempted.
