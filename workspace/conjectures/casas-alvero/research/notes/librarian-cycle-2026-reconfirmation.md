# Librarian cycle — 2026 re-confirmation and one redundancy cleaned up

## What this cycle established

1. **The library remains current through 2026.** A fresh `exa_search` restricted
   to `start_published_date 2026-01-01` returns ONLY already-held works (Ghosh
   2501.09272, Schaub–Spivakovsky 2411.13967 / s40687-024-00444-z, Ghosh
   2402.18717, Castryck et al. 1208.5404, Graf-von-Bothmer et al. 2007). No new
   settled degree, no new disproof, no new refereed partial result outside the
   held set. `citation_graph` on 2402.18717 and 2411.13967 each added 0 new
   works: the highest-weight works in the field, both correctly shown to cite
   only material already in the library.

2. **The three documented blocked fetches were re-attempted and remain
   network-blocked** (same class of failure as every prior cycle):
   - Chávez Martínez 2018 thesis: both Unican handles
     (`repositorio.unican.es/xmlui/handle/10902/15246`,
     `hdl.handle.net/10902/15246`) fail at the network layer; Dialnet has no
     record for it. Its abstract (held, quoted) remains the only held content.
   - de Frutos Marín 2015 JTN note: uva.es host unreachable (same as
     uvadoc.uva.es).
   - Díaz-Toca & Gonzalez-Vega 2006 Maple proceedings: still no open PDF.
   These are recorded as documented-blocked in the notes; the `request_research`
   gate refuses to re-register them because claim-level content covers their
   subject — a known design misfit for *source-availability* gaps, not a sign
   they are unnecessary.

3. **Redundancy cleaned up (my one concrete new action).** This cycle fetched
   `https://doi.org/10.4153/CMB-1971-050-9` (Rahman 1971) and got only the
   Cambridge landing page. On inspection the **full text was already held** at
   `research/sources/rahman1971_distinct-zeros-product.pdf.full.md` (all 3 pages
   including the complete proof). The landing-page copy is a weaker duplicate;
   I marked it SUPERSEDED/redundant so nothing cites the abstract page as the
   full paper, and so a later pass does not re-fetch it.

## Assessment

Every angle of GOAL.md remains served by a held full text. The status
(CA open; smallest open degree 20; Ghosh 2501.09272 an unverified claimed
proof), minimal-counterexample structure (≥5 distinct roots, ≤4 ⇒ CA,
multiplicity-N−2 ⇒ pure power, shared-root set ≠ 2), verification bound
(d≤7 Gröbner /ℚ, d=12 settled, d=20 open), and the settled restricted classes
(p^k, 2p^k, …; ≤4 distinct roots; real-rooted; degree-20 no-3-recycled-roots)
all trace to held primary sources.

The frontier's top is worked: every rank≥2 lead is held or documented-blocked.
There is no fetchable, non-duplicate source that would change the run's
understanding. Per GOAL.md's phase-1 exit rule and the prior coverage-recheck
note's recommendation, the run should spend its next cycles on the mathematics
directly (the open tasks: diversify-search-constructions, rdc-charp-break
and its downstream decisions) rather than on re-sweeping this ground.

**NOTHING FURTHER — library current; all documented gaps blocked at the network
layer; next cycles are mathematics, not gathering.**
