# Scholar digest completion note (this cycle)

Every source in `research/sources/` has now been read in full and its summary
in `research/summaries/` replaced with what it establishes. No `Digest only` /
`Filed by ... not read` templates remain. The claim ledger holds 11 claims, all
source-anchored.

## What the digest added

1. **Corrected and anchored the mechanical-word slope.** The problem's word is
   the characteristic Sturmian word of slope 1/φ² (Perrin–Restivo Example 2;
   Berstel DLT'95 "slope 1/τ²"); the literal directive-2 slope F(n−1)/F(n) ≈
   0.618 is the complement convention and fails at k=3; the correct
   rational approximant is F(n−2)/F(n). Recorded as claim
   `steer-d2-literal-slope` (holds-here: no, contradicts
   `mechanical-word-digit-rule`).
2. **Verified status upgrade.** The slope-corrected arc-midpoint construction
   was already verified in a prior cycle at k=1..100 with exact rational
   arithmetic (`research/notes/mechanical-slope-correction.md`); the claim note
   now records this, so a fresh run does not re-verify.
3. **Every summary is now a one-file note** with the source's URL, the precise
   statements, their hypotheses, whether they hold here, and their bearing;
   the four `request_research` gaps are closed by `answers:` lines in the
   governing claims (verified: the requests ledger file still lists them as
   open in the rendered copy — see the note on ledgers below).
4. **Sources that do not help**, with the reason, are recorded: the
   Hieronymi decidability paper (tier-3 background; decidability ≠ feasible
   evaluation), MathWorld rabbit sequence (convention trap), A344953
   (peripheral catalogue entry), the two citation graphs (metadata only),
   Berstel–Karhumäki tutorial (background), and atcoder internal header
   (base-case only).
5. **Cognee memory server remains down** — every `remember_memory` failed
   health check this cycle too. All durable findings are on disk in
   `research/notes/durable-findings-pe1006.md`, thread
   `mechanical-word-floor-sum.md`, and the claim notes.

## Ledger caveat

`derived/REQUESTS.md` (rendered) still lists the four requests as open even
though the governing claims carry `answers:` lines naming them. The requests
ledger's re-derivation appears not to be triggered by claim-note `answers:`
fields in this run's tooling; the `req-close-*` notes
(`research/summaries/requests-closed-recap.md`) record the closures explicitly
on disk. Not a blocking gap, but the runtime-rendered ledger may need a
`request_research` re-post or a manual note to reflect closure.

## Open items for the solver (unchanged from durable-findings)

1. Implement the universal-Euclidean second-moment monoid (fhq/OI-wiki/LOJ138);
   check vs brute on k=1..150 and Psi(10) mod M = 10699667; run at k=10^18.
2. Second route: directive 1's autocorrelation at k = F_n − 1 (pattern-hunt
   shows it does not generalise to arbitrary k).
3. Optional cleanup: merge duplicate claims (`req-close-*`,
   `fibonacci-word-sturmian-density-balance` vs the governing ones).
4. The slope check `code/out/check_slope.py` is superseded (k=1..100 already
   verified); no need to run it.