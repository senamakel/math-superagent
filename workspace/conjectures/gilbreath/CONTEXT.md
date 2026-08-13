# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it. It carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. It is not a file
catalogue (`research/INDEX.md` is that) and not a narration of activity.

Token budget 10,000 (currently well under). Every model call in every role is
sent this file, so length is a bill the whole run pays; add only what an agent
would otherwise re-derive, and link the file holding any detail compressed
away.

## Established

- **The whole conjecture reduces to the second entry of every row lying in
  `{0,2}`.** Basis: `2` is the only even prime, so `|p_{i+1}-p_i|` is even for
  `i≥2` and `3-2=1` is odd, giving `A_1 = (1, even, even, ...)`. The shape
  `(odd, even, even, ...)` is preserved by the absolute-difference operator,
  and `A_{k+1}(0)=|1-A_k(1)|` is `1` iff `A_k(1)∈{0,2}`. Status: **proved**
  (elementary parity induction). Checked against full rows to depth 599
  (`code/out/check_reduction.captured.txt`), not just witness slices.
  If ever `A_k(1)=4`, the conjecture dies that row.
  Anchor: `research/notes/reduction.md` + `check_reduction_operator.md`.

- **An oracle exists and has been checked.** `code/out/witnesses.json`
  (exact integer arithmetic, sieve to 400000, 33860 primes) reproduces the
  problem's rows exactly and reports `depth_verified = 600`,
  `leading_entry_is_1 = true`, `second_entry_always_0_or_2 = true`,
  `min_leading_02_block = 2`.

- **Block profiles computed to depth 1000** (`code/out/blocks_depth1000.json`,
  `code/out/blocks_deep.captured.txt`): 1270607 primes below 20M, depth 1000
  rows, agrees with witnesses on k=1..40. Key stats: 60 regeneration events
  (b diff ≥ 0) in 999 row transitions; longest pure-erosion run = 838;
  intruder (first value past block): 59.6% = 4, all 0 or 2 mod 4; s = 520
  zeros, 480 twos; max block = 1,270,444 at k=162; max regen jump = +360,698
  at k=146.

- **Consumption is proved (erosion bound):** b_{k+1} ≥ b_k - 1. A {0,2} block
  loses at most one entry per row. This is the {0,2} closure theorem.
  Consumption says a block of length n protects ~n/2 rows. This is NOT
  persistence — it only buys time.

## Ruled out

None yet as refuted. But the directive establishes: approaches that prove only
consumption and treat it as persistence have proved nothing. Every claim must
name which of consumption/regeneration it establishes.

## Numbers

- Leading `{0,2}`-block length for rows k=1..40: see `witnesses.json`.
- Depth-1000 summary: min b=2 (k=1), max b=1,270,444 (k=162), regen events=60,
  longest erosion=838, intruder mostly 4 (59.6%).
- Full sequences in `code/out/blocks_depth1000.json`.

## Recalled

- `recall_memory` and `relate_memory` return **nothing** for Gilbreath, the
  `{0,2}` block, or Odlyzko: durable memory holds no prior-run findings on this
  problem.

## Contradictions

- None.

## Gaps

- **THE OPEN PROBLEM: regeneration.** Why does a fresh {0,2} block always
  reappear before the current one is exhausted? Consumption is understood;
  regeneration is not. The longest erosion run is 838 consecutive rows — the
  block is shrinking the whole time, yet never reaches 0. What property of the
  row below the block forces a fresh {0,2} stretch to emerge? Thread at
  `research/threads/regeneration.md`.

- **Odlyzko (1993) block lemma** — exact statement and constant needed. Cited
  but not re-derived.

- **Short-block stress case:** min b=2. When the block is this short,
  regeneration has almost no buffer. The mechanism that works here is the
  simplest case and must be characterized first.

- **Intruder mechanism:** the first non-{0,2} value past the block is mostly 4
  and always 0 or 2 mod 4. How does the absolute-difference operator force
  intruder values into {0,2} as they reach the front of the row?

- **Which side:** the approach is on the general-class side — this is not a
  theorem about primes specifically; it's about any sequence starting 2
  followed by odd numbers with bounded gaps. A theorem for that class settles
  the prime case as a corollary.
