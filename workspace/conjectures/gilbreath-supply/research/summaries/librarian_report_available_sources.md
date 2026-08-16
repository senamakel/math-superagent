# Librarian report — what is now available locally

The SUPPLY reference library is **complete** for the live lines of attack.
It is also **reachable**: every full text is on disk under
`research/sources/` (URL recorded on the first line of each) and search-reachable
via `search_documents`; every digest is under `research/summaries/` with claim
blocks feeding `research/CLAIMS.md`.

## The mathematics covered (grouped by what SUPPLY needs)

**1. The parity barrier (the reason the fold is the only live route).**
- **Ash, Beltis, Gross & Sinnott 2011**, *Frequencies of successive pairs of
  prime residues*, Experimental Math. — `sources/ash_beltis_gross_sinnott_prime_residues.full.md`
  — http://fmwww.bc.edu/gross/ABGS.pdf — states the consecutive-prime pair
  frequency problem is *wide open and cannot be treated using L-functions*
  (verified verbatim, §1).
- **Lau 2024**, *Residue class patterns of consecutive primes* — `sources/lau_residue_patterns.full.md`
  — https://arxiv.org/pdf/2409.12819 — even ONE non-constant pattern is
  "beyond the reach of existing methods" (verified, line 125).
- **Lemke Oliver & Soundararajan 2016**, *Unexpected biases…*, PNAS — `sources/lemke_oliver_soundararajan_bias.full.md`
  — https://pmc.ncbi.nlm.nih.gov/articles/PMC4978288/
- **Granville & Martin**, *Prime Number Races* (two mirrors) — `sources/granville_martin_prime_races.full.md`,
  `sources/granville_martin_prime_number_races.full.md` — https://personal.math.ubc.ca/~gerg/papers/downloads/PNR.pdf
- **Rubinstein & Sarnak**, *Chebyshev's Bias* — `sources/rubinstein_sarnak_chebyshev_bias.full.md`
  — https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf

**2. The equal-residue side (door-3 refutation; the wrong direction SUPPLY needs).**
- **Shiu 2000** via **Ethan Yang's expository** — `sources/shiu_strings_expository.full.md`
  — http://simonrs.com/eulercircle/analyticnt/ethan-shiustrings.pdf — full
  quantitative theorem (arbitrarily long congruent-prime strings, q=4, a=1,3).
- **Maynard 2016**, *Dense clusters of primes in subsets* — `sources/maynard_dense_clusters_primes_subsets.full.md`
  — https://arxiv.org/pdf/1405.2593
- **Banks–Freiberg–Turnage-Butterbaugh 2015** — `sources/banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples.full.md`
  — https://arxiv.org/pdf/1311.7003
- **Freiberg 2010**, *Strings of congruent primes in short intervals* —
  `sources/freiberg_strings_short_intervals.full.md` — https://arxiv.org/pdf/1005.4703

**3. The fold Φ (Pascal-mod-2 / Rule-90 / Lucas-submask).**
- **Meštrović 2014**, *Lucas' theorem survey* — `sources/mestrovic_lucas_theorem_survey_html.full.md`
  — https://arxiv.org/html/1409.3820v1 — C(d,i) odd ⟺ i submask of d.
- **Hofer 2025**, *Matrices over ℤ with binomial/Catalan entries mod 2* —
  `sources/hofer_pascal_matrices_mod2.full.md` — https://arxiv.org/pdf/2502.01343 —
  Thue-Morse sign structure of the mod-2 Pascal matrix.
- **Bacher 2008** — `sources/bacher_beeblebrox_reduction.full.md` —
  https://arxiv.org/pdf/0708.1430 — determinants of mod-2 Pascal/recurrence matrices.
- **Allouche & Shallit**, *The ring of k-regular sequences* I & II — `sources/allouche_shallit_kregular_sequences.full.md`,
  `sources/allouche_shallit_kregular_II.full.md`.
- **Rampersad & Wiebe 2023** — `sources/rampersad_wiebe_2regular_fulltext.full.md`
  — https://arxiv.org/html/2309.04012v1 (and `_binomial` mirror).
- **Binary Steinhaus triangles / Rule 90** — `sources/binary_steinhaus_triangles_rule90.full.md`
  — https://hal.science/hal-02313960v1/file/articleV1.pdf

**4. The Walsh/Krawtchouk/MacWilliams/Delsarte transform tier**
  (backs the `fold-second-moment-krawtchouk` route): MacWilliams 1963,
  Krawtchouk polynomials, Guruswami LP notes, Ashikhmin–Barg–Litsyn, Friedlander
  2024, the Guruswami–Rudra–Sudan textbook, Meshulam & Tao uncertainty.

**5. The ergodic / Lucas-mixing tier** (backs the `lucas-mixing-finite-transfer`
  route): Pivato–Yassawi *sofic randomization* Thm 7.1, *affine limit measures* I
  & II, Pivato *LCA entropy randomization*, Takei *limiting measures* (Rule 90),
  Bertrand et al. rule-90.

**6. Direct prior work on the exact object, and the canonical encyclopedic tier.**
- **Odlyzko 1993**, *Iterated absolute values of differences of consecutive
  primes*, Math. Comp. — `sources/odlyzko_iterated_abs_values_diff_primes.full.md`
  — https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/ —
  the absolute-difference triangle of primes itself; {0,2} structure; Gilbreath
  verified to 10^13 (Gilbreath itself is **out of scope** — do not claim).
- **Chase 2022**, *A random analogue of Gilbreath's conjecture* — `sources/chase_random_gilbreath.full.md`.
- **Encyclopedia of Math**, *Gilbreath conjecture* — `sources/encyclopedia_gilbreath.full.md`.

## What is NOT in the library, and why

- **`walsh-spectral-subset-b904`** (the one open request): a Walsh/subset-sum
  lower bound on `wt(Φ_n x)` for inputs not "complicated" in the five refuted
  senses. This is a *theorem* the run must find, not a source — no published
  result states it. It is the load-bearing gap.
- **The Gilbreath conjecture itself and its solution** — explicitly out of scope
  (GOAL.md), and no solution exists (open problem). Not to be claimed.
- **A published answer to any contest problem** — correctly absent; none applies
  to this open research problem.

## Where everything is

- Full texts: `research/sources/<descriptive>.full.md`
- Digests/claim-bearing notes: `research/summaries/<name>.md`
- The derived claim ledger: `research/CLAIMS.md` (read-only, re-derived)
- The phase-1 completion record: `research/ROOT.md`
- See also `research/summaries/librarian_reachability_verification.md` for the
  indexing fix and the search-ranking caveat.
