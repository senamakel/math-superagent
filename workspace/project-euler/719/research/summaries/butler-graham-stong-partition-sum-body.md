# Butler–Graham–Stong — "Partition and sum is fast"

Source: https://arxiv.org/html/1501.04067v1 (full text:
`research/sources/butler-graham-stong-partition-sum-body.full.md`; abstract page
`research/sources/butler-graham-stong-partition-sum.full.md`). Stephen Butler,
Ron Graham, Richard Stong, arXiv:1501.04067, Jan 2015, 4 pages.

## What the paper studies

The **partition-and-sum** operation on a natural number: treat the decimal (or
base-b) digit string, insert plus signs between some digits, and sum the blocks.
This is *exactly the digit-splitting operation* Project Euler 719 uses — the
difference is only the goal. PE 719 asks whether one split's block-sum equals the
square root m; this paper asks how few *iterations* of partition-and-sum reduce
any number to a single digit.

## Statements that matter here

- **The invariant.** (p. 2, in the proof of the observation): "the process is
  always invariant modulo (b−1) (this is the same principle which states that a
  number is divisible by 9 iff the sum of the digits is divisible by 9)."
  Every partition-and-sum of n is ≡ n (mod b−1). This is the structural reason
  behind the OEIS fact that every S-number term ≡ 0 or 1 (mod 9).
- **Theorem 1.** In base 2 any number collapses to a single digit in ≤ 2
  applications; in base b ≥ 3 in ≤ 3 applications.
- **Lemma 1 (base b ≥ 4):** any n < 3b² − b − 1 collapses in ≤ 2 steps; tight,
  with the worst case 2(b−2)(b−1)(b) = 3b²−b−1 and infinitely many numbers
  taking 3 steps (20…0(b−2)(b−1)_(b)).

## Bearing on PE 719 / the S-number problem

1. **Fixes the mod-9 structure with a citable source.** For an S-number
   n = m², a split's block-sum equals m, and by the invariant (mod 9 in base
   10) the block-sum ≡ n. Hence m ≡ m² (mod 9), so m(m−1) ≡ 0 (mod 9), giving
   m ≡ 0 or 1 (mod 9). This is the cross-check used to prune candidate roots
   (all of A038206's roots and hence all S-numbers are ≡ 0 or 1 mod 9). It is
   a *necessary* condition, not sufficient.
2. **Places the S-number test in the right family.** The split of n into
   blocks summing to m is the same object the paper's one-shot partition-and-sum
   considers; the paper confirms the digit-block-partition operation is the
   natural setting, and confirms there is no published structure theorem for the
   fixed-point (block-sum = m) condition beyond the two-block Kaprekar case.

## What it does NOT establish

- No method for the multi-block (k ≥ 3) split-and-sum-to-root condition. The
  paper's target (fast collapse to one digit) is a different question. It does
  not give a formula for T(10^12); that still comes from the A104113/A038206
  recursion.

```claim
id: partition-sum-invariant-mod9
statement: The partition-and-sum operation (insert plus signs into a base-b digit string and sum the blocks) is invariant modulo b−1: every split of a number n into contiguous blocks sums to a value congruent to n (mod b−1). In base 10 this is the digit-divisibility-by-9 principle. Consequently an S-number n = m^2 whose split sums to m satisfies m == m^2 (mod 9), i.e. m == 0 or 1 (mod 9), and every S-number is ≡ 0 or 1 mod 9.
hypotheses: base 10, contiguous decimal blocks read left to right; a block's value ≡ its digit string (mod 9).
holds-here: yes
status: sourced (Butler-Graham-Stong, arXiv:1501.04067 invariant; mod-9 congruence follows)
bearing: necessary-condition cross-check on candidate roots m (all A038206 roots and all A104113 S-numbers are ≡ 0 or 1 mod 9); pruning/verification only, not a method for T(10^12).
anchor: research/summaries/butler-graham-stong-partition-sum-body.md
```
