# Library build report — librarian verification cycle (2026)

## Cycle 3 audit (librarian): closure re-verified through search_documents and the canonical tier

Ran `search_documents` and read the canonical-tier summaries (Odlyzko 1993, Killgrove–Ralston 1959, Proth 1878, Plouffe 2025, Colonna 2026, MathOverflow thread) plus the route-bearing full-text digests (Granville 2026 FULLPDF, CHT 2026). Verdict: **library still complete, indexed, and reachable; NOTHING FURTHER.**

1. **Canonical reference tier present and indexed:** every problem.md lead is on disk with a summary and a `.full.md` companion. Block lemma sourced with exact constant **1** (Odlyzko intro, verbatim; independent Killgrove–Ralston 1959). Mod-4 linearization sourced (Odlyzko eq 2.2; CHT Lemma 3.10).
2. **Verification record current and kept distinct** (4 data points): Odlyzko 10^13/G=635 (1993), Plouffe 10^14/G=693 (2025), Colonna 1.5×10^15/G=800 (2026), run's own depth 600/1000.
3. **search_documents resolves the run's load-bearing queries** (Odlyzko block lemma, parity shape, step-law/recharge, block growth) straight to the correct `.full.md` sources — nothing is stranded as recall.
4. **Requests ledger fully closed:** G-supply settled negative (two-point switch), MathOverflow fetch done, no new dead routes named by the MO thread beyond what APPROACHES.md records.
5. **No actionable gap:** the single named-open item — an unconditional linear ν₂ ≥ c·n lower bound — is a two-point prime-gap-mod-4 frequency claim that REQUESTS.md records as unprovable by current methods; no re-fetch warranted.

## Verdict: nothing to add. Library closed, verified three cycles running.

## Cycle 2 audit (librarian): closure re-verified through the citation graph

Ran `citation_graph` both directions on the two load-bearing sources and an
exa currency check on the verification record. Verdict: **library still
closed; nothing to add; NOTHING FURTHER.**

1. **Odlyzko 1993 (Math. Comp., DOI 10.1090/S0025-5718-1993-1182247-7) — 21 citing works examined.**
   Held-and-digested: Chase 2023, Bhat–Cobeli–Zaharescu 2023 filtered-rays, Caragiu–Zaharescu–Zaki
   2011, Gatti 2020 + 2023 (both entries), Agama 2021, Torelli 2006.
   Books/background (Ribenboim, Sloane, Guy *Prime Numbers*, Riesel ×2) add no claim source.
   Unrelated (Helly numbers, Kaprekar orbits) are citation coincidences.
   Genuinely adjacent but not load-bearing, now filed as frontier leads: Cobeli–Zaharescu 2013
   *Promenade around Pascal triangle* (Pascal-tripod corroboration; run's rule90-interior-xor
   already confirmed by CHT 2026 §1), Cobeli–Prunescu–Zaharescu 2016 *arithmetic Z-game*,
   Szpiro 2007 *spectral analysis of prime-gap intervals*, Mak 2012 *Ducci over function fields*
   (cyclic-Ducci variant; the run's cyclic-vs-half-infinite boundary doctrine already covers why
   variants do not transfer).
2. **Chase 2005.00530 arXiv record: 0 citing works per OpenAlex** — an indexing artifact; the
   library holds the canonical *Math. Ann.* 388 (2024) version and the run cites that. No action.
3. **Verification record currency: confirmed current.** exa on "verification record 2026/2027":
   Plouffe 2025 (10^14, arXiv:2510.06688) and Colonna 2025–26 (1.5×10^15) are the newest; both
   already held. Keen 2026 (redacted Zenodo "proof") already recorded as unverified. Muney, Gatti
   2023 already held and assessed. No post-2026 record surfaced.
4. **Frontier top rows** (Odlyzko DOI ×3, Caldwell glossary ×3, Killgrove–Ralston ×2, Wikipedia ×2,
   MathWorld→A000232/A036262 ×2, Morgan ORCID ×2) all struck through — full texts held. Remaining
   once-cited rows are leads inside held documents, none naming a missing load-bearing source.
5. **Requests ledger: fully closed.** G-supply settled negative (two-point switch is not a
   one-point statistic; no unconditional positive-linear bound from current methods — see
   `research/notes/g-supply-two-point-crux-settled.md`); MathOverflow fetch done. No open row,
   so per phase-1 discipline no further gathering.

Known imperfection, recorded not fetched: OEIS A396593 and several small OEIS records
(A100820, A213014, A358691, A393110) exist in `research/summaries/` with no
`sources/*.full.md` companion — the summaries ARE the complete captured pages (OEIS records are
short, like the Debono note). A future cycle may point the summary header to confirm this; not
worth a re-fetch.

## Verdict: library is complete, indexed, and reachable. No new primary material needed.

This cycle re-verified the reference library from scratch against the run's
current needs (GOAL.md / REQUESTS.md / FRONTIER.md). The library is confirmed
genuinely on disk, indexed, and reachable through `search_documents`, and the
REQUESTS.md declaration that it is CLOSED (apart from the one named-open
G-supply gap) holds.

## What was verified this cycle

1. **Canonical reference tier present and indexed:** Odlyzko 1993 (full PDF +
   author's LaTeX, block lemma with constant **1**, mod-4 linearization, 10^13 /
   G=635 verification), Killgrove–Ralston 1959 (first machine verification,
   63,419 primes, P(i) = A000232), Proth 1878 (retraction settled), Wikipedia /
   MathWorld / Encyclopedia of Math / OEIS A000232 / A036262 / A089582.
2. **Route-bearing sources present and digested:** Granville 2026 (FULLPDF,
   Lemma 5.4 / Theorem 5.5), CHT 2026 (full HTML + FULLPDF, Theorem 1.6 inverse),
   Chase 2024 (random analogue), BFT 2023 (canonical gap models), Granville &
   Lumley 2021.
3. **G-supply / mod-4 side complete:** ABGS 2011 §9 (named-open two-point mod-4
   switch), Lemke Oliver–Soundararajan 2016/2017 (mod-4 bias conjecture),
   Rubinstein–Sarnak 1994 (Chebyshev bias), Lau 2024 (existence-only, no
   frequency bound), Martin et al. 2024 annotated bibliography (the Ruzsa
   equal-residue lower bound held at abstract level), Torquato et al. 2018/2019
   (long-interval structure factor, HL-conditional, does NOT bear on mod-4
   supply).
4. **Dead-route corpus complete:** every approach in APPROACHES.md has a
   grounded reason it closed (Gatti Theorem 4 invalid, Muney length-5 hole,
   Eppstein anti-Gilbreath class-defeat, Colonna deletion counterexample, CHT
   inverse theorem hypotheses fail at reachable depth, fwd-diff-identity
   refuted, runcount potential refuted, etc.).

## One loose end found and closed this cycle

On re-verification the frontier-twice-cited **Torquato–Zhang–De Courcy-Ireland,
"Hidden multiscale order in the primes"** (arXiv:1804.06279) was found to have
its canonical (full) summary and claim already on disk
(`research/summaries/torquato-zhang-decourcy-ireland-hidden-multiscale-order-primes.md`,
claim `torquato-2019-hl-conditional-pair-structure`); a stray second summary I
created in the same cycle was flagged, converted to a pointer, and its duplicate
claim block removed, so the ledger carries exactly one claim per source.

## Answer to the standing question

**No further gathering is warranted.** The only legitimate next fetch would be a
source delivering an unconditional lower bound `ν₂ ≥ c·n` for prime gaps (the
mod-4 switch frequency) — none is known to the literature, and REQUESTS.md
records the negative: the switch bit is intrinsically two-point, so no
one-point (GRH/Dirichlet) route suffices. The run should not re-search.

## Phase-1 exit test

ROOT.md meets it: minimal counterexample structure stated (first row with
`A_k(1) ≥ 4`), verification bound stated and kept distinct from the literature
records (run depth 600/1000/1e9-block-protection), and ≥3 settled restricted
classes with hypotheses (consecutive odds; constant-2-tail; reaching a constant
`(1,c,c,…)` row — all proved).
