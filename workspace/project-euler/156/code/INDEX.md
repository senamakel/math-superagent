# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for PE156: f_naive(n,d) counts digit d in 0..n by literal string counting; f_incremental(limit,d) returns solutions of f(n,d)=n in one running pass. Verified: reproduces the full f(n,1) table n=0..12, first solutions [0,1,199981] within 0..200000, and that f(n,1)=3 never occurs there. O(limit*digits) time, O(1) space. Deliberately non-efficient; the fast method later checks against it. |
| `solution.py` | Efficient PE156 solver: jump-iteration over f(n,d)=n in [0, d·10^10] using closed-form f_place_value (never enumerating the range), mandated jumps (n←c when f>n; n+=ceil((n−c)/(D−1)) when f<n), exhaustive by the g=f−n monotonicity argument with D=11. Verifies f_place_value vs brute force on all n≤10^5, d=1..9; cross-checks d=1 solutions ≤300000 against the oracle file; s(1)=22786974071 vs statement; counts vs sourced OEIS A130432. Run: reproduces the statement table, s(1)=22786974071, GRAND TOTAL Σs(d)=21295121502550, 661 solutions in 86649 iterations, 0.70 s. Writes code/out/solutions-d{d}.txt. |
