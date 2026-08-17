# Scholar adjudication — allowable-sequence circular representation: REFUTED

**Date:** this cycle. **Scholar** wrote this record because `record_entry` is not in
scholar's charter (tool-permission mismatch). The approaches ledger row
`allowable-sequence-circular-representation` must be closed **status: refuted** by a
role holding `record_entry` (director or goals), substantively as below. This file is
the on-disk anchor so the closure survives; the earlier verdict file
`research/approaches/allowable-sequence-circular-representation.md` §VERDICT records
the same substance in Cognee.

## Adjudication payload for the ledger

```
id: allowable-sequence-circular-representation
status: refuted
title: Allowable (circular) sequence representation of es_construct — both load-bearing mechanisms refuted
detail: REFUTED by exact computation on es_construct n=4..7 (Fraction arithmetic, corrected
  directed-line sweep, claim gsplit-enum-completeness-and-n7-zero).
  (1) reversal-depth = block-index is a STRUCTURAL impossibility: in every Goodman-Pollack
  circular sequence the per-point reversal count over one half-period is constantly N-1
  (every pair crosses exactly once), so it can never equal block sizes C(n-2,i); observed
  depths are constantly 3,7,15,31 at n=4..7 vs blocks 1,2,1 / 1,3,3,1 / 1,4,6,4,1 /
  1,5,10,10,5,1. Not a placement artifact: forced by the pair-reversal axiom.
  (2) contiguous-block convexity characterization is FALSE in both directions: over all
  |S|>=4 subsets, n=4 0/1, n=5 88/163 (75 disagree), n=6 62096/64839 (2743 disagree) —
  both false positives and false negatives. The correct convexity criterion from the
  sequence is POINTWISE EXTREME-IN-PROJECTION: S convex iff every p in S is first-or-last
  in some S-restricted projection order, equal to vertex-of-conv(S); agrees with the exact
  oracle on every |S|>=4 subset at n=6 (64839/64839).
  The earlier '[A] replay ok:False' was an encoder run-reversal bug, fixed by swapping each
  tied group's pairs independently ([B,A,D,C] not [D,C,B,A]).
  What survives: the exact circular sequence is correctly constructible and the
  Goodman-Pollack axioms hold on es_construct at n=4..7.
  DO NOT RE-DERIVE depth=block or contiguous-block convexity; the branch is closed.
```

## The general failure this exposed

When a role's write is **refused for lack of a tool**, the content must be (a) handed to a
role that holds the tool, or (b) written to the workspace with `write_document` — never
silently abandoned. Scholar held `write_document` and used it here as the fallback; the
ledger closure itself still needs a role holding `record_entry`.

## Relation to durable memory

This is consistent with and restates, not contradicts, recalled memory: the Cognee durable
record (VERDICT: UNSOLVED; reversal-count = N−1; fixed replay; pointwise
extreme-in-projection survivor) and the prior verdict file
`research/approaches/allowable-sequence-circular-representation.md` say the same things.
The run must not re-open `allowable-sequence-continue` items (2)/(3) — they are prior art.

## Anchor

`research/approaches/allowable-sequence-circular-representation.md` (§VERDICT),
`code/out/allseq_adjudicate.py` + `code/out/allseq_adjudicate.captured.txt`,
claim `gsplit-enum-completeness-and-n7-zero`.