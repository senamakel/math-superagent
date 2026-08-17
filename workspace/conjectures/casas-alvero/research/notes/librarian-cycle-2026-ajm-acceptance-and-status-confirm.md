# Librarian cycle — 2026-09: AJM acceptance of Ghosh finiteness, published JCA metadata, origin paper still blocked

## Genuine findings this cycle (two) — both are status/metadata upgrades, not new mathematics

### 1. Ghosh finiteness result ACCEPTED at American Journal of Mathematics

`Soham Ghosh, "A finiteness result towards the Casas-Alvero Conjecture"`
(arXiv:2402.18717) has been **accepted for publication at the American
Journal of Mathematics**:

- Hopkins Press journal site (press.jhu.edu, American Journal of
  Mathematics) lists it as accepted, dated 4/7/2026.
- The author's UW page (`sites.math.washington.edu/~soham13/`) lists it as
  "to appear in American Journal of Mathematics".

Scope of the upgrade — **crucial**: this is peer-review acceptance for the
**finiteness** result (the arithmetic CA scheme has finitely many K-points /
the projective variety of CA polynomials is at most 2-dimensional in every
characteristic). It is **NOT** acceptance of the full claimed proof
(arXiv:2501.09272), which remains an unpublished, 0-citation preprint
(v2 21 Mar 2026 "Major revisions"). No independent validation, no journal
version, no retraction. CA remains open as an accepted result; smallest
open degree remains 20.

### 2. Published metadata for Schaub-Spivakovsky "On the Casas-Alvero Conjecture"

Confirmed via Project Euclid (downloaded): **J. Commut. Algebra 17(2):
199-202, Summer 2025**, DOI 10.1216/jca.2025.17.199, received 7 Nov 2024,
accepted 12 Jan 2025, published 2 Sep 2025. Statement: for
i ∈ {d-3, d-2, d-1}, R_i ∉ (R_1,…,R̂_i,…,R_{d-1}), the height
ht(R_1,…,R_{d-1}) = d-1 partial-result direction.

- The Euclid page is paywalled (abstract + citation captured only, not the
  full proof); the **identical content is already held** at
  `research/sources/schaub_spivakovsky_jca-2025_hal-open.full.md` (HAL open
  variant). The new Euclid download (`schaub_spivakovsky_jca-2025_published.full.md`)
  is therefore a **metadata/provenance record, not new content** — it fixes
  the official pagination/citation so nothing cites the HAL preprint as the
  publication.

## Re-confirmed (no change)

- A fresh 2026-01+ arXiv sweep (`exa_search`, category research paper)
  returns only held works: Ghosh 2501.09272, Ghosh 2402.18717, Schaub-
  Spivakovsky s40687-024-00444-z, Graf-von-Bothmer ≥2007, Lu 1707.04754.
  No new settled degree, no new disproof, no new refereed partial result
  outside the held set.
- `citation_graph` on 2501.09272 adds 0 connected works (held 0-citation
  record). No independent verification/refutation of the claimed proof
  anywhere in the 2026 record.

## Still blocked (documented fetch-limits, not misses)

- **Casas-Alvero 2001 origin "Higher order polar germs"** (J. Algebra
  240:326-337, DOI 10.1006/jabr.2000.8727): Elsevier paywall; UB repository
  (`diposit.ub.edu`) has no public record under the attempted handle
  (2445/135055 → 404). The statement/motivation/status are fully covered by
  held secondary tier (MaRDI/zbMATH records, the polar-germs literature,
  Wikipedia, and the held `casas-alvero_2012_roots-and-foci` EMS paper). Not
  load-bearing for the run's scheme-theoretic agenda.
- **Chávez Martínez 2018** thesis (unican.es / hdl.handle.net): network-blocked;
  abstract held.
- **de Frutos Marín 2015** JTN note (uva.es): network-blocked; abstract held,
  and the run has independently verified every bad-prime list it reports.

## Verdict

Library remains comprehensive and current through 2026-09. The only
durable update this pass adds is the AJM acceptance of the finiteness
result — which strengthens the run's `ghosh2024-finiteness` claim's status
(asserted-by-source → accepted-for-publication) while leaving the
**full-proof claim unverified**. The derived ledgers should be updated by
whichever role owns them to reflect: (a) claim `ghosh2024-finiteness`
now "accepted at AJM"; (b) `ca-status-2025` unchanged — 2501.09272 not
independently validated.
