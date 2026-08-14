# LearnYard — count occurrences of digit 1 in all numbers from 1 to n

**Source:** https://read.learnyard.com/dsa/count-the-occurrences-of-digit-1-in-all-numbers-from-1-to-n-solution-in-c-java-python-js/ (LearnYard DSA "Math Basics" tutorial). Full text: `research/sources/digit-one-occurrence-learnyard.full.md`.

## What it establishes

- **Problem:** count occurrences of digit '1' in all numbers 1..n (constraint n ≤ 10^9).
- **Brute force:** iterate 1..n, string-scan each; O(n·d) time with d ≈ number of digits. Stated explicitly as infeasible for n up to 10^9 ("iterating through all numbers from 1 to n ... is not feasible").
- **Optimal (per-position) algorithm** — the same identity the run uses. For each place value `factor = 1, 10, 100, ...`, with
  higher = n // (factor·10), current = (n // factor) % 10, lower = n % factor:
  - current == 0: count += higher · factor
  - current == 1: count += higher · factor + lower + 1
  - current > 1: count += (higher + 1) · factor
  The loop runs while n // factor > 0; **O(log n) time, O(1) space**, exact integer arithmetic.
- **Worked examples (cross-check targets):** n=11 → 4; n=13 → 6; n=100 → 21; step-by-step n=315 → 168.
- The three-case formula above is the digit-d=1 specialization of G1; the d>1 variant replaces the `current==1` and comparison logic with `current<d / ==d / >d` (as in `code/lib/digits.py`), which is the exact G1 identity.

## Implications for PE156

- Independent tutorial confirmation of the place-value closed form and its O(log n) cost — same structure as Khovanova–Marton §7 eq. (1) and the math.SE analytic form.
- The brute-force/O(n·d) approach they reject at n=10^9 is precisely the method prohibited for PE156 at ~2·10^10; the per-position algorithm is the evaluation primitive for the skip-search.

## Does not settle

- Nothing about fixed points, the bound d·10^10, or the skip-search; it is only the counting primitive, and only for d=1 (generalization to other d is immediate but not stated there).