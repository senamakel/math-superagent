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

- [ ] **PRIORITY 1 (directive 16): Mark the four "discharged" structural gaps honestly.**
  `research/backward/heven-finiteness-via-mod16.md` now correctly shows 6 open gaps:
  the four Maciejewski structural results (`G-prime-case-reduction`,
  `G-mod4-restriction`, `G-higgs-cubefree-structure`, `G-conditional-finiteness`)
  are **conditional-on-paper** — asserted/catalogued, not independently proved or
  checked here — plus the two genuinely open (H1) and (H2). The reduction is
  **conditional**: finiteness of H_even reduces to (H1)+(H2) *given* the
  Maciejewski structural results. That is a real result and is what the skeleton
  now states. The parallel `heven-finiteness-via-c29-second-moment` skeleton
  correctly shows 4 genuinely open gaps (no structural borrows masked as
  discharged). Both skeletons are now honest.

- [ ] Next: pick one gap with a concrete `next` step and attack it. The cheapest
  is `C29-L2-character-orthogonality` (elementary character theory on C₄ — a
  theorem_prover can close it in one go). Then `C29-L3-first-moment-quartic` has
  a clear symbolic_math task (closed-form evaluation of `(2/(2^p+i))_4` per
  directive 14's already-computed constant +1, now verify the product identity
  side numerically). The heaviest is `C29-L4-second-moment-bound` (requires
  Aurifeuillean split + variance bound) or `C29-omega-growth` (Stewart/Hong
  radical lower bound → ω unbounded).

- [x] **DIRECTIVE 14: DONE — CLOSED-no-constraint.** `(2/(2^p+i))_4 = +1`
  identically for all odd primes p; the global quartic character of 2 carries
  NO constraint beyond the per-divisor mod-16 test. Definitively closed.

## Standing

- [ ] Do not fetch any new sources while FRONTIER.md unworked count > 100. The Maciejewski paper (93 KB) is already on disk at `research/sources/maciejewski-bounded-box-subbarao-warren.full.md`. Surveys (Guy B3, Handbook, Goto 2007) are already in the library.
- [ ] The [74:08] "progress no" verdict came from a judge that TIMED OUT. It is not an assessment. H_even is the correct branch.
- [ ] Budget: 31.17 remaining of 75 daily cap (~19 hours). Spend on depth, not breadth — the directive says close something, not start something new.

## Active approaches

The adopted approach is `second-moment-character-mod16` (targets Conjecture 29 via
Dirichlet orthogonality on (Z/16Z)* + second-moment bound). `biquadratic-character-divisors`
is REFUTED and absorbed — its one-way generator equivalence survives inside the
adopted approach as first-moment evaluation; the standalone line is closed per
directive 14's `(2/(2^p+i))_4 = +1` identity result. The only approach with a
verified first-moment computation is the adopted one.

## Don't

- Do not write more approach files. 7 approaches against 4 checked and 1 proved is already lopsided.
- Do not re-derive the 2-adic budget identity, the parity theorem, or the lower bound on a.
- Do not search for a sixth unitary perfect number.
- Do not fetch further sources.
