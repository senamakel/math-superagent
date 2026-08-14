# GeeksforGeeks — count occurrences of digit in 1..n (place-value algorithm)

**Source:** https://www.geeksforgeeks.org/dsa/find-the-occurrences-of-y-in-the-range-of-x/ (GeeksforGeeks "Find the occurrences of a digit in the range of x", updated 2024). Full text: `research/sources/digit-count-place-value-algorithm.full.md`.

## What it establishes

- **Problem:** count total occurrences of digit d in all numbers 1..n (mod 10^9+7 in their statement, but the identity is exact).
- **Naive approach:** enumerate every number 1..n, string- or digit-scan each; O(n·log₁₀ n) time. Works only for small n — exactly what PE156 prohibits.
- **Expected approach (the one the run uses):** per-position contribution, O(len(n)·10) time with memoized Digit-DP, or the equivalent per-digit closed-form.
- Example in the source: n=25, d=2 → 9 occurrences ("2","12","20","21","22"(2),"23","24","25"); n=25, d=3 → 3. These are cross-check targets for any implementation.
- Complexity: O(number of digits) time, O(number of digits) space — independent of the magnitude of n's range.

## Implications for PE156

- Confirms from a standard algorithmic reference that the place-value identity (G1) is exact and O(#digits); matches `code/lib/digits.py::f_place_value` and the Khovanova–Marton §7 eq. (1).
- The naive approach is the exact shape of the method the run must NOT use at full size (enumerating to ~2·10^10 is prohibited); the closed form is the replacement.

## Does not settle

- Nothing about the solution set S_d, the bound d·10^10, or the search strategy; it is only the evaluation primitive. Use the Khovanova–Marton paper and OEIS catalogue for the rest.