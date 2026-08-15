# G-balance (per-event `j >= d`) is REFUTED by the run's own data

`status: refuted`, `killed-by: real-row counterexample (depth-1000 record)`

## The claim attacked

`G-balance` (event-rate-sufficiency skeleton, `research/backward/event-rate-sufficiency.md`):

> At every `(2,4)`-regeneration event, the jump `j` (amount by which `b_{k+1}`
> exceeds `b_k`) satisfies `j >= d`, where `d` is the number of erosion rows
> (`b` decreases) since the previous `(2,4)`-event.

This is the *strong* per-event form. The skeleton's own weaker form
(`Σ_events j_i >= k_n − k_1 − n + 1`, total jump ≥ total erosion) is the one
verified to hold (block grows); the per-event claim is asserted as "would close
the conjecture".

## The counterexample

From `code/out/blocks_depth1000.json` `b` array (agrees with `witnesses.json`
rows 1..40 per `oracle_agree_first_40: true`) and independently from
`code/out/regeneration_analysis.captured.txt`, which lists all 60 events with
their jumps:

```
transition 23:  b 739 -> 873,  jump j = 134   (event)
transition 24:  b 873 -> 872,  erosion (d=1)
transition 25:  b 872 -> 871,  erosion (d=2)
transition 26:  b 871 -> 872,  jump j = 1     (event)   <-- j=1 < d=2  VIOLATION
```

At the transition-26 event, there were 2 erosion rows since the previous event
(transition 23), so `d = 2`, while the jump is `j = 1`. Hence **`j < d`**,
contradicting `j >= d`.

A second, larger instance:

```
transition 86: b 31530 -> 31537, jump j = 7   (event)
transitions 87,88,89,90:         four erosion rows (d=4)
   31537->31536, 31536->31535, 31535->31534, 31534->31533
transition 91: b 31533 -> 31534, jump j = 1   (event)  <-- j=1 < d=4  VIOLATION
```

A third (a stall right after erosions):

```
transition 72: b 31496 -> 31527, jump j = 31  (event)
transitions 73,74:               two erosion rows (d=2)
transition 75: b 31525 -> 31525, jump j = 0   (stall event)  <-- j=0 < d=2
```

Stalls (j = 0) immediately following erosion rows are the generic way the
per-event claim fails: the block erodes for a row or two and then an event
refills it by less than it just lost.

## Why this is a result, not just a number

The claim is asserted in the skeleton as the route that "would close the
conjecture". The counterexample shows the per-event `j >= d` bound is **false
on the actual prime rows to depth 1000** — the exact rows the run uses as its
oracle. So the stronger per-event form of G-balance cannot be the mechanism,
and the route must fall back to the weaker *aggregate* form
(`Σ j_i ≥ total erosion`), which remains numerically supported but is not
implied by any per-event bound.

Bound of the finding: refuted on the depth-1000 record (1,270,607 primes below
2×10⁷), rows 1..1000, all 60 events. Not a statement about larger depth — but
the mechanism (a stall or small jump after erosion) is not depth-specific and
is the generic behaviour, so there is no reason the per-event claim would
resurge deeper.

## Verification

Checked against two independent on-disk artifacts that agree with each other:
- `code/out/blocks_depth1000.json` `b` array (block lengths per row);
- `code/out/regeneration_analysis.captured.txt` (all 60 events, jumps, and the
  full erosion-run list).

Both list the same `(k, b_k -> b_{k+1}, j)` triples. The step law (event iff
`b_{k+1} >= b_k`, else erosion `-1`) is itself `status: checked` in this run.

```claim
id: g-balance-per-event-refuted
statement: The per-event bound j >= d, where j is the jump at a (2,4)-event
  and d is the number of erosion rows since the previous event, is FALSE on
  the prime rows to depth 1000. Explicit: transition 23 (739->873, j=134),
  then erosions 24,25 (873->872, 872->871, d=2), then transition 26
  (871->872, j=1) has j=1 < d=2. Also transition 86->91 with j=1 < d=4, and
  transition 75 stall j=0 after d=2. The aggregate form (sum of jumps >= total
  erosion since first event) still holds numerically (block grows), but it is
  not implied by any per-event j >= d.
hypotheses: rows are iterated absolute differences of primes below 2e7;
  events = transitions where b_{k+1} >= b_k; d = erosion rows since previous
  event; depth 1000
holds-here: yes (this is the run's own oracle record)
status: checked
bearing: kills the strong per-event form of the G-balance rung in the
  event-rate-sufficiency skeleton; the route must reduce to the weak aggregate
  form, which is not deduced from any per-event bound. Consumption is not
  regeneration even in the strong per-event sense.
anchor: code/out/blocks_depth1000.json, code/out/regeneration_analysis.captured.txt
source: operator-computation (this run's own depth-1000 record)
```
