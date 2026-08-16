# Brute-force oracle — reproduced the statement's worked examples and T(10^4)

Source: `code/brute.py` run by tool_builder, output in `code/out/brute.txt`.

The naive oracle enumerates, for each root m in [2, isqrt(N)], every partition
of the digit string of m^2 into 2+ contiguous non-empty blocks and checks
whether any sums to m. Exact integer arithmetic expected (Python ints; each
block's value is recovered from its digit string). This is the definition
itself, so it is the ground truth the efficient solver is checked against.

**What it established (output reproduced in brute.txt):**
- The four worked examples 81, 6724, 8281, 9801 all test True with the
  statement's own witness splits (e.g. 8281 splits both (8,2,81) and
  (82,8,1)).
- T(10^4) = 41333, and the ≤10^4 S-number set is exactly
  {81,100,1296,2025,3025,6724,8281,9801,10000} from roots
  9,10,36,45,55,82,91,99,100 — matching the statement oracle and the A104113
  term list.
- T(10^6) = 10804656, T(10^12) = 128088830547982 (reached by the memoised
  recursive route `is_s_number_rec`, an independent code path over the same
  definition).

```claim
id: snumber-sum-oracle
statement: The brute-force oracle in code/brute.py reproduces the statement's four worked examples (81,6724,8281,9801) as S-numbers with the statement's witness splits, and reproduces T(10^4)=41333 with the S-number set {81,100,1296,2025,3025,6724,8281,9801,10000}.
hypotheses: S-number definition as in problem.md/GOAL.md; exact integer arithmetic; base 10; root m starts at 2 so n=1 is excluded.
holds-here: yes
status: checked (brute.py output code/out/brute.txt, CHECK line PASS)
bearing: ground-truth oracle that every candidate solver (solution.py and the b-file route) must agree with; the thread split_and_sum_search rests on it.
anchor: code/out/oracle.md
```
