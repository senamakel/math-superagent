> **Note — duplicate rendering; the owning note holds the claims.**

This file is the **HTML rendering** of Koshelev & Koshka, "Combinatorial Geometry
of Erdős–Szekeres Type Problems: SAT/ASP Modeling and Linear Subreduction"
(arXiv:2604.20120). The owning note holds the full digest and claims:

→ [[koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120]]
(claims `kk-linear-subreduction`, `kk-h61-h62`, `kk-adjacent-not-esz7`, all
asserted-by-source, 2026 preprint).

**Bottom line.** A linear-subreduction realizability method (feed the full
logical formula + geometric inequalities to SMT with abscissae fixed, turning
orientation determinants into linear-integer constraints) that lets a search run
over all admissible signotopes at once rather than per-signotope. Reproduces
ES-boundary values (h(6,≥2)=17, h(6,1)=18) with explicit integer coordinates the
run's oracle can check. The adjacent bicolored/Ramsey values it also proves
(h_nc(4,0;4,0)=26, R_EC(3,3)=21) are **not** ES(7) progress.
