# Librarian report — fourth pass (third-pass question: verification-only)

Author: librarian. Scope: verify the reference library is intact, complete, and
indexed for the third pass's single question — whether the minimum weight ratio
at which linear supply becomes *typical* (`mean ν₂/n ≥ 0.40` and `frac ≥ 0.5`)
tends to 0 or plateaus near 1/8 (GOAL.md, CONCLUSION-PASS2 §2, thread
`supply-class-characterisation`). Confirm no genuine library gap remains around
that question; report availability with source URLs. No new download is made.

## The third-pass question, and the theory it needs

The computation is a sweep over random weight-`w` strings of length `n` measuring
`wt(Φ_n h)/n`, where `Φ_n` is the Pascal-mod-2 (Rule-90) fold. The mathematical
content that would explain *why* the ratio behaves as it does is:

- **Weight distribution of a random/sparse vector under a linear map** — MacWilliams
  1963; the weight-enumerator / Krawtchouk / Delsarte machinery (Essential Coding
  Theory, Guruswami notes, Friedlander); O'Donnell for Boolean-function Fourier
  analysis of such maps.
- **The Pascal/Sierpinski structure that makes `Φ_n` amplify sparse inputs** —
  the exact submission that a single 1 at the shared boundary reaches all `n−2`
  depths (thread `sparse-fold-capacity`, settled), and Yoshida's fractal-code
  analysis of Pascal/Sierpinski weight (`d = L^{log(p(p+1)/2)/log p}`), which is
  the only source on disk that computes exact minimal/nonzero weights of Pascal-
  structure images.
- **Threshold / concentration phenomena for random code images** — O'Donnell
  (Chapter on concentration, majority/threshold functions).

All of this is on disk.

## What I verified this pass

1. **Library complete and indexed.** `research/sources/` holds 78 files, of which
   72 are full texts, each carrying its source URL on line 1 via the
   `<!-- source: … -->` marker (verified across all files in a grep sweep —
   the three `DELETED_*` markers record genuinely unobtainable primaries, and
   `matomaki_radziwill_tao_averaged_chowla.full.md` is the in-place "wrong
   download" pointer to the correct MRT file). `research/summaries/` holds 94
   digests carrying claim blocks that feed `CLAIMS.md`. `search_documents`
   reaches the load-bearing subjects (confirmed this pass on the Pascal/weight,
   Rule-90 randomization, and Thue–Morse level-of-distribution queries).

2. **The two newest additions (this run's own, not library re-downloads) are
   indexed and digested:**
   - Müllner & Spiegelhofer, *Normality of the Thue–Morse sequence along
     Piatetski–Shapiro sequences, II* (arXiv:1511.01671) —
     `sources/mullner_spiegelhofer_normality_piatetski_II.full.md`,
     `summaries/mullner_spiegelhofer_normality_piatetski_II.md` — claim
     `mullner-spiegelhofer-normality-subsequence`.
   - Spiegelhofer, *The level of distribution of the Thue–Morse sequence*
     (arXiv:1803.01689) — `sources/spiegelhofer_level_distribution_thuemorse.full.md`,
     `summaries/spiegelhofer_level_distribution_thuemorse.md` — claim
     `spiegelhofer-thuemorse-level-1`.
   Both price the "h is well-distributed on progressions" input family
   **negatively**: Thue–Morse has level of distribution 1 (essentially optimal
   equidistribution) yet sublinear fold weight — so a weaker-than-switch input of
   the "h equidistributes" form is refuted by Thue–Morse as a witness. Consistent
   with the five closed doors; the needed input must live in `Φ`'s submask-XOR
   reading (request `walsh-spectral-subset-b904`).

3. **The third-pass question's territory is covered.** No source states the
   weight-threshold ratio of the fold's supply class — that is this run's own
   computation (tasks `linear-supply-threshold-limit`, then
   `linear-supply-threshold-claim-block`). But every piece of theory that would
   explain the ratio is present. There is no literature gap to fill here; the
   work is the computation, which is not the librarian's.

## Availability — the tiers and their URLs (full text in research/sources/, URL on line 1)

| Tier | Full-text source | Source URL |
|---|---|---|
| The `{0,2}` difference object / direct prior work | odlyzko_iterated_abs_values_diff_primes | https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/S0025-5718-1993-1182247-7.pdf |
| | chase_random_gilbreath | https://arxiv.org/pdf/2005.00530 |
| | encyclopedia_gilbreath | https://encyclopediaofmath.org/wiki/Gilbreath_conjecture |
| The fold / Lucas / 2-regular | mestrovic_lucas_theorem_survey | https://arxiv.org/pdf/1409.3820 |
| | bacher_beeblebrox_reduction | https://arxiv.org/pdf/0708.1430 |
| | hofer_pascal_matrices_mod2 | https://arxiv.org/pdf/2502.01343 |
| | allouche_shallit_kregular_sequences / _II | https://cs.uwaterloo.ca/~shallit/Papers/as0.pdf ; http://plouffe.fr/simon/articles/kreg2.pdf |
| | rampersad_wiebe_2regular_fulltext | https://arxiv.org/html/2309.04012v1 |
| | binary_steinhaus_triangles_rule90 | https://hal.science/hal-02313960v1/file/articleV1.pdf |
| | yoshida_information_storage_fractal_codes | https://arxiv.org/pdf/1111.3275 |
| Weight distributions / coding theory | macwilliams_1963_weight_distribution_fulltext | https://user.eng.umd.edu/~abarg/ECC/macwilliams1963.pdf |
| | essential_coding_theory_…_fulltext | https://users.math.msu.edu/users/iwenmark/Teaching/MTH810/web-coding-book.pdf |
| | guruswami_macwilliams_lp_notes_fulltext | https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/notes/notes5a.pdf |
| | friedlander_macwilliams_krawtchouk | https://arxiv.org/pdf/2401.07319 |
| | odonnell_analysis_boolean_functions | http://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf |
| Switch-density / mod-4 barrier | ash_beltis_gross_sinnott_prime_residues | http://fmwww.bc.edu/gross/ABGS.pdf |
| | lemke_oliver_soundararajan_bias | https://pmc.ncbi.nlm.nih.gov/articles/PMC4978288/ |
| | lemke_oliver_soundararajan_sawtooth | https://ar5iv.labs.arxiv.org/html/1709.06168 |
| | lau_residue_patterns | https://arxiv.org/pdf/2409.12819 |
| | granville_martin_prime_races | https://personal.math.ubc.ca/~gerg/papers/downloads/PNR.pdf |
| | rubinstein_sarnak_chebyshev_bias | https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf |
| K>1 higher-order prime structure | lacasa_dynamical_prime_sequences | https://arxiv.org/pdf/1802.08349 |
| | wu_nonuniform_residues_prime_sequences | https://arxiv.org/pdf/1908.07095 |
| Equal-residue strings (doors 1–3) | shiu_strings_expository | http://simonrs.com/eulercircle/analyticnt/ethan-shiustrings.pdf |
| | maynard_dense_clusters_primes_subsets | https://arxiv.org/pdf/1405.2593 |
| | banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples | https://arxiv.org/pdf/1311.7003 |
| | freiberg_strings_short_intervals | https://arxiv.org/pdf/1005.4703 |
| Rule-90 CA / ergodic randomization | pivato_yassawi_sofic_randomization | https://arxiv.org/pdf/math/0306136 |
| | pivato_yassawi_affine_limit_measures / _II | https://arxiv.org/pdf/math/0108082 ; https://arxiv.org/pdf/math/0108083 |
| | takei_limiting_measures_rule90 | https://doi.org/10.15803/ijnc.7.2_124 |
| Thue–Morse normality / level of distribution | mullner_spiegelhofer_normality_piatetski_II | https://arxiv.org/pdf/1511.01671 |
| | spiegelhofer_level_distribution_thuemorse | https://arxiv.org/pdf/1803.01689 |
| | konieczny_gowers_thuemorse_rudinshapiro | https://arxiv.org/pdf/1905.03283 |
| Analytic-NT (weak prime inputs, value-domain) | matomaki_radziwill_multiplicative_short_intervals | https://arxiv.org/html/1501.04585 |
| | matomaki_radziwill_tao_fourier_uniformity_averaged | https://arxiv.org/pdf/1812.01224 |
| | green_tao_mobius_nilsequences | https://arxiv.org/pdf/0807.1736 |
| | mauduit_rivat_gelfond_somme_chiffres_premiers_primary | http://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p04-p.pdf |
| Uncertainty / nonabelian tools | meshulam_uncertainty_finite_abelian | https://arxiv.org/html/math/0312407 |
| | tao_uncertainty_cyclic_prime | https://arxiv.org/html/math/0308286v6 |

## Could not be obtained (recorded so nobody retries)

- **Shiu 2000 primary PDF** — Wiley paywall, no free copy; the full theorem is
  reproduced by the held expository (`shiou_strings_expository.full.md`), claim
  `shiu-string-theorem`. Do NOT retry the Wiley URL.
- **The `walsh-spectral-subset-b904` bound** — not a download gap; no such theorem
  exists in the literature to fetch. It remains the one open request, and it is a
  theorem to be proven, not a paper to be obtained.

## Bottom line

The reference library meets the phase-1 exit test and is topically complete for
the third pass's question. The single unfinished computation this pass owes —
the weight-threshold ratio `w/n` → 0 vs plateau at 1/8 — is in-house computation
(tasks `linear-supply-threshold-limit` / `linear-supply-threshold-claim-block`,
thread `supply-class-characterisation`), backed by every source that would explain
it. No further download is warranted; any new source demanded by the run must
first name an unworked FRONTIER candidate it has read and why none answers
(directive 7), and the one genuine open gap in REQUESTS.md is a theorem to be
proven, not a paper to be fetched.
