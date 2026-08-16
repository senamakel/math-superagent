# Librarian findings — what the library establishes about SUPPLY

Author: librarian. This is a geography note: what primary material is now
available locally, and what single fact it establishes that bears on the goal.

## The one fact that governs the whole attack

The library fixes, with primary sources, why SUPPLY must be attacked through the
fold `Φ` and not through raw mod-4 switch frequency:

- **ABGS 2011 §9** (`ash_beltis_gross_sinnott_prime_residues`): the
  consecutive-prime-pair frequency question — whether all ordered residue-pair
  classes `(a, a+d) mod m` occur asymptotically equally often — is *wide open
  and cannot be treated using L-functions*. This is the exact barrier problem.md
  names.
- **Lau 2024** (`lau_residue_patterns`): even a *single non-constant* 2-term
  pattern mod 4 (e.g. `(1,3)` or `(3,1)`) is **not known to occur infinitely
  often**. Constant patterns `(a,a,…,a)` are the only ones with unconditional
  infinitude, via Shiu.
- **Shiu 2000 / Maynard 2016 / BFTB 2015**: the *equal-residue* side IS
  unconditional and positive-density. Maynard Thm 3.3 gives a positive-density
  lower bound for strings of `m` congruent primes in a fixed class mod q; BFTB
  Cor 3 makes the gaps bounded. But all of this is the *equal* side — in `h`
  terms, long constant (all-0/all-1) runs, **not switches**.

**Conclusion (verified across sources):** every unconditional result the
literature has is on the equal-residue side, which is precisely the side SUPPLY
*averaged over* does not need — and which refutes doors 1–3 (weight / no-constant
runs / aperiodicity). The switch side (pairs differing mod 4) is where the
parity barrier lives, and it is untouched by the positive-density equal-side
machinery. Hence the only live route is the fold `Φ` making the image heavy on
`h` despite these five failed structural hypotheses — exactly the run's stated
hypothesis under test.

## Coding-theory tier (added for the adopted Krawtchouk/Delsarte route)

The live approach `fold-second-moment-krawtchouk` rests its geometry engine on
Delsarte's linear-programming / MacWilliams / Krawtchouk machinery bounding the
*distance distribution* of the fold's row code. That tier is local and indexed:

- **MacWilliams 1963 (original)** — `sources/macwilliams_1963_weight_distribution_fulltext.full.md`. The weight-spectrum/dual identity, the exact theorem the adopted route names.
- **Ashikhmin–Barg–Litsyn** — `sources/ashikhmin_barg_litsyn_polynomial_method.full.md`. Delsarte's polynomial method.
- **Guruswami LP/MacWilliams course notes** — `sources/guruswami_macwilliams_lp_notes_fulltext.full.md`. Delsarte LP bound, Krawtchouk evaluations, MRRW — the notes stating the exact machinery the route cites.
- **Essential Coding Theory (Guruswami–Rudra–Sudan)** — `sources/essential_coding_theory_guruswami_rudra_sudan_fulltext.full.md`. Full textbook backing.
- **Friedlander 2024** — `sources/friedlander_macwilliams_krawtchouk.full.md`. MacWilliams identity for Krawtchouk association schemes.
- **Wikipedia: Krawtchouk polynomials / MacWilliams identity** — canonical encyclopedic tier.

## Canonical reference tier (all local, all indexed)

| Source | File | Role |
| --- | --- | --- |
| ABGS 2011 | `sources/ash_beltis_gross_sinnott_prime_residues.full.md` | Switch-density barrier (§9 "wide open … cannot use L-functions") |
| Lemke Oliver–Soundararajan 2016 | `sources/lemke_oliver_soundararajan_bias.full.md` | Fair-share conjecture; slowly-decaying biases |
| Shiu 2000 | `sources/shiu_strings_expository.full.md` (+ summary `shiu_strings_congruent_primes.md`) | Equal-residue strings; refutes door 3 |
| Maynard 2016 | `sources/maynard_dense_clusters_primes_subsets.full.md` | Positive-density strengthening of Shiu (Thm 3.3) |
| BFTB 2015 | `sources/banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples.full.md` | Bounded-gap congruent-prime strings (Cor 3) |
| Lau 2024 | `sources/lau_residue_patterns.full.md` | Non-constant 2-term patterns mod 4 open |
| Odlyzko 1993 | `sources/odlyzko_iterated_abs_values_diff_primes.full.md` | The iterated-abs difference object; {0,2} reduction; Gilbreath verified to 10^13 |
| Chase 2022 | `sources/chase_random_gilbreath.full.md` | Random analogue of Gilbreath — probabilitistic setting where the fold works |
| Mestrović 2014 | `sources/mestrovic_lucas_theorem_survey.full.md` | Lucas' theorem (C(d,i) odd iff i submask of d) — the run's door 2 |
| Rampersad–Wiebe 2023 | `sources/rampersad_wiebe_2regular_binomial.full.md` | Sums of binomial products mod 2; 2-regular sequences; Walnut |
| Bacher 2008 | `sources/bacher_beeblebrox_reduction.full.md` | Determinants/self-similar block structure of mod-2 Pascal (fold) matrices |
| Granville–Martin | `sources/granville_martin_prime_races.full.md` (+ `_prime_number_races` mirror) | Prime races; Chebyshev bias context |

## Why the fold route is the only live one — and what to read next

- For an attack on **target 4** (an arithmetic input strictly weaker than
  positive switch density), the load-bearing structural tools are local:
  Mestrović (Lucas/submask), Bacher (fold block structure), Rampersad–Wiebe
  (2-regularity / run-length transforms / Walnut — a *computation* route to
  identifying `wt(Φ_n h)` structure).
- For **target 3** (density-1 / averaged), the relevant contrast is Maynard's
  theorem: positive-density equal-residue strings exist, so any averaged
  argument that would "sum over all classes" is dominated by the equal side and
  cannot be converted to a switch lower bound without new input. The averaged
  SUPPLY statement must come from `Φ`-side cancellation, not from equal-residue
  density.

## Open requests

`walsh-spectral-subset-b904` (in REQUESTS) — a Walsh-spectral/subset-sum lower
bound on `wt(Φ_n x)` for inputs not "complicated" in the five refuted senses.
None of the local sources states such a bound; that is the actual gap, and no
library source closes it.

## Full-text availability

All full texts are in `research/sources/` (43 files) with short digests in
`research/summaries/` (55 files incl. citation-graph and OEIS records). All
indexed and reachable via `search_documents`. Two Granville–Martin copies exist
(same paper, different mirrors) — intentional, both kept. The seven-source
coding-theory tier driving the adopted Krawtchouk/Delsarte route is local and
indexed (see below).

## The coding-theory (Walsh/Krawtchouk/MacWilliams) tier — completed by the librarian

The open request `walsh-spectral-subset-b904` (a Walsh/subset-sum bound on
`wt(Φ_n h)`) sits on the coding-theory transform machinery. Seven sources were
already downloaded but their summaries were unfilled template stubs ("Digest
only — read this first"). The librarian wrote real digests (each with a claim
block) for all seven:

- `macwilliams_1963_weight_distribution_fulltext` — the original MacWilliams
  identity (Thm 1: `Σ A_i(1+vz)^{n−i}(1−z)^i = Σ B_i z^i`).
- `wikipedia_macwilliams_identity` — encyclopedic form
  `W(C^⊥;x,y) = (1/|C|)W(C;y−x,y+x)`.
- `wikipedia_krawtchouk_polynomials` — definitions/orthogonality/generating
  function of the Krawtchouk transform basis.
- `guruswami_macwilliams_lp_notes_fulltext` — MacWilliams from Fourier analysis
  on the cube + the Delsarte LP bound.
- `ashikhmin_barg_litsyn_polynomial_method` — Delsarte/polynomial-method survey.
- `friedlander_macwilliams_krawtchouk` — the identity in Krawtchouk association
  schemes (b-algebra moment machinery).
- `essential_coding_theory_guruswami_rudra_sudan_fulltext` — the textbook
  (808KB) depth version of the whole toolbox.

**Common bearing (uniform across all seven):** these fix the *transform
machinery* — the Walsh/Hadamard/Krawtchouk coordinate system in which
`wt(Φ_n h)`, the weight of the image of an F₂-linear map, becomes a spectral
statement, and give the *dual-positivity/LP* template shape
(`Σ_i A_i K_j(i) ≥ 0`) a submask-positive constraint on Φ's image would
instantiate. **None states the requested input-dependent bound**
`wt(Φ_n h) ≥ c·n` for the fixed prime string h — that is the genuine, still-open
gap `walsh-spectral-subset-b904`, per the scholar's overreach flag.
