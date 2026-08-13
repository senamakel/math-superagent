# Literature grounding: block-apex-parity-forcing — refuted

Research role report (checked against `research/approaches/block-apex-parity-forcing.md`).
Status set: **refuted**. This note records the reading behind that verdict and what was
verified vs. queued.

## The approach in one line

"If the worst-case constant {0,2} blocks (all-0 or all-2) never occur in the prime
triangle beyond small size, then every block is mixed, and a mixed block forces its
erosion-front entry to be 2 at some descendant, which forces the boundary intruder to
reduce — so regeneration follows. This reduces regeneration to classifying which
{0,2} block patterns are realizable from the prime gap sequence, possibly via mod-4
constraints." (The apex formula it cites — sub-triangle evolution by XOR/Rule 90 with
apex = Sierpinski dot product of the pattern — is this run's own proved block-lemma
result and is not in dispute.)

## The three questions asked, and what the literature says

### Q1. Does the literature characterize which {0,2} block patterns arise from 2-then-odds sequences?

**No.** Nothing in the library or in fresh searches (CHT 2026 arXiv:2607.08712, Muney 2026
arXiv:2606.23721, Eppstein 2011, Odlyzko 1993, Alkan 2023, Agama 2021, Li 2026, Chase 2024)
characterizes the realizable leading-block patterns. What exists is strictly weaker:

- **Parity only:** Odlyzko 1993 eq. 2.2, generalized as CHT Lemma 3.10:
  `a(i,j) ≡ Σ_k C(i,k) a_{j+k} (mod 2)`. CHT explicitly state they "will not use
  Lemma 3.10 directly"; it excludes long 0-blocks and long {0,d}-blocks for **even** d
  but "does not easily reduce the likelihood of long {0,d}-valued blocks for **odd** d".
  Parity never fixes an exact value, and this run already proved the free lift stops at
  mod 4 (`|2−6| = 4 ≢ 0 (mod 8)`; `mod-lift-obstruction`).
- **Global extension criteria:** Muney 2026's valid-extension set is an
  order-sensitive analogue of Brown's subset-sum completeness criterion, computed by a
  folding map over the whole anti-diagonal; Alkan 2023's criterion has factorial
  weights over the entire prefix. Both are as hard to check as the conjecture and give
  no pattern-level characterization.
- **Class-level impossibilities fail:** Eppstein 2011 constructs 2-then-odds sequences
  with arbitrarily long blocks of zeros (his "big empty triangle") whose right edge
  escapes to non-1 and re-enters 1 infinitely often. So "constant blocks cannot form
  from 2-then-odds" is **false as a class statement**; the prime-specific version is
  exactly the open part of the conjecture.

### Q2. Are constant blocks known to arise, or known to be impossible?

- **In the 2-then-odds class: known to arise.** Eppstein's construction produces
  arbitrarily long all-zero blocks (and escape/re-entry infinitely often).
- **In the prime triangle: not established either way at depth.** The on-disk records
  (`witnesses.json`: rows A_1..A_5 first-12; `blocks_depth1000.json`: b, second-entry,
  intruder per row) verify by hand that rows A_1..A_5 have blocks `[2,2]` (constant,
  k=1, length 2), `[0,2,2,2,2,2,2]`, `[2,0,0,0,0,0,2]`, `[2,0,0,0,0,2,2,2,2,0,0]`,
  `[2,0,0,0,2,0,0,0,2,0,2]` — all mixed for k≥2 — and the block-length record
  (min b=2 at k=1 only; min b=7 for k≥2) is consistent with non-constancy. But full
  block bit patterns for k≥6 are NOT stored anywhere on disk; "no constant block of
  length ≥ 3 in the 161 live rows" is a **queued check** (code/block_apex/
  check_constant_blocks.py), not an established fact, and the refutation does not
  depend on it.
- **Known impossibility result in the relevant direction:** none. On the contrary, CHT
  Theorem 1.6 isolates long 0-blocks and long shallow {0,d}-blocks as the only
  obstructions to decay, and the authors state that ruling out even long 0-blocks for
  the primes "looks difficult to establish rigorously, even if one assumes strong
  conjectures on the primes such as the Hardy–Littlewood prime tuples conjecture".

### Q3. Is there a known connection between mod-4 constraints and block pattern formation?

- The only mod-4 constraint in the literature is the linearization (Odlyzko eq. 2.2 =
  CHT Lemma 3.10), and it is **parity-only**. It cannot rule out {0,d}-blocks with odd
  d (CHT's own words) and cannot separate {0,2} from {4,6,...} (this run's proved
  mod-lift-obstruction). Nothing else in the literature connects mod-4 arithmetic to
  block pattern formation. The approach's appeal to "mod-4 constraints on block
  formation" therefore has no literature support beyond the parity fact already on
  file.

## The mechanism itself is refuted, not just unsupported

The approach's middle step — "a mixed block has an internal 0↔2 transition, which
forces the erosion-front entry to be 2 at some descendant, which forces the intruder
to reduce" — is contradicted by CHT **Lemma 3.7(iii)**: a {0,d}-valued block stays
{0,d}-valued in **all** descendants with **no decrease in magnitude**, independent of
the pattern. Constancy is not the pathology; persistence is, and it applies to mixed
blocks equally. The documented regeneration trigger in the prime data is the boundary
pair (x,y) = (2,4) — last block entry 2, intruder 4 — holding for 60/60 regenerations
with 0/65 at y≥6 (regeneration_data.md); block pattern class, whole-block constancy,
and apex never enter that mechanism. The apex formula governs only the block's own
sub-triangle bottom vertex; the entry A_k(b_k+1) that actually meets the boundary is
outside the block and the block lemma is sharp exactly there. So "pattern ⟹ boundary
reduction" is a restatement of the regeneration step, not a consequence of any
proved or sourced fact. In CHT's dichotomy, the approach is simultaneously trying to
rule out obstruction one (long 0-blocks) and asserting obstruction two (long shallow
{0,d}-blocks) never matters — the second half is exactly what CHT prove is the
subtle obstruction (odd d, no parity handle).

## What was verified vs. queued vs. searched-and-absent

- **Verified (hand-checked from on-disk witnesses):** rows A_1..A_5 block patterns
  (mixed for k≥2; constant only the trivial [2,2] at k=1); block-length record
  consistency; the boundary-trigger facts (60/60 at y=4) from regeneration_data.md.
- **Queued (NOT executed — no shell tool in this role; for the compute agent):**
  `code/block_apex/check_constant_blocks.py` — full constancy / longest-run / terminal
  suffix scan of the 161 live rows (fresh sieve to 20M, ~4 s per the earlier
  blocks_deep run); `code/block_apex/front_sequence_oracle.py` — exact 2^n oracle for
  the claim "every mixed pattern has a 2 at some front offset" (Pascal-mod-2 front
  map, n ≤ 11).
- **Searched and absent:** any source characterizing realizable {0,2} block patterns
  (exa_search: "Gilbreath absolute differences primes blocks of zeros pattern
  classification two-valued blocks"; "Gilbreath conjecture {0,2} blocks constant
  blocks apex mod 4 gap sequence characterization"; plus the library). Recorded as a
  gap in Cognee so it is not re-searched.

## Files

- `research/approaches/block-apex-parity-forcing.md` — status: refuted, with killed-by,
  precedent, falsifies, buy, retired first step.
- `code/block_apex/check_constant_blocks.py` — queued empirical probe.
- `code/block_apex/front_sequence_oracle.py` — queued exact oracle for the front claim.