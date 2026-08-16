# Librarian audit — this cycle (fresh determination)

**Verdict: NOTHING FURTHER.** No new source this cycle.

This is an independent re-audit, not a rubber-stamp of the prior two
terminus determinations (`librarian_audit_pass3_closed.md`,
`librarian_pass3_terminus_cycle.md`). Both readers already said NOTHING
FURTHER; I re-checked the load-bearing facts from the live on-disk state
rather than from their notes.

## What I checked directly (not from prior notes)

- **FRONTIER.md top rows are held.** Cited-by-3: Hoi 2025 *Annotated
  bibliography for comparative prime number theory* (`hoi_annotated_bibliography_comparative_prime_number_theory.full.md`,
  `..._html.full.md`), Granville–Martin *Prime Number Races*
  (`granville_martin_prime_number_races.full.md`, `granville_martin_prime_races.full.md`).
  Cited-by-2 core: Tao *Higher Order Fourier Analysis*
  (`tao_higher_order_fourier_analysis.full.md`), the Allouche–Shallit
  k-regular / automatic-sequences tier (`allouche_shallit_kregular_sequences`,
  `allouche_shallit_kregular_II`), ABGS (`ash_beltis_gross_sinnott_prime_residues`),
  Lacasa (`lacasa_dynamical_prime_sequences`), LOS (`lemke_oliver_soundararajan_*`,
  `los_sawtooth...`).
- **The coding-theory engine required by recent passes is present and full.**
  MacWilliams 1963, Krawtchouk association schemes (Friedlander),
  Guruswami–Rudra–Sudan LP notes, Essential Coding Theory, the Abbe–Shpilka–Ye
  Reed–Muller survey, Lou–Wang weight spectrum of RM(m−6,m), Carlet–Solé
  weight-spectrum families. No weight-estimation route in `APPROACHES.md` or
  `notes/` lacks its source.
- **The one open request is a theorem gap, not a source gap.**
  `walsh-spectral-subset-b904` asks for a Walsh/subset-sum lower bound on
  `wt(Φ_n x)` for submask-support x not "complicated" in the five refuted
  senses. That is a statement to be proved in-house (F₂ / hypergeometric /
  Krawtchouk structure), not a paper to be downloaded. Nothing to fetch.
- **The pass-3 head is concluded** (`CONCLUSION-PASS3.md`): threshold weight
  is sublinear, `w*(n) = n^0.555 · P(log₂ n)` with P bounded period-1 in
  log₂ n, amplitude ≈ 0.069; `1/2` and `log₂3−1` ruled out; the two open
  lemmas (G-threshold-asymptotic-zero, G-threshold-concentration) are
  self-provable, not missing sources.
- **Directive tail** ends at 48 (all pass-3 exponent/log-periodic work, since
  concluded). The search freeze (directives 7/27/30) governs: a fetch requires
  naming an unworked FRONTIER candidate read and why none answers. I did not
  find such a case; every ranked frontier row is held and every held row is
  digested.

## Why this is not a refill pass

Every live line's theory is on disk. The remaining work is (1) the two open
F₂/hypergeometric lemmas, (2) `E[S(n)²]=O(n)` for the prime gap-parity string
(density-1 SUPPLY via Chebyshev), and (3) the finite-prefix transfer from
Lucas-mixing randomization to the single fixed-string fold. All three are
theorems to be derived/computed in-house; no source answers any of them.

## Record of unattainable primaries (unchanged, for the record)

- Shiu 2000 (Wiley paywall) — fully reproduced by the local expository
  `sources/shiu_strings_expository.full.md`; `DELETED_shiu_primary_unobtainable.md`.
- Three `DELETED_*` markers hold genuinely unobtainable or wrong-arXiv
  primaries; they are correctness markers, not gaps.

Cognee recall remains unavailable this run (404 on recall_memory); the durable
state is carried by `research/ROOT.md`, `research/CLAIMS.md`, and the
per-note claim blocks instead, so a Cognee miss here is not evidence that a
subject is unrecorded.
