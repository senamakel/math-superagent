# Goal

## Objective

Solve Project Euler problem 1006: compute `Psi(10^18) mod 101001001`, where `Psi` is
defined as follows.

## Restatement, every symbol defined

Let `S_0 = "0"`, `S_1 = "01"`, and for `n >= 2` let `S_n = S_{n-1} S_{n-2}`
(concatenation). Thus `S_2 = "010"`, `S_3 = "01001"`, `S_4 = "01001010"`, ...

A **Fibonacci subword** is a contiguous substring (factor) of some `S_n`.

FACT (given in the statement, and the key structural input): for each positive
integer `k`, there are exactly `k+1` distinct Fibonacci subwords of length `k`.

Each such length-`k` subword is a binary string; interpret it as a decimal number,
ignoring leading zeros (so a string beginning with `0` is read from its first `1`).
Let `Psi(k)` be the sum of the squares of these `k+1` values.

### Worked examples (test oracle)

- Length 3. The four distinct Fibonacci subwords of length 3 are
  `001, 010, 100, 101`.
  - `001` -> 1
  - `010` -> 10
  - `100` -> 100
  - `101` -> 101
  - `Psi(3) = 1^2 + 10^2 + 100^2 + 101^2 = 1 + 100 + 10000 + 10201 = 20302`. ✓
- `Psi(10) = 10699667 (mod 101001001)`. ✓ (given)

### Target

`Psi(10^18) mod 101001001`.

## Completion criteria

1. `code/brute.py` reproduces `Psi(3) = 20302` and `Psi(10) = 10699667 (mod 101001001)`
   by direct enumeration of distinct length-`k` substrings over finite `S_n`.
2. `code/solution.py` computes `Psi(10^18) mod 101001001` with exact integer arithmetic
   using a method whose cost does NOT grow with `k = 10^18` (poly(log) or closed form).
3. `solution.py` agrees with `brute.py` on every reachable case, and the final answer
   is verified by an independent route.
