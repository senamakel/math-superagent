# Intended verification of the reduction — PENDING (no exec tool in this run)

Purpose: numerically confirm, against the real generated rows, the two reduction
facts that `witnesses.json` already reports in aggregate:

1. `shape (odd, even, even, ...)` for every row k>=1;
2. `A_{k+1}(0)==1  iff  A_k(1) in {0,2}` for every k>=1.

`witnesses.json` already gives `leading_entry_is_1=true`,
`second_entry_always_0_or_2=true` over `depth_verified=600`, which is the same
statement in aggregate. This script would make it per-row explicit, but this run
has no `exec` tool, so it was **not run** and produces no output. Until it runs,
the reduction rests on (a) the elementary proof in
`research/notes/reduction.md` (status: proved) and (b) the aggregated depth-600
check in `witnesses.json` (status: computed). Do not cite this file as a check.

The reduction is elementary arithmetic; the substantive numbers live in
`witnesses.json`, not here.
