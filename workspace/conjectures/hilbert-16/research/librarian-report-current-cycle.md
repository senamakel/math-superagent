# Librarian cycle report — monomial-count variant, trivial-monodromy Abelian integrals, DRR status re-confirmed

## What was added this pass

1. **Gasull & Santana, "On a variant of Hilbert's 16th problem" (arXiv:2405.04281,
   Nonlinearity 2024) — NEW library addition, published source.**
   - Full: `research/sources/gasull-santana-monomial-hilbert-variant-arxiv-html.full.md`
     (+ abstract page `...-arxiv.full.md`); summary
     `research/summaries/gasull-santana-monomial-hilbert-variant.md`.
   - Counts limit cycles by NUMBER OF MONOMIALS m instead of degree: H^M(m).
     Theorem 1: H^M(m) >= (1/2)m^2 - 3m - 8 for m >= 9 (quadratic growth).
     Theorem 2: H^M(4..10) >= 12,12,12,16,20,24,32. Methods: Abelian integrals
     (Poincare-Pontryagin/Melnikov) for the quadratic bound and H^M(9)>=24;
     reversible-center + weak-focus cyclicity for H^M(4)>=12 (planar-S system).
   - Why: **adjacent problem the library had no source on** — the first
     monomial-count Hilbert analogue held. It independently reproduces and
     improves the O(n^2 ln n) lower bound on H(n) (ties to
     `h16-canard-asymptotic-lower-bound-2020`), and is a test-bed for the
     adopted sharp-Abelian approach. Claim: `h16-gasull-santana-monomial-hilbert-variant-2024`.

2. **Muciño-Raymundo & Rebollo-Perdomo, "Abelian integrals for polynomials with
   trivial global monodromy on C^2" (arXiv:2508.15925, 2025) — NEW, directly
   relevant to the adopted sharp-Abelian approach.**
   - Full: `research/sources/mucino-rebollo-abelian-trivial-monodromy-html.full.md`
     (2117 lines) + abstract page; summary
     `research/summaries/mucino-rebollo-abelian-trivial-monodromy.md`.
   - Trivial-global-monodromy structure makes Abelian integrals POLYNOMIALS of
     the level c, so degree-bounds replace Picard-Fuchs/argument-principle
     machinery. Theorem 23 (primitive type (0,2)): at most floor((n+1)m/2)
     isolated zeros; three-cycle example bounds; worked n=3 case with 15 distinct
     zeros. **Caveat recorded**: Remark 9's "infinitely many complex limit
     cycles" across homology classes is a complex-algebraic phenomenon and must
     NOT be misread as a real-planar counterexample/challenge to H16.2.
   - Claim: `h16-mucino-rebollo-abelian-trivial-monodromy-2025`.

3. **Shao & Li hyperelliptic Liénard (EJQTDE 2024) — capture attempt recorded as
   landing-page-only.** The journal DOI resolved only to the home page (no
   mathematics). Claim `data-shao-li-hyperelliptic-lienard-landing-only` records
   that the paper is NOT held, so the search-summary's "at most six limit cycles"
   claim survives only at recall level and must not be cited as held.

## DRR / open-requests status — re-confirmed by deep research (no new closure)

The open request `complete-current-ledger-cb3d` / `dumortier-roussarie-rousseau-9c4f`
(the full 121-graphics open count) was re-attacked with `deep_research`
bounded to 2023-2026. Result: **no new peer-reviewed closure beyond the 2015
picture**. The literature universally reports:
- 88 of 121 closed by 2015; RR 2015 fully closed I^1_14 + boundary sets only of
  (I^1_6b),(H^3_13),(DI_2b);
- **exactly one graphic, (H^3_14), with no full finite-cyclicity proof**, and
  Lu arXiv:2607.13785 (2026, unrefereed preprint) is the sole claim to it.
This corroborates the run's existing triangulated inventory — the open-count
question's falsifier (a source showing a different open count or a new closure)
did NOT appear. No new download warranted; the DRR open ledger remains the
88/121 + I^1_14 + (3 boundary-only) + H^3_14 picture, with Lu unrefereed.

## Not obtained (re-confirmed genuine)

- Shao-Li EJQTDE 2024 full text (landing page only).
- DRR 1994 raw catalogue, Roussarie 1998 book, Planar Dynamical Systems
  (De Gruyter) — unchanged, prior passes recorded them unobtainable.

## Frontier work

Top frontier rows remain ScienceDirect paywall shells and the two known
unobtainable items (DRR 1994, Planar Dynamical Systems). The Gasull-Santana and
Muciño-Rebollo downloads added ~120 citations to the frontier; those re-point
into the already-deep core. Library remains well-covered across every axis the
goal names (finiteness, DRR, Abelian integrals, lower bounds, Liénard, canards,
o-minimality, Dulac gap/contention).

## Memory

`remember_memory` stored both new findings (Gasull-Santana monomial variant;
Muciño-Rebollo trivial-monodromy Abelian integrals) for cross-run recall.
