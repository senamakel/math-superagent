# Pattern-finder round 8 — NOTHING FURTHER (re-survey confirms no new data)

## What I did

Re-mapped every result file under `code/out/` by modification time (ls -lt on
both `*.captured.txt` and `*.md`), read the set of per-n series the run has
computed, and checked the memory graph for what is already related.

## Result: no new sequence has landed since round 7

The newest data on disk is `convex_spectrum_n8_k4.captured.txt` (07:04), which
was already consumed by pattern-finder round 6 and surveyed by round 7. The only
files newer than that are round 7's own artifacts:

- `pattern_finder_report7.md` (12:46)
- `nnc_from_captured_claim.md` (12:46)
- `INDEX.md` (12:47)

So the conditions the brief assigns to NOTHING FURTHER are met: the results have
not changed since the last look, and nothing new computed since.

## The per-n series already tabulated (re-confirmed, no new tools run)

These are all recorded in earlier rounds; none is new:

| Quantity | Terms | Status |
|---|---|---|
| gsplit valid splits n=4..7 | 6, 4, 2, 0 | arithmetic decay 12−2n to 0; template-scoped; mirrored in `gsplit_phase2.captured.txt` (4/2/0 at n=5/6/7, n=4 from `gsplit_seq.py`) |
| realized (n-1)-convex block-pattern classes | 3, 6, 10, 15, 21 | = C(n−1,2) = A000217; explicit bijection verified exactly n=4..7 |
| full transversals | 2, 9, 96, 2500, 162000, 26471025 | = prod C(n−2,i) = A001142(n−2); proved identity, all convex |
| distinct (n-1)-convex subsets | 4, 38, 802, 39648 | OEIS miss; super-exponential; dead thread |
| non-convex 4-subsets NNC | 32, 701, 12740, 213190 | filed round 7; feeds the LIVE queued task `con4-supersat-nnc-count` |

## Why I did not compute anything new

Directive 22 (in `config/DIRECTIVES.md`, lines 225–239) prohibits further
es_construct convex spectra, OEIS lookups on numbers off this placement, and n=8
extensions of any template quantity. The comparison criterion it sets — a pattern
counts only if the quantity is defined for every n-avoiding set of size 2^{n−2}
and is computed on two non-isomorphic sets and compared — cannot be satisfied
here: the second family (Karolyi–Toth twin, Aichholzer order types) is not
realized on disk and the Aichholzer fetch is still queued.

So the honest answer is NOTHING FURTHER: every cached regularity is already
recorded, and every new computation that would be permitted requires a second
family that does not exist in this workspace yet.
