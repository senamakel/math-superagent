# G-supply-transfer is REFUTED on the successful consecutive-odds family

## The claim under attack

`G-supply-transfer` (research/BACKWARD.md, `nu2-supply-split`):

> For every successful 2-then-odds prefix q_1..q_n (q_1=2, q_2=3, q_j strictly
> increasing odd for j>=3, all gaps even), let
>   w(n) = #{ j in [2, n-1] : q_{j+1} - q_j ≡ 2 (mod 4) }
> and let nu2(q_n) be the number of 2s in the maximal {0,2} suffix of the
> right diagonal delta(q_n).  Then
>   nu2(q_n) >= (2/3) * w(n).

## The counterexample: q = (2,3,5,7,9), n = 4

**Hypothesis holds (prefix is successful).** A_0 = (2,3,5,7,9):
```
A_0 = (2, 3, 5, 7, 9)
A_1 = (1, 2, 2, 2)
A_2 = (1, 0, 0)
A_3 = (1, 0)
```
The bottom entry A_3(0) = 1, so the prefix is successful. (Consecutive odds
is the settled class `R2-consecutive-odds-class`: A_k(0) = 1 for all k.)

**w = 2.** The gaps q_{j+1} - q_j for j in [2, n-1] = [2,3] are
g_3 = 7-5 = 2 and g_4 = 9-7 = 2, both ≡ 2 (mod 4). So w(4) = 2.

**nu2 <= 1.** Right diagonal through q_4: delta_k = A_k(4-k), k = 0..3 =
(A_0(4), A_1(3), A_2(2), A_3(1)) = (9, 2, 0, 0). The maximal {0,2} suffix is
(2,0,0) → nu2 = 1 by the literal reading. Under the run's own convention
(`nu2_vs_gap_parity.py`, tail = `d[2:-1]`, which drops delta_1 and excludes
delta_0) it is nu2 = 0.

**Conclusion.** In both conventions nu2 ∈ {0,1} and
(2/3)·w = (2/3)·2 = 4/3 > nu2. So **nu2 >= (2/3)·w is FALSE**, and the claim
G-supply-transfer is refuted **within its own stated domain** (a successful
2-then-odds prefix).

## Why it is structural, not a numerical fluke

For ANY consecutive-odds prefix (all gaps = 2 ≡ 2 mod 4), A_1 = (1,2,2,2,...),
A_2 = (1,0,0,...), A_3 = (1,0,0,...), and the right diagonal is
(2n-1, 2, 0, 0, ..., 0). Its {0,2}-suffix is essentially all zeros, so
nu2 = 0 (run's convention), while w = n-2 grows linearly. So
nu2 >= (2/3)w fails for every n >= 4, uniformly. This is a family of
counterexamples, not a single instance.

## What this decides (the S1 fork)

The `S1-nu2-transfer-weight` decomposition asks whether the transfer is:

- (a) UNIVERSAL: nu2 >= w/2 for ALL halved-gap bit strings h, or
- (b) PRIME-SPECIFIC: holds only for the prime bit string.

The all-ones halved-gap bit string (consecutive odds) refutes (a): nu2 = 0
but w = n-2. **The fork lands on (b).** The decomposition nu2 >= c·w is NOT a
universal combinatorial reduction: it does not discharge the number-theoretic
content to a clean F2 weight inequality. As the `S1` note itself says, "if
nu2 >= w/2 holds only for the prime bit string, then S1+S2 does NOT reduce
difficulty." That is exactly the situation.

This is the honest negative result the fork's first step asked for: the
supply side has no universal combinatorial shortcut at the (2/3)W constant.

## How this was checked

- Hand arithmetic on the explicit n=4 triangle (above), independent of the
  run's code.
- Cross-checked against the run's own settled class `R2-consecutive-odds-class`
  and the exact nu2 convention in `code/gap_analysis/nu2_vs_gap_parity.py`
  (tail = `d[2:-1]`, suffix scan from the right, count of 2s).
- The measured real-prime range nu2/w ∈ [0.689, 0.867] (from
  `nu2_vs_gap_parity.captured.txt`) sits strictly above 2/3, but that range is
  for the PRIME bit string only and does not extend to all successful
  sequences — exactly the (b) reading the consecutive-odds family pins down.
- The finite-model finder `find_counterexample` returned `undecided` on both
  the `$int` arithmetic encoding and the relational encoding (the environment
  cannot interpret arithmetic; cf. the run's own note in
  `cb_dying_pair_statement.md` that the model finder returns `undecided` on
  every refutable encoding here). So this result rests on the hand-verified
  arithmetic, which is exact and stated in full above.

## Claim

```claim
id: g-supply-transfer-refuted
statement: The supply-side transfer claim G-supply-transfer
  "for every successful 2-then-odds prefix, nu2(q_n) >= (2/3)*w(n), where
  w(n) = #{j in [2,n-1] : gap_j ≡ 2 mod 4} and nu2 is the # of 2s in the
  maximal {0,2} suffix of the right diagonal" is FALSE.  Counterexample:
  the successful consecutive-odds prefix q = (2,3,5,7,9), n = 4, has
  w = 2 (gaps 7-5 and 9-7 both ≡ 2 mod 4) but right diagonal (9,2,0,0)
  gives nu2 = 0 (run's tail convention) or 1 (literal), both < 4/3 = (2/3)w.
  In fact nu2 = 0 for every consecutive-odds prefix n>=4 while w = n-2, a
  family of counterexamples.  Hence the S1 transfer holds only for special
  bit strings (prime-specific, case (b)), not universally: the
  nu2 >= c*w supply decomposition is NOT a universal combinatorial reduction.
hypotheses: the claim's own hypotheses (any successful 2-then-odds prefix,
  all gaps even, w, nu2 as defined there).
holds-here: yes (the counterexample lives inside the claim's stated domain)
status: checked (exact hand arithmetic; model finder unavailable for
  arithmetic in this environment, consistent with cb_dying_pair_statement.md)
bearing: decides the S1-nu2-transfer-weight fork to (b) prime-specific;
  G-supply-transfer as a universal statement is refuted, so the supply
  decomposition nu2 >= c*w does not reduce the difficulty by itself.
anchor: code/refute/g_supply_transfer.p, code/refute/g_supply_transfer_refuted.md
```

## Co-ordinates in the ladder

This does NOT touch the core conjecture, the step law, the recharge identity,
or Lemma 5.4 (which is a *sufficiency* result — budget 2*nu2+2 — and is
unaffected by this). It refutes only the *transfer lower bound* that the
supply-side skeleton was using to turn a gap-mod-4 density into a nu2 bound
for the successful general class. The primes still satisfy nu2/w ~ 0.69-0.87,
so the Route B supply statement is not dead — it is just not a universal
combinatorial identity; it is a statement about the particular prime bit
string (case (b)).
