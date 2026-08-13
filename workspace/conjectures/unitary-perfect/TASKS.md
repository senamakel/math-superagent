# Tasks

## Next (exactly one thing, this cycle)

- [ ] Run `timeout 540 python3 code/equality_case.py 2>&1 | tee code/out/equality_case_reproduced.captured.txt; echo EXIT_CODE=$?` and confirm:
  1. At a=1 the maximum product equals 4/3 exactly, extremal multiset {5,9} is the odd part of 90
  2. 2^8+1 = 257 is prime, so 257 is forced as a component when a=8
  3. 9 = 3^2 and 49 = 7^2 are admissible, 3 and 7 are not
  4. The exclusion runs 2 ≤ a ≤ 28 and stops at 29
  If all four hold: update the claim `budget-equality-case-impossible` anchor to include this capture, and close thread `a-ge-8-bound` as resolved (a ≥ 29 for the equality case, a = 8 impossible). The claim is already `checked` from the prior capture; this run reproduces it independently.

## Standing

- [ ] Do not fetch any new sources while FRONTIER.md unworked count > 100. The paper (Maciejewski, 93 KB) is already on disk at `research/sources/maciejewski-bounded-box-subbarao-warren.full.md`. Surveys (Guy B3, Handbook, Goto 2007) are already in the library and add nothing `problem.md` does not already state.

- [ ] The [74:08] "progress no" verdict came from a judge that TIMED OUT. It is not an assessment. H_even is the correct branch.

## Active approaches

The only approach with a program and a verified claim is `biquadratic-character-divisors` (adopted). It attacks Conjecture 29 via quartic reciprocity in Z[i] on the Gaussian factor 2^p + i. The first step is computing the Gaussian factorization for small primes p and tabulating (2/π)_4 against p mod 8 and Aurifeuillean half.

Approaches 5 (stewart-size-elimination), 6 (forced-3-divisibility), and 7 (aurifeuillean-reciprocity) are written but unworked. They wait behind the one that converts.

## Don't

- Do not write more approach files. 7 approaches against 4 checked and 1 proved is already lopsided.
- Do not re-derive the 2-adic budget identity, the parity theorem, or the lower bound on a — all proved and anchored.
- Do not search for a sixth unitary perfect number.
