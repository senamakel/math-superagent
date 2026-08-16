```thread
question: Which split-and-sum implementation of the S-root predicate passes the brute-force oracle at T(10^4)=41333 and scales to T(10^12)?
status: settled
rests-on: [a038206-expr-recursion, snumber-sum-oracle, a038206-bfile-cover, a104113-bfile-cover, proofwiki-digit-sum-bound, f1-f2-infinite-pair-families, a038206-no-recurrence-filter]
blocked-by: none
next: none — the search thread is closed. T(10^12)=128088830547982 is established by three independent routes (solution.py digit-partition recursion, verify_bfile.py A038206 b-file sum of squares, candidates_mitm.py full 10^12 run), all reproducing T(10^4)=41333. The three candidate encodings (DFS+prune, memoized digit-DP, meet-in-the-middle) were explored in parallel and are all flavours of the same split-and-sum predicate; all reduce to the OEIS Branicky `expr` recursion. Research refuted the two reformulations that promised asymptotic gain (k-automaticity, Hensel digit-lifting) and adopted the repunit-witness reformulation as an open question; none beats the O(sqrt N)=10^6 root scan for T(10^12).
```

An S-number n has n = m^2 and m equal to the sum of parts of some split of n's
decimal digits into ≥ 2 numbers. The method is determined by the root
bijection (T(N) = Σ_{m=2}^{isqrt(N)} m²·[S(m)]), and the digit-partition
recursion is the OEIS A038206/A104113 `expr` program (claim
`a038206-expr-recursion`), confirmed correct by brute.py's exhaustive cut
enumeration at every reachable N and by agreement with the A038206 and A104113
b-files.

**Status.** The three candidate encodings were built on the attempts ledger
(branches 01 dfs, 02 digitdp, 03 mitm) and all reproduced T(10^4)=41333; MITM
had 0 mismatches on [2,5000]. The adopted method is the root-scan recursion
(`code/solution.py`).

**Structural bounds found after the search.** F1/F2 proven infinite pair
families cover only ~4.4% of roots; only mod-9 is a cheap necessary filter; no
linear recurrence, no k-automaticity, no Hensel-lifting gain. The O(sqrt N)
root scan is the settled method; open research question (recorded on
`repunit-witness-identity`) is whether the k≥3 witness equation has a compact
parametrisation.

Leading-zero note: a block like "01" is handled by splitting off its leading
zero as a separate "0" block, so the convention does not change which
S-numbers exist (covered by the A038206 recursion's arbitrary first-block
handling).
