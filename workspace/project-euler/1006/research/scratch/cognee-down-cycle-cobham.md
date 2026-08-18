# Cognee down — cycle record

`remember_memory` failed again this cycle: "the memory server cannot index
right now, so this document would be accepted and dropped rather than stored:
its own health report did not answer within 8 seconds". Same failure mode as
the earlier `scratch/cognee-down-cycle.md` cycles.

Consequence: the Cobham–Semenov survey addition is recorded in the workspace
note `research/notes/library-build-cycle-cobham-survey.md` (with the claim
block that carries the `answers:` provenance), and will be stored to Cognee by
a later cycle when the server is healthy. Nothing about the finding depends on
memory: the full text and the summary are on disk.

Do not retry remember_memory this cycle.