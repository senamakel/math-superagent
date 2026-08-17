# Recent-literature survey — Singmaster (2022–2026)

Purpose: a durable record of a wide survey of 2022–2026 literature, so a later
run does not re-survey the same ground. Surveyed 2026-06 via `exa_search`
(research-paper category, multiple phrasings) and `citation_graph` on the two
strongest held sources.

## What the citation graph reports

- **MRSTT 2021** (arXiv:2106.03335, QJM haac006) is cited by only 4 works:
  1. Matomäki–Shao–Tao–Teräväinen, "Higher uniformity of arithmetic functions
     in short intervals I" (Forum Math. Pi 2023 / arXiv:2204.03754) — these
     authors' own short-interval program; cites the Singmaster-in-interior
     theorem as an application, no new Singmaster-bound content.
  2. Bazsó–Mező–Pintér–Tengely, "Singmaster-type results for Stirling numbers"
     (IJNT 2024, DOI 10.1142/s1793042125500137) — **already held** as
     `research/sources/singmaster-type-stirling-2023.full.md`.
  3. Melles–Joyner, "Harmonic Graph Morphisms and the Moonlight of
     Mathematics" (College Math J 2024) — unrelated.
- **GRKTU 2020** (arXiv:1904.11369, "On the Diophantine equation C(n,k)=C(m,l)+d")
  has **0 citations** — the near-collision complete-solution paper is not built
  on by anyone else.

## What wide searching adds

Nothing new and load-bearing. Adjacent items found, none a multiplicity bound:

- **Allen 2024**, arXiv:2406.10404, "Solvability of C(2k,k)=C(2a,a)·C(x+2b,b)".
  Proves solvability iff x=a=1 under k=a+b. A product-of-central-binomials
  identity; not a multiplicity bound. Marginal to Singmaster.
- **Bui–Pratt–Naprienko–Zaharescu 2026**, arXiv:2605.21221, "Binomial
  coefficients with divisors avoiding an interval". GRH-conditional typical
  statements about binomial coefficients having no divisors near n. Relates to
  Erdős Problem #684, not to multiplicity. Not load-bearing.
- **Erdős Problem #684 density-one** (Li 2026, arXiv:2606.08216): small-prime
  part of binomial coefficients; normal-order theorem, not a multiplicity bound.

## Fake/crackpot resolutions — do not cite

The Zenodo preprints (Okolo 2025, Keen 2026, Hall 2026) claiming a full proof of
Singmaster are non-peer-reviewed, 0-citation, and catalogued as such in
`research/summaries/claimed-resolutions-2025-2026-caution.md`. None is held in
`research/sources/`. Treat any claimed proof not in `research/sources/` as
unverified unless it survives N(3003)=8 and gives an effective uniform bound.

## Librarian re-sweep (deep_research + exa, same period) — confirms the bottom line

A second, independent sweep this run (deep_research on "any boundary/uniform-in-k
progress since MRSTT" plus wide exa searches over 2021-2026) returned nothing new
and load-bearing. Results, all already held or explicitly excluded:

- **MRSTT 2021** (held): interior only, does not touch the boundary regime; its
  four surface citers have no Singmaster-bound follow-up.
- **Kane "Improved Bounds" (Zenodo 8337164)**: is the already-held Kane 2007 h53.
- **Bazsó–Mező–Pintér–Tengely Stirling analogue** (held, arXiv:2311.06080).
- **Yamada 2021 "On a problem of De Koninck"** (Moscow Math J): methodologically
  adjacent only — it is about σ(n)=(rad n)², not binomial collisions.
- **Crackpot "resolutions"** (Okolo 2025, Kashino 2025, Hall 2026 Zenodo preprints):
  non-peer-reviewed, 0-citation, catalogued in
  `claimed-resolutions-2025-2026-caution.md`; never store.
- **MRSTT is the penultimate-word work in its citation graph**; no one builds a
  boundary result on it. **Yamada's binomial-collisions 2020 (arXiv:2002.07043)
  is cited zero times** — no one has extended its necessary conditions.

Conclusion: the open boundary (2 ≤ m ≤ (log t)/(log log t)^{3/2−ε}) genuinely has
no new upper bound and no uniform-in-k result as of mid-2026. Do not re-survey
under this name.

## Bottom line

As of 2026-06 the landscape is unchanged from what the library already holds:
MRSTT's interior bound is the sharpest statement of the gap; the boundary
regime `2 <= m <= log t / (log log t)^{3/2 - eps}` remains the open part; no
peer-reviewed source has closed it. The only multiplicity-8 value is 3003; the
only infinite N>=6 family is the Fibonacci/Pell one. No re-survey needed under
this name.
