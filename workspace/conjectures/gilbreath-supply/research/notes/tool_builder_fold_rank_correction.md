# Fold-matrix rank: correction of inherited fact 3

**Result (decisive, exact F2 arithmetic, verified and captured).** The operative
fold matrix `Φ_n` whose weight is SUPPLY's `ν₂(n) = wt(Φ_n h)` is
`(n−2) × n` with rows `d = 2..n−1`, entry

    Φ_n[d, j] = 1  ⟺  j − (n−1−d) is a bitwise submask of d.

Over F₂, for every `n = 2..20`: **rank = n−2 (full row rank), nullity = 2.**
The kernel is exactly the span of the two alternating vectors
`e = (1,0,1,0,…)` and `o = (0,1,0,1,…)`; the all-ones vector equals `e ⊕ o`,
so it is in the kernel (as problem.md's door-1 witness states) but is **not** the
whole kernel.

**Inherited fact 3 is wrong.** It reads *"rank Φ_n = n−3, nullity 1,
ker = span(all-ones)"*. For an n-column matrix nullity 1 forces rank n−1, so
"rank n−3" and "nullity 1" are mutually inconsistent. Moreover "rank n−3" fits
**no** row-range convention: rows `d = 0..n−1` give rank `n`; rows `d = 1..n−1`
(the "k = 1..n−1" verbal range, which is what bacher_pascal_verify.py found)
give rank `n−1`, nullity 1; rows `d = 2..n−1` (the operative one) give rank
`n−2`, nullity 2.

**Mathematical meaning of the correction.** `ker Φ_n` = the period-2 strings
(h constant on parity classes), a 2-dimensional space; a string gives
`ν₂(n) = 0` iff it is a linear combination of the two alternating vectors.
This sharpens, for period 2, the dyadic-collapse fact 4 (eventually-periodic
power-of-two period ⇒ `ν₂ = O(1)`): for period 2 the collapse is exactly 0.

**Cross-check / negative control.** `wt(Φ_n h)` computed as a matrix image
equals `ν₂(n)` by the `t_direct` submask-XOR oracle for `n = 3..10`, 5 random
`h` each — all match. Exact F2 Gaussian elimination, O(n⁴) over n≤20.

Author: tool_builder. Anchor: `code/fold_rank/rank_of_fold.py`,
capture `code/out/supply_fold_rank.final.captured.txt`.

```claim
id: fold-rank-is-n-2-nullity-2-alternating
statement: The operative SUPPLY fold matrix Phi_n — whose image weight is
  nu2(n) = wt(Phi_n h) — is (n-2) x n with rows d = 2..n-1 and entry
  Phi_n[d,j] = 1 iff j-(n-1-d) is a bitwise submask of d. Over F2, for every
  n = 2..20: rank Phi_n = n-2 (full row rank), nullity = 2, and the kernel is
  exactly span((1,0,1,0,...), (0,1,0,1,...)) — the period-2 strings. The
  all-ones string is their sum, so it is in the kernel but is not the whole
  kernel. Inherited fact 3 ('rank = n-3, nullity 1, ker = span(all-ones)') is
  internally inconsistent for an n-column matrix and matches no row-range
  convention.
hypotheses: Lucas-submask reading of the fold (C(d,i) odd iff i submask of d);
  the operative nu2 definition sums cells d in [2, n-1].
holds-here: yes — this is the actual matrix whose weight the run measures.
status: checked (exact F2 Gaussian elimination, n=2..20; wt(Phi_n h) by image
  == nu2 by t_direct oracle for n=3..10, 5 random h each, all match)
bearing: corrects an inherited assertion the whole kernel/rank picture was built
  on. ker Phi_n is 2-dimensional, equal to the period-2 strings, so nu2(n)=0
  exactly on span of the two alternating vectors. Sharpens dyadic-collapse
  (fact 4) at period 2 to 'exactly 0'.
anchor: code/fold_rank/rank_of_fold.py, code/out/supply_fold_rank.final.captured.txt

<!-- NOTE: this claim's `contradicts` line previously read "problem.md fact 3 ('rank=n-3, nullity 1, ker=span(all-ones)')", which generated three phantom contradiction rows ('problem.md','fact','3') in CLAIMS.md for an inherited prose fact. problem.md has since been corrected to rank n-2, nullity 2 (Kernel item 3), so the contradiction is resolved; the stale-fact text survives only in this note's history and in the corrected-problem note. -->
```

