# Librarian report — 2026 cycle (DRR status + generalized saddle-connection machinery)

**Memory note:** Cognee server is down this cycle; verified findings persist in
`research/notes/` and the claims ledger instead (per CONTEXT.md).

## What this cycle searched and found

Goal: keep building the reference library against the live gaps
(`complete-current-ledger-cb3d`, `dumortier-roussarie-rousseau-9c4f` — the DRR
121-graphics ledger), and cover the angles the library is thinnest on.

### 1. DRR ledger status — reconfirmed, no post-2020 consolidated table exists

Searches (research-paper category, 2023–2026 window) for a graphic-by-graphic
open/closed ledger of the 121 DRR graphics, and for closures of the open classes
(degenerate graphics, hemicycles), returned **no consolidated post-2020 ledger**.
This matches the existing claim `drr-ledger-no-consolidated-post2020`. The
picture stands, triangulated from held full texts:

- **RSZ 2015** (Rousseau–Shan–Zhu, arXiv:1502.00689) closes `(I¹₁₂)` and
  `(I¹₁₃)` — authors state this brings the closed count to **88**.
- **RR 2015** (Trans. Moscow Math. Soc., arXiv:1506.07104) fully closes
  `(I¹₁₄)` (Thm 1.2); proves only the *boundary* limit periodic sets of
  `(I¹₆b)`, `(H³₁₃)`, `(DI₂b)` (Thm 1.1); and names `(H³₁₄)` as the **one**
  graphic through a triple point at infinity with **no partial result at all**.
- **Lu 2026** (arXiv:2607.13785, UNREFEREED preprint) claims local uniform
  finite cyclicity of exactly `(H³₁₄)`; finite algebraic core VERIFIED
  clean-room by this run, full analytic proof NOT machine-checked, bound
  existential. Still a preprint (no journal acceptance located this cycle).
- **Shan 2013 Table 1.1** counts **125** graphics in the standard origin family
  (vs 121 in DRR/RSZ/RR) — counting-convention discrepancy. Per-class prose:
  11 degenerate graphics open (only DF1a, DF2a done; DF2a finished by Huzak
  2018); only (I₆a) elementary non-hyperbolic open; thesis closes the 4
  RH-graphic families (Ji2, Ua(1), IJb, I1b). OCR'd column totals (85/36/4/125)
  do not sum cleanly — cite labels/prose, not totals.

**Bottom line:** the ledger gap is confirmed unfillable from one source; the
run's honest statement is the one in `drr-list.md` (≥89/121 closed by 2015,
3 boundary-sets-only, `(H³₁₄)` open/claimed, ≥11 degenerate open).

### 2. New primary source added: generalized separation function (QTDS 2025)

Downloaded and filed:
`research/sources/separation-function-generalized-saddle-connections-qtds-2025.full.md`
(open access, Qual. Theory Dyn. Syst. 24, art. 227, 2025; URL recorded in file).
Summary at
`research/summaries/separation-function-generalized-saddle-connections-qtds-2025.md`.

- **Relevance:** generalises the Melnikov separation function to connections
  whose endpoints are semi-hyperbolic or nilpotent (where the classical
  improper integral can diverge) via a residue-type object (Theorem A). Applies
  to: heteroclinic connections between nodes / semi-hyperbolic saddles at
  infinity / non-elementary singularity at infinity, and a **quadratic
  perturbation of a center whose unbounded period annulus has a semi-hyperbolic
  hemicycle as outer boundary** — exactly the object class of the open
  `(H³₁₄)` graphic and the hemicycle threads.
- **Status:** methodological tool; does NOT close any DRR graphic or change the
  count. Open-access, refereed.

### 3. Hemicycle paper published status upgraded

Marín–Villadelprat, *The cyclicity of hyperbolic hemicycles* — held full text
from arXiv:2501.16924; this cycle confirmed it is **published** as
J. Differential Equations 258, doi:10.1016/j.jde.2025.113281 (2025). Updated
the summary's header line. Same content (Theorems A–D: cyclicity exactly 2 for
the QR³ hemicycles Γu, Γℓ when a₀≠−1; ≥2 when a₀=−1; simultaneous alien cycle
bifurcations in 3 cases).

## What remains open (for requests)

- The complete 121-row DRR catalogue (DRR 1994 raw list) is still not held; the
  exact open-count per family rests on triangulation, not a single authoritative
  ledger. `complete-current-ledger-cb3d` / `dumortier-roussarie-rousseau-9c4f`
  remain open.
- Whether Lu 2026 `(H³₁₄)` closure has been accepted/published is NOT settled
  (no journal record found this cycle); thread `lu-h14-3-verification` open.

## Nothing further

The library is thick on the DRR program, Écalle/Ilyashenko finiteness, Bautin/
Lyapunov machinery, Liénard, canards, Abelian integrals, and o-minimality. This
cycle added the one genuinely on-thread primary source found (generalized
separation function) plus a publication-status upgrade. Further gathering should
continue only against a stated gap in `research/REQUESTS.md`.
