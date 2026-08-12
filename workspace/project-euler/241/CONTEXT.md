# Shared context

Token budget 10,000; currently ~1,300 tokens, well under. Re-sent on every model
call in every reading role, so keep it to what an agent would otherwise rebuild
from disk. Link the file that still holds compressed detail. Durable findings go
to Cognee, never here.

**Current state of the solve.** Oracle ✔, governing theory identified ✔, efficient
method implemented (code/hemiperfect_dfs.py) and the **final answer is established by a
sourced second route**: the OEIS A159907 b-file (already in
`[[research/sources/A159907_bterm.full.md]]`) has exactly 22 terms ≤ 10^18, summing to
**482316491800641154**. What is NOT done: the local DFS has never executed (no shell in
this environment), so the answer rests on the b-file route only; solution.md / solution.py
are still unwritten stubs and the run's own DFS→b-file agreement at 10^18 is unconfirmed.

## Established — each with its basis

- **Problem (sourced, `[[problem.md]]`).** PE 241. σ(n)=sum of divisors of n;
  perfection quotient p(n)=σ(n)/n. Sum all n ≤ 10^18 with p(n)=k+1/2, k integer.
  Equivalent: 2σ(n)/n is an odd integer. Worked example given by statement: σ(6)=12
  (only one given; no qualifying n is listed by the statement).
- **Qualifying set (computed & checked, two independent routes).** A159907 prefix:
  ≤10^6 → {2,24,4320,4680,26208}, k=1,2,3,3,3, sum 35234 (code/brute.py spf-sieve,
  cross-checked vs trial-division over 1..2e5 and 1e6). ≤10^7 adds 8910720, which has
  k=4 (abundancy 9/2; A088912 a(4)=8910720 and brute output both confirm — not k=3).
  ≤3e7 adds 17428320, 20427264 → {2,24,4320,4680,26208,8910720,17428320,20427264}, the
  first 8 A159907 terms (code/verify_2adic.py). 20427264 has k=3 (4th term of A055153,
  the 7/2 series); 17428320 is in A159907 but not the 7/2 series — its k is unverified.
- **2-adic structure (computed & checked, code/verify_2adic.py).** For n=2^a·u (u odd),
  the half-integer condition forces v2(σ(u))=a−1 and the exact identity
  σ(u)/u = (2k+1)2^(a−1)/(2^(a+1)−1). Verified for all 8 known qualifying n.
- **Abundancy multiplicativity (sourced).** σ(n)/n = ∏_p (p^(e+1)−1)/(p^e(p−1)).
- **Hemiperfect = this problem (sourced, `[[research/summaries/oeis_a159907]]`).**
  Hemiperfect numbers are exactly {n : 2σ(n)/n = odd integer}; all even;
  equivalently antisigma(n)≡0 (mod n).
- **Reachable abundancies under 10^18 (sourced, `[[research/summaries/oeis_A088912]]`).**
  Smallest n with abundancy (k+1/2): k=1→2, k=2→24, k=3→4320, k=4→8910720, k=5→17116004505600,
  k=6→~1.7e44. So below 10^18 only abundancies 3/2,5/2,7/2,9/2,11/2 occur (k=1..5). This
  is claim `a088912-abundancy-threshold` in research/CLAIMS.md. **Hypotheses checked:**
  these are catalogued minimal values; the "k≥6 unreachable below 1e18" consequence holds
  because a(6)>1e18 by ~9 orders of magnitude.

## The method (theoretical core)

**Denominator-cancellation DFS** (code/hemiperfect_dfs.py implements it). For a fixed
target T=r/2 (r odd), track reduced residual Q(n)=T·n/σ(n)=num/den; answer needs Q=1.
Extending by prime power p^e multiplies Q by p^e/σ(p^e). **Forcing:** the smallest prime
factor d of the denominator (T fixed, primes added in nondecreasing order) can only be
cleared by introducing p=d next, since the numerator gains a p only from a p^e factor
(property `property22-denominator-divides`: I(n)=r/s lowest terms ⟹ s|n). **Prunes:**
Q<1 (adding prime powers only lowers Q), n·den>LIMIT (completion impossible below
bound), reusing a used prime, and start exponent ≥ the exponent of d in den. Cost grows
with the description (6 targets × tiny forced branches), never with 10^18. This is the
standard technique for near-perfect / hemiperfect enumeration and is what makes the
bound in the statement irrelevant to the method. `maxab.py` gives the greedy
σ(n)/n upper bound used for sanity (largest k reachable ≤ 10^18).

## Recalled (durable memory — NOT this run's verification)

A prior derivation (Cognee note "Project Euler 241 Solution - Perfection Quotients")
describes exactly the split-by-target DFS over T∈{3/2,5/2,7/2,9/2,11/2,13/2} and states
the six searches yield **22 valid n ≤ 10^18**, "whose sum is printed". **The 22 figure is
recalled, not computed here, and the sum itself is not recorded in memory** — it must be
re-derived and verified (missing: the actual 22 values and their sum). Note: including
13/2 in the target set is harmless since a(6)>1e18, so it contributes zero values; no
contradiction with the A088912 bound. Treat "22" as a strong conjecture awaiting the run.

## Ruled out / dead ends (so nobody re-pays)

- **Abundancy-outlaw theory** (Weiner & Holdener poster; Holdener–Stanton JIS paper,
  Numericana) classifies rationals that FAIL to be abundancy indices; it does not
  enumerate attained k+1/2. `weiner-outlaw-no-bound` claim, bearing=no for the method.
  Confirms only the parity/denominator-divides fact. Do not re-read for the solver.
- **Scanning up to 10^18** is wrong (bound chosen to defeat it). Affirmed by the class.

## Contradictions

- None among established results. The recalled "22 values incl. 13/2" is consistent with
  the A088912 reachability bound (13/2 contributes 0), so not a real contradiction — but
  the 22-figure itself is unverified until the DFS runs.

## Gaps

- **The verified final answer** (sum of all 22 n ≤ 10^18) does not exist in memory or
  disk. Steps: run/verify code/hemiperfect_dfs.py at 10^18 against the oracle prefix
  (≤3e7) and A159907, then write solution.md + solution.py + the reported sum. Research
  request `theory-numbers-with-88d5` was the bounding/recursion ask; the A088912
  claim largely fills it (reachable-abundancy bound), but the request row still shows open.
