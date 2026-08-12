# Goal

Solve Project Euler problem 185: **Number Mind**.

## Precise restatement

A secret sequence is a string of decimal digits. A *guess* is a digit string of
the same length as the secret, together with an integer reported as the number
of positions at which the guess agrees exactly with the secret (a digit that
appears in the secret but in a different position **does not count** — that is
the difference from Master Mind).

Let:

- `L` = length of the secret sequence (number of digits).
- `n` = number of guesses.
- `g_i` = the i-th guess, a string of `L` digits.
- `c_i` = the reported "correct" count for guess `i`: the number of positions
  `j` such that `secret[j] == g_i[j]`.

A candidate secret `s` satisfies the constraints iff
  `|{ j : s[j] == g_i[j] }| == c_i` for every guess `i`.

The task: find the unique secret `s` (given it is unique) satisfying all
constraints.

## Worked examples (test oracle)

Inline semantics check: sequence `1234`, guess `2036` → 1 correct
(only `3` at position 1 matches; the other three differ).

Main worked example: `L = 5`, six guesses:

```
90342 ;2
70794 ;0
39458 ;2
34109 ;1
51545 ;2
12531 ;1
```

The statement claims the unique satisfying secret is `39542`.

Main problem: `L = 16`, 22 guesses (listed in problem.md) → find the unique
16-digit secret.

## Completion criteria

- `code/brute.py` reproduces the 5-digit worked example (unique `39542`) and
  the inline `1234/2036` check. ✔ (confirmed 2025, `python code/brute.py`)
- A fast method is derived (`solution.md`), implemented (`solution.py`),
  agrees with brute.py on every case brute reaches, and produces the answer to
  the 16-digit case.
