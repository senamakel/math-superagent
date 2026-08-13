THIS FILE IS THE LEDGER, NOT THE LOG. Write entries here that say what was decided, and the operator will read them from the console. The last entry is top. Log output is config/directives.jsonl; keep them in sync — after a new entry here, ask tool_builder to append it there too.

---

## Directive 36 — 2026-08-16

Done. The 1e9 run's capture was read in full; row-248 is STILL capped (b_land = W−248−1, floor=0, jump ≥ 27,684,003). Geometric doubling at 1.765×/giant (R²=0.968) with gaps 9–64 means each giant costs 1.5–8× the width of the last — the empirical route is at its ceiling at 1e9/1.37 GiB.

Changes made:
- **TASKS.md** rewritten: parity correction first (15 genuine, 1 odd, base-rate p=0.0052), then settlement note, then Granville/CHT reading as the primary theoretical work. "Do not queue a 2e9 or 4e9 sieve run" is a standing instruction.
- **`code/out/1e9_settlement.md`** written: four settled findings (row-248 capped, max gap 64, ratio bound ≤ 0.01264 everywhere, oracle passed), ceiling rationale, parity correction.
- **`research/threads/regeneration.md`** thread header pivoted: empirical route at ceiling, Route B (Granville ν_2) primary, Lemma 5.4 re-derivation as next step, parity corrected.
- **`CONTEXT.md`** Run state, Established (wider-width record), and Gaps sections updated to Directive 36 — 1e9 record, ceiling, pivot to theoretical routes. Granville/CHT FULLPDFs are in `research/sources/` and have not yet been read.

What was not changed: the 6e8 record stands as the last genuine-giant record (15 giants); the 1e9 run confirmed it and added the ceiling finding. The Granville and CHT FULLPDFs were read by this director to confirm they are in the library; the actual summaries and Lemma 5.4 re-derivation are TASKS items for the next roles.