# HANDOFF — closure payload for approaches ledger: `allowable-sequence-circular-representation`

**To:** director or goals (the roles that hold `record_entry` / `close_entry`).
**From:** scholar (this role does NOT hold `record_entry`; the system prompt's ledger-write
claim does not match the actual tool list. Fallback per steering directive: write the payload
to the workspace so it is never lost.)
**Why this exists:** scholar/agent-run-79 attempted to close this approaches entry and was
refused with "unknown tool record_entry". The adjudication must not be dropped. Substantively
the closure is ALREADY on disk in three places (approach note `status: refuted`; the rendered
`derived/APPROACHES.md` row; Cognee durable memory), but per the directive this payload is
provided verbatim so the ledger write can be completed by a role that holds the tool.

## Action requested (one `record_entry`, status `refuted`)

```
record_entry { ledger: "approaches", id: "allowable-sequence-circular-representation",
  fields: { status: "refuted",
            reason: <the payload below, verbatim in substance> } }
```

If the entry is already refuted in the ledger store, record a confirmation instead:
`status` stays `refuted`; add the payload below as the canonical close reason.

## Payload — the adjudicated closure, verbatim in substance

Both load-bearing mechanisms of the allowable-sequence approach are REFUTED, by exact
computation on `es_construct` at n=4..7 (all Fraction arithmetic, corrected directed-line
sweep, captures `code/out/allseq_adjudicate.captured.txt`,
`code/out/allseq_axiom_adjudication.captured.txt`).

1. **Reversal-depth = block index T_i is a STRUCTURAL impossibility, not a placement
   artifact.** In every (Goodman–Pollack) allowable sequence, the per-point reversal count
   over one half-period is constantly N−1, because every unordered pair crosses exactly once
   per period (the pair-reversal axiom). Observed depths at n=4..7: 3, 7, 15, 31 — constant
   — vs the block binomials {1,2,1}, {1,3,3,1}, {1,4,6,4,1}, {1,5,10,10,5,1}. Hence the
   binomial coefficients C(n−2,i) of the ES construction are NEVER recovered as a per-point
   sweep statistic; the staircase/depth induction has no working mechanism.

2. **Contiguous-block/staircase convexity is FALSE as stated, in both directions.** Over all
   |S|≥4 subsets: n=4 0/1 agree, n=5 88/163 (75 disagree), n=6 62096/64839 (2743 disagree).
   Failure modes include full-set false positives (the full set is always one contiguous
   block yet need not be convex) and convex 4-sets predicted non-convex (elements never
   separable from an interior point in a single projection).

3. **What survives (the part worth keeping):** the exact circular sequence IS correctly
   constructible and the Goodman–Pollack axioms hold on `es_construct` at n=4..7 (every
   pair reversed exactly once per half-period; every event an adjacent swap, tied parallel
   pairs handled as disjoint adjacent groups). The earlier "[A] replay ok: False" was an
   ENCODER BUG, since fixed: `replay()` merged consecutive simultaneous blocks into one
   reversed run; the correct replay swaps each tied group's pairs independently —
   [B,A,D,C], not [D,C,B,A]. The correct convexity-from-sequence criterion also survives:
   S is convex iff every p∈S is first-or-last in some S-restricted projection order
   (extreme-in-projection = hull vertex); agrees with the exact oracle on EVERY |S|≥4
   subset at n=6 (64839/64839) and n=5 (163/163). This reduces to the classical
   "convex = all points extreme in their hull" in sweep language: real order-type data,
   but no new handle on block structure.

4. **Do NOT re-derive either refuted mechanism.** A future attempt must not re-prove
   depth=block or contiguous-block convexity, and must not spend another pass confirming
   the encoder self-check (that diagnosis is banked). The allowable sequence remains a
   correct vocabulary (standard finite order-type encoding) but yields no mechanism for
   the exact 2^{n-2} bound. Branch closed as refuted.

## Evidence anchors

- `research/approaches/allowable-sequence-circular-representation.md` §VERDICT
  (full adjudication, July 2025)
- `code/out/allseq_adjudicate.captured.txt`, `code/out/allseq_axiom_adjudication.captured.txt`
- Durable memory (Cognee): "ALLOWABLE-SEQUENCE APPROACH ADJUDICATED ... REFUTED on both
  load-bearing claims"

## Director verification (directive 19)

Verified this pass (director): the closure is NOT lost — it is already fully
banked in the source file the approaches ledger derives from,
`research/approaches/allowable-sequence-circular-representation.md`
(`status: refuted`; `killed-by` carries both mechanisms refuted, what survives,
and the "do NOT re-derive depth=block or contiguous-block convexity"
instruction), and tasks `allowable-sequence-continue` and `allseq-adjudicate`
are already dropped with the full reason. `record_entry` is correctly refused on
the approaches ledger because it is file-derived; the source `approach` block is
the canonical record and is complete. The only cosmetic gap is that the derived
`derived/APPROACHES.md` renders the multiline `killed-by` as "no reason
recorded" — a renderer artifact, not missing content; the source file is
authoritative. Process lesson (tool-permission fallback → write_document /
source-file path, never silently abandon) is documented here and in the
SCHOLAR-REPORT summaries. Attempted Cognee store of the lesson but the memory
server was down (health check timed out); the disk record above is the durable
copy this run.

## General failure pattern being recorded

When a role's write is refused for lack of a tool, the content must be handed to a role
that has it or written to the workspace with `write_document` — never silently abandoned.
This file is that handoff. scholar does not hold `record_entry`/`close_entry`; director and
goals do. (Verified this pass: the actual tool list contains no ledger-write tool despite
the system prompt's "You hold record_entry and close_entry" wording.)