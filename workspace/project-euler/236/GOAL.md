# Goal — Project Euler 236, Luxury Hampers

## Objective
Find the largest rational m > 1 for which the following holds simultaneously,
for the five products with supplies (a_i, b_i) below.

## Symbols
- i = 1..5, product index.
- a_i = number of product i supplied by A; b_i = number supplied by B.
- s_i = number of product i that spoiled for A; t_i = number spoiled for B.
  Integers with 1 ≤ s_i ≤ a_i, 1 ≤ t_i ≤ b_i (spoilage counts are positive).
- Per-product spoilage rate for a supplier = (count spoiled)/(count supplied).
- Overall spoilage rate  = (Σ count spoiled)/(Σ count supplied).

Supply table (given):

| i | product            | a_i  | b_i  |
|---|--------------------|------|------|
| 1 | Beluga Caviar      | 5248 | 640  |
| 2 | Christmas Cake     | 1312 | 1888 |
| 3 | Gammon Joint       | 2624 | 3776 |
| 4 | Vintage Port       | 5760 | 3776 |
| 5 | Champagne Truffles | 3936 | 5664 |

## Conditions for a valid m
1. Per product: B's rate is worse than A's by factor m (m > 1):
   t_i / b_i = m · (s_i / a_i), equivalently s_i/t_i = (a_i/b_i)/m, for every i.
2. Overall: A's rate is worse than B's by the SAME factor m:
   (Σ s_i)/(Σ a_i) = m · (Σ t_i)/(Σ b_i), i.e. overall (Σs)/(Σa) = m·(Σt)/(Σb).

Equivalently for the reciprocals (B worse per product, A worse overall):
per-product  s_i/t_i = (a_i b-ratio)/m ;  overall (Σt)/(Σb) = m·(Σs)/(Σa).

## Worked examples (the test oracle)
Statement gives: there are THIRTY-FIVE values of m > 1 for which this holds;
the smallest is m = 1476/1475. Oracle = reproduce count 35 and smallest 1476/1475.
Final answer = the largest of these 35, as a reduced fraction u/v.

## Completion criteria
- [x] code/brute.py (naive oracle) reproduces 1476/1475 and the count 35.
- [x] code/solution.py (derived method, exact arithmetic) agrees with brute.py and
      finds the largest m at full size, verified by an independent route.
      EXECUTED: asserts pass (35, 1476/1475, 123/59) + literal six-equality check.
- [x] Answer reported as reduced fraction u/v = **123/59**.
