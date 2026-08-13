```approach
idea: block-apex-parity-forcing
mechanism: |
  Within the {0,2} regime, the block lemma's apex formula says the block's
  interior evolves by XOR (Rule 90), and the apex value
  A_{k+b_k-1}(1) = 2 · XOR_{j=0}^{b_k-1} [C(b_k-1, j) mod 2 · (A_k(j+1)/2)]
  is exactly 0 or 2 depending on the block's bit pattern.

  Now focus on the boundary: the value A_k(b_k+1) — the "intruder" — meets the
  last block entry A_k(b_k) ∈ {0,2}. After one difference:
    - If A_k(b_k)=0: A_{k+1}(b_k) = intruder (passes through unreduced)
    - If A_k(b_k)=2: A_{k+1}(b_k) = intruder − 2 (reduced by 2)
  So whether the intruder gets reduced depends on the PARITY OF THE LAST BLOCK
  ENTRY.

  The block's apex formula lets us trace the last block entry back through the
  block's evolution. The pattern of 0s and 2s in the block determines, via XOR,
  whether the last entry is 0 or 2 at every depth. In particular, the "erosion
  front" — the value that meets the intruder — is determined by the pattern of
  the original block.

  The new question: can we prove that for the PRIME triangle, the block patterns
  that occur are NOT the worst-case ones? Specifically, the constant block
  (0,0,...,0) and the constant block (2,2,...,2) both have apex 0 (XOR of equal
  bits). If the prime triangle NEVER produces these worst-case blocks beyond
  some small size, then every block has an internal 0↔2 transition, which forces
  the last entry to be 2 at some descendant row, which forces the intruder to
  reduce.

  This reduces regeneration to a DIFFERENT question: classify which {0,2} block
  patterns are realizable from the prime gap sequence under the absolute-difference
  operator. The constant blocks might be ruled out by the mod-4 linearization
  constraint on how blocks form from below.

  Why it's different from mod4-pascal: we don't need mod-8 or higher. We only
  need to show that constant-0 and constant-2 blocks of sufficient length cannot
  form in the prime triangle. This is a statement about the MOD-4 CONSTRAINTS on
  the entries that feed into block formation, not about lifting to higher moduli.

  Why it's different from rule90-absorption: we're not claiming uniform absorption.
  We're claiming that the SPECIFIC worst-case block patterns that would prevent
  absorption cannot arise from the prime gap structure.
status: refuted
killed-by: >
  The literature contradicts the approach's two load-bearing premises.

  (1) "Constant {0,2} blocks have apex 0 and prevent intruder reduction; every
  mixed block forces intruder reduction" — FALSE as a mechanism. CHT 2026
  Lemma 3.7(iii) proves a {0,d}-valued block stays {0,d}-valued in ALL
  descendants with NO decrease in magnitude regardless of the pattern (a block
  that attains both 0 and d — i.e. mixed — persists unchanged, it does not
  force anything); constant blocks are only the d=0 special case of the same
  persistence, not a distinct pathology. The apex value of a block (Sierpinski
  XOR, this run's proved block-lemma) affects only the sub-triangle's own
  bottom vertex, NOT the entry just past the block A_k(b_k+1) that meets the
  boundary: that entry is outside the block, its reduction toward {0,2} is
  uncontrolled by any pattern statement, and the block lemma is sharp exactly
  there (offset n uses index n+1 outside the block). So "mixed ⟹ intruder
  reduces" is not a consequence of anything proved or sourced: no source
  establishes it, and it is exactly the unproved regeneration step restated.
  The run's own depth-1000 data confirms the trigger is the BOUNDARY pair
  (x,y)=(2,4) — last block entry 2 with intruder 4 — not the block's pattern
  class: 60/60 regenerations at y=4, 0/65 at y≥6, whole-block constancy and
  apex never enter.

  (2) "If no worst-case constant blocks beyond small size occur, regeneration
  follows" — the classification premise is not in the literature, and the
  class-level version is outright false: constant blocks DO occur in the
  2-then-odds class, since Eppstein 2011's construction builds arbitrarily
  long constant-zero filled triangles (his "big empty triangle" of zeros to
  the right of a column of 2s). So "constant blocks cannot form from
  2-then-odds" fails as a class statement, and Muney 2026 shows the
  valid-extension machinery that would classify realizable patterns is a
  global, order-sensitive, folding-map criterion — as hard as the conjecture,
  not a usable filter. No source characterizes which {0,2} block patterns
  arise from 2-then-odds sequences; the connection the approach postulates
  between mod-4 constraints and block formation is precisely the part CHT 2026
  say they CANNOT do: Lemma 3.10 (Odlyzko's mod-4 linearization, the
  identically-named source of the "mod-4 constraint" idea) gives only parity,
  is useless against {0,d}-blocks with ODD d, and in this run was already
  refuted as a lift to exact values (mod-lift-obstruction, |2-6| mod 8).

  Empirical check (queued, NOT executed by this role — code/block_apex/
  check_constant_blocks.py): recompute whole-block constancy, longest 0/2
  runs, and terminal constant suffixes for the 161 live rows from a fresh
  exact sieve. What IS verified on disk and by hand: rows A_1..A_5
  (witnesses.json first-12 entries) have blocks [2,2] (constant, k=1),
  [0,2,2,2,2,2,2], [2,0,0,0,0,0,2], [2,0,0,0,0,2,2,2,2,0,0], and
  [2,0,0,0,2,0,0,0,2,0,2] — all mixed for k>=2; and blocks_depth1000.json's
  record (b, s, intruder per row; min b=2 at k=1 only, min b=7 for k>=2) is
  consistent with non-constancy but does NOT store full block patterns, so
  "no constant block of length >= 3 in 161 live rows" is a queued check, not
  an established fact. The refutation below does not depend on it.

  (3) The approach is not merely unsupported — it is the refuted
  rule90/regeneration problem in disguise. CHT Theorem 1.6 isolates the ONLY
  obstructions to decay as long 0-blocks and very long shallow {0,d}-blocks;
  the approach's "no constant blocks" is one of the two obstructions and its
  "mixed blocks force reduction" is a claim that the second obstruction never
  occurs — but CHT state ruling out even long 0-blocks for the primes "looks
  difficult to establish rigorously, even if one assumes strong conjectures on
  the primes". The data says the boundary (x=2,y=4) recurrences are what
  regenerate, and proving THAT recurrence is the conjecture itself.
precedent: >
  - https://arxiv.org/abs/2607.08712 (CHT 2026, Lemma 3.7(iii) {0,d} persists
    in all descendants without decrease; Theorem 1.6 long-0-block and long
    shallow {0,d}-block are the only obstructions; Lemma 3.10 mod-4 parity
    only, useless for odd d)
  - https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html
    (Eppstein 2011: 2-then-odds sequences with arbitrarily long blocks of
    zeros, right edge escaping/re-entering 1 infinitely often — constant
    blocks DO arise in the class)
  - https://arxiv.org/abs/2606.23721 (Muney 2026: valid-extension set is a
    global order-sensitive folding-map criterion with interior holes; the
    machinery that would classify realizable block patterns is as hard as the
    conjecture)
  - research/notes/block_lemma.md (this run's proved block lemma: sharp at the
    entry just past the block; apex exact but cannot reach it)
  - research/notes/regeneration_data.md (computed: 60/60 regen at y=4,
    whole-block constancy never a trigger)
holding-claims: larger
  mod-lift-obstruction, odlyzko-mod4-linearization, rule90-identification-real-absorption-refuted,
  anti-gilbreath-construction, valid-extension-nonlocal, odlyzko-block-lemma-exact
falsifies: >
  That (a) a mixed {0,2} block forces its boundary intruder to reduce within a
  bounded number of rows, or (b) constant {0,2} blocks cannot arise from
  2-then-odds sequences beyond small size. CHT Lemma 3.7(iii) refutes (a) —
  mixed {0,d} blocks persist in all descendants without decrease (the pattern
  class does not govern the boundary) — and Eppstein's construction refutes
  (b) at the class level. The prime-specific version of (b) is equivalent to
  ruling out one of CHT's two obstructions, which CHT explicitly state is
  beyond current techniques even under Cramér-style gap conjectures.
buy: >
  Nothing beyond what is already proved: the block patterns verified in the
  early prime rows (A_1..A_5, mixed for k>=2) and the block-length record
  (min b=2 at k=1 only) are consistent with the {0,2} regime, and the depth-1000
  regeneration data shows the trigger is the boundary pair (x,y)=(2,4). But the
  approach's claim that non-constancy forces regeneration is exactly the open
  conjecture restated, with no theorem — in this library or the papers it cites
  — connecting block pattern class to boundary reduction. The one durable
  residue is a clean falsifier statement: any future "pattern ⟹ regeneration"
  claim must first survive CHT Lemma 3.7(iii) and the sharp boundary of the
  block lemma (offset n uses A_k(n+1) outside the block).
first-step (retired): >
  Extracting and classifying block patterns from the depth-1000 data can only
  re-record the observed non-constancy; the SMT query "does a 2-then-odds
  start admit a constant {0,2} block of length L?" is answered YES at the
  class level by Eppstein's construction, so a positive answer to the query is
  not a falsifier of anything, and a negative answer for the primes alone is
  the conjecture. Not worth running as a route to a proof.
```