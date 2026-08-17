# Pattern-finder round 9 — NOTHING FURTHER

## What I did

Re-surveyed `code/out/` by modification time (`ls -lt *.captured.txt *.md`) and
re-checked the memory graph for what is already related.

## Result: no new sequence has landed since round 8

The only file newer than pattern-finder round 8's NOTHING FURTHER
(`pattern_finder_report8.md`, 12:55) is `brute_existing.captured.txt` (12:58),
which is an ES **oracle self-check reproduction** — largest convex subset =
2,3,4,5 at n=3..6 and the cup/cap spectra, exactly the values GOAL criterion 3
requires. It carries **no new integer series**.

## The sequence inventory (re-confirmed, unchanged)

| Quantity | Terms | Status |
|---|---|---|
| full transversals | 2, 9, 96, 2500, 162000, 26471025 | = A001142(n−2), all convex (n≤9) — holds exactly, recorded |
| realized (n−1)-convex block-pattern classes | 3, 6, 10, 15, 21 | = C(n−1,2), explicit bijection n=4..7 — recorded |
| distinct (n−1)-convex subsets | 4, 38, 802, 39648 | OEIS miss, super-exponential, dead thread |
| NNC non-convex-4 counts | 32, 701, 12740, 213190 | OEIS miss; feeds queued `con4-supersat-nnc-count` |
| gsplit valid splits n=4..7 | 6, 4, 2, 0 | arithmetic artifact, template-scoped |
| onion layer profiles | [4,4],[5,5,3,3],[6,6,6,5,6,3] | order-type invariants, no numeric regularity; already refuted the Gale route |

## Why not compute anything new

Directive 22 prohibits further es_construct convex spectra / OEIS lookups on
this placement / n=8 extensions. The run's own crossover standard — a pattern
counts only if the quantity is defined for **every** n-avoiding 2^{n−2}-set and
computed on **two non-isomorphic families** and compared — cannot be met: the
second family (Karolyi–Toth twin, Aichholzer order types) is not realized on
disk and the Aichholzer fetch is still queued.

The one live structural quantity, the covering-ratio inequality
NNC·C(N−4,n−4) ≥ C(N,n) (filed in `nnc_from_captured_claim.md`), is unchanged:
its decisive falsifier (convex4 at N+1 = 9,17,33,65) is **not on disk** and
needs the second family.

## Verdict

Conditions for NOTHING FURTHER are met: results unchanged since the last look,
too few per-n terms to assert any exact new sequence, and the cross-family
comparison that would make a new regularity real is impossible until the
Karolyi–Toth twin or Aichholzer order types are realized. I am not inventing a
pattern.
