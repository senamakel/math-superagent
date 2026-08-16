# Librarian report — verifies the reference set is complete for the current pass

**Cycle:** this run's librarian pass (third-pass continuation / after pass-3 close).
**Verdict: NO NEW DOWNLOAD.** The reference library meets the phase-1 exit test and is
topically complete for every live line — including the one computation this pass owes.
No stated gap justifies a fetch; the search freeze (directives 7/27/30) governs.

## What the head question needs, and that it is on disk

The pass's single computation (GOAL.md) is whether the minimum weight ratio at which
linear supply becomes *typical* tends to 0 or plateaus near 1/8. Per
`research/CONCLUSION-PASS3.md` that question is **answered** (tends to 0, threshold
weight sublinear). The two still-open tasks are `log-periodic-oscillation-test-d47`
(two-horse exponent test, directive 48) and `write-pass3-conclusion-d47`, both pure
in-house computation. Every piece of theory that would explain the ratio — and the
exact primary source that grounds the open test — is held:

| Need | Held source | URL |
| --- | --- | --- |
| Weight distribution under a linear map (Krawtchouk/MacWilliams/Delsarte) | `macwilliams_1963_weight_distribution_fulltext`, `essential_coding_theory_…_fulltext`, `guruswami_macwilliams_lp_notes_fulltext`, `friedlander_macwilliams_krawtchouk`, `odonnell_analysis_boolean_functions`, `wikipedia_krawtchouk_polynomials` | user.eng.umd.edu/~abarg; users.math.msu.edu; cs.cmu.edu; arxiv 2401.07319; cs.cmu.edu/~odonnell |
| Pascal/Sierpinski fold structure (submask-XOR, Lucas) | `mestrovic_lucas_theorem_survey`, `hofer_pascal_matrices_mod2`, `bacher_beeblebrox_reduction`, `binary_steinhaus_triangles_rule90`, `yoshida_information_storage_fractal_codes`, `rampersad_wiebe_2regular_fulltext` | arxiv 1409.3820, 2502.01343, 0708.1430; hal.science; arxiv 1111.3275, 2309.04012 |
| **Log-periodic Pascal-mod-2 counting (the directive-48 test's prototype)** | `hwang_janson_tsai_periodic_minimum_binomial_modp` (HJT 2024, Thm 2.2: F₂(n)=n^ρ·P(log₂n), ρ=log₂3−1=0.58496) | https://arxiv.org/pdf/2408.06817 |
| Rule-90 / asymptotic randomization | `pivato_yassawi_sofic_randomization`, `pivato_yassawi_affine_limit_measures`/`_II`, `takei_limiting_measures_rule90`, `pivato_lca_entropy_randomization` | arxiv math/0306136, math/0108082/83; doi 10.15803/ijnc.7.2_124 |
| Switch-density / mod-4 barrier (the dead-end reduction) | `ash_beltis_gross_sinnott_prime_residues`, `lemke_oliver_soundararajan_bias`/`_sawtooth`, `lau_residue_patterns`, `granville_martin_prime_races`, `rubinstein_sarnak_chebyshev_bias` | fmwww.bc.edu; pmc.ncbi; arxiv 2409.12819, 1709.06168; personal.math.ubc.ca |
| Equal-residue strings (closed doors 1–3) | `shiu_strings_expository`, `maynard_dense_clusters_primes_subsets`, `banks_freiberg_turnagebutterbaugh_…`, `freiberg_strings_short_intervals` | simonrs.com; arxiv 1405.2593, 1311.7003, 1005.4703 |
| The {0,2} difference object / direct prior work | `odlyzko_iterated_abs_values_diff_primes`, `chase_random_gilbreath`, `encyclopedia_gilbreath` | ams.org; arxiv 2005.00530; encyclopediaofmath |
| Weak prime inputs (value-domain analytic NT) | `matomaki_radziwill_multiplicative_short_intervals`, `matomaki_radziwill_tao_fourier_uniformity_averaged`, `green_tao_mobius_nilsequences`, `mauduit_rivat_gelfond_somme_chiffres_premiers_primary` | arxiv 1501.04585, 1812.01224, 0807.1736; annals.math.princeton.edu |
| Thue–Morse level of distribution / normality (prices "h equidistributes" negatively) | `spiegelhofer_level_distribution_thuemorse`, `mullner_spiegelhofer_normality_piatetski_II`, `konieczny_gowers_thuemorse_rudinshapiro` | arxiv 1803.01689, 1511.01671, 1905.03283 |

## Integrity checks performed this cycle

- **`research/sources/` — 60 full texts carry their `<!-- source: URL -->` marker on
  line 1** (grep sweep; the 6 non-matching rows are the 5 `DELETED_*` provenance
  markers recording unobtainable/wrong primaries and the in-place "WRONG DOWNLOAD"
  pointer). All full texts therefore have recorded provenance.
- **`research/summaries/`** carries the digests feeding `research/CLAIMS.md`; the
  load-bearing subjects are reachable by `search_documents` (confirmed this cycle on
  the Pascal/weight, Rule-90 randomization, and log-periodic queries).
- **The HJT 2024 primary** (the source that grounds the open `log-periodic-oscillation-test-d47`)
  is landed, digested, indexed, and claim-filed (`hjt-p2-log-periodic-representation-proved`).
- **Top FRONTIER rows are all held** (Hoi 2025 bibliography, Granville–Martin, LOS,
  Shiu, Maynard, BFTB, Lau). No ranking target is missing.
- **The one open request** (`walsh-spectral-subset-b904`) was **superseded** at the
  terminus: it is a theorem to be proven (an unconditional submask-window Walsh bound
  on `wt(Φ_n h)`), not a paper to be obtained. Nothing to download for it.

## Could not be obtained (recorded, do not retry)

- **Shiu 2000 primary PDF** — Wiley paywall; the full theorem is reproduced by the held
  expository (`shiu_strings_expository.full.md`, claim `shiu-string-theorem`). Do not
  retry the Wiley URL.
- **Stolarsky 1977** — SIAM paywall; its asymptotics are reproduced in the OEIS A006046
  record and, decisively, in the HJT 2024 theorem.

## Bottom line

The library is complete and mature for the current pass. The two open tasks are
in-house computation (`log-periodic-oscillation-test-d47`, `write-pass3-conclusion-d47`),
not references. No new source is fetched this cycle; the search freeze holds and any
future fetch must first name an unworked FRONTIER candidate read and why none answers
(directive 7).
