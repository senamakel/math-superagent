# Librarian cycle — final status and access boundaries (2026-08-18)

## Search scope
This cycle worked the open requests `complete-current-ledger-cb3d` and `dumortier-roussarie-rousseau-9c4f`, then checked the newer status of the named graphics and the primary lower-bound/smooth-test sources. Searches used citation-graph, Exa research-paper/pdf queries, and the held-source corpus; no URL was invented.

## Verified additions / confirmations

1. **Shan 2013 Table 1.1 was read directly in the held thesis** (`research/sources/shan-phd-thesis-2013.full.md`, lines 540–640): at thesis time the table uses a 125-graphic convention and records 85 done, 36 open, 4 the author's work; its prose states that only DF1a and DF2a were finite-cyclic at that point and the other 11 degenerate graphics were open. This confirms the named open degenerate list already recorded in `research/drr-list.md`.

2. **Lu arXiv:2607.13785 is a real, current preprint**, verified by a fresh research-paper search: “Local Uniform Finite Cyclicity of the H^3_14 Semihyperbolic Hemicycle,” submitted July 2026. Its abstract claims a local uniform bound in a five-parameter source-normalized unfolding, exactly the graphic RR 2015 left without a partial result. The full source is already held at `research/sources/lu-h14-3-2026.full.md`; the workspace's exact checks establish only finite algebraic/Bautin identities, not the analytic domain, remainder, itinerary completeness, root uniqueness, or uniform zero theorem. Therefore it remains asserted-by-source/unrefereed, not a settled closure.

3. **Recent status search found no published closure of the remaining named rows.** Deep research and targeted Exa searches through 2026 consistently returned: RR 2015 proves only boundary limit-periodic-set results for `(I^1_6b)`, `(H^3_13)`, `(DI_2b)`; no peer-reviewed source found in this cycle closes those full graphics or the 11 degenerate rows. The 2025 Marín–Villadelprat hemicycle paper is already held and concerns hyperbolic hemicycles, not these open DRR rows.

4. **Dulac 1923 canonical record is already held** at `research/sources/dulac-1923-sur-les-cycles-limites-numdam.full.md`, with DOI `10.24033/bsmf.1031`. The 144-page PDF was found on Numdam but the downloader refused conversion because it is too large; the smooth-test/error analysis is instead supported by held Ilyashenko and Yeung sources. This is a genuine access boundary, not a missing citation.

5. **Christopher–Lloyd lower-bound primary remains paywalled.** Searches found the exact title, DOI `10.1098/rspa.1995.0081`, and abstract: the Hilbert numbers grow at least as fast as `n^2 log n`. The full paper is not held; the claim remains source/abstract-level. The adjacent weakened-H16 lower-bound PDF is held and does not replace the `n^2 log n` primary.

## Requests still open

- The DRR 1994 JDE paper's raw 121-label catalogue and the 1997 Nonlinear Analysis survey remain paywalled/blocked. UHasselt, MaRDI, MathSciNet and Rousseau's publication site provide records/abstracts but no full catalogue. The honest ledger remains triangulated: at least 89/121 fully closed in the 2015-era arithmetic (88 RSZ plus `(I^1_14)` RR), three boundary-only rows `(I^1_6b),(H^3_13),(DI_2b)`, `(H^3_14)` claimed only by Lu 2026, and 11 degenerate rows open in Shan's 2013 list.
- Fishkin's “perturbed center” full text remains unavailable: AMS PDF requests were rate-limited, and legitimate mathnet searches did not locate a volume-71 full-text record. Only the abstract-level claim is held.

## Evidence boundary
No theorem about the full H16.2 conjecture was obtained. No numerical result was promoted to proof. No new Lean theorem was produced in this librarian cycle. The library is sufficient for phase 1 under `GOAL.md`; further searching should be driven by a new precise request rather than broad duplicate fetching.
