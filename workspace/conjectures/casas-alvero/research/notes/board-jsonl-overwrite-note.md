# NOTE (scholar, this pass): teams/board.jsonl was accidentally overwritten and reconstructed

## What happened

During this scholar pass I intended to APPEND a board post recording the digest
findings. I mistakenly used `write_document` on `teams/board.jsonl`, which
**replaced the whole file** (the runtime treats board.jsonl as an append-only
event log; writing the whole file destroyed the 18 prior entries).

I then reconstructed the file from my earlier full read of `teams/board.jsonl`
(the 18 lines appeared verbatim in the read I performed at the start of the
pass). All 19 records are present again (18 original + 1 new scholar post), and
the rendered `teams/BOARD.md` shows 19 entries — matching the pre-pass count of
18 + 1.

## What may be lost

Two of the original "offer" posts (the ones announcing the
`research/backward/ca20-good-prime-lift.md` and `full-ca-regular-sequence.md`
decompositions) carry long report bodies. My read of `board.jsonl` at the
start of the pass was the FULL JSONL (not the truncated BOARD.md render), and I
restored them from that read. HOWEVER — the read I restored from was the
tool's returned content, which for the two long offers was itself truncated
with "[truncated — the full report is in this school's gap briefing]".

**Therefore the reconstructed board.jsonl bodies of those two long offer posts
are incomplete** — they do not contain the truncated tails. The SUBSTANTIVE
content they announced is NOT lost: those reports live intact in
`research/backward/ca20-good-prime-lift.md` and
`research/backward/full-ca-regular-sequence.md`, which are complete and
unchanged. The loss is confined to the duplicated summary text in the board
itself.

## Honest consequence

- The scholar's three deliverables this pass (digests, claims, Cognee memory)
  are complete and unaffected.
- The board is a parallel communication record; its loss here does not affect
  the mathematical state, which lives in the ledgers, claims, backward files,
  and notes.
- Any later role reading board.jsonl for those two offers should consult
  `research/backward/` for the full content.
- Action for the future: never `write_document` an append-only runtime file
  (board.jsonl); the board is meant to be appended via the runtime, not a
  plain file write.

If a prior snapshot of board.jsonl exists in the runtime's own logs (e.g. in
`config/start.*.log` or a git state), the two offer bodies could be recovered
verbatim from there; nothing in this workspace holds them in full.
