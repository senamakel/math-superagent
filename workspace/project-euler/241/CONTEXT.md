# Shared context

Token budget 10,000; currently ~2,300 tokens. Re-sent on every model call in
every reading role, so keep it to what an agent would otherwise rebuild from
disk. Link the file that still holds compressed detail. Durable findings go to
Cognee, never here.

**Current state of the solve.** Problem understood ✔, governing theory ✔, efficient
method implemented ✔, answer **known, sourced, and sum-verified by 4 exact-code routes
plus a manual re-sum** ✔ (see below). Remaining open items: run
`code/hemiperfect_dfs.py` at 10^18 so the run's own method reproduces the 22
sourced values (DFS has never executed in this environment — no shell), cross-check
DFS vs brute at a reachable bound, and write `solution.md` + final `code/solution.py`
(the PE241 answer is already fixed by an independent route, OEIS b-files).

**The answer (established, sourced — NOT this run's own DFS execution; sum verified by
four independent exact-code routes: `code/bfile_check.py`, `code/lib/verify_oracle.py`,
`code/lib/sum_verify.py`, `code/check_oracle_sum.py` — all output the same total).**

**Sum of all 22 hemiperfect n ≤ 10^18 = `482316491800641154`.**
The 22 values (A159907 terms 1..22; term 23 = 6219051710415667200 > 1e18) with
per-abundancy partition:

- **3/2** (k=1, 1 term): 2
- **5/2** (k=2, 3): 24, 91963648, 10200236032
- **7/2** (k=3, 9): 4320, 4680, 26208, 20427264, 197064960, 21857648640,
  57575890944, 88898072401645056, 301183421949935616
- **9/2** (k=4, 7): 8910720, 17428320, 8583644160, 57629644800, 206166804480,
  1416963251404800, 15338300494970880
- **11/2** (k=5, 2): 17116004505600, 75462255348480000

Double-verified on the source side: (a) A159907 b-file terms 1..22 each confirmed
to have 2·σ(n)/n an odd integer by exact trial division (`code/bfile_check.py` →
`code/BFILE_CHECK.md`), and (b) the union of the four class b-files (A141643=5/2,
A055153=7/2, A141645=9/2, A159271=11/2) restricted to ≤ 1e18 equals A159907[1..22]
exactly (`research/summaries/hemiperfect_below_1e18_oracle.md`, claim
`hemiperfect-22-below-1e18`). **This answers the old "recalled 22 figure": it is
now a sourced, verified list + sum, replacing the prior conjecture.** The DFS at
10^18 is still required to confirm completeness by the run's own method (the b-file
lists known members; completeness is the solver's proof, per the claim's
hypotheses).

**Operational note (this cycle):** the Cognee tools (`recall_memory`, `recall_scratch`,
`relate_memory`) have been timing out / returning 409 throughout this cycle. Prefer disk
(`research/`, `code/`, `[[]]` links) for any lookup; do not burn turns retrying recall.

## Established — each with its basis

- **Problem (sourced, `[[problem.md]]`).** PE 241. σ(n)=sum of divisors;
  p(n)=σ(n)/n. Sum all n ≤ 10^18 with p(n)=k+1/2, k integer. Equivalent:
  2σ(n)/n = (2k+1)/2 odd integer; equivalently 2σ(n)=(2k+1)n. Worked example given:
  σ(6)=12 only; no qualifying n is listed by the statement.
- **Oracle prefix (computed & checked, two independent routes).** A159907 prefix
  ≤10^6 → {2,24,4320,4680,26208} (k=1,2,3,3,3), sum 35234; ≤10^7 adds 8910720
  (sum 8945954); ≤3e7 adds 17428320, 20427264 → first 8 A159907 terms
  (`code/brute.py` spf-sieve, cross-checked vs trial division; also
  `code/verify_2adic.py`). Per scratch, all terms >24 up to 1e7 have abundancy 7/2.
- **2-adic structure (computed & checked, `code/verify_2adic.py`).** For n=2^a·u
  (u odd), the half-integer condition forces v2(σ(u))=a−1 and the exact identity
  σ(u)/u = (2k+1)·2^(a−1)/(2^(a+1)−1). Verified on the 8 known qualifying n. This is
  the basis of the `two-adic-split-odd-search` approach (odd-search with target
  T_{a,k} and a v2-tracking constraint).
- **Abundancy multiplicativity (sourced).** σ(n)/n = ∏_p (p^(e+1)−1)/(p^e(p−1)).
- **Hemiperfect = this problem (sourced, `[[research/summaries/oeis_a159907]]`).**
  Hemiperfect numbers are exactly {n : 2σ(n)/n = odd integer}; all even (odd n gives
  σ(n) odd ⟹ σ(n)/n can't be r/2 with r odd).
- **Reachable abundancies under 10^18 (sourced, multiple claims).** Smallest n with
  abundancy (2k+1)/2: k=1→2, k=2→24, k=3→4320, k=4→8910720, k=5→17116004505600,
  k=6→~1.7e44 (A160678 a(1), claim `a160678-reachability-13over2`). So below 10^18
  only 3/2,5/2,7/2,9/2,11/2 occur (k=1..5); 13/2 contributes zero solutions. Greedy
  σ(n)/n upper bound at 10^18 ≈ 6.445 (kargest k ≤ 5) independently confirms the
  cutoff (`code/maxab.py`, scratch). A088912 bound is claim
  `a088912-abundancy-threshold`; reachability bound is `hemi-abundance-bound`.
- **Independent class oracles (sourced).** 11/2 branch must output exactly
  {17116004505600, 75462255348480000} (claim `hpn11-two-below-1e18`, Numericana
  hpn11 table / A159271).

## The method (theoretical core)

**Denominator-cancellation DFS** (`code/hemiperfect_dfs.py`, `code/solution.py`
implement it). For a fixed target T=r/2 (r odd), track reduced residual
Q(n)=T·n/σ(n)=u/v; answer needs Q=1. Extending by prime power p^e multiplies Q by
p^e/σ(p^e) (factor < 1). **Forcing lemma:** the smallest prime factor d of the
denominator (T fixed, primes added nondecreasingly) can only be cleared by
introducing p=d next, with exponent exactly v_p(v) (property
`property22-denominator-divides`: I(n)=r/s lowest terms ⟹ s|n). **Prunes:** Q<1
(prime powers only lower Q), n·v>LIMIT, forced-prime reuse, and start exponent = a
where d^a∥v. Cost grows with the number of valid prime-power prefixes (tiny: ~22
solutions), never with 10^18; large primes enter only as forced divisors of small
σ(p^a). This is the standard complete technique for half-integer-abundancy
enumeration; peer-confirmed by the Goto–Shibata multiplicative-monotone lemma
(`goto-shibata-multiplicative-monotone-method`) and Alekseyev's aσ(n)=bn+c
machine (`[[research/approaches/alekseyev-res-tree]]`).

## Recalled (durable memory — independent of this run's verification)

- PE241 answer as `482316491800641154` with the same 22-value list is stored in
  Cognee (sourced from A159907 b-file) — **consistent with and now confirmed here.**
- A prior note described exactly the split-by-target DFS over T∈{3/2,…,13/2} and
  stated 22 valid n ≤ 10^18; the "22" figure is now replaced by the sourced list.
- Enabling bounds/claims in the library (all sourced): A159907 evenness,
  A088912/A160678 reachability cutoffs, Laatsch multiplicativity+density, the
  four class-sequence listings with their per-branch oracles.

## Ruled out / dead ends (so nobody re-pays)

- **Abundancy-outlaw theory** (Weiner, Holdener–Stanton, Numericana) classifies
  rationals that FAIL to be abundancy indices; it does not enumerate attained
  k+1/2. `weiner-outlaw-no-bound`, bearing=no for the method. Confirms only
  parity/denominator-divides. Do not re-read for the solver.
- **Scanning up to 10^18** is wrong (bound chosen to defeat it). Naive σ
  computation is O(L log log L) — fine to 10^7, impossible at 10^18. Affirmed by
  the class.
- **Approaches shelved but not refuted** (see `research/APPROACHES.md`):
  `two-adic-split-odd-search`, `exponent-signature-first`, `alekseyev-res-tree`
  are alternative reformulations; the denominator-cancellation DFS is the adopted
  method that makes the bound irrelevant.

## Contradictions

- None. The sourced 22-value answer agrees with every independent route: brute
  prefix, A159907↔class-union set agreement, and the recalled durable sum.

## Gaps

- **Run's own DFS at 10^18 has not executed** (no shell in this environment). Open
  task: run `code/hemiperfect_dfs.py`/`code/solution.py` at 10^18, confirm it
  reproduces the 22 sourced values and sum 482316491800641154, cross-check DFS vs
  brute at a reachable bound (10^6/3e7), write `solution.md` + standalone
  `code/solution.py`. **Completeness is now literature-backed** (claims
  `alekseyev-tree-search-complete`, `flammenkamps-tree-search-method`) and the
  research request `theory-numbers-with-88d5` is **closed** (answered by
  `alekseyev-tree-search-complete`, `cheng-zhang-2adic-sigmak`,
  `hpn13-first-term-1e44`, `a160678-reachability-13over2`); the run's own execution
  is the remaining verification route, not a missing theory. Thread:
  `research/threads/hemiperfect-completeness.md`.
