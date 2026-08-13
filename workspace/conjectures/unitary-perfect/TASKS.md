# Tasks

## Completed

- [x] Library audit + scholar pass 2026-08-14 (see research/notes/scholar-pass-library-audit.md)
- [x] `budget-equality-case-impossible` verified from captured output `code/out/equality_case_verify.captured.txt`:
  (1) a=1 max product = 4/3 exactly, {5,9} is odd part of 90;
  (2) 2^8+1=257 prime, forced when a=8;
  (3) 9=3^2 and 49=7^2 admissible, 3 and 7 are not;
  (4) exclusion runs 2 ≤ a ≤ 28, stops at 29. Correct M values: M(28)=1.997752860 < T(28), M(29)=2.004964964 > T(29).
  BUG-FIX (directive 11): admissible_sizes() had a slice-then-sort bug (missed 37,41,53; wrongly included 121,361,529). Fixed to sort-then-slice over BOUND=800 with safety assertion. The 28-boundary survives the fix; a=29 was never recorded as excluded in any task or thread. All four checks confirmed.
  Thread `a-ge-8-bound` resolved: equality case impossible for 2 ≤ a ≤ 28.

- [x] **Independent reproduction (operator directives 4/7/8/9/10, attempt 3).** Reran `code/equality_case.py` verbatim -> `code/out/equality_case_reproduced.captured.txt` (3728 bytes, EXIT_CODE=0) and wrote a from-scratch exact-Fraction verifier `code/equality_case_verify.py` -> `code/out/equality_case_verify.captured.txt` (5015 bytes, EXIT_CODE=0). All four points PASS on fresh arithmetic: (1) T(1) = Fraction(4,3) exactly, (1+1/5)(1+1/9) = 4/3 exactly, {5,9} = odd part of 90; (2) 257 prime, M(8) = 4235328000/2498670421 approx 1.6950 < 512/257 approx 1.9922; (3) 3,7 = 3 mod 4 not admissible, 9 = 3^2 and 49 = 7^2 admissible; (4) M(a) < T(a) exactly for all 2 <= a <= 28, M(29) >= T(29). Claim `budget-equality-case-impossible` anchor updated with both captures; status `checked` on this run's own evidence. First verifier draft had a real bug (admissible list in prime-count order, missed 37,41 for 121,361); fixed by generating sizes for all odd primes, sorting, truncating, asserting safety. Zero-byte captures cleared and confirmed: `sieve_pass_1e8` and `sieve_timing_1e6` now carry tombstones (76, 94 bytes).

## Next

- [ ] **DIRECTIVE 12:** Run the fixed equality-case verifier and record the capture.
  ```bash
  timeout 540 python3 code/equality_case_verify.py 2>&1 | tee code/out/equality_case_verify_FIXED.captured.txt; echo EXIT_CODE=$?
  ```
  Confirm M(28) < T(28) and M(29) >= T(29), then update claim
  `budget-equality-case-impossible` anchor to include this capture. Record the
  boundary as 28, no exclusion at 29 or beyond. Move checked from 4 to 5.

- [ ] Attack H_even via the divisor-level problem for Φ_{4p}(2).

## Standing

- [ ] Do not fetch any new sources while FRONTIER.md unworked count > 100. The Maciejewski paper (93 KB) is already on disk at `research/sources/maciejewski-bounded-box-subbarao-warren.full.md`. Surveys (Guy B3, Handbook, Goto 2007) are already in the library.
- [ ] The [74:08] "progress no" verdict came from a judge that TIMED OUT. It is not an assessment. H_even is the correct branch.

## Active approaches

The only approach with a program and a verified claim is `biquadratic-character-divisors` (adopted). It attacks Conjecture 29 via quartic reciprocity in Z[i] on the Gaussian factor 2^p + i.

## Don't

- Do not write more approach files. 7 approaches against 4 checked and 1 proved is already lopsided.
- Do not re-derive the 2-adic budget identity, the parity theorem, or the lower bound on a.
- Do not search for a sixth unitary perfect number.
- Do not fetch further sources.
