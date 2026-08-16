# OEIS A238237 — two-block torn numbers

Source: https://oeis.org/A238237
Full text: `research/sources/oeis-A238237-torn-numbers.full.md` (the canonical
OEIS record page for this two-block class).

**Definition (two-block, equal halves).** A238237: "Numbers which when chopped
into two parts with equal length, added and squared result in the same
number." Example: 2025 = (20+25)² = 45²; 3025 = (30+25)² = 55²; 9801 =
(98+01)² = 99². Terms (starting 81, 2025, 3025, 9801, 494209, 998001, …).

**Structure (Sloane/Schott comments).** It is a variant of the Kaprekar
numbers A006886, and a *subsequence* of A102766 (all two-block Kaprekar
splits, not forcing equal halves). It is the special case of the two-block
split where the two parts have equal length (root's square has an even number
of digits). The three infinite subsequences are:
- {(10^m − 1)²} = A059988 \ {0} — e.g. 9801, 998001, 99980001, …
- {(10^m − 1)² · 10^(2m) / 4} = A350869 \ {0} — e.g. 2025 (m=1), 24502500, …
- {(10^m + 1)² · 10^(2m) / 4} = A038544 \ {1} — e.g. 3025 (m=1), 25502500, …

a(n) = A290449(n)² (the roots).

**Bearing on PE 719.** This is exactly the *two-block* (Kaprekar/torn) special
case of the general 2+-block S-number rule, restricted to equal-length halves
(so an even number of digits). It is a proper subset of the S-number set, which
allows any number of blocks. Its parametric form cannot give T(10^12); it
corroborates that the two-block theory is fully understood. It is the record
for this sub-variant, retained alongside A102766, A006886, Iannucci, and
Dudeney/Javaheri as part of the two-block theory tier, and it links Javaheri
(AMM 2025) and Kodrnja (KoG 29).
