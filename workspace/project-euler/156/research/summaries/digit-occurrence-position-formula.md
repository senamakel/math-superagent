# GeeksforGeeks — "Occurrences of 2 as a Digit in 0 to n" (per-position identity for digit 2)

**Source:** original URL https://www.geeksforgeeks.org/dsa/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/ (a redirect of the 2017 article http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/). This library holds a Wayback capture of the 2017 original: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/ . Full text: `research/sources/digit-occurrence-position-formula.full.md`.

A standard DSA tutorial on counting digit-2 occurrences in 0..n inclusive, by per-position (place-value) analysis rather than enumeration.

## What it establishes

- For each digit position d (0 = units), total occurrences of digit 2 at that position across 0..n is computed from the higher part `high` and the lower part `low` of n:
  - current digit `cur < 2`:  (round n down to the next multiple of 10^(d+1)) / 10  → `high·10^d`
  - current digit `cur == 2`: `high·10^d + (low + 1)`
  - current digit `cur > 2`:  `(high + 1)·10^d`
- Worked examples: n = 22 → 6 (numbers 2, 12, 20, 21, 22, the last contributing two 2s); n = 100 → 20.
- Complexity: O(log n) time, O(1) space.

## Bearing on PE156

- Independent tutorial-level corroboration of claim `G1-digit-count-closed-form` for digit 2, from a different formulation than the already-held GfG "Occurrences of a Digit in 1 to n" (Digit-DP) page. Its worked example f(22,2) = 6 is exactly the value the run's oracle checked (`G1-checked`). The three-case identity generalizes verbatim to any nonzero digit d by replacing 2 with d.
- Not a primary source; the authoritative treatment is Khovanova–Marton (arXiv:2305.10357 §7 / AMM 132(8) 2025).

## Does not settle

- Does not address the fixed-point equation f(n,d)=n, its finiteness, or bounds on solutions.