# Librarian cycle — re-check: library verified complete, gap confirmed unobtainable

## What this cycle did (verified against disk, not recall)

Re-checked the library against the run's requests ledger and found it complete.
The three requests rendered as "open" in `derived/REQUESTS.md` are all answered
by genuine held primary full texts; the ledger showing them open is a
re-derivation/bookkeeping artifact, not a library gap.

1. `balko-valtr-attack-baa4` and `open-access-full-1e6e` — closed by
   `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
   (EuroComb 2015 ENDM 49:425–431, source URL
   https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf). The claim block in
   `research/summaries/balko-valtr-A-SAT-attack-on-ES-ENDM2015.md` carries
   `answers: balko-valtr-attack-baa4` and `answers: open-access-full-1e6e`
   (lines 40–41). The EJC 2017 "full" stub remains a known MIS-DOWNLOAD
   (arXiv:1601.03182 is an unrelated probability paper) — cite the ENDM version,
   never the stub.

2. `full-text-faithful-b96b` — closed by
   `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
   (source URL https://renyi.hu/~p_erdos/1960-09.pdf, the actual ES 1960/61
   paper carrying the lower-bound construction). Claim block in
   `research/summaries/erdos-szekeres-1961-construction-concrete.md` carries
   `answers: full-text-faithful-b96b` (line 56).

## Fresh searches run this cycle (to avoid re-running them)

- Baek–Balko "Erdős–Szekeres Conjecture Revisited" — returns only the held
  SoCG 2025 LIPIcs PDF (DOI 10.4230/LIPIcs.SoCG.2025.13) and metadata pages.
  No full-text PDF with the omitted Theorem 8 proof surfaced.
- JCTA 2026 (DOI 10.1016/j.jcta.2026.106195) — KIAS publications page confirms
  the journal version exists (Baek, JCTA A, 2026), but **no open PDF**.
  Paywalled at ScienceDirect.
- arXiv (constrained) — no preprint of the joint Baek–Balko paper exists; the
  only arXiv Baek item is the unrelated ETV 2022 preprint arXiv:2206.04260.
- Author copy — none on Balko's kam.mff.cuni.cz listing or elsewhere.
- The Balko arXiv PDFs found are the "SAT attack" slides/preprint
  (kam.mff.cuni.cz/~balko/prezentace/...) and the RP² paper — neither carries
  the Baek–Balko Theorem 8 proof.

## The one genuine load-bearing gap — unchanged

**`baek-balko-decomposable` remains asserted-by-source (proof not on disk).**
The held SoCG 2025 PDF (`research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md`)
states Theorem 8 verbatim (lines 343–352) and then says **"The proof of Theorem 8
is omitted"** (lines 352–353). The split lower-bound lemmas (Lemma 9, 12) are
likewise proof-omitted. The definition is on disk (lines 439–443), so the run
can still TEST decomposability of its own es_construct sets with the exact
orientation oracle; it just cannot treat the theorem as proved.

The theorem must be used as **asserted-by-source (author-claimed, proof not held)**
until the JCTA 2026 full text is fetched — not as a proved basis for a structural
step.

## Decision

NOTHING FURTHER to acquire this cycle. Every open request carries a held
answering source; the lone missing proof is unobtainable in open access; no
angle is thin. The next valuable work is the run's own computation (a run-side
task, not librarian acquisition), or a future re-check for an openly-posted JCTA
2026 proof / author copy of Baek–Balko Theorem 8.
