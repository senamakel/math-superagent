# Librarian — Cycle Report: frontier worked, full-proof claim evaluated from its primary text

## What this cycle accomplished

The library was already mature (ROOT.md met the phase-1 exit test; 44 sources on disk). This cycle worked the stated gaps and the frontier, adding **6 new sources** and delivering one **primary-text verdict**:

| Source | What it adds |
|--------|-------------|
| **Pak 2008** (arXiv:0804.0657) | Every simple polygon inscribes a square; generic polygons have an **odd** number of squares; two direct elementary proofs. The finite exact oracle/Lean anchor for polygon verification. |
| **Asano–Ike–Kuo–Li 2025** (arXiv:2510.01746) | C⁰-rigidity of Legendrians/coisotropics via sheaf quantization. **Does not settle** the Legendrian-lift frontier (thesis `legendrian-lift-frontier` remains standing); the theorems require smooth limit images + bounded conformal factors. |
| **Wright 2026** (Aequationes Math.) | Rhombi with diagonals collinear with specified points; uncountably many rhombi (new proof of Fung); regional diagonal-collinearity. Frames the rhombus→square gap (equality of diagonals) with prescribed diagonal lines. |
| **CDM 2021** (arXiv:2103.13848) | Square-like quadrilaterals in embedded space curves; FTCWC class; explicit side-length bound π−d(γ) > 0 — a **curvature-based** anti-shrinkout scale certificate (the fourth named device). Source statement: "nobody has managed to construct such an argument in the past century." |
| **Ueoka 2025 landing** (Zenodo 17847990) | The only full-proof claim for the Toeplitz conjecture: five overlapping self-published preprints, 0 citations, no review. |
| **Ueoka 2025 v5 PDF** (full text!) | **The headline result.** Downloaded the actual 62.5 kB proof and read it. |

## The headline: Ueoka's v5 proof is closed as incorrect-in-the-steps-that-matter

The only full-proof claim in existence for the Toeplitz conjecture has now been **read in full and evaluated from its primary text**, not guessed at:

- **Lemma 3.1 is false as stated.** At the all-coincident boundary point (t,t,t,t), every ℓᵢⱼ = 0, so **F ≡ 0 identically for every curve**. The proof smuggles in "non-zero" without justification.
- **Lemma 3.2's uniform positive boundary margin cannot hold** — min over ∂T⁴ of ‖F₀‖ = 0. Its positivity is *the* claim that Stromquist's local monotonicity and Asano–Ike's Legendrian-lift hypothesis exist to guarantee.
- **Lemma 4.1 (zeroes stay away from the boundary) is a non sequitur** — uniform convergence does not control zero locations; this is exactly the shrinkout phenomenon (Tao; GL 2024 sharpness).
- **Reference [3] mis-cites Stromquist 1989** (wrong journal: "Amer. Math. Monthly 96(6):521–523" vs the correct Mathematika 36(2):187–197).
- It is **not** a counterexample either (no curve constructed). **The conjecture remains open** — now with a documented, sentence-level reason why the only claimed full proof fails, exactly at the boundary-margin and anti-shrinkout steps the library's structural thesis predicted.

This is precisely the "hold the claim with its exact falsifier" role: the run can now name where full-proof claims die, instead of guessing.

## Acquisition gaps closed and remaining

Closed this cycle: Pak 2008, AIKL 2025, Wright 2026, CDM 2021, Ueoka landing + v5 PDF. The Fung-rhombi and Rius-thesis acquisition errors were already fixed before this cycle (both full texts verified on disk; the memory entries claiming otherwise are stale).

Still genuinely missing (all paywalled/blocked, each documented):
- **Stromquist 1989 primary** (Mathematika) — triangulated via Cambridge abstract + Rius thesis + Matschke 2009 + Barber 2026 Def 1.9; the verbatim Condition A wording is the one gap.
- **Wright 2025 Monthly primary** — T&F returns HTTP 403 to download_document.
- **Jerrard 1961 primary** (Trans. AMS) — AMS rate-limited/oversized transfer; classic is well-characterized via Matschke survey + search summaries.
- **Emch 1916 primary** (Amer. J. Math.) — paywalled; content carried by Matschke survey + Rius thesis + Aslam/Fung intros.

The request_research tool refused these as "claims already bearing on the gap" — the tool's claims-based filter is a false negative (the *claims* exist; the *primary texts* do not), and the gaps are recorded in CONTEXT.md's Gaps section regardless.

## Frontier state

Worked the top of the frontier: CDM 2022 (in library), Akopyan–Avvakumov 2018 (in library), Aslam 2020 (in library), Schwartz 2020 trichotomy (in library), the Emch classics (paywalled), Jerrard 1961 (paywalled), "Four Lines and a Rectangle" (Schwartz's rectangle methods — covered by the in-library trichotomy + Greene–Lobb 2021). The four-line-rectangle geometry (Olberding–Walker conic treatment) is a frontier lead not yet downloaded — it bears on the four-lines engine behind Pak's polygon proof and Schwartz's rectangle work, and is free (Proc. AMS 15374).

## Infrastructure note

**The memory server (Cognee) was down for the entire cycle** — 5 `remember_memory` calls and all download filings failed with "the memory server cannot index right now." All findings are safely stored in `research/summaries/` (with claim blocks feeding the CLAIMS ledger) and `research/sources/`; the durable-memory store should be re-synced once the server recovers. The CLAIMS ledger picked up all new claims (verified via search_claims): pak2008 ×3, wright2026 ×3, aikl2025 ×3, cdm2021 ×4, ueoka2025 ×4 (including the new v5 verdict and the mis-citation).

## Next cycle's thin angles (if gathering resumes)

1. Olberding–Walker four-lines-rectangle conic geometry (free, directly on the four-lines engine).
2. Schwartz 2018 "Rectangle Coincidences and Sweepouts" (arXiv:1809.03070, free) — the rectangle-coincidence counting framework.
3. Re-sync Cognee with this cycle's findings once the server recovers.
