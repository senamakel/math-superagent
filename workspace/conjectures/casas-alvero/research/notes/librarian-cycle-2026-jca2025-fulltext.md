# Librarian cycle — JCA 2025 full text retrieved; Chávez 2018 abstract captured

## What this cycle added

1. **`research/sources/schaub_spivakovsky_jca-2025_hal-open.full.md`** — the FULL
   refereed text of Schaub & Spivakovsky, "On the Casas-Alvero Conjecture",
   J. Commut. Algebra 17(2):199–202 (Summer 2025), fetched from the open HAL
   deposit hal-04341794v3 (5 Feb 2025). This source was previously held ONLY as
   an abstract (`schaub_spivakovsky_jca-2025_on-casas-alvero.full.md`); now the
   complete 4-page text is in the library. It establishes:
   - The CA ⇔ √(R_1,…,R_{d−1}) = (a_1,…,a_{d−1}) regular-sequence reformulation
     (Conjecture 3, Remarks 2–4) — the exact object this run's scheme-theoretic
     elimination targets, in a peer-reviewed venue.
   - **Theorem 5**: for i ∈ {d−3,d−2,d−1}, R_i ∉ √(R_1,…,R̂_i,…,R_{d−1}) — the
     three highest resultants are each outside the radical of the others' ideal.
   - The proof is **real-rooted / Rolle-based** (Prop 6, Cor 7) + an
     almost-counterexample recursion on first roots — an order/analytic argument
     with **no char-p analogue**, same failure mode as the
     Gauss–Lucas/convex-hull step in `rdc-charp-break`. Consistent with CA false
     in char p.
   - Summary: `research/summaries/schaub_spivakovsky_jca-2025_hal-open.md`
   - Claim: `schaub-spivakovsky-jca2025-theorem5` in `research/notes/casas-alvero-status.md`

2. **`research/notes/chavez-martinez2018-fixed-roots-thesis.md`** — the Chávez
   Martínez 2018 UCrea thesis abstract, which a fresh `exa_search` surfaced. Full
   text remains network-blocked (hdl.handle.net and repositorio.unican.es both
   unreachable, same as prior cycles), but the abstract is a genuine, previously
   unattempted find: CA for char-0 polynomials with 2 and 3 distinct roots, and
   **degree 20 with 4/5/6 distinct roots in 302 of 627 cases** (via Gröbner bases
   of the top derivatives), plus a correction of one theorem in a held source [6]
   and a tropical-geometry example. This is the nearest published work to the
   run's `degree20-scored-search` and `fiveroots-multipattern` analyses.
   - Claim: `chavez-martinez-2018-fixed-roots` in `research/notes/casas-alvero-status.md`

## Currency re-confirmed

Fresh 2026-window and broad searches return only already-held works (Ghosh
2501.09272, Schaub–Spivakovsky 2023/2024/2025, Castryck et al 2012, Massri 2018,
Battiston 2015, de Frutos Marín). No new settled degree, no new disproof, no new
refereed partial result outside the held set. The Ghosh claim remains unverified
(preprint, not refereed, not withdrawn).

## Blocked / recorded so nobody re-fetches

- Chávez 2018 thesis full text: network-blocked (abstract held). Do not re-attempt
  from this box; the abstract covers the claim content.
- Casas-Alvero 2001 origin paper: paywalled, closed as irrelevant (background/out
  of scope).
- de Frutos Marín 2013 thesis / 2015 note PDFs, Siebeck curves 2012 full text,
  Diaz-Toca–Gonzalez-Vega 2006: still unobtainable (recorded in prior cycles).

## Memory note

`remember_memory` could not persist the JCA finding this cycle (memory server
health check failing — "would be accepted and dropped"). The finding is safely in
the workspace (full text + summary + claim block); store to durable memory on a
later cycle once the memory server recovers.
