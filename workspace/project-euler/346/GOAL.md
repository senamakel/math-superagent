# Goal

**Problem: Project Euler 346 — Strong Repunits**

## Precise restatement

A **repunit** in base `b` is a positive integer whose base-`b` representation
is a string of only `1`'s:

```
R_k(b) = 1 + b + b^2 + ... + b^(k-1) = (b^k - 1)/(b - 1),   k >= 1, b > 1
```

- `k = 1` gives `R_1(b) = 1`: the single-datum "1", a repunit in *every* base.
- `k = 2` gives `R_2(b) = 1 + b = b + 1`: every `n >= 3` is the two-digit
  repunit `11` in base `b = n - 1`.

A **strong repunit** is a positive integer `n` that is a repunit in **at least
two** distinct bases `b > 1`.

## Worked examples (the test oracle)

- There are **8** strong repunits below 50:
  `{1, 7, 13, 15, 21, 31, 40, 43}`.
- The sum of all strong repunits below 1000 equals **15864**.

## Target

Compute the sum of all strong repunits `n < 10^12`.

## Completion criteria

1. `code/brute.py` reproduces both worked examples (done: matched).
2. `solution.py` agrees with `code/brute.py` on every case brute can reach and
   reproduces both examples.
3. `solution.py` returns the sum for the `10^12` bound, verified by an
   independent route.
