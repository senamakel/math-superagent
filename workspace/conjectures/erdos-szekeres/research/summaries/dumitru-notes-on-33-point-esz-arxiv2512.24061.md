# Dumitru, "Notes on the 33-point Erdős–Szekeres problem" (Dec 2025)

> **Source:** arXiv:2512.24061 (math.CO), 30 Dec 2025. Full text: `research/sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md` (verified genuine this cycle — no mis-assignment; the encoding numbers in the digest match the paper body). The claim lives in the consolidated [[sat-machinery-es-type-problems]] note as `dumitru-es7`; this file is the owning note with the verified details.

**Role in this run:** the live ES(7) frontier — the most recent direct SAT attack on ES(7)=33. It proves UNSAT only for anchored convex-layer subfamilies, NOT for the full 33-point case; ES(7)=33 remains open.

## What the full text establishes (verified verbatim this cycle)

- **Encoding ((n,k)=(33,7)):** 5456 triple-orientation variables + 14 selector variables per 4-set × 40920 4-sets = 572,880 → **578,336 variables total**; **16,670,808 clauses** (reduced 5-point CC constraints 9,493,440 + 4-set consistency 2,905,320 + no-convex-7-set 4,272,048, each of length 280).
- **4-set criterion (Proposition 1):** S in convex position iff every 4-subset is — exactly this run's `es35-four-criterion`/oracle backbone. Used to exclude convex 7-sets: every 7-set must contain at least one non-convex 4-subset.
- **14 realizable 4-set patterns** (of 16); 6 treated as convex (++++, −−−−, ++−−, −−++, −++−, +−−+), 8 non-convex.
- **Convex-layer (hull-template) anchoring** with layer sizes h, plus a w sub-cubing parameter fixing relative rotation between consecutive layers.
- **Soundness principle:** the reduced 5-point clause family omits clauses; omission only enlarges the admissible set, so a relaxed UNSAT is a valid certificate for the stronger instance.
- **Results:** UNSAT certificates for a collection of anchored subfamilies; heavy-tailed runtimes (2.5×10³ s to 2.28×10⁶ s single-threaded Kissat; subproblems weeks on commodity hardware). No full 33-point UNSAT.
- **Future-work directions (reusable):** coarser 4-set convex/non-convex indicator to shorten 7-set clauses; stronger outer-layer geometric anchoring.

## Claims

```claim
id: dumitru-es7
statement: There is a triple-orientation + 4-set-criterion + convex-layer-anchoring SAT encoding for ES(7); it yields UNSAT certificates for anchored subfamilies but does NOT settle ES(7) (no full 33-point UNSAT; runtime is heavy-tailed and currently dominant).
hypotheses: 33-point planar sets, general position
holds-here: yes
status: asserted (reports UNSAT certificates for anchored subfamilies; full ES(7) open)
bearing: the concrete next computational frontier; the 4-set criterion and layer-anchoring are directly reusable. An empty result only rules out the anchored subfamilies tested, NOT ES(7).
anchor: research/sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md
```

**Bearing on this run's queued tasks:** the run's `es-nogon-k7-rung` must treat 32 as the record and any 33+ as a would-be refutation needing independent re-verification. Dumitru's 4-set criterion is the compact Boolean form of "no convex k-gon", exactly as the run's SAT arm plans to use it.