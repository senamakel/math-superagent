# Shared context

Token budget 10,000; currently roughly 1,700 tokens, well under. Re-sent on every model
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
  because a(6)>1e18 by ~9 orders of magnitude. **Now confirmed by two further sources:**
  Numericana hpn13's first term = A160678 a(1) = 170974031122008628879954060917200710847692800
  ≈ 1.71e44 (claims `hpn13-first-term-1e44`, `a160678-reachability-13over2`), so 13/2
  contributes zero; and hpn11's table holds exactly the two 11/2 members below 1e18
  (claim `hpn11-two-below-1e18`).

## The final answer (sourced — OEIS A159907 b-file, independent route)

Exactly **22** A159907 terms are ≤ 10^18 (term 23 = 6219051710415667200 > 1e18 cuts off).
Their **sum = 482316491800641154.** The 22 values and per-abundancy split are listed in
code/sum_answer.py and code/factors22.py (terms hard-coded from the b-file). Per-k
(abundancy k+1/2): k=1:{2}; k=2:{24,91963648,10200236032}; k=3:{4320,4680,26208,20427264,
197064960,21857648640,57575890944,88898072401645056,301183421949935616}; k=4:{8910720,
17428320,8583644160,57629644800,206166804480,1416963251404800,15338300494970880};
k=5:{17116004505600,75462255348480000}. Cross-validated in code/crosscheck_oeis.py
(per-k vs A141643/A055153/A141645/A159271). **Status: sourced & arithmetic-checked, not
independently recomputed by this run's own DFS.** This matches the recalled "22 values"
figure.

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
σ(n)/n upper bound used for sanity (largest k reachable ≤ 10^18). **Completeness precedent
is sourced, not ad hoc:** Flammenkamp's exhaustive tree search enumerated all multiply-perfect
numbers < e^350 (claim `flammenkamps-tree-search-method`); Goto–Shibata proved the monotone
multiplicative structure such searches rest on (claim `goto-shibata-multiplicative-monotone-method`);
Alekseyev (arXiv 2601.17832) solves bounded aσ(n)=bn+c by exactly this forced-cancellation recursion.

## Recalled (durable memory)

A prior derivation (Cognee note "Project Euler 241 Solution - Perfection Quotients")
describes exactly the split-by-target DFS over T∈{3/2,5/2,7/2,9/2,11/2,13/2} and states
the six searches yield **22 valid n ≤ 10^18**, "whose sum is printed". **CONFIRMED by the
b-file route above** (22 terms, sum 482316491800641154) — the recalled figure and the
sourced data now agree; what no longer exists anywhere is a local computation of that sum
(the memory did not record the sum itself, so it remains sourced-not-computed). 13/2 in
the target set contributes zero values (a(6)>1e18), consistent with the A088912 bound.

## Ruled out / dead ends (so nobody re-pays)

- **Abundancy-outlaw theory** (Weiner & Holdener poster; Holdener–Stanton JIS paper,
  Numericana) classifies rationals that FAIL to be abundancy indices; it does not
  enumerate attained k+1/2. `weiner-outlaw-no-bound` claim, bearing=no for the method.
  Confirms only the parity/denominator-divides fact. Do not re-read for the solver.
- **Scanning up to 10^18** is wrong (bound chosen to defeat it). Affirmed by the class.

## Contradictions

- None among established results. The recalled "22 values incl. 13/2" is consistent with
  the A088912 reachability bound (13/2 contributes 0) and now CONFIRMED by the A159907
  b-file. One residual inconsistency: code/hemiperfect_dfs.py scans r∈{3,5,…,39} and
  hard-codes PRIMES up to 2e6 while the report (report_hemiperfect_enumeration.md) and
  remembered technique scan r∈{3,5,7,9,11,13}; harmless for the count (r>11 impossible
  below 1e18) but a sign the DFS is untested, not verified.

## Gaps

- **Independent verification of the sum by this run's own computation** (not by OEIS):
  code/hemiperfect_dfs.py at 10^18 → compare against the b-file's 22 terms and
  482316491800641154. Requires a shell, which this environment lacks — a tool_builder
  run with an executor is the unblock. Also still open: solution.md + code/solution.py
  (write the derivation and the report-ready solver). Research request
  `theory-numbers-with-88d5` (bounding/recursion ask) is ANSWERED: the A088912
  claim gives the reachable-abundancy bound, and the claim block in
  research/summaries/hemiperfect_below_1e18_oracle.md carries `answers: theory-numbers-with-88d5` —
  REQUESTS.md's still-open row is stale until its next rewrite; do not re-search this.
