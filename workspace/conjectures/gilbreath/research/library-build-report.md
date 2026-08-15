# Library build report — what is now available locally

This run inherited a near-complete Gilbreath reference library. This cycle
verified the canonical tier was genuinely held and closed the one real gap the
run's own memory had flagged as open.

## What was added this cycle

Two primary sources on the Rule-90 / Pascal-mod-2 machinery — the algebraic
structure this run *proved* for the halved `{0,2}` block interior
(`rule90-interior-xor`) and the quantity the live `rule90-regeneration` thread
needs (the density of edge-2 reads during erosion):

- **Malyshev, "Boolean analogues of the Pascal triangle with maximal possible
  number of ones", Discrete Math. Appl. 31(5) (2021), doi 10.1515/dma-2021-0029.**
  Sharp bound: a GF(2) Pascal triangle `T_s` has at most `⌈s(s+1)/3⌉` ones,
  equality exactly for Fibonacci-mod-2 top rows → an upper bound on edge-2
  density in the halved interior. Sourced from the published abstract; the full
  PDF is a scanned image with no text layer (unobtainable, recorded).
- **Northshield, "Sums across Pascal's triangle modulo 2", Congressus
  Numerantium 200 (2010), hdl 20.500.12648/1110.** The
  `A(x) = P(x)·A(x²)` generating-function technique for mod-2 binomial line
  sums; the (1,1)-case is Gould's sequence, the exact algebraic form of the
  Rule-90 edge convolution. Sourced from the item record + abstract; the
  repository PDF bitstream blocked by the converter and the journal sibling is
  paywalled (unobtainable, recorded).

Both registered as sourced claims (`malyshev-max-ones-boolean-pascal-bound`,
`northshield-pascal-mod2-line-sums-gf`), logged in the CLAIMS ledger, indexed
for `search_documents`, and stored in durable Cognee memory. Full-text absence
recorded in REQUESTS.md's unobtainable section so nobody re-attempts.

## What was verified present this cycle

- **Canonical reference tier:** Odlyzko 1993 (full text + author's LaTeX),
  Killgrove–Ralston 1959, Proth 1878 (googlebooks scan), Gilbreath 2011,
  Wikipedia, MathWorld, Encyclopedia of Math, OEIS A036262/A000232/A089582 —
  all held and digested.
- **The generalisations / surrounding theory:** Chase 2024 (Math. Ann.),
  Chase–Hunter–Tao 2026 (both full HTML and FULLPDF), Banks–Ford–Tao 2023
  (Cramér/Granville models), Eppstein (anti-Gilbreath + practical numbers),
  Muney 2026 (valid-extension holes), Gatti 2020/2023, Li 2026 (modulo-k),
  Colonna 2025–26 (record), Plouffe 2025 (10^14), Arias de Reyna, Caldwell,
  Houston, Tao blog.
- **The Ducci / cellular-automaton side that transfers:** Glaser–Schöffl,
  Calkin–Stevens–Thomas, Avart, Caragiu–Zaharescu–Zaki 2011/2014, Chamberland,
  Giacomelli 2021/2025, Lewis–Tefft 2024, Webb 1982, Wikipedia Rule 90,
  MathWorld Rule 90 — all held.
- **The run's own recent additions** (already in place, confirmed): Blair
  Morgan 2026 (frontier/corridor), Granville 2026 (piercing, FULLPDF), Ross
  2026 (decay constants + parity note), Torelli 2006, the OEIS family.

## Sourced claims the library now establishes (relevant to this run)

- Odlyzko block lemma, constant **1** (one row per `{0,2}` entry), sourced and
  re-derived by the run — `odlyzko-block-lemma`, `gc-block-lemma-odlyzko`.
- Rule 90 interior XOR = Pascal mod 2, proved — `rule90-interior-xor`.
- Parity reduction: GC ⟺ `A_k(1) ∈ {0,2}` every row, proved + Lean formalised —
  `gilbreath-reduces-to-second-in-02`, `gilbreath-second-entry-equivalence`.
- Step law + recharge identity `b_k = b_1 + Σ(j_i+1) − (k−1)`, proved —
  `step-law-and-recharge-identity`.
- Gatti 2020 prime proof invalid (located flaw), Muney length-5 hole, Eppstein
  class-defeat, Colonna g=4 left-edge failure — all held with full texts.

## The honest gap (unchanged by this cycle's additions)

The `(2,4)`-event regeneration rate is still open. The two added sources
(Malyshev, Northshield) characterise the *interior* `{0,2}` structure only;
neither proves anything about the boundary intruder or the rate at which edge-2
reads arrive while the intruder is 4. So they are leads on the interior-frequency
half, not a regeneration proof — exactly as flagged in the claims' bearing
fields.
