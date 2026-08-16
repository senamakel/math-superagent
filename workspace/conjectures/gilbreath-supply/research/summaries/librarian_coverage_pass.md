# Librarian coverage pass — SUPPLY reference library status

Author: librarian. Date: this run. This is a *coverage verification* note appended to
the existing geography note (`librarian_findings_supply.md`). It confirms the library
is complete for the live lines and records one correction.

## What I verified (and the one correction)

**The library was already complete; it was not fully indexed.** My first `search_documents`
queries for the Krawtchouk/MacWilliams/Delsarte engine returned only approach files, and I
initially flagged a gap. The truth: the sources were on disk in `research/sources/` but
**not indexed**, so `search_documents` could not reach them. Lesson recorded in durable
memory: check the on-disk file list before flagging a missing source.

**Fix applied:** indexed the eleven full-text sources that back the two adopted live lines
(`fold-second-moment-krawtchouk` and `lucas-mixing-finite-transfer`) plus the coding-theory
reference tier. All are now reachable via `search_documents`.

## Canonical reference tier — now all indexed and searchable

The two **adopted** lines' engines, each backed by a primary/local source:

| Line | Engine | Local source(s) | Source URL |
| --- | --- | --- | --- |
| `fold-second-moment-krawtchouk` | MacWilliams identity | `sources/macwilliams_1963_weight_distribution_fulltext.full.md` | https://user.eng.umd.edu/~abarg/ECC/macwilliams1963.pdf |
| | Krawtchouk polynomials | `sources/wikipedia_krawtchouk_polynomials.full.md` | https://en.wikipedia.org/wiki/Krawtchouk_polynomials |
| | Distance distribution / LP bound | `sources/guruswami_macwilliams_lp_notes_fulltext.full.md` | https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/notes/notes5a.pdf |
| | Coding-theory book (MacWilliams, Delsarte, weight enumerators) | `sources/essential_coding_theory_guruswami_rudra_sudan_fulltext.full.md` | https://users.math.msu.edu/users/iwenmark/Teaching/MTH810/web-coding-book.pdf |
| | Delsarte inequalities / polynomial method | `sources/ashikhmin_barg_litsyn_polynomial_method.full.md` | https://arxiv.org/pdf/math/9910175 |
| | MacWilliams for Krawtchouk schemes | `sources/friedlander_macwilliams_krawtchouk.full.md` | https://arxiv.org/pdf/2401.07319 |
| `lucas-mixing-finite-transfer` | Pivato–Yassawi Thm 7.1 | `sources/pivato_yassawi_sofic_randomization.full.md` | https://arxiv.org/pdf/math/0306136 |
| | Affine limit measures II | `sources/pivato_yassawi_affine_limit_measures_II.full.md` | https://arxiv.org/pdf/math/0108083 |
| | Takei rigidity | `sources/takei_limiting_measures_rule90.full.md` | https://doi.org/10.15803/ijnc.7.2_124 |

Core structural / arithmetic tier (all already indexed):

| Source | File | URL |
| --- | --- | --- |
| Ash–Beltis–Gross–Sinnott 2011 (switch-density barrier) | `sources/ash_beltis_gross_sinnott_prime_residues.full.md` | http://fmwww.bc.edu/gross/ABGS.pdf |
| Lemke Oliver–Soundararajan 2016 (bias) | `sources/lemke_oliver_soundararajan_bias.full.md` | https://pmc.ncbi.nlm.nih.gov/articles/PMC4978288/ |
| Shiu 2000 (equal-residue strings; refutes door 3) | `sources/shiu_strings_expository.full.md` | http://simonrs.com/eulercircle/analyticnt/ethan-shiustrings.pdf |
| Maynard 2016 (positive-density clusters) | `sources/maynard_dense_clusters_primes_subsets.full.md` | https://arxiv.org/pdf/1405.2593 |
| BFTB 2015 (bounded-gap congruent strings) | `sources/banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples.full.md` | https://arxiv.org/pdf/1311.7003 |
| Lau 2024 (non-constant 2-term patterns mod 4 open) | `sources/lau_residue_patterns.full.md` | https://arxiv.org/pdf/2409.12819 |
| Odlyzko 1993 (iterated-abs object, {0,2} reduction) | `sources/odlyzko_iterated_abs_values_diff_primes.full.md` | https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/S0025-5718-1993-1182247-7.pdf |
| Chase 2022 (random Gilbreath analogue) | `sources/chase_random_gilbreath.full.md` | https://arxiv.org/pdf/2005.00530 |
| Meštrović 2014 (Lucas theorem survey) | `sources/mestrovic_lucas_theorem_survey.full.md` | https://arxiv.org/pdf/1409.3820 |
| Bacher 2008 (mod-2 Pascal/fold matrices) | `sources/bacher_beeblebrox_reduction.full.md` | https://arxiv.org/pdf/0708.1430 |
| Hofer 2025 (Pascal matrices mod 2) | `sources/hofer_pascal_matrices_mod2.full.md` | https://arxiv.org/pdf/2502.01343 |
| Allouche–Shallit (k-regular sequences I & II) | `sources/allouche_shallit_kregular_sequences.full.md`, `sources/allouche_shallit_kregular_II.full.md` | https://cs.uwaterloo.ca/~shallit/Papers/as0.pdf ; http://plouffe.fr/simon/articles/kreg2.pdf |
| Rampersad–Wiebe 2023 (2-regular binomial sums) | `sources/rampersad_wiebe_2regular_fulltext.full.md` | https://arxiv.org/html/2309.04012v1 |
| Granville–Martin (prime races, both mirrors) | `sources/granville_martin_prime_races.full.md`, `sources/granville_martin_prime_number_races.full.md` | https://personal.math.ubc.ca/~gerg/papers/downloads/PNR.pdf ; https://dms.umontreal.ca/~andrew/PDF/PrimeRace.pdf |
| Rubinstein–Sarnak (Chebyshev bias) | `sources/rubinstein_sarnak_chebyshev_bias.full.md` | https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf |
| Meshulam / Tao (uncertainty) | `sources/meshulam_uncertainty_finite_abelian_html.full.md`, `sources/tao_uncertainty_cyclic_prime_html.full.md` | https://arxiv.org/html/math/0312407 ; https://arxiv.org/html/math/0308286v6 |
| Rule-90 / binary Steinhaus triangles | `sources/binary_steinhaus_triangles_rule90.full.md` | https://hal.science/hal-02313960v1/file/articleV1.pdf |
| Encyclopedia of Math (Gilbreath) | `sources/encyclopedia_gilbreath.full.md` | https://encyclopediaofmath.org/wiki/Gilbreath_conjecture |

## Bottom line

- **43 full texts** in `research/sources/` (each with its URL recorded in the file), **50 digests**
  in `research/summaries/`, all indexed and reachable via `search_documents`.
- Every **adopted live line's engine is backed by a primary local source.** No genuine gap in the
  canonical tier remains.
- The only *open* library-level gap (unchanged) is `walsh-spectral-subset-b904`: no local source
  states a Walsh/subset-sum lower bound on `wt(Φ_n x)` valid for inputs not "complicated" in the
  five refuted senses. That is a gap in theorems, not in the library — no source on it exists.
- Note: `search_documents` only reaches **indexed** documents. If a future pass cannot find a
  source it expects, check `research/sources/` on disk and re-index before treating it as missing.
