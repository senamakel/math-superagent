# Citation-graph records — existence and influence only (not evidence)

**Source:** OpenAlex/Crossref citation-graph lookups for the Stromquist 1989
paper ([[research/summaries/citations_w2106991731.md]]), the Matschke 2014
survey ([[research/summaries/citations_w2037502603.md]]), Matschke 2022 Trans.
AMS ([[research/summaries/citations_w4214890841.md]]), Asano–Ike 2024
([[research/summaries/citations_w4405957718.md]]), Morales–Villanueva 2025
([[research/summaries/citations_w4408904160.md]]).

**What these establish:** a paper exists, where it is published, and how often
it is cited. Explicitly *not* what any of them proves. Their value to this run
is the **frontier leads** they name, none of which is on disk as a primary:

1. **Wright 2025, "Every Jordan Curve Contains All Vertices of Uncountably
   Many Rhombi—A Short Proof," Amer. Math. Monthly** (DOI
   10.1080/00029890.2025.2556357) and **Wright 2026, "Inscribed rhombi having
   diagonals collinear with specified points," Aequationes Math.** (DOI
   10.1007/s00010-026-01307-4) — the rhombi theorem's current published form.
   The Fung 2021 primary is not on disk (acquisition error); these records
   confirm the result exists in the literature. **If the run wants the rhombi
   statement, acquire Wright 2025 — it is the short proof.**
2. **van Heijst 2014** (algebraic square peg, arXiv:1403.5979) — degree-m
   algebraic curves inscribe ≤ (m⁴−5m²+4m)/4 squares; count claim recorded in
   the arXiv sweep note (claim `van-heijst-2014-algebraic-count`).
3. **Aslam–Chen–Frick–Saloff-Coste–Setiabrata–Thomas 2020, "Splitting loops
   and necklaces: Variants of the square peg problem," Forum Math. Sigma 8,
   e5** — continuous-curve rectangle variants (Hadwiger's parallelogram
   conjecture in R³; rectangles dense in the loop; fair-division
   reformulations). A different attack surface for the continuous case; not in
   library.
4. **Matschke 2022, "On the square peg problem and its relatives," Trans. AMS
   373** — the journal version of the open/dense-class paper (the 2009 arXiv
   text in the library is the accepted version per its abstract; the two agree
   on the statement: several open classes, one dense, "solved for generic
   curves"). No conflict with `matschke2009-open-dense-class`.
5. **Matschke 2020, "Quadrilaterals inscribed in convex curves," Trans. AMS** —
   in library (matschke-2020-quadrilaterals-convex-curves).
6. **Morales–Villanueva 2025** (circularly chainable continua, annulus) —
   abstract carried in-library; full text paywalled.

**Absence signal:** Asano–Ike 2024 has 0 citing works in OpenAlex — nobody has
published a follow-up building on it, so no published confirmation or
refutation of the rectifiable theorem exists as of the check.

```claim
id: wright2025-rhombi-short-proof-exists
statement: A short proof that every Jordan curve contains all vertices of uncountably many rhombi is published: Wright, Amer. Math. Monthly (2025), DOI 10.1080/00029890.2025.2556357; a companion (Wright, Aequationes Math. 2026) treats rhombi with diagonals collinear with specified points. The primary texts are not in this library.
status: catalogued (citation records; no primary text on disk)
evidence: OpenAlex citation graphs (citations_w4214890841.md)
holds-here: yes — confirms the rhombi result is real literature; re-acquire before citing
falsifies: a retraction of Wright 2025
anchor: research/summaries/citations_w4214890841.md
```
