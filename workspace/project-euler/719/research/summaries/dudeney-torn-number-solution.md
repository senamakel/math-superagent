# Dudeney — "The Torn Number", Amusements in Mathematics, 1917 (Problem 113)

Source: https://bookofproofs.github.io/branches/fun/dudeney/arithmetical-and-algebraic-problems/various-other-aa-problems/the-torn-number-solution.html
Full text: `research/sources/dudeney-torn-number-solution.full.md`
Problem statement: `research/sources/dudeney-torn-number.full.md`
Original: H. E. Dudeney, *Amusements in Mathematics*, The Authors' Club, 1917
(public domain; Project Gutenberg #16713).

**What this is.** The historical origin of the *two-block* case of the S-number
rule. A label bears a 4-figure number torn in half so 30 | 25 remain;
30 + 25 = 55 and 55² = 3025. Puzzle: find another 4-figure torn number with
four *distinct* digits. Answer: 9801 (98 + 01 = 99, 99² = 9801); 2025 is
excluded only by the all-distinct-digits condition.

**The general solution (Dudeney's, 1917 — the two-block split).** For a label
made of two halves of n figures each, the number of torn-number solutions is
the product over the prime-power divisors p^a of 10^n − 1 (other than the 3s,
with 1 counted as a constant-exponent factor) of (a + 1). The solutions are
recovered by factorising 10^n − 1 (keeping powers of 3 together) as d × m and
solving the linear congruence d·x ≡ ±1 (mod m) — i.e. by the modular inverse of
d modulo (10^n − 1)/d. Example: n = 3, 10³ − 1 = 999 = 37 × 27, solutions
703² = 494209 and 088209 (= 297² with leading zero block), plus the trivial
98|01 and 00|01 family.

**Bearing on PE 719.** This is exactly the Kaprekar-number construction already
in the library (claim `iannucci-kaprekar-divisor-formula`, `kaprekar-two-block-subcase`),
rediscovered by Dudeney a decade before Kaprekar and framed as a puzzle. It
confirms that the two-block special case is fully parametrised by unitary
divisors of 10^n − 1 and therefore *cannot* be the whole of the S-number set
(which allows 3+ blocks). It is the historical reference, not the method, and
must not be leaned on for T(10^12).

```claim
id: dudeney-torn-number-two-block
statement: A torn number (two-block split of a 2n-figure square into halves summing to the root) is parametrised by the multiplicative structure of 10^n − 1: the count is the product of (exponent+1) over prime-power factors other than 3, matching the Iannucci unitary-divisor formula. It is exactly the Kaprekar (two-block) subcase and is strictly smaller than the S-number set, which allows 3+ blocks.
hypotheses: decimal, two equal halves (n figures each), sum of halves equals root.
holds-here: yes, but it is the two-block subcase only — cannot give T(10^12).
status: asserted (historical source; matches independently-proved iannucci formula)
bearing: cross-checks the two-block subcase; confirms multi-block generality is essential.
anchor: research/summaries/dudeney-torn-number-solution.md
```
