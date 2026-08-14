# LearnYard — "Count the occurrences of digit 1 in all numbers from 1 to n"

**Source:** https://read.learnyard.com/dsa/count-the-occurrences-of-digit-1-in-all-numbers-from-1-to-n-solution-in-c-java-python-js/ . Full text: `[[digit-one-occurrence-learnyard.full]]` — `research/sources/digit-one-occurrence-learnyard.full.md`.

A tutorial page (part of a large DSA course index) solving the LeetCode-style problem "count occurrences of digit 1 in 1..n". The bulk of the captured text is site navigation; the useful content is the two algorithms.

## What it establishes

- **Problem:** count '1' occurrences in all numbers 1..n; examples n=13 → 6, n=100 → 21, n=11 → 4; constraint n ≤ 10^9.
- **Brute force:** loop 1..n, stringify, count — O(n·d) time; "not feasible" for n ≤ 10^9. Same message as GeeksforGeeks and `code/brute.py`.
- **Optimal (per-place):** with factor = 10^i, higher = n//(factor·10), current = (n//factor)%10, lower = n%factor:
  - current == 0: count += higher·factor
  - current == 1: count += higher·factor + lower + 1
  - current > 1: count += (higher+1)·factor
  O(log n) time, O(1) space.
- Worked example n=315: ones place (higher=32, current=5>1) → 32; tens place (higher=3, current=1) → 3·10+5+1 = 36; hundreds (higher=0, current=3>1) → 100; total 168. This is exactly the identity in `code/lib/digits.py::f_place_value`.

## Hypotheses and hold-here

- Digit fixed to 1, counts 1..n. For PE156 (d ∈ {1..9}, counting 0..n) the same per-place formula holds per digit; the article's restriction to d=1 is a presentation choice.
- d=0 case (leading zeros) not treated; not needed for PE156.

## Implication for this run

Third independent tutorial corroboration of the closed form (with GeeksforGeeks and Khovanova–Marton §7). No bound, no fixed-point theory, no sums.

## Does not settle

Nothing about f(n,d)=n solutions or their sum. Not the answer source.

```claim
id: learnyard-place-value-corroboration
statement: LearnYard's per-place digit-1 count (current==0 → high·f; current==1 → high·f+low+1; current>1 → (high+1)·f) matches the closed form verified as G1-checked; O(log n) time, O(1) space.
hypotheses: decimal base, digit 1, counting 1..n (equivalent to 0..n for nonzero d).
holds-here: yes
status: asserted (tutorial, worked example n=315 → 168; corroborates G1-checked)
bearing: corroboration only; no new bound or sum information.
anchor: research/sources/digit-one-occurrence-learnyard.full.md
```
