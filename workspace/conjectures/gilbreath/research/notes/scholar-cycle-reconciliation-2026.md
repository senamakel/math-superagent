# Scholar cycle — library reconciliation, no re-digest needed

The reference library is CLOSED (REQUESTS.md) and every held source already has
a summary (research/summaries/) and a claim block (research/CLAIMS.md). This
scholar cycle therefore verified and reconciled rather than re-read. Findings:

## 1. Trust anchor confirmed
The oracle generator (`code/lib/gilbreath.py`) reproduces all five worked rows
`A_1..A_5` of problem.md exactly (verified against the literal table; the
on-disk captured run `code/out/oracle_depth600.captured.txt` shows match=True
for all five, and depth-600 shape: leading entry 1, second entry ∈ {0,2}, and
the (odd, even, ...) parity shape for every k). Nothing measured against this
generator is built on a broken checker. Scholar has no exec tool in this run,
so the re-execution helper (`code/out/scholar_oracle_run.py`) is available but
the authenticated capture is the authoritative second route.

## 2. The four flagged contradictions are all already-resolved
- `odlyzko-block-lemma-asserted` (holds-here: no) vs `odlyzko-block-lemma-exact`
  (proved, constant 1): a recorded SELF-CORRECTION. The asserted row is the
  run's own old refuted n/2 figure; the exact row (n+1 rows, coefficient 1)
  supersedes it. Not a live dispute.
- `caldwell-proth-myth-repeats` vs `proth-myth-retracted`/`proth-citation-correction`:
  a DOCUMENTED-INTENDED contradiction. The Caldwell summary exists to record
  that the Prime Glossary repeats the retracted Proth myth and miscites
  C.R. 85:329–331 (actually Pépin). The `contradicts:` field is the point.
- `lemma54-lean-and-linkA-current-verified` vs `regeneration-thread-blocked-by`:
  the latter is stale thread text (Directive 49 "does not compile"); the Lean
  JSON verdict (code/out/lean/code_lean_descent_lemma.lean.json: compiled=true,
  verified=true, sorries=[]) is authoritative and carries the reconciliation
  note. The ledger flags the dangling id because that id was never a claim
  block — a generated-ledger artifact, resolved on disk.
- `descent-lemma-halved-formalised` is the canonical kernel-backed row for the
  Lean descent lemma (formalisation: code/lean/descent_lemma.lean).

## 3. The single open content (unchanged, and it IS the deliverable)
Route B rests completely on the supply-side bound `nu2(q_{n-1}) >= c*n`
(c > 0), which is genuinely TWO-POINT (consecutive-prime mod-4 switch count),
so no one-point analytic route can deliver it. Measured c ~ 0.5 with factor-26
margin over n^0.525 at n=3999. The honest deliverable is the CONDITIONAL
theorem on the HL/LOS two-point mod-4 switch-correlation bound. No held source
proves the bound; maynard/lau give existence not frequency; Ruzsa/Shiu/Martin
bound only the wrong (non-switch) side. Stored to durable memory.

## 4. What this run still lacks
A proof (or unconditional bound) of `nu2 >= c*n`. That is the named-open
hypothesis; everything else in the library's claims is either proved,
machine-checked, or a recorded refutation.
