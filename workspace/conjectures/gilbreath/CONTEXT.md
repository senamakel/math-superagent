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

**Run state: very early.** The oracle exists and checks out, but `research/`
is empty (no notes, sources, claims), no thread or approach is open, and no
candidate invariant has yet been proposed. The phases below — library, then
claim extraction, then the oracle, then the loop — have not begun. `GOAL.md`
and `problem.md` carry the task statement and the deliverable; read both.

## Established

- **The whole conjecture reduces to the second entry of every row lying in
  `{0,2}`.** Basis: `2` is the only even prime, so `|p_{i+1}-p_i|` is even for
  `i≥2` and `3-2=1` is odd, giving `A_1 = (1, even, even, ...)`. The shape
  `(odd, even, even, ...)` is preserved by the absolute-difference operator
  (the lead differences against the first `1`, all the rest even−even), and
  `A_{k+1}(0)=|1-A_k(1)|` is `1` iff `A_k(1)∈{0,2}`. Status: **proved**
  (elementary parity induction; `2` the only even prime). This is the spine of
  the problem and every write-up must centre it. If ever `A_k(1)=4`, the
  conjecture dies that row.
  Anchor: `problem.md` "The real content, stated exactly".
- **An oracle exists and has been checked.** `code/out/witnesses.json`
  (exact integer arithmetic, sieve to 400000, 33860 primes) reproduces the
  problem's rows exactly (`A_1=A_2=A_3=A_4=A_5` first 12 entries match
  `problem.md`) and reports `depth_verified = 600`, `leading_entry_is_1 =
  true`, `second_entry_always_0_or_2 = true`, `min_leading_02_block = 2`.
  Status: **computed and checked** against the statement's tables. Any new row
  generator must reproduce the same tables before being trusted.

## Ruled out

None yet. No candidate invariant, lemma, or thread has been proposed, so
nothing is closed. The one known dead end, carried from the task framing, is
recorded as a gap (below) rather than a refutation.

## Numbers

- Leading `{0,2}`-block length (`block_profile` in witnesses.json), rows
  k=1..40: `2, 7, 13, 13, 24, 23, 22, 21, 24, 58, 97, 96, 97, 96, 173, 175,
  175, 175, 175, 290, 289, 288, 739, 873, 872, 871, 872, 871, 870, 869, 868,
  867, 866, 865, 2179, 2178, 2177, 2176, 2770, 2769`.
- Computed observation: the leading block length **grows over time** (roughly
  doubling in bursts around k=15, k=20, k=23, k=35, k=39), with `second ∈
  {0,2}` throughout. This bears directly on the regeneration question — but is
  verified only to depth 600, a restricted class to date. Do not present it as
  a proof of regeneration.
- Minimum leading block over the 40 profiled rows is `2` (at k=1).

## Recalled

- `recall_memory` and `relate_memory` return **nothing** for Gilbreath, the
  `{0,2}` block, or Odlyzko: durable memory holds no prior-run findings on this
  problem. Agents should not expect prior work there; there is none to import.

## Contradictions

- None established inside this run. The one tension is between Odlyzko's
  `{0,2}` self-propagation (a lead in `problem.md`, **not yet sourced or
  re-derived**) and the central open question of regeneration. Until the block
  lemma with its explicit constant is reproduced, treat "a block of length n
  protects ~n/2 rows" as an asserted lead, not an established result.

## Gaps

- **The consumption/regeneration obstruction, stated as the open question:**
  a `{0,2}` block of length `n` protects only roughly `n/2` rows (protection
  spent geometrically), so the regime must be endlessly regenerated from below.
  Nobody has proved regeneration always happens; this is where every prior
  attempt stops. Any proof must either show regeneration rate exceeds
  consumption with an explicit mechanism, or find an operator invariant
  forcing `A_k(1)∈{0,2}` directly. Say which of the two any claim establishes —
  consumption of a block is not regeneration.
- **Odlyzko (1993) block lemma** — exact statement and the constant in `~n/2`
  are needed as a primary source. Verify before relying.
- Research phase not begun: `research/REQUESTS.md` and `research/ROOT.md` do
  not exist. ROOT.md's phase-1 exit test (minimal counterexample structure,
  current verification bound, ≥3 restricted classes settled with hypotheses)
  is unmet.
- **Which side the approach is on is not yet decided.** `problem.md` argues
  Gilbreath is probably a theorem about *any* sequence starting `2` followed by
  odd numbers with small gaps, not about primes; a proof for such a general
  class would settle the prime case as a corollary. No approach is open yet, so
  this decision is pending.
