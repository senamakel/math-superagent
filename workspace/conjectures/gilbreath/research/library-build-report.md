# Library build report — librarian verification cycle (2026)

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
