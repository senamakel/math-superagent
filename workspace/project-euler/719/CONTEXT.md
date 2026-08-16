# Shared context

## Established

**Problem:** projecteuler.net/problem=719 "Number Splitting". Full statement in
`/workspace/problem.md`. Restated with all symbols in `/workspace/GOAL.md`.

**Definition (sourced — OEIS A104113/A038206, and the problem statement).**
An S-number is `n = m^2` whose decimal digit string splits left-to-right into
`k >= 2` contiguous blocks summing to `m`. Define `T(N)` = sum of S-numbers
`n <= N`. Oracle: `T(10^4) = 41333`. Task: `T(10^12)`.

*Computed and checked*: the oracle T(10^4)=41333 is reproduced by summing the
A104113 S-number terms <= 10^4 (81,100,1296,2025,3025,6724,8281,9801,10000),
which equals the roots 9,10,36,45,55,82,91,99,100 squared. `n=1` is correctly
excluded (its only digit split is the single block `1`; m^2=m only for m in
{0,1}, and we start at m=2).

**Method (the structural reduction).** Since an S-number is *determined by its
root*, test only `m in [2, isqrt(N)] = [2, 10^6]` instead of all `n <= 10^12`.
Each test: does str(m^2) admit a partition into >=2 blocks summing to m? Exact
integer recursion over at most 13 digits (<= 4096 partitions). O(sqrt(N)) total.
The A038206/A104113 OEIS program uses exactly this recursion.

**Canonical sequence records (downloaded):**
- OEIS A104113 — the S-numbers themselves. `a(n) = A038206(n)^2`. Every term ≡ 0 or 1 mod 9. Links Project Euler 719.
- OEIS A038206 — the roots m. b-file runs to 3200 roots; the full b-file we
  have runs to 408 roots ending exactly at **1000000 = isqrt(10^12)**, i.e. it
  enumerates every S-number <= 10^12.

**Independent verification route.** Sum of squares of the A038206 b-file roots
<= 10^6 equals T(10^12) by a route disconnected from the solver's recursion.
`code/verify_bfile.py` does this from the downloaded b-file.

## Ruled out

- Scanning all n <= 10^12 and testing each is ~10^12 trials — the stated bound
  defeats it. The root reduction is what makes most of the search space
  unnecessary.

## Numbers

- S-numbers <= 10^4 (from A104113 / roots 9,10,36,45,55,82,91,99,100):
  81, 100, 1296, 2025, 3025, 6724, 8281, 9801, 10000; sum = T(10^4) = 41333.
- sqrt(10^12) = 10^6; roots to test: 2..10^6.
- **T(10^12) = 128088830547982 — computed and double-verified.**
  Intermediate reference values (computed and checked against brute force at
  every reachable N): T(10^6) = 10804656, T(10^9) = 6222187932.
- 408 S-roots <= 10^6 (A038206 b-file, term 408 = 1000000 = isqrt(10^12)).
- Every S-root m satisfies m^2 == m (mod 9), i.e. m ≡ 0 or 1 (mod 9) — this
  mod-9 filter prunes candidates by 7/9. Claim `partition-sum-invariant-mod9`.

## Recalled

- Kaprekar numbers (already in library) are the *two-block* special case
  (D.R. Kaprekar: 45^2=2025, 20+25=45). S-numbers generalise to arbitrary
  numbers of blocks. See `research/summaries/kaprekar-number-wikipedia.md`.
- ProofWiki: the *single-block* equality sqrt(n)=digit-sum(n) has only
  solutions 0,1,81; confirms the 2+ block requirement is essential and that
  81 is the boundary case. `research/summaries/proofwiki_sumofdigits_sqrt.md`.

## Contradictions — resolved

- **`code/verify_bfile.py` off-by-one (fixed, no longer a live contradiction).**
  Earlier `T(10^4) from b-file = 41334` came from summing `m^2` over b-file
  roots including the sentinel roots `m=0` and `m=1`; `n=1` is not an S-number.
  `verify_bfile.py` now filters `2 <= m <= isqrt(N)`, and on a fresh run
  (`code/out/final.log`) reproduces `T(10^4)=41333` and `T(10^12)=128088830547982`,
  agreeing with `solution.py`. The spurious +1 is gone; this contradiction is
  closed.

## Gaps

- None material. The answer is settled and double-verified. (`recall_memory`
  graph lookups fail with a Cognee triplet-embedding 404; the passage search
  still works, so this is a tooling limitation, not a knowledge gap.)
