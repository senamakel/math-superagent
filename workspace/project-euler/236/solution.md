# PE236 — Luxury Hampers: derivation and result

## Result
The largest rational m > 1 for which all six spoilage equalities hold is

**m = 123/59** ≈ 2.0847.

There are exactly 35 such values; the smallest is 1476/1475 (the statement's
oracle), and the largest is 123/59. Verified by three independent programs.

## Notation
- i = 1..5 products in table order.
- a_i, b_i = counts supplied by A and B of product i.
- s_i, t_i = counts that spoiled for A and B (1 ≤ s_i ≤ a_i, 1 ≤ t_i ≤ b_i).
- SA = Σa_i, SB = Σb_i.
- m = p/q, a reduced rational > 1.

Six equalities must hold:
1. per product i, B's rate worse than A's by m:  t_i/b_i = m·s_i/a_i
2. overall, A's rate worse than B's by the same m:  Σs/SA = m·Σt/SB

## Data (given)
| i | product            | a_i  | b_i  |
|---|--------------------|------|------|
| 1 | Beluga Caviar      | 5248 | 640  |
| 2 | Christmas Cake     | 1312 | 1888 |
| 3 | Gammon Joint       | 2624 | 3776 |
| 4 | Vintage Port       | 5760 | 3776 |
| 5 | Champagne Truffles | 3936 | 5664 |

SA = 18880, SB = 15744.

## The structural reduction (the governing fact)
From the per-product condition, s_i/t_i = (a_i·q)/(b_i·p).  Let
g_i = gcd(a_i·q, b_i·p) and (c_i, d_i) = (a_i·q/g_i, b_i·p/g_i), the coprime
minimal pair.  Then every feasible (s_i, t_i) equals k_i·(c_i, d_i) for an
integer multiplier, and the box constraints allow 1 ≤ k_i ≤ K_i where

    K_i = min(a_i//c_i, b_i//d_i) = g_i // max(p, q).

So per-product feasibility is exactly the **gcd threshold** g_i ≥ max(p, q).

The overall equality clears denominators to an exact bounded subset sum:

    Σ_i k_i · (q·SB·c_i − p·SA·d_i) = 0,   1 ≤ k_i ≤ K_i.

Because m solves product 1's condition, m = a_1·t/(b_1·s) for some pair; the
candidates are the distinct reduced fractions of a_1·t/(b_1·s) with value > 1.
For each candidate the gcd thresholds and the subset sum decide validity.

Complexity: the candidate set is O(a_1·b_1) gcds over the fixed input data
(not over any m-bound); per candidate 5 gcds and, only for candidates passing
all thresholds, a subset sum over sets bounded by K_1·…·K_5. Nothing scales
with the size of the answer space.

## Why the naive bound-24000 enumeration is wrong and this is right
A brute enumeration over every integer spoilage count up to the supply sizes
is exponential in the data. The reduction replaces that with (a) a fixed-size
candidate set obtained from one product's condition, and (b) per-candidate
gcd tests plus a 5-term bounded subset sum. The 35 values all fall out of this
without ever visiting the spoilage-count space.

## Implementation
- `code/lib/pe236.py` — shared exact machinery: base_set, per_product (gcd
  threshold, c/d/K), overall_feasible (subset sum), reconstruct_ks,
  literal_witness.
- `code/solution.py` — the derived solver: builds candidates from product 1,
  filters by feasibility, asserts 35 / 1476/1475 / 123/59, and literally
  checks the six equalities for the largest with fractions.Fraction.

## Verification (three independent routes, all agree)
`python code/solution.py`    → EXIT 0; asserts pass; COUNT=35, MIN=1476/1475,
                               MAX=123/59; literal six-equality Fraction check
                               passes on the largest (witness s=[413,1,1,30,10],
                               t=[105,3,3,41,30], m=123/59).
`python code/brute.py`       → naive oracle; COUNT=35, MIN=1476/1475,
                               MAX=123/59; the 35-value list is identical.
`python code/verify_oracle.py`→ independent recomputation from a different base
                               product + explicit witness satisfying all six
                               equalities for every one of the 35 values;
                               sets equal True; smallest/largest reconfirmed.

The literal Fraction check proves the per-product equalities
t_i/b_i = (123/59)·s_i/a_i for each i and the overall equality
Σs/SA = (123/59)·Σt/SB, holding with the explicit integer witness — so
m = 123/59 is a genuine solution, not a sampled value. Since the three
programs enumerate all valid m by independent routes and both reachable
enumerations return exactly the same 35 and the same largest, 123/59 is the
largest m > 1.
