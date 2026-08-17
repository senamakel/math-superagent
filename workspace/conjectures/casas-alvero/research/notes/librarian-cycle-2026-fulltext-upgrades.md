# Librarian cycle 2026 — full-text upgrades for load-bearing abstract-only records

## What was upgraded from abstract-only to full text

Three sources the run's claims cited with specific sections, but whose held files were only arXiv landing pages (the PDF-URL fetch had redirected to the abstract):

1. **Graf von Bothmer, Labs, Schicho, van de Woestijne 2007** — `research/sources/grafvonbothmer2007_infinitely_many_html.full.md` (arXiv HTML v2, 23614 bytes). Now the primary source for: the p^k/2p^k theorem (Section 2, Props 2.1–2.6), Prop 3.1 (char-p witness X^{p+1}−X^p), Remark 3.2 (bad primes bounded; explicit degree-6 bad prime 7390044713023799; "degrees under 30 except 12, 20, 24, 28"), Section 4 (computational aspects; the char-p Gröbner route). Summary: `research/summaries/grafvonbothmer2007_infinitely_many_html.md`.
2. **Massri 2018 (v6 2023)** — `research/sources/massri2018_degree20_html.full.md` (arXiv HTML v6, 54165 bytes). Now the primary source for: Theorem 7.10 (no degree-20 CA with three recycled roots, 3^17-case check), Theorem 7.9 (no degree-20 CA with root multiplicity ≥ 11; no degree-24 with ≥ 15), Remark 7.6 (common root |·| > 19^−5 for degree-20 CA), Prop 7.7 (p-adic bound), Sections 5–6 (finiteness, algebraic coefficients). Summary: `research/summaries/massri2018_degree20_html.md`.
3. **Schaub & Spivakovsky, "A note on the Casas-Alvero Conjecture"** — `research/sources/schaub_spivakovsky_2023_note_html.full.md` (arXiv HTML v7, 16392 bytes). Now the primary source for: the resultant/height formulation (Conjectures 2–3), the Gröbner interpretation (Remark 3), the regular-sequence equivalence (Remark 4), Theorem 5 (R_i ∉ √(others) for i ∈ {d−3,d−2,d−1}), the Rolle/Hasse Proposition 6, the Draisma–de Jong almost-counterexample Theorem 9, and the "Added in press" note acknowledging Ghosh. Summary: `research/summaries/schaub_spivakovsky_2023_note_html.md`.

The old abstract-page files are kept (they carry the original source URL) but the summaries now point to the full-text files.

## What was added new (full texts)

4. **Macintyre 1949**, "On the zeros of successive derivatives of integral functions", Trans. AMS 67 (1949) 241–251 — `research/sources/macintyre1949_zeros-successive-derivatives.full.md` (AMS open PDF, 21232 bytes). The classical Gontcharoff-polynomial / Whittaker-constant paper: re-proves Levinson's inequalities (2.1),(2.4); M_n ≤ (1.3775)^{n+1}; Theorem II (2(4/π)^n bound); Whittaker constant W ≥ .7259 (Levinson's theorem); Schoenberg's theorem extended. This is the analytic backbone of the Abel–Gontcharoff toolchain the run's adopted root-difference-coloring approach uses. Summary: `research/summaries/macintyre1949_zeros-successive-derivatives.md`.
5. **Kostov 2017**, "A property of discriminants", arXiv:1701.02912 (Vietnam J. Math. 47 (2019) 287–296) — `research/sources/kostov2017_property-discriminants_html.full.md` (arXiv HTML, 40410 bytes). Theorem 4: D̃_k = c_k (a_n)^{d(n,k)} M_k² T_k³ with M_k=0 the projection of the two-double-roots (Maxwell) stratum, T_k=0 the triple-root stratum; quasi-homogeneous weight(a_j)=j — exactly the run's weighted scaling. Summary: `research/summaries/kostov2017_property-discriminants.md` (canonical) and `_html.md` (record).

## What is blocked / paywalled (recorded, do not re-fetch)

- **Levinson 1944**, "The Gontcharoff polynomials", Duke Math. J. 11 (1944) 729–733 — paywalled at Project Euclid; three URL attempts failed (404, landing page, bot-detection). Content covered by Macintyre 1949 (which re-proves the inequalities) + Massri §3. See `research/notes/levinson1944-gontcharoff-paywalled.md`.
- Existing documented blocks unchanged: Casas-Alvero 2001 origin paper (ScienceDirect), Díaz-Toca–González-Vega 2006 (Maple proceedings), de Frutos Marín 2013 thesis + 2015 note (uva.es unreachable), Siebeck curves 2012 (MSP 404), Sudbery 1973 (Wiley), Yakubovich 2016 (Taylor & Francis), Gasull 2021 (Springer).

## Cleanup

- **`research/sources/kostov2020_higher-order-discriminants.full.md` is a mislabeled duplicate**: it holds the arXiv abstract landing page of the 2017 paper (1701.02912), NOT the 2020 higher-order-discriminants paper (which is `kostov2020_highorder-discriminants.full.md`, arXiv:1702.08216, held in full). Do not cite the mislabeled file for the 2020 paper. Recorded in both the Kostov 2017 summary and Cognee.

## Claims/leads added

- `okolo-2025-zenodo-crank`, `leggett-2025-zenodo-dyadic` — two further 2025 Zenodo claimed-proof data points, recorded (not evidence, not fetched) in `research/notes/casas-alvero-status.md` alongside the existing claimed-proof family (Battiston, Dobrowolski, Lu, Fernández de las Heras, Yakubovich, Ghosh).
- Frontier additions from the new full texts' citations: Levinson 1944, Macintyre 1947 ("An upper bound for the Whittaker constant"), Schoenberg 1936 (zeros of successive derivatives), Whittaker 1935 (Interpolatory function theory), Gontcharoff 1930.

## Library totals after this cycle

52 files in `research/sources/` (49 distinct sources; the Kostov mislabeled duplicate and two superseded landing-page records are the overlap). All full-text files indexed and searchable. Every claim the run cites in CLAIMS.md now traces to a held full text or a documented-blocked record.

---

## Cycle 2026 (librarian continuation) — frontier-row resolutions + currency sweep

### Four frontier rows resolved via the OpenAlex works API (metadata records, now HELD)

The OpenAlex records resolved four previously-unidentified frontier entries.
Full detail: `research/notes/frontier-lead-resolutions-openalex.md`; claim
`frontier-lead-resolutions-openalex` in `research/notes/casas-alvero-status.md`.

- **W2003962780 = the ORIGIN paper**, Casas-Alvero, "Higher Order Polar Germs",
  J. Algebra 240 (2001) 326–337. OpenAlex marks it bronze-OA with a content
  mirror; **both the OpenAlex mirror (401) and ScienceDirect PDF (403) fail** —
  fresh proof of the documented paywall. Not load-bearing (statement/status
  fully covered by held secondary texts).
- **W1579326781 = duplicate of a HELD source**: it is the original 2013 title
  of Yakubovich arXiv:1308.5320, already held under its v5 title "Polynomial
  problems of the Casas-Alvero type". No new download.
- **W1558046128 = a 2003 Choice book review** of Qing Liu's "Algebraic geometry
  and arithmetic curves" — not a primary treatment; discard as a lead.
- **W2062454016 = Barwise–Eklof 1969 "Lefschetz's principle"** (J. Algebra 13,
  554–570), paywalled, background-only (model-theoretic char-0→ℂ transfer; the
  run's schemes are explicit over ℤ).

The four OpenAlex API responses are held under `research/sources/openalex_W*.full.md`
with their source URLs; the auto-digests were replaced by real summaries. The
citation-graph side effects (book-review citations, Lefschetz citations) are
noise and should be ignored.

### The two documented network-blocked theses: re-attempted, still blocked (3rd cycle)

- **de Frutos Marín 2015 JTN note**: the alternate host discovered this cycle,
  `http://singacom.uva.es/JTN2015/contribuciones/ordinarias/frutos.pdf`, also
  fails at the network layer (socket error, same as uvadoc.uva.es). The
  abstract (with the L(3)..L(7) ineffective-prime lists) remains the only held
  content; corroborated against the run's independently verified lists.
- **Chávez Martínez 2018 thesis**: `http://hdl.handle.net/10902/15246` fails at
  the network layer this cycle too. Abstract only (held): proves CA for 2 and 3
  distinct roots in char 0; degree-20 4/5/6 distinct roots in 302 of 627 cases.

### 2026 currency sweep — nothing new beyond the held set

A fresh `exa_search` restricted to 2026-01-01+ and to 2025-09-01+ returns ONLY:
Ghosh 2501.09272 (held, unverified claim, v2 Mar 2026), Ghosh 2402.18717
(held), Schaub–Spivakovsky 2411.13967 and 2312.08742 and s40687-024-00444-z
(all held), plus **one genuinely new data point**: Ender Uygun, "Arithmetic
Projection of the Casas-Alvero Conjecture — Structural Rigidity in Fermat
Polynomials and the FB Theorem" (OSF/Zenodo 17978524, 2025-12-18) — a claim in
the documented "does-not-help" pattern (Fermat-number structural seal; no peer
review). Recorded as claim `uygun-2025-zenodo-fermat` in
`research/notes/casas-alvero-status.md`. No new settled degree, no new
disproof, no new refereed partial result outside the held set.

### Infrastructure note

The Cognee memory server was unreachable throughout this cycle (health check
timed out at 8s); the OpenAlex downloads and the two `remember_memory` calls
were not filed in durable memory. Everything is recorded workspace-locally
(the notes above), to be stored in Cognee once the memory server recovers.
