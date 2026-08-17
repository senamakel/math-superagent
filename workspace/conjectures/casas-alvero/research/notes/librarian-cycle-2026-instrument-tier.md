# Librarian cycle — instrument tier, Yakubovich v2, and lead resolutions

What this cycle changed in the library, and what it could not.

## Added to `research/sources/` (full texts, read-only)

1. `clo2005_using-algebraic-geometry.full.md` — Cox, Little, O'Shea, *Using
   Algebraic Geometry* (GTM 185, 2nd ed., Springer 2005) — the canonical
   reference for the run's named instruments **resultants and Gröbner bases
   (incl. weighted orders, elimination, zero-dimensional ideals)**. Full PDF
   converted; 37k lines, 11 sections, genuine book-level text.
   URL: https://eclass.uoa.gr/modules/document/file.php/D231/Papers/Cox-UsingAlgebraicGeometry.pdf
2. `eom_resultant.full.md` — Encyclopedia of Mathematics, "Resultant".
   URL: https://encyclopediaofmath.org/wiki/Resultant
3. `eom_groebner-basis.full.md` — EoM, "Gröbner basis".
   URL: https://encyclopediaofmath.org/wiki/Gr%C3%B6bner_basis
4. `eom_newton-diagram.full.md` — EoM, "Newton diagram" (the EoM name for the
   Newton polygon / Puiseux diagram method). The URL `.../Newton_polygon`
   404s; this is the correct page.
   URL: https://encyclopediaofmath.org/wiki/Newton_diagram
5. `wikipedia_newton-polytope.full.md` — Wikipedia, "Newton polytope"
   (multivariate-general Newton polygon: convex hull of exponent support).
   URL: https://en.wikipedia.org/wiki/Newton_polytope
6. `wikipedia_hasse-derivative.full.md` — Wikipedia, "Hasse derivative" (the
   char-free derivative convention the bad-prime literature uses).
   URL: https://en.wikipedia.org/wiki/Hasse_derivative
7. `towards-casas-alvero_porto.full.md` — Yakubovich, *Towards the
   Casas-Alvero conjecture* (arXiv:1504.00274 **v2**, 14 Aug 2015) via the
   University of Porto repository — a distinct primary (real-rooted distinct-
   roots constraints, Abel–Gontcharoff machinery) now held alongside the v1
   already present. See `research/notes/yakubovich-1504-00274-v1-v2.md`.

## Not obtainable (recorded, not silently dropped)

- **Gelfand–Kapranov–Zelevinsky, *Discriminants, Resultants, and
  Multidimensional Determinants*** (Birkhäuser 1994, Modern Birkhäuser
  Classics) — the definitive elimination-theory monograph; **paywalled**, no
  free full text (SpringerLink; ranicki mirror 404s). Record as a would-be
  instrument-tier addition; the run's needs at this tier are covered by CLO +
  EoM + the held de Frutos Marín 2013 thesis (whose §1.3.1 has the classical
  resultant weighted-degree statement) + Ghosh 2024's citations.
- **Chávez Martínez 2018 thesis** PDF — still network-blocked at every route
  attempted (repositorio.unican.es, hdl.handle.net, web.archive.org 503).
  The abstract is held in
  `research/notes/chavez-martinez2018-fixed-roots-thesis.md`. Single most
  valuable degree-20 primary not held. Recorded as a fetch-blocked request.
- **de Frutos Marín 2015** JTN note PDF — still blocked (singacom.uva.es).
  Abstract-held, bad-prime lists already corroborated (claim
  `badprimes-lists-corroborated-by-defrutosmarin2015`).
- **Casas-Alvero 2001 origin paper** — paywalled; content covered by held
  García Barroso et al. 2025 full text (the modern development of the origin
  theorem). Closed-as-irrelevant previously; not re-fetched.

## Lead resolutions (frontier/instrument)

- **"Cen" false lead resolved.** The frontier's `Cen, X.: New lower bound …`
  is **not** a CA distinct-roots result: it is Cen's *New lower bound for the
  number of critical periods for planar polynomial systems*, J. Differ. Equ.
  271 (2021) 480–498 — dynamical systems, unrelated to CA. Do not chase it
  again as a CA-lead.
- **The EoM Newton-polygon 404** is a naming issue; the correct page is
  "Newton diagram" (held).
- **Ghosh 2024 finiteness** status datum: Soham Ghosh's own page says the
  2024 finiteness result (arXiv:2402.18717) is "to appear in the American
  Journal of Mathematics". The 2025 proof (2501.09272) remains an unverified
  preprint, v2 "major revisions", not withdrawn, not journal-published.

## Library-integrity notes

- The memory server was unhealthy during this cycle; every download reported
  "would be accepted and dropped". All seven documents are present on disk
  with full text + summary + each state's source URL; **durable Cognee
  storage must be re-attempted once the memory server recovers** — do not
  assume it happened.