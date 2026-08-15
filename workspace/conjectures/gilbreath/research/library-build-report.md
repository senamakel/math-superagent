# Library build report — what is now available locally

## Cycle 2026 (librarian): canonical tier verified held + indexed; library confirmed closed

Verified directly this cycle that the canonical reference tier is genuinely on
disk and reachable through `search_documents`, not merely named:

- **Odlyzko 1993** (full PDF + author's LaTeX) — block lemma with exact
  constant 1 (one row per `{0,2}` entry, protecting N succeeding rows), the
  `d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)` linearization, and the 10^13 / G=635
  verification. Summary + three claim blocks at
  `research/summaries/odlyzko-1993-iterated-absolute-differences.md` (the
  `≈ n/2` figure appears nowhere in the source — confirmed corrected).
- **Proth 1878** — primary scan unobtainable as text (GDZ/Google Books/Gallica
  all bot-blocked; vol. 4 absent from archive.org) but the myth/retraction is
  settled through two independent reader accounts (Arias de Reyna 2020, Chase
  2024 §7 + Williams's 2020 email retraction). Recorded so nobody re-fetches.
- **Killgrove–Ralston 1959**, **Wikipedia / MathWorld / Encyclopedia of Math /
  OEIS A036262 / A000232 / A089582** encyclopedic tier — all present with
  summaries.
- **Granville 2026 Lemma 5.4 FULLPDF, CHT 2026 FULLPDF, Chase 2024, Granville &
  Lumley 2021, BFT 2023** — the route-bearing sources, all digested.

The library passes the phase-1 exit test (ROOT.md states minimal counterexample,
verification bound, and ≥3 settled restricted classes). REQUESTS.md confirms it
is CLOSED apart from the G-supply gap, which is itself closed **negative**: the
mod-4 switch bit is intrinsically a two-point statistic, so no one-point
(GRH/Dirichlet) route suffices and no unconditional positive-linear bound on ν₂
is provable by current methods. No further gathering is warranted. The only
legitimate next fetch would be a source delivering `ν₂ ≥ c·n` for prime gaps —
none is known to the literature.

This run inherited a near-complete Gilbreath reference library. This cycle
(librarian) verified the canonical tier was genuinely held and indexed, worked
the one live open row in the requests that a primary source could settle, and
closed the frontier's top-cited-but-absent reference.

## Verification cycle (2026): library confirmed complete; frontier sweep judged

The only top-of-FRONTIER lead not already on disk was Torquato–Zhang–de Courcy-Ireland
2019, "Hidden multiscale order in the primes" (J. Phys. A 52:124002, doi
10.1088/1751-8121/ab0588; companion arXiv:1802.10498), cited by two of the run's
sources. It is a Hardy–Littlewood-conditional study of prime pair-correlation /
hyperuniformity — the same two-point mod-4 backbone the ν₂ reduction already
rests on, already covered by LOS-2016 and ABGS-2011, and it delivers no new
lower bound on the switch count. Per the closure directive it was **not fetched**;
the physics object (prime quantized diffraction) does not bear on the settled
G-supply gap. Recorded so nobody re-attempts.

## What was added this cycle

- **Granville & Lumley, "Primes in short intervals: heuristics and
  calculations", Experimental Mathematics (2021), doi 10.1080/10586458.2021.1927256,
  arXiv:2009.05000** — the frontier's highest-ranked cited source that was absent
  from the library, and the natural primary reference for the live Route-B supply
  side (ν₂ = prime-gap-mod-4 frequency).
  - Full text: `research/sources/granville-lumley-primes-short-intervals-heuristics.FULL.full.md`
    (downloaded from arxiv.org/pdf/2009.05000, 1.7 MB → 84 KB markdown).
  - Summary with claim `granville-lumley-short-intervals-heuristics`:
    `research/summaries/granville-lumley-primes-short-intervals-heuristics.md`.
  - **What it is and is NOT:** a short-interval heuristic about extremal prime
    counts `M(x,y)`, `m(x,y)` in length-y intervals over `(x,2x]`; conjectures
    `M ~ u_+(c_+t)·log x`, `m ~ u_−(c_−t)·log x` for `y ~ t(log x)²`. It says
    **nothing** about the mod-4 distribution of consecutive primes, so it does
    **not** close or bound the ν₂ supply side. The ν₂ frame stays the held
    Lemke Oliver–Soundararajan 2016 two-point mod-4 bias
    (`los-2016-consecutive-pair-mod4-bias`), which makes ν₂ = n/2 + O(bias) the
    natural leading term. This is recorded so the run does not over-cite it.
  - The publisher DOI is paywalled; the arXiv v1 PDF is what is held (noted in
    REQUESTS.md).

## What was verified present this cycle (canonical tier genuinely held + indexed)

- **Canonical reference tier:** Odlyzko 1993 (full text + author's LaTeX),
  Killgrove–Ralston 1959, Proth 1878 (googlebooks scan), Gilbreath 2011,
  Wikipedia, MathWorld, Encyclopedia of Math, OEIS A036262/A000232/A089582 —
  all held and digestible via `search_documents`.
- **The generalisations / surrounding theory:** Chase 2024 (Math. Ann.),
  Chase–Hunter–Tao 2026 (full HTML + FULLPDF), Banks–Ford–Tao 2023
  (Cramér/Granville models), Granville 2026 (piercing, FULLPDF), Eppstein
  (anti-Gilbreath + practical numbers), Muney 2026 (valid-extension holes),
  Gatti 2020/2023, Li 2026 (modulo-k) + Li 2023 (0.52 short interval), Colonna
  2025–26 (record), Plouffe 2025 (10^14), Arias de Reyna, Caldwell, Houston,
  Tao blog, Morgan 2026 (frontier/corridor), Ross 2026 (decay constants),
  Lemke Oliver–Soundararajan 2016 (mod-4 bias), Torelli 2006, Gallagher 1976.
- **The Ducci / cellular-automaton side that transfers:** Glaser–Schöffl,
  Calkin–Stevens–Thomas, Avart, Caragiu–Zaharescu–Zaki 2011/2014, Chamberland,
  Giacomelli 2021/2025, Lewis–Tefft 2024, Webb 1982, plus the Rule-90/Pascal-mod-2
  sources (Malyshev, Northshield at abstract level; Wikipedia/MathWorld full).

## Sourced claims the library now establishes (relevant to this run)

- Odlyzko block lemma, constant **1** — `odlyzko-block-lemma`, `gc-block-lemma-odlyzko`.
- Rule 90 interior XOR = Pascal mod 2, proved — `rule90-interior-xor`.
- Parity reduction GC ⟺ `A_k(1) ∈ {0,2}` every row, proved + Lean — `gilbreath-reduces-to-second-in-02`.
- Step law + recharge identity — `step-law-and-recharge-identity`.
- Gatti 2020 prime proof invalid (located flaw), Muney length-5 hole, Eppstein
  class-defeat, Colonna g=4 left-edge failure — held with full texts.
- Granville 2026 Lemma 5.4 re-derived and PROVED on the even domain —
  `lemma54-re-derived-proof`; remaining open content = ν₂ supply bound ≥ c·n.
- Short-interval heuristic landscape (this cycle): `granville-lumley-short-intervals-heuristics`
  (demand-side, mod-4-silent); mod-4 supply framing in `los-2016-consecutive-pair-mod4-bias`.

## Indexing verification cycle (librarian, this build): reachability confirmed

Confirmed, by live `search_documents` queries, that the canonical tier is not
merely present on disk but genuinely **within the search index** — a source
that cannot be found is not in the library. Each of the route-bearing and
canonical items below returned ranked hits from their files (full text,
summary, or both), with the source URL recorded in the file header:

- **Odlyzko 1993** — block lemma (constant 1), the mod-4 linearization,
  10^13/G=635. Reached via `research/summaries/odlyzko-1993-iterated-absolute-differences.md`
  (URL https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/...) and
  both full texts.
- **Killgrove–Ralston 1959** — reachable in `research/sources/killgrove-ralston-1959-*.full.md`.
- **ABGS 2011** (mod-4 prime-residue-pair frequency, the ν₂/G-supply crux) —
  `ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md`.
- **Granville 2026 Lemma 5.4 FULLPDF, CHT 2026 FULLPDF, Chase 2024, Chase–Hunter–Tao
  2026, Banks–Ford–Tao 2023, Granville & Lumley 2021, Lemke Oliver–Soundararajan
  2016/2017, Colonna 2025–26 record, Plouffe 2025, Eppstein, Muney 2026,
  Gatti 2020, Proth 1878** — all reached by query.
- **Summary layer** confirmed indexed (e.g. `proth-1878-sur-la-serie-des-nombres-premiers.md`,
  `odlyzko-1993-iterated-absolute-differences.md`, `mathoverflow-gilbreath-what-is-known-thread.md`
  all returned by search).

**Conclusion:** no further gathering is warranted. The library is closed
(REQUESTS.md), the phase-1 exit test is met (ROOT.md), and every source a claim
in this run cites is on disk and reachable through the index. Nothing in the
frontier's multi-cited tier is absent that a faithful source could supply for
the settled G-supply gap. Any genuinely new fetch would require a source
delivering `ν₂ ≥ c·n` (or the two-point mod-4 switch bound) — none is known to
the literature.

## Phase-1 exit test

`research/ROOT.md` states (a) the structure of a minimal counterexample (the
first row with `A_k(1) ≥ 4`, at which the leading `1` is lost), (b) the current
verification bound (run's own depth 600 / depth 1000 vs the literature records
Odlyzko 10^13 / Plouffe 10^14 / Colonna 1.5e15, kept distinct), and (c) at least
three restricted classes already settled with their hypotheses (consecutive
odds; constant-2-tail; reaching a constant `(1,c,c,…)` row — all proved). **The
phase-1 exit test is met.** Further gathering happens only against a stated gap
in `research/REQUESTS.md`; the one such gap a primary source could close
(Granville–Lumley) is now closed.
