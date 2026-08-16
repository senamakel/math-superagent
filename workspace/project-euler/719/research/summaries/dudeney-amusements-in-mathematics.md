# Dudeney — Amusements in Mathematics (1917), Problem 113 "The Torn Number"

Source: https://www.gutenberg.org/cache/epub/16713/pg16713-images.html
(Project Gutenberg #16713; original: H. E. Dudeney, *Amusements in
Mathematics*, The Authors' Club, 1917 — public domain).
Full text: `research/sources/dudeney-amusements-in-mathematics.full.md`
(10,460 lines; problem 113 at line 1155, its solution at line 5602).

## What the primary text establishes (the historical origin of the two-block class)

Problem 113, "The Torn Number", is Dudeney's 1917 statement of the **two-block**
special case of Project Euler 719's S-number rule — a decade before Kaprekar.
A label bearing `3025` is torn in half into `30 | 25`; `30 + 25 = 55` and
`55² = 3025`. Puzzle: find another four-figure torn number with all digits
distinct.

The book's answer (solution, line 5602):
- The other such number is **9801** = 99², since `98 + 01 = 99`. (2025 also
  works, `20+25=45`, but is excluded by the all-distinct-digits condition.)
- **The general two-block solution (Dudeney's, 1917).** For a label of two
  halves of n figures each, the number of torn-number solutions is the product
  over the prime-power factors of `10^n − 1` (keeping powers of 3 together,
  and 1 counted as a constant-exponent factor) of `(exponent + 1)`. Solutions
  are recovered by factorising `10^n − 1` as `d × m` and solving the linear
  congruence `d·x ≡ ±1 (mod m)` — i.e. via the modular inverse of `d` modulo
  `(10^n − 1)/d`. Example n = 3: `10³ − 1 = 999 = 37 × 27`, giving solutions
  703² = 494209 and 297² = 088209 (leading-zero block preserved), plus the
  trivial 998|001 and 0…01 family.

## Bearing on PE 719

This is the **two-block** (Kaprekar-equivalent) special case — exactly the
unitary-divisor parametrisation later proved independently by Iannucci (see
`research/summaries/iannucci-kaprekar-numbers.md`, claim
`iannucci-kaprekar-divisor-formula`, and `dudeney-torn-number-two-block`). It
confirms that the two-block subcase is fully parametrised by the factors of
`10^n − 1` and is *strictly smaller* than the S-number set of PE 719, which
allows **3+ blocks** (e.g. 82² = 6724 = 6+72+4). This primary text is held as
the historical reference and problem-collection origin; **it is not the method
for T(10^12)** — that still comes from the arbitrary-block digit-partition
recursion over roots (A038206/A104113). The whole book is also the source of
many other classic digit puzzles (e.g. 114 Curious Numbers, 115 A Printer's
Error), none of which bears on T(10^12) directly.

```claim
id: dudeney-primary-torn-number
statement: Dudeney's Amusements in Mathematics (1917), Problem 113, is the original statement of the two-block torn-number class (30+25=55, 55^2=3025), with answer 9801 and a general count = product over prime-power factors of 10^n - 1 (other than 3) of (exponent+1), recovered via modular inverses — identical in content to the later Kaprekar/unitary-divisor theory and strictly a two-block subcase of the S-numbers.
hypotheses: decimal; two equal halves of the square's digit string summing to the root.
holds-here: yes, as the two-block subcase only; does not give T(10^12).
status: sourced (primary 1917 text)
bearing: historical origin and independent statement of the two-block subcase; cross-checks iannucci-kaprekar-divisor-formula; confirms multi-block generality is essential.
anchor: research/summaries/dudeney-amusements-in-mathematics.md
```
