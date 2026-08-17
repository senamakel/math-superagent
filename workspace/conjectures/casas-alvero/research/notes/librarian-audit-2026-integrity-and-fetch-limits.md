# Librarian audit — 2026: library integrity, coverage, and the two genuine fetch limits

Audit of the full-text library under `research/sources/`, checking (a) which
`.full.md` files are genuine full texts vs failed/abstract-only fetches, and
(b) whether any primary treatment of CA from 2023–2026 is absent.

## Verdict: library is comprehensive and, for every load-bearing item, genuine.

The reference set already covers every phase-1 requirement. This audit
confirmed explicit full texts (not stubs) for the load-bearing primary tier,
and found no missing 2023–2026 primary.

## The arXiv abstract-stub pattern is benign

Several `/pdf/...` fetches returned only the arXiv **abstract page** (≈250
lines) rather than the paper. In every case the real text is held in the
companion `_html.full.md` variant, so nothing is lost:
- `grafvonbothmer2007_infinitely_many` ← `..._html.full.md` (real text, incl.
  the char-p counterexample section)
- `massri2018_degree20` ← `..._html.full.md`
- `castryck2012_degree12` (both variants held)
- `kostov2017_property-discriminants` / `kostov2020_higher-order-discriminants`
  are BOTH the same arXiv:1701.02912 abstract page; the genuine full text is
  `kostov2020_highorder-discriminants.full.md` (arXiv:1702.08216, 1566 lines).
- `schaub_spivakovsky_2023_note` ← `..._html.full.md`

## Genuine full texts confirmed this cycle (spot-checked, not just listed)

- `chellali2012_degree-5p-hal.full.md` — real HAL PDF (642 lines),
  "La conjecture de Casas Alvero pour les degrés 5p^e", p ∉
  {2,3,7,11,131,193,599,3541,8009}.
- `three-proofs-casas-alvero_2013.full.md` — real arXiv:1306.5656 PDF, all
  three (flawed) proofs of the Fernández de las Heras attempt.
- `casas-alvero_2012_roots-and-foci.pdf.full.md` — real EMS PDF
  (L'Enseignement Mathématique 58 (2012) 223–248), Siebeck-curve geometry.
- `casas-alvero_2012_siebeck-curves.full.md` — abstract stub (Math. Scand.
  111, paywalled body) — background only; not load-bearing.
- `castryck2012_badprimes7.txt.full.md` — the author's own degree-7 bad-prime
  file, 366 primes (the authoritative d=7 count).

## Failed/paywalled fetches, documented and NOT load-bearing

These are recorded as "NOT OBTAINED" blocks inside the file, so they read as
what they are (records of a failed attempt), never as sources:
- `diaz-toca-gonzalez-vega-2006.full.md` — verification bound ≤7 is
  double-corroborated by two held primaries (Draisma–de Jong;
  Castryck et al. 2012), so the origin paper is not needed.
- `casas-alvero_2012_... polar-germs 2001` origin paper — paywalled; the
  conjecture's statement/motivation/status fully covered by held sources.
- `sudbery1973_distinct-roots.full.md` — Wiley paywall; ≥5-distinct-roots is
  proved directly in held Laterveer–Ounaïes.
- `levinson1944_gontcharoff-polynomials.full.md` — Project Euclid paywall;
  the Abel–Gontcharoff side is covered by held Yakubovich + Dzhaparidze–Janssen.

## The two genuinely un-fillable items this cycle (network-block, not a miss)

Both hosts are unreachable at the network layer from this environment (the
recorded `uva.es` / `unican.es` / `repositorio` blockage; tool error at the
socket, not 404; 8 download attempts failed this cycle). The abstract is held
for each and the run's claims from them are labelled asserted-by-abstract:

1. **Chávez Martínez 2018** thesis, "La Conjetura de Casas-Alvero para un
   número fijo de raíces" (Univ. de Cantabria). Degree-20 restricted result:
   CA holds for polynomials with 4, 5, 6 distinct roots; 302/627 multiplicity
   partitions confirmed. Third degree-20 restricted-class result.
2. **de Frutos Marín 2015** JTN note, "Un problema sobre números
   combinatorios". Bad/ineficaces-prime lists L(3)..L(7) that corroborate the
   run's independently verified lists. The L(7)=661 figure is a scheme-level
   count (not the strict 366 per Castryck's own file). Already recorded as
   claim `badprimes-lists-corroborated-by-defrutosmarin2015`.

Both are recorded as library gaps (request_research), which correctly refused
on the ground that the library already carries the covering claims — the gaps
are fetch-limited, not unknown.

## Negative finding stored in durable memory

A targeted deep search (2023–2026) found **no independent, referee-backed
commentary** on Soham Ghosh's claimed proof (arXiv:2501.09272). Stored via
Cognee: the conjecture remains an unverified preprint, smallest open degree
20, every refereed 2024-25 source treats it as open, and the run's own
stress-test pins the char-0-only step to eq (4.18) / Prop 4.3 (see claim
`ghosh-char0-break-4-18`).

## No action needed
- FRONTIER leads already held (Schaub–Spivakovsky note/bad-primes/upper-bound,
  Draisma–de Jong, Polstra, Massri, Castryck, de Frutos thesis) — confirmed.
- Citation graph of Castryck 2012 adds only Dobrowolski 2017 (already held,
  withdrawn).
- 2023–2026 sweep surfaces only Ghosh (held) and Schaub–Spivakovsky (held);
  the single name "Gholami 2025" in an abstract is not a distinct source in
  the library and produced no corroborating record.
