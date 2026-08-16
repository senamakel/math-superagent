# OEIS A006886 — Kaprekar numbers (two-block)

Source: https://oeis.org/A006886
(`research/sources/oeis-A006886-kaprekar.full.md`, b-file in
`oeis-A006886-kaprekar-full.full.md`).

**Definition.** n is a Kaprekar number: n = q + r and n² = q·10^m + r for some
m ≥ 1, q ≥ 0, 0 ≤ r < 10^m, with n ≠ 10^a (a ≥ 1). Terms: 1,9,45,55,99,297,703,
…  Digital root is 1 or 9.

**Bearing on PE 719.** This is the **two-block** special case: the S-number rule
allows 2+ blocks, of which exactly-two-blocks are the Kaprekar numbers. So the
Kaprekar numbers are a *subset* of the S-number roots and their machinery (the
unitary-divisor formula, `berg` Iannucci) does not solve the general problem.
E.g. 82 (6724 = 6+72+4) and 91 (8281 = 8+2+81) are S-roots requiring 3 blocks,
so they are not two-block Kaprekar numbers.

```claim
id: a006886-kaprekar-subset
statement: Kaprekar numbers (two-block) form a proper subset of the S-number roots; the S-number 2+-block rule is strictly more general, so Kaprekar generation formula cannot give T(10^12).
hypotheses: base 10, definitions as stated.
holds-here: yes
status: asserted (OEIS definition + contrast with A038206 term list)
bearing: rules out the Kaprekar divisor route as the method; recursion needed.
anchor: research/summaries/oeis-A006886-kaprekar.md
```

**Does not help** give the answer: restricted to two blocks. Supplementary
context only.
