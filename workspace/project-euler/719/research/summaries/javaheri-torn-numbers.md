# Javaheri — On 2025 and Other Torn Numbers

Source: https://doi.org/10.1080/00029890.2025.2561491
(American Mathematical Monthly Vol. 133, No. 5, 2026; Mohammad Javaheri, Siena College).
`research/sources/javaheri-torn-numbers.full.md`.

## Accessibility caveat

The Taylor & Francis capture is **abstract-only (paywalled)** — the file holds the
title, abstract, MSC classification (11A99; MaRDI lists 11A63 Radix
representation and digital problems) and acknowledgements, but no proofs,
theorems, or body. Anyone needing the mathematics must fetch the full text via
the DOI with institutional access. Verified: no open PDF of the body is readily
available (MaRDI portal and the publisher both gateway the DOI behind login).

## What the abstract establishes

A **torn number** is a perfect square that is a fixed point of split-add-square:
tear k² in half as p and q (so k² = p·10^m + q), add p + q = k, square to get
k². 2025 = 45², 20 + 25 = 45. The abstract states:
- there are at least 2^μ(k) − 1 2k-digit torn numbers, k ≥ 1, where μ(k) is the
  number of prime factors of 10^k − 1;
- the split-add-square procedure has infinitely many periodic points of any
  arbitrary period.

## Bearing on PE 719

"Torn numbers" are precisely the **two-block** split (tear in half exactly two
parts), which is the Kaprekar-number subcase — not the 2+-block S-number rule.
The 2^μ(k) − 1 count over prime factors of 10^k − 1 is the same unitary-divisor
structure as Iannucci's correspondence (Kaprekar numbers ↔ unitary divisors of
10^n − 1). So this paper does **not** give a method for the multi-block
T(10¹²); it corroborates that the two-block (Kaprekar) theory is well understood
and count-limited, reinforcing that the general problem needs the digit-partition
recursion over arbitrary block counts.

**Does not help** with the answer directly; retained as the most recent AMM
treatment of the surrounding (two-block) class. Read the abstract here; for the
body, obtain the DOI-hosted full text.
