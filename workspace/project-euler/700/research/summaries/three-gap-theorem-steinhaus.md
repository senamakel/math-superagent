<!-- source: https://hal.science/hal-00090031/PDF/three-gap.pdf | converted from PDF; full text at [[three-gap-theorem-steinhaus.full.md]] -->

# Three Gap (Three Distance) Theorem — Mayero, HAL-00090031

Primary source for the Steinhaus/Tony van Ravenstein proof of the Three Gap
Theorem, presented with a fully Coq-formalised proof.

## Statement (verified against full text)

**Theorem.** Place N points consecutively around a circle of unit circumference by
rotating through a fixed angle α (points `0, {α}, {2α}, …, {(N−1)α}`, where
`{x}` = fractional part). The points partition the circle into gaps of
**at most three distinct lengths** — for irrational α; at most **two** for
rational α. The three candidate gap lengths are `{first(N)α}`, `{last(N)α}`, and
`{first(N)α} + {last(N)α}`, where
`first(N) = argmin_{0<m<N} {mα}` (closest point to 0 from the right) and
`last(N) = argmax_{0<m<N} {mα}` (closest point to 1). The `after`/successor
function takes at most three values (Theorem 2).

**Important hypothesis:** the proof is given for **α irrational**; the paper
explicitly notes the irrationality is essential and that the theorem is only
"trivially true" for rational α (Remark 2, Remark 3). `first`, `last`, `after`
are not even well-defined functions in general when α is rational.

## Why it is / is not load-bearing here

For PE 700, `α = A/M = 1504170715041707/4503599627370517` is **rational**, so
the full Three Gap Theorem does **not** apply verbatim. What does transfer to the
discrete orbit `{A·n mod M}` is the *conceptual identification*: `first(N)` is
the record-low (new-minimum-fractional-part) index and `last(N)` the record-high
index. That identification is elementary and correct (the smallest positive
fractional part seen so far is exactly the running minimum of `A·n mod M`). But
the paper's bound of "at most three/two gap lengths" and the O(log M) conclusion
are **not** what this source proves for the rational case; the small number of
record lows is established instead by the recurrence/continued-fraction argument
in `record-low-recurrence.md`, not by this theorem.

So: **corroboration and vocabulary only.** The candidate-gap/gap-length picture
explains *why* the record lows track the continued fraction of A/M, but the run
should not cite this theorem as the proof that there are few Eulercoins for this
(specific, rational) instance.

```claim
id: eu700-three-gap-record-lows
statement: first(N) (the index minimising {mα} over 0<m<N) is the running-minimum / record-low index of the orbit {nα}; last(N) the running-maximum index. For irrational α the orbit gaps take at most three lengths.
hypotheses: α irrational for the three-gap statement; HERE α = A/M is rational, so only the first(N)/last(N) identification carries over, not the gap-length bound.
holds-here: partial — the first(N)=record-low index identification holds for the discrete orbit {A n mod M} with gcd(A,M)=1; the three-gap length bound does not (rational case).
status: sourced and proved (for irrational α); the rational-case application here is an inference, not a theorem from this source.
bearing: vocabulary/corroboration for why record lows track A/M's continued fraction. NOT the proof of the O(log M) bound — see eu700-record-low-recurrence for that.
anchor: research/summaries/three-gap-theorem-steinhaus.md
```
