# Librarian cycle report — the hyperbolic-polycycle instrument chain

## What was added this cycle (all primary full texts, held locally)

The run's displacement-function attack needs the theory of the return/Dulac map
at *hyperbolic* vertices: its asymptotic expansion, its coefficients, and the
flat-remainder regularity that makes cyclicity uniform in parameters. The
library held only second-hand attributions before. This cycle built the whole
chain from primaries:

| # | Source | Held file | Claim |
| --- | --- | --- | --- |
| 1 | **Mourtada 1991**, Ann. Inst. Fourier 41(3):719–753, DOI 10.5802/aif.1271 | `research/sources/mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.full.md` | `h16-mourtada-1991-hyperbolic-finite-cyclicity-primary` |
| 2 | **Buzzi–Gasull–Santana 2024**, arXiv:2407.20721 | `buzzi-gasull-santana-cyclicity-hyperbolic-polycycles-2024.html.full.md` | `h16-hyperbolic-polycycle-cyclicity-lower-bound-bgs2024` |
| 3 | **Queiroz Arakaki–Santana 2025**, arXiv:2504.07225 / J. Dyn. Diff. Eq. | `queiroz-arakaki-santana-persistent-hyperbolic-polycycles-2025.html.full.md` | `h16-persistent-polycycle-cyclicity-qas2025` |
| 4 | **Marín–Villadelprat 2020**, JDE 269:8425–8467 (URV accepted version) | `marin-villadelprat-dulac-map-local-setting-2020-full.full.md` | `h16-mv-dulac-map-local-expansion-2020` |
| 5 | **Marín–Villadelprat 2024**, JDE 404:43–107 (arXiv:2105.09785) | `marin-villadelprat-dulac-coefficient-properties-2024-arxiv.html.full.md` | `h16-mv-dulac-coefficient-formulas-2024` |
| 6 | **Dukov 2023**, Sb. Math. 214(2):226–245 (arXiv:2201.03652) | `dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.html.full.md` | `h16-dukov-multiplicity-hyperbolic-polycycles-2023` |
| 7 | **Dukov 2025**, Sb. Math. 216(7):902–947, DOI 10.4213/sm10206e | `dukov-lower-bound-cyclicity-hyperbolic-polycycles-2025.full.md` | `h16-dukov-lower-bound-cyclicity-hyperbolic-polycycles-2025` |

Each has a summary in `research/summaries/` and a fenced claim block that
re-derives into `derived/CLAIMS.md` (verified present via `search_claims`).

## The two load-bearing verified findings

1. **The instrument chain is closed and primary.** Mourtada 1991 proves generic
   hyperbolic polycycles have finite cyclicity in C^∞ families (Thm 3, with a
   coarse explicit bound). MV 2020 gives the local Dulac map/time expansion with
   the **parameter-uniform flat class F^∞_L**, and **Remark 1.4 identifies and
   fixes a gap in Roussarie's Theorem F** (an s-only-flat remainder stated as
   C^L in (s,α), which caused a gap in Roussarie [16]) — this is the exact
   smooth-test shape (Test 1) this run must respect. MV 2024 gives the explicit
   first coefficients Δ₀₀, Δ₁₀=Δ₀₀λS₁, Δ₀₁=−Δ₀₀²S₂, Δ₁₁=−2Δ₀₀²λS₁S₂ and the
   factorization Δ_{ij}=Ω_{ij}Δ_{0j}. QAS 2025 shows a persistent polycycle's
   return map is ℛ(s;μ)=s^{r(μ)}(A_{1,n}+flat) with cyclicity 0/1/2/3 read off
   the coefficients. BGS 2024 gives the breaking lower bound Cycl ≥ Δ(Γⁿ).

2. **The cross-link S₁,S₂ was verified by reading both full texts**: the
   S₁^{m+1}, S₂^m in QAS2025 Theorem B's 𝒜 ARE the S₁,S₂ of MV2024 Theorem A
   (the Dulac-map coefficients, explicit integrals along separatrices). So the
   persistent-polycycle cyclicity coefficients are *computable data*, not
   existence statements — the concrete finite core a Lean certificate can hold.

## The honest boundary (state for the other roles)

The open DRR rows — (I¹₆b), (H¹³₃), (DI₂b) boundary sets, the ≥11 degenerate
graphics, and the H¹⁴₃ hemicycle (Lu 2026, unrefereed) — are **non-hyperbolic
and/or non-persistent**. Mourtada/BGS/QAS/MV/Dukov all require hyperbolic
saddles; QAS is explicitly the no-breaking case. So the hyperbolic side of the
DRR inventory is now settled and primary-sourced, and the open rows are exactly
the ones outside this instrument chain — to be attacked with the nilpotent/
degenerate machinery (Zhu–Rousseau, RR 2015, fake-saddle, canard) the library
already holds. This is the position the g-transition/g-zeros/g-uniform nodes
start from.

## Corrigendum recorded (open check — flagged to the run)

A **2026 corrigendum to the MV 2020 local-setting paper** exists (SSRN 6809315,
Marín–Villadelprat). Not held. The held 2020 statements must be checked against
it before quantitative use. Recorded in the MV 2020 summary and in assertion
`h16-mv-dulac-map-local-expansion-2020`.

## What could not be obtained

- **Marín–Villadelprat 2021, "General setting", JDE 275:684–732** — the direct
  successor to the held 2020 local paper (sections at arbitrary distance).
  RECERCAT and URV are bot-blocked; no open arXiv version. Its Theorem B is what
  QAS 2025 Theorem 1 quotes. Requested; remains a frontier gap.
- **The 2026 corrigendum** (SSRN) — not held.
- Lower-bound primaries (Li–Liu–Yang 2009 H(3)≥13; Han–Li 2012 growth;
  Álvarez–Coll–De Maesschalck–Prohens 2020 canard) — re-confirmed paywalled.
- DRR 1994 raw catalogue and any post-2020 consolidated ledger — re-confirmed
  non-existent as a single accessible source.

## Caveat on method (recorded honestly)

One arXiv id was initially guessed (`2401.07218` for the persistent-polycycle
paper) and resolved to an unrelated computer-vision paper; that wrong file was
immediately overwritten with the correct `2504.07225` when the true id was
surfaced by search. The rule — never fetch an arXiv id not seen in a search
result or held source — was bent once and caught by verification. Noted so the
next cycle reads the search result first.

## Storage

Cognee memory server is down this cycle (every `remember_memory` call errored),
so all findings are persisted in the workspace: claim blocks in
`research/summaries/*.md` → `research/notes/claims.md` → `derived/CLAIMS.md` (all
verified live), and this report / LIBRARY-STATUS.md addendum. Nothing needs
re-fetching; store to Cognee once it recovers.
