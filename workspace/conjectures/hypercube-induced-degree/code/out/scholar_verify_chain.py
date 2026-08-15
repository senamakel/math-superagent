# Scholar verification script (NOT RUN in this session)

This file was written as a fresh independent duplicate of the existing spectral
verification, but could not be executed in the scholar session.

**Do not cite or trust its output** — it was never run. The authoritative,
already-captured runs are:

- `code/out/huang_spectral.captured.txt` (exact A_n^2==nI, spectrum ±sqrt(n),
  interlacing λ_max>=sqrt(n), degree bound, n=1..10)
- `code/out/verify_interlacing_chain.captured.txt` (exact integer chain, n=1..8)
- `code/out/f_exact_verify.captured.txt` (λ_max>=sqrt(n), every admissible S,
  n=1..4)

This script's checks duplicate those and would add nothing. It is kept only to
record that the check was attempted independently; its conclusion, if it were
run, is expected to match the captured outputs above. See
`research/notes/scholar-synthesis-gap-closed.md` for the synthesis.
