# Durable findings, librarian cycle 2026-08-17 — PENDING COGNEE PUSH

The Cognee memory server was down this cycle (health check timed out), so the
three librarian findings below could NOT be stored with `remember_memory`.
They are fully recorded in workspace files and the claims ledger. A later run
with a healthy memory server should push each as a `remember_memory` call, so
they are reachable from Cognee rather than only from disk.

Each `remember_memory` should take `text` verbatim from the bullet, with the
listed `source`.

## 1. Hilbert-covariants mislabel RESOLVED → remember_memory

- source: librarian cycle 2026-08-17 / research/notes/abdesselam-chipalkatti-mislabel.md
- text: Casas-Alvero library-integrity repair RESOLVED: the correct Abdesselam &
  Chipalkatti "On Hilbert covariants" paper (arXiv:1203.4761 = Canad. J. Math.
  66(1) 2014 3-30, DOI 10.4153/CJM-2012-046-1) IS held in full at
  research/sources/abdesselam-chipalkatti2012_hilbert-covariants.full.md (2205
  lines, Prop 3.2 line 822: G_{1,d} = (F,F)_2 is the Hessian of F). Two
  wrong-content files under the same name are marked DO-NOT-CITE (arXiv:1010.2358
  Campagna & Pagh data-mining; arXiv:1010.2667 Guo & Zhang wireless). The earlier
  recalled memory "paper not held / correct id 1010.2667" was WRONG on both
  counts and is superseded. The Hessian-iff-perfect-power theorem is now
  anchored; hessian-covariant-transvectant remains refuted on its unproved
  bridge. Claim: abdesselam-chipalkatti-file-mislabel-corrected.

## 2. Origin-paper OA status → remember_memory

- source: librarian cycle 2026-08-17 / research/notes/librarian-cycle-hessian-anchored.md
- text: Casas-Alvero origin paper (Casas-Alvero, "Higher Order Polar Germs",
  J. Algebra 240(1) 2001 326-337, DOI 10.1006/jabr.2000.8727, OpenAlex W2003962780)
  is bronze open-access in principle but NOT obtainable from this host: OpenAlex
  content URL returns HTTP 401, ScienceDirect PDF returns HTTP 403, no arXiv
  version. Still un-held, documented as obtainable-in-principle, network-blocked.
  Nothing load-bearing is missing; substance covered by the held secondary tier.

## 3. Fresh arXiv sweep confirms coverage → remember_memory

- source: librarian cycle 2026-08-17 / research/notes/librarian-cycle-hessian-anchored.md
- text: Casas-Alvero reference-library coverage re-check: fresh arXiv API sweep
  (all:"Casas-Alvero", 40 results, date desc, held at
  research/sources/arxiv_search_casasalvero_fresh.full.md) returns 23 items, all
  already held or deliberately excluded. No new 2023-2026 primary treatment
  absent. Status unchanged through Aug 2026: CA open, degree 20 smallest open,
  Ghosh arXiv:2501.09272 v2 (21 Mar 2026, "Major revisions") the only
  complete-proof candidate and an unverified preprint. Further gathering only
  against a stated gap in research/REQUESTS.md.
