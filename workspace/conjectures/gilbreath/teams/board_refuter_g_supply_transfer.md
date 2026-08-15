# Refuter report — G-supply-transfer refuted

## Statement attacked
`G-supply-transfer` (research/BACKWARD.md, `nu2-supply-split`): for every
successful 2-then-odds prefix q_1..q_n, nu2(q_n) >= (2/3)·w(n), where
w(n) = #{j in [2,n-1] : gap_j ≡ 2 mod 4} and nu2 = # of 2s in the maximal
{0,2} suffix of the right diagonal delta(q_n).

## Why this one
The run's own note flags the S1 fork: is the transfer universal (case a) or
prime-specific (case b)? If (b), the supply decomposition does not reduce
difficulty. The simplest successful family (consecutive odds) is exactly the
all-ones halved-gap bit string that tests the universal claim.

## Answer: refuted (by hand, exact arithmetic)
Success prefix (2,3,5,7,9), n=4:
```
A_0 = (2,3,5,7,9)
A_1 = (1,2,2,2)
A_2 = (1,0,0)
A_3 = (1,0)         <- bottom entry 1, so successful
```
delta(q_4) = (9,2,0,0); {0,2}-suffix (2,0,0) → nu2 = 1 (literal) or 0 (the
run's tail convention d[2:-1]).  w = #{j in [2,3]} = 2 (gaps 2,2 both ≡2 mod4).
(2/3)w = 4/3 > nu2.  **FALSE.**

Structural: every consecutive-odds prefix n≥4 has nu2=0 while w=n-2 — a whole
family, not one instance.

## Four-answer status
`find_counterexample` returned **undecided** on both the `$int` arithmetic
encoding and a relational encoding. This environment's model finder cannot
interpret arithmetic (documented in the run's own
`cb_dying_pair_statement.md`: it returns `undecided` on every refutable
encoding here). So the result rests on exact hand arithmetic, fully written
out above, cross-checked against the settled class `R2-consecutive-odds-class`
and the exact nu2 convention in `code/gap_analysis/nu2_vs_gap_parity.py`.

## What it means
Decides the S1 fork to **(b) prime-specific**: nu2 >= c·w is not a universal
combinatorial transfer. The supply-side decomposition cannot offload the
number-theoretic content to a clean F2 weight inequality. The primes still
measure nu2/w ≈ 0.69-0.87, so Route B's *supply statement* is not dead — it
is just not a universal identity; it is a claim about the particular prime bit
string.

## Not touched
The core conjecture, the step law, the recharge identity, and Lemma 5.4 (a
sufficiency budget 2*nu2+2, unaffected) are all untouched by this refutation.
