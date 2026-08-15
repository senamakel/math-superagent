# Library build report — what is now available locally

This run inherited a near-complete Gilbreath reference library. This cycle
(librarian) verified the canonical tier was genuinely held and indexed, worked
the one live open row in the requests that a primary source could settle, and
closed the frontier's top-cited-but-absent reference.

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
