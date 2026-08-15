# Hand-check: G-supply-transfer is FALSE on the consecutive-odds family

## The claim being attacked (research/BACKWARD.md, `G-supply-transfer`)

> For every successful 2-then-odds prefix q_1..q_n (q_1=2, q_2=3, q_j strictly
> increasing odd, all gaps even), let
>   w(n) = #{ j in [2, n-1] : q_{j+1} - q_j ≡ 2 (mod 4) }
> (Hamming weight of the halved-gap window), and let nu2(q_n) be the number of
> 2s in the maximal {0,2} suffix of the right diagonal delta(q_n).
> Then  nu2(q_n) >= (2/3) * w(n).

This is the S1/G-supply-transfer *transfer* inequality that the run's
supply-side decomposition rests on.  Below it is refuted on the simplest
successful family, which decides the S1 fork in case (b).

## The counterexample: consecutive odds, q = (2,3,5,7,9)  (n = 4)

Consecutive odds is a **successful** Gilbreath class (settled
`R2-consecutive-odds-class`: A_k(0) = 1 for all k), and every gap after the
first is 2 ≡ 2 (mod 4).

The triangle:
```
A_0 = (2, 3, 5, 7, 9)
A_1 = (1, 2, 2, 2)
A_2 = (1, 0, 0)
A_3 = (1, 0)
```

Right diagonal through q_4 (delta_k = A_k(4-k), k = 0..3):
```
delta = ( A_0(4), A_1(3), A_2(2), A_3(1) ) = ( 9, 2, 0, 0 )
```

**w(4)** = #{ j in [2,3] : gap_j ≡ 2 mod 4 }.  gaps g_j = q_{j+1}-q_j:
g_2 = 7-5 = 2, g_3 = 9-7 = 2, both ≡ 2 mod 4.  So **w(4) = 2**.

**nu2(4)** = number of 2s in the maximal {0,2} suffix of delta.
- literal reading (suffix extends left through the 2): suffix = (2, 0, 0),
  nu2 = 1.
- run's convention in code/gap_analysis/nu2_vs_gap_parity.py (tail =
  d[2:-1], excluding delta_1): nu2 = 0.

Either way,
```
nu2  <= 1   <  (2/3)*w(4)  =  (2/3)*2  =  4/3
```
so **nu2 >= (2/3)*w FAILS at n = 4** for the successful consecutive-odds
prefix (2,3,5,7,9).  (With the run's nu2=0 it fails for every n >= 4.)

## Why this is structurally inevitable, not a fluke

For consecutive odds, A_1 = (1, 2, 2, 2, ...) and every adjacent pair is
(2,2), so A_2 = (1, 0, 0, 0, ...) and every later row is (1, 0, 0, ...).
The right diagonal is therefore (2n+1, 2, 0, 0, ..., 0): the {0,2} suffix is
essentially all zeros and nu2 is 0 (or a single 2).  Meanwhile w = n-2 is
linear.  So the "transfer" nu2 >= c*w says a large count of gaps ≡ 2 mod 4
forces a large number of 2s in the diagonal's {0,2} suffix — but the
consecutive-odds family has maximal gap uniformity and *zero* such 2s.

Hence the halved-gap Hamming weight w does NOT lower-bound nu2 in any
successful 2-then-odds class.

## Consequence for the supply-side decomposition (the S1 fork)

The fork in `S1-nu2-transfer-weight`:
- (a) UNIVERSAL: nu2 >= w/2 for all halved-gap bit strings h  <-- FALSE here.
- (b) PRIME-SPECIFIC: holds only for the prime bit string.

The all-ones bit string h (consecutive odds) refutes (a): nu2=0 but w = n-2.
So the fork lands on **(b)**, and G-supply-transfer as a *universal*
combinatorial transfer is FALSE.  The decomposition nu2 >= c*w is therefore
NOT a reduction for the general successful class: it does not discharge the
number-theoretic content (the primes' gap irregularity) to a clean F2 weight
inequality.  This is the honest negative result the fork asked for: the
supply side has no universal combinatorial shortcut.

## How this was checked
Hand arithmetic on the explicit triangle above (n = 4), plus the same argument
for general n.  Consistent with the run's own nu2_vs_gap_parity convention
which reports nu2=0 for this family while w grows linearly.  The claim's own
"first step" asked to exhaust all bit strings — the all-ones string is in that
exhaustive set and is the counterexample.

AGENTS housekeeping: this is a derivation note; a claim block is recorded
below in the write-up.
