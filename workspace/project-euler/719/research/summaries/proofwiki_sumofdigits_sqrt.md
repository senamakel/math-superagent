# ProofWiki — positive integers whose sqrt equals digit-sum

Source: https://proofwiki.org/wiki/Positive_Integers_whose_Square_Root_equals_Sum_of_Digits
(full).

**Theorem (proved).** The only positive integers n with √n = digit-sum(n),
i.e. n = [s(n)]² where s(n) is the digit sum, are 0, 1, 81.

**Proof idea.** For n > 36, the digit sum of n² is ≤ 18d (n² has at most 2d
digits) while n ≥ 10^(d−1); Bernoulli's inequality gives n ≥ 90d−170 > 18d for
d ≥ 3, and the 2-digit case forces n > 36. So the sum of the *digits* of n² can
never reach n once n > 36.

**Bearing on PE 719.** This explains why the trivial single-block form
(sqrt n = one number summing to n, i.e. n = digit sum) gives only 0,1,81 — which
is *not* the S-number rule, because S-numbers allow the digit string to be split
into 2+ blocks (so the parts are not single digits). The only place the
single-block versus multi-block distinction matters for counting here is n=1:
excluding it (as PE 719 does, requiring 2+ parts) is exactly what the oracle
T(10⁴)=41333 confirms (if 1 counted, the sum would be 41334).

```claim
id: proofwiki-digit-sum-bound
statement: sqrt(n) = digit-sum(n) iff n in {0,1,81}; for n > 36 the digit sum of n^2 is < n, bounded by 18d where d = digits(n).
hypotheses: base 10; n a positive integer.
holds-here: yes
status: proved (ProofWiki argument)
bearing: confirms the single-digit-block reading is insufficient and that n=1 is the only boundary the 2+-block rule excludes from the trivial case.
anchor: research/summaries/proofwiki_sumofdigits_sqrt.md
```

**Does not help** by giving a route to T(10¹²): it concerns digit *sums*, not
general block partitions; the enumeration must still search all splits. Its only
use here is clarifying the 2+ parts rule and confirming the n=1 exclusion.
