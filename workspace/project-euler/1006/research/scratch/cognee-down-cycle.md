# Scratch: Cognee memory server down this cycle

`remember_memory` repeatedly refused on 2026-02: "the memory server cannot
index right now" / health-check timeout. `describe_file` also refused for
`research/` ("research/ uses Cognee for durable cataloguing and recall"). This
is the same documented limitation from prior cycles (see
`research/summaries/library-build-status.md`).

Consequence and workaround:
- Durable findings that would normally go to Cognee were persisted on disk:
  `research/notes/scholar-verified-monoid-primitive.md` (the verified
  universal-Euclidean monoid; claim `monoid-composition-formulas-verified`).
- The on-disk catalogue (per-source digests under `research/summaries/`, the
  notes under `research/notes/`) is the authoritative durable store until the
  memory server recovers. The claim ledger is derived from the notes and is
  complete.
- Do NOT keep retrying `remember_memory`/`describe_file` for research/ until a
  health check says the server is back; each call times out.
