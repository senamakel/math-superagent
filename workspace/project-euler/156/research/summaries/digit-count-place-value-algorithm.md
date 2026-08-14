# GeeksforGeeks — "Occurrences of a Digit in 1 to n" (place-value count)

**Source:** https://www.geeksforgeeks.org/dsa/find-the-occurrences-of-y-in-the-range-of-x/ . Full text: `[[digit-count-place-value-algorithm.full]]` — `research/sources/digit-count-place-value-algorithm.full.md`.

A standard DSA write-up of the digit-occurrence counting problem. Not a primary research source; it is a tutorial corroborating the same closed form the run already sources from Khovanova & Marton §7.

## What it establishes

- **Problem:** count occurrences of digit d in the decimal writings of all numbers 1..n inclusive; worked examples: n="25", d=2 → 9; n="25", d=3 → 3. (Same function as PE156's f(n,d) for d ∈ {1..9}: 0 contributes no nonzero digit.)
- **Naive approach:** loop 1..n, stringify, count — O(n·log₁₀ n) time, "will lead to TLE" for large n. This is precisely the oracle method `code/brute.py` uses for small ranges, and the method the bound n ≤ d·10^10 defeats.
- **Efficient approach (Digit DP with count and contribution):** per-position place-value decomposition with (higher, current, lower) at each factor = 10^i:
  - current < d: contribution higher·factor
  - current == d: higher·factor + lower + 1
  - current > d: (higher + 1)·factor
  O(len(n)) time, O(len(n)) space (memoized DP).
- This is the identical identity as `f_place_value` in `code/lib/digits.py` (which implements the equivalent `high*factor` / `high*factor+low+1` / `(high+1)*factor` branching), already computationally checked against the brute oracle (`claim G1-checked`).

## Hypotheses and hold-here

- Counts 1..n (not 0..n): holds for d ∈ {1..9} because 0 contributes no occurrence of any nonzero digit.
- d=0 handled via a `started` flag (skip leading zeros) — not needed for PE156.

## Implication for this run

Confirms `place-value-closed-form` by an independent tutorial treatment; adds nothing beyond it. The run's own verified implementation already matches it.

## Does not settle

Nothing about the *bound* on solutions (the article never discusses f(n,d)=n fixed points) and nothing about the sum. Not the answer source.

```claim
id: gfG-place-value-corroboration
statement: The GeeksforGeeks place-value/Digit-DP algorithm for counting occurrences of digit d in 1..n (per-position higher/current/lower branching: cur<d → high·f; cur==d → high·f+low+1; cur>d → (high+1)·f) gives the same O(#digits) closed form as Khovanova–Marton §7 eq. (1) and as code/lib/digits.py::f_place_value.
hypotheses: d ∈ {1..9}; counting 1..n equals counting 0..n for nonzero d.
holds-here: yes (d in 1..9, decimal base)
status: asserted (tutorial, no proof; corroborates a form already verified computationally by G1-checked)
bearing: independent corroboration of the closed form; no new bound or sum information.
anchor: research/sources/digit-count-place-value-algorithm.full.md
```
