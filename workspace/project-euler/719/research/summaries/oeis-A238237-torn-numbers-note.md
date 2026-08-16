```claim
id: a238237-torn-number-record
statement: A238237 lists the torn numbers: perfect squares whose decimal string splits into exactly two equal-length halves p,q with (p+q)^2 = n; a(n) = A290449(n)^2, and A238237 ⊂ A102766 ⊂ A104113. The torn rule (two equal blocks, sum squared) is a proper subcase of the PE 719 S-rule (k>=2 blocks of any length summing to the root).
hypotheses: base 10; exactly-two equal-length halves.
holds-here: yes, as the boundary case k=2 of equal halves; it bounds the two-block theory, not the general T(10^12).
status: catalogued (OEIS A238237).
bearing: confirms the two-block (Kaprekar/torn) class is a proper subset and gives no closed form for the general multi-block problem.
anchor: research/summaries/oeis-A238237-torn-numbers-note.md
```

# OEIS A238237 — Torn numbers (the two-block split-and-square class)

Source: https://oeis.org/A238237 (canonical encyclopedic record; internal format also
retrieved). Full retrieved text is at `research/summaries/oeis-A238237-torn-numbers.md`
(the download landed there rather than as a separate `.full.md` in sources/).

## What the record establishes

A **torn number** is a perfect square that, chopped into two equal-length halves
`p` and `q`, satisfies `(p + q)^2 = n`. Terms:
81, 2025, 3025, 9801, 494209, 998001, 24502500, 25502500, 52881984, 60481729,
99980001, 6049417284, … (squares of A290449 roots).

Sloane's comment: "Yet another variant of the Kaprekar numbers [A006886]."

Bernard Schott isolates three infinite subfamilies:
- `{(10^m − 1)^2, m ≥ 1}` = A059988 \ {0}; e.g. 9801 = 99² = (98+01)².
- `{(10^m − 1)² · 10^{2m} / 4, m ≥ 1}` = A350869 \ {0}; e.g. 2025 = 45² = (20+25)².
- `{(10^m + 1)² · 10^{2m} / 4, m ≥ 1}` = A038544 \ {1}; e.g. 3025 = 55² = (30+25)².

Formula: `a(n) = A290449(n)²`. A238237 is a subsequence of A102766 (chopped into
two parts of *any* length). Crossrefs: A006886 (Kaprekar), A102766, A290449 (roots),
A350869, A350870, A059988, A038544. Example checks: 2025 = (20+25)², 3025 = (30+25)²,
9801 = (98+01)² — the "01" block read as integer 1.

## Bearing on PE 719

Torn numbers are precisely the **two-block** split-and-sum class: the decimal string
split into exactly two equal-length blocks whose (sum)² = the number. This is a
*proper subcase* of this run's S-numbers (PE 719), which allow **any number k ≥ 2 of
blocks of any length** whose blocks *sum to the root* (not whose sum, squared, equals
the number). Concretely, 3025 = (30+25)² is a torn number *and* an S-number (30+25 =
55 = its root), but an S-number like 81 = 9² = 8+1 (single 9² is 81) uses unequal
blocks and parity of block-count; more decisively, the S-class allows three-plus-block
splits (e.g. 8281 = 8+2+81) that the equal-two-block torn rule cannot express.

So A238237 gives the count/structure of the two-block subclass only — the same
bound as the Kaprekar/torn theory already in the library (Javaheri's 2^μ(k) − 1
count; Iannucci's unitary-divisor correspondence). It does **not** parametrise the
general multi-block T(10^12); that needs the digit-partition recursion
(`a038206-expr-recursion`). Record retained as the canonical encyclopedic name for
the torn-number subclass, and because both Javaheri (AMM 2025) and Kodrnja (KoG
2025) cite A238237 as the record for the class.
