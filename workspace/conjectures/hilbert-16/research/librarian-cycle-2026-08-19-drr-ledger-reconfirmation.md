# Librarian cycle 2026-08-19 — DRR ledger re-confirmation and library integrity

*Memory server is down (Cognee 409/health-check timeouts throughout this cycle), so
this note carries the cycle's verified findings in place of a `remember_memory`
call. Store it to memory once the server recovers.*

## What this cycle did

Worked the two open request rows (`complete-current-ledger-cb3d`,
`dumortier-roussarie-rousseau-9c4f`) — the DRR 121-graphic target inventory —
plus the top of `derived/FRONTIER.md`. No broad library growth: ROOT.md already
meets the phase-1 exit criterion and the library holds ~170 primary/scholarly
sources.

## Verified re-confirmations (all asserted-by-source; held full texts cited)

1. **No consolidated post-2020 graphic-by-graphic DRR ledger exists in the
   reachable public record.** Confirmed independently by:
   - `deep_research` (2026-08-19): returned only already-held sources (RSZ 2015,
     RR 2015, Shan 2013, Zhu 2005, Roussarie–Rousseau 2008, DR 2009, DRR
     companions) and no synthesis — the agent found no ledger either.
   - Two Exa sweeps for post-2015 status and for closures of I¹₆b/H³₁₃/DI₂b.
   This matches the held claim `drr-ledger-no-consolidated-post2020`.
2. **DRR 1994 (JDE 110:86–133, PII S0022039684710618) is not openly
   available.** The UHasselt Document Server record `hdl.handle.net/1942/3763`
   is metadata-only (title/authors/abstract; no PDF attachment). This matches
   the held claim and `research/drr-list.md`'s honest bound: the full 121-row
   catalogue cannot be truthfully produced by this run.
3. **The 121 vs 125 discrepancy is a counting-convention difference, not an
   error.** 121 is used by Zhu 2005, RSZ 2015, RR 2015, and the published
   Marín–Villadelprat 2025 (JDE 2025, full text held). Shan 2013 (thesis, held)
   uses 125 = 85 done + 36 open + 4 proved in-thesis (families Ji2, Ji3, Jb,
   fib), listing per-class done/open counts including "Degenerate graphics 2
   done / 11 open". The held claim `drr-shan-2013-table11-ledger` already
   records that the OCR'd column totals do not sum cleanly and the reliable
   content is the class labels and prose.
4. **Current standing account (unchanged by this cycle):** ≥88 of 121 closed by
   RSZ 2015 (the authors' own count); I¹₁₄ closed by RR 2015 (run arithmetic
   89); I¹₆b, H³₁₃, DI₂b boundary-limit-periodic-sets only (RR 2015 Thm 1.1,
   full graphics open); H³₁₄ open per RR 2015 with Lu arXiv:2607.13785
   (unrefereed) claiming local closure; 11 degenerate graphics open per Shan
   2013: DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5.
5. **Marín–Villadelprat 2025 (JDE, arXiv:2501.16924, full text held) is a
   modern refereed confirmation** of the 121-graphic frame and adds: Theorem B
   (cyclicity of hyperbolic hemicycles in quadratic integrable systems Q3^R,
   perturbed inside the full quadratic family), Theorem C (simultaneous
   cyclicity exactly 3 on K1, 2 on K2, ≥3 at a0=−1), Theorem D (alien limit
   cycles in simultaneous bifurcation, for three specific cases). This is a
   tangential-adjacent result (hemicycles H2^1 class), not a DRR-row closure.

## What failed this cycle (recorded so it is not retried)

- `citation_graph` (OpenAlex API) returned 429 Too Many Requests on every
  attempt this cycle — 7 failures. The endpoint is rate-limited from this host
  right now; do not retry it in the same cycle. Frontier leads were instead
  checked against the held corpus by grep (all top-40 rows already covered).
- `remember_memory` — memory server down (health-check timeout; 18 failures
  across the run). Findings stored in this note instead; store to Cognee when
  the server recovers.
- `download_document` for the UHasselt DRR record was correctly refused as a
  duplicate (already held at `research/summaries/drr-1994-hilbert-16-quadratic-record.md`).

## Library state (unchanged in content this cycle)

- Canonical tier held: Ilyashenko Centennial History (2002), Marín–Villadelprat
  2025 (JDE), RSZ 2015, RR 2015, Shan 2013 thesis, Zhu 2005, DGR 2002,
  DR 2009, Roussarie–Rousseau 2008, Huzak 2018, Lu 2026, BNY 2010,
  Binyamini–Dor 2011, Mourtada 2009, Écalle avant-propos page, and the rest of
  the ~170-source corpus.
- Confirmed closed-access (will not be re-fetched): DRR 1994 (JDE),
  Roussarie 1998 book (Birkhäuser PM 164), Roussarie 1986 (Springer),
  Écalle 1992 book (Hermann), Dumortier–Roussarie 1996 Memoirs AMS 577.
- Open requests stand: the two DRR-ledger rows, with falsifiers stated. This
  cycle's searches are further negative evidence that they are genuinely open.

## Claim-block for the ledger

```markdown
statement: As of 2026-08-19, no source published after 2020 closes the full
quadratic graphics (I^1_6b), (H^3_13), (DI_2b) (RR 2015 proves only their
boundary limit periodic sets), and no source closes any of the 11 degenerate
graphics (DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5) beyond
(DF1a) [DR 2009] and (DF2a) [Huzak 2018]. (H^3_14) remains open with Lu
arXiv:2607.13785 (unrefereed) as the sole claim.
hypotheses: quadratic planar polynomial systems; DRR 1994 program inventory;
full graphic vs boundary limit periodic set distinction.
evidence: asserted-by-source — held full texts RR 2015 (arXiv:1506.07104),
RSZ 2015 (arXiv:1502.00689), Shan 2013 (hdl.handle.net/10315/32000),
DR 2009 (CPAA 8:1133–1157); 2026-08-19 deep_research and Exa sweeps found no
later closure.
falsifier: a primary source dated after 2020 proving finite cyclicity of the
full (I^1_6b), (H^3_13), (DI_2b), (H^3_14), or any of the 11 named degenerate
graphics, with the graphic label matched to the DRR convention.
```

This re-confirms `h16-drr-open-rows` and `drr-rr-boundary-only-for-3-graphics`
rather than changing them.
