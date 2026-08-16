# Kaprekar numbers (Wikipedia) — the two-block special case

Source: https://en.wikipedia.org/wiki/Kaprekar_number
(`research/sources/kaprekar-number-wikipedia.full.md`).

**Definition.** A p-Kaprekar number k in base b: the representation of k² in
base b can be split into two parts, the right part having p digits, that add up
to k. In base 10 a Kaprekar number needs only the two-block split of k² into
left a and right r (≤ some 10^m) with k = a + r; the Wikipedia article states
it via unitary divisors of 10^m − 1 (Iannucci's correspondence, see the Iannucci
note).

**Bearing on PE 719.** These are *strictly a special case*: an S-number is the
2-or-more-block generalisation, and a root m is an S-number root whether or not
the witnessing split is exactly two blocks. Examples from Kaprekar that are also
S-roots: 9²=81 (8+1), 45²=2025 (20+25), 297²=88209 (88+209). But S-numbers are
not limited to two blocks — e.g. 6724 splits 6+72+4 into three blocks, so 82 is
an S-root but the two-block Kaprekar machinery does not capture it.

```claim
id: kaprekar-two-block-subcase
statement: Kaprekar numbers are exactly the S-number roots whose witnessing split uses exactly two blocks; they are a proper subset of S-number roots for N >= 2025 (45) and the general S-rule (2+ blocks) is strictly larger.
hypotheses: base 10; definitions as above.
holds-here: yes
status: sourced (Wikipedia/A006886) — and directly visible in the term lists: e.g. 50, 7389 are S-roots in A038206 not in the two-block list.
bearing: do not solve PE 719 with Kaprekar machinery alone; use the full 2+-block recursion.
anchor: research/summaries/kaprekar-number-wikipedia.md
```

**Does not help** by giving the answer: it only covers two-block splits. It is
supplementary context that S-numbers generalise Kaprekar numbers, confirming the
multi-block recursion is required.
