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

- [x] **DIRECTIVE 13 (priority 1): DONE 2026-08.** Ran
  `timeout 540 python3 code/equality_case_verify.py 2>&1 | tee
  code/out/equality_case_verify_FIXED.captured.txt; echo EXIT_CODE=$?` ->
  `EXIT_CODE=0`, 4/4 points PASS on fresh exact-Fraction arithmetic.
  M(28)=1.997752859598546538 < T(28)=1.999999993 and
  M(29)=2.004964963784822807 > T(29): boundary confirmed at 28, no
  exclusion at 29. Claim `budget-equality-case-impossible` anchor updated
  with the FIXED capture as primary anchor (directive 13). Both
  `equality_case_verify.captured.txt` (previous run) and the FIXED capture
  show the same boundary; the operator-requested filename is now on disk.

- [ ] **DIRECTIVE 13 (priority 2):** Attack the biquadratic-reciprocity question
  for the Φ_{4p}(2) thread. For which odd primes p is 2 a fourth power modulo
  a primitive divisor r of Φ_{4p}(2)? The condition r ≡ 1 (mod 4p) already
  forces r ≡ 1 (mod 4), so the biquadratic character (2/r)_4 is defined.
  Gauss determines it by the representation r = a² + b². The supplementary
  law [2/π]_4 for the Gaussian prime π | r gives (2/r)_4 = +1 iff r ≡ 1
  (mod 16). The product identity Π_{π^e || 2^p+i} (2/π)_4^e = (2/(2^p+i))_4
  evaluated via the supplementary law expresses how many divisors of Φ_{4p}(2)
  are ≡ 1 (mod 16) as a function of p mod 16 alone — this is the divisor-
  transference formula. State whether this constrains which r can be 3-Higgs,
  and if not, say so and close the approach. The existing `heven_gauss.py`
  already computes the per-factor characters through p=61; the next step is
  the closed-form evaluation of (2/(2^p+i))_4 by quartic reciprocity on the
  Gaussian integer 2^p + i, comparing it against the per-factor product.

- [x] **Executed (2026-08, this run):** Gaussian factorization of `2^p + i`
  and quartic-character table for every odd prime `p ≤ 61` —
  `code/heven_gauss.py` → `code/out/heven_gauss_61.captured.txt`
  (`EXIT_CODE=0`, all checks C1–C7 pass, 71 divisor rows, nothing left
  unfactored). Proved by exact computation for this range: (F1) every prime
  divisor `r | Φ_{4p}(2)` is primitive, `ord_r(2) = 4p`, `r ≡ 1 (mod 4p)`,
  with the single exception `r = 5 | Φ_20(2)` at `p = 5` (LTE
  `v_5(2^{2p}+1) = 1 + v_5(p)`); (F2) `(2/r)_4 = +1 ⟺ r ≡ 1 (mod 16)` for
  all 71 divisor rows. 12 heads (`r ≡ 1 (mod 16)`, necessarily non-3-Higgs)
  found, independently certified by `code/heven_heads_verify.py` →
  `code/out/heven_heads_verify.captured.txt` (`ALL HEADS CERTIFIED 12/12`).
  Empirical (exact, not a proof): for the 16 3-Higgs primes `p ≤ 61`,
  `2p ∈ H_even` (the seven Thm-8 members {6,10,26,46,62,82,122}) iff
  `Φ_{4p}(2)` has no prime divisor `≡ 1 mod 16` — all seven members have
  all-3-Higgs divisors and zero heads; all nine excluded 3-Higgs `p`
  (7,11,19,29,37,43,47,53,59) carry a head witnessing `2p ∉ H_even`.
  Also first-executed `code/higgs/check_a057447.py`
  (`code/out/higgs_a057447.captured.txt`): literal A057447 recursion
  reproduces all 58 OEIS DATA terms; all five witnesses pass
  `σ*(n) = 2n`; every witness prime divisor is 3-Higgs.

- [ ] Next step on the chosen line: extend the same divisor-level table to
  larger `p` (partial-factor if needed — a head needs only one found
  divisor) and seek a congruence class of `p mod 8` where a head is forced;
  the character-distribution table (p mod 8 × Aurifeuillean half) is already
  in the capture.

## Standing

- [ ] Do not fetch any new sources while FRONTIER.md unworked count > 100. The Maciejewski paper (93 KB) is already on disk at `research/sources/maciejewski-bounded-box-subbarao-warren.full.md`. Surveys (Guy B3, Handbook, Goto 2007) are already in the library.
- [ ] The [74:08] "progress no" verdict came from a judge that TIMED OUT. It is not an assessment. H_even is the correct branch.
- [ ] Budget: 31.17 remaining of 75 daily cap (~19 hours). Spend on depth, not breadth — the directive says close something, not start something new.

## Active approaches

The only approach with a program and a verified claim is `biquadratic-character-divisors` (adopted). It attacks Conjecture 29 via quartic reciprocity in Z[i] on the Gaussian factor 2^p + i.

## Don't

- Do not write more approach files. 7 approaches against 4 checked and 1 proved is already lopsided.
- Do not re-derive the 2-adic budget identity, the parity theorem, or the lower bound on a.
- Do not search for a sixth unitary perfect number.
- Do not fetch further sources.
