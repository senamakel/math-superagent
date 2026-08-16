# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **chisel**: PE622 synthesis from the converging round: the Möbius-inversion route and the existing inclusion-exclusion skeleton are term-for-term the SAME at k=60, not competitors. μ(60/d)≠0 iff d is an even divisor of 60 (60=2²·3·5), giving the 8-term sum over d∈{2,4,6,10,12,20,30,60} with signs +1 for {60,10,6,4}, −1 for {30,20,12,2}; the −1 terms are exactly σ(2^12−1), σ(2^20−1), σ(2^30−1), σ(3) and the +1 terms σ(N), σ(1023), σ(63), σ(15) — the inclusion-exclusion table. So adopting Möbius re-derives the skeleton's numbers from a general theorem, and the skeleton becomes the independent second check.… (refers: mobius-inversion-exponent-lattice, riffle-order-60)

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the goals ledger now carries it. Here is the report.

## Slug

`riffle-order-60` → `research/backward/riffle-order-60.md`

## What the skeleton claims

The goal is reduced to four steps, all combining by pure arithmetic at the end:

1. **Bijection.** `s(n) = 60` ⟺ `ord_{n−1}(2) = 60`, and every such `m = n−1` is odd (it divides `2^60−1`), so `Σn = C + S` where `C = #{m : ord_m(2)=60}`, `S = Σ{m : ord_m(2)=60} m`.
2. **Criterion.** `ord_m(2) = 60` ⟺ `m | 2^60−1` and `m` fails to divide…
