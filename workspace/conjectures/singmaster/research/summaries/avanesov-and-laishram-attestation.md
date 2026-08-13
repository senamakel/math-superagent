# Attestations recorded this cycle (librarian pass)

Purpose: lock in two primary results that are NOT directly downloadable but are
attested inside papers this library already holds in full, so a later run does
not re-badge them as unverified or re-fetch the blocked originals pointlessly.

## 1. Avanesov 1966 — C(n,2) = C(m,3) completely solved

- **Result**: Avanesov (1966) found ALL integral solutions of C(n,k) = C(m,l)
  for (k,l) = (2,3) (triangular = tetrahedral).
- **Attestation** (primary, held): GRKTU 2020
  `research/sources/gallega-ruiz-katsipis-tengely-ulas-binommld-2019.full.md`
  (arXiv:1904.11369), Introduction: "In 1966, Avanesov [1] found all integral
  solutions of equation (1) with (k,l)=(2,3)."
- Also cross-attested: de Weger reduced (2,3) to Mordell's elliptic curve
  `Y^2+Y=X^3-X` (held `research/summaries/deweger-equal-binomial-1995.md`);
  BMSST 2008 holds full-text; and Singh-Kane-SDW confirm genus-1 effective
  solvability.
- **Bearing**: TASKS.md item 3 (Matveev effective constant for {2,3}).
  Avanesov already establishes finiteness with a listed solution set; the
  GOAL-eligible deliverable is an independent EFFECTIVE height bound with a
  computed constant via Matveev 2000 Thm 2.3 (K=Q). Avanesov is the
  finite-list check oracle for that computation.
- **Obtained**: the 1966 primary itself (Soviet Math. / Mat. Zametki-era note)
  is not freely held; attestation via held GRKTU + de Weger is sufficient for
  the use here (source of the finiteness, not of a constant).

## 2. Laishram–Shorey — correct citation fixes a corrupt library file

- The library file named `laishram-shorey-prime-divisors-consecutive-2004`
  is already flagged (CLAIMS.md `laishram-shorey-corrupt-download`) as holding
  a topology paper (F. Johnson, "On the triangulation of smooth fibre
  bundles", Fund. Math. 118 (1983) 39-58) — NOT Laishram–Shorey.
- **Correct reference**: S. Laishram, T.N. Shorey, "The greatest prime divisor
  of a product of consecutive integers", Acta Arithmetica 120 (2005),
  DOI 10.4064/aa120-3-5. Let Δ(n,k)=n(n+1)...(n+k−1), P = greatest prime
  divisor, ω = number of distinct prime divisors, ω(1)=0, P(1)=1.
- **Precise bounds** (attested by held Shorey–Tijdeman review
  `research/sources/shorey-tijdeman-survey.full.md`):
  - P(Δ(n,k)) > 1.8k for n>k, unless (n,k) in a specified finite list
    { (8,3),(6,4),(7,4),(15,13),(16,13),(4,3),(5,4),(6,5),(9,8),(12,11),
      (14,13),(15,14),(19,18),(64,63) }.
  - P(Δ(n,k)) > 1.97k for n>k+13.
  - P(Δ(n,k)) > 2k for n > max(k+13, 279k/262)  (note P(279,262) ≤ 2·262,
    so the threshold n>279k/262 is necessary).
  - All finitely many exceptions to P(Δ(n,k))>1.95k with n>k were computed
    (list too long to reproduce here).
- **Bearing**: this is the refined Sylvester–Schur engine behind the
  `sylvester-prime-machine` approach, which is REFUTED (the overlap at 3003:
  primes 7,11,13 serve k=2,5,6 representations together — see APPROACHES.md).
  So the correct citation is recorded for provenance but carries no live thread.

## 3. Tian's conjecture (C(n+1,2) prime-factorization) — blocked, method confirmed

- Source: "Tian's Conjecture on the Prime Factorization of the Binomial
  Coefficient C(n+1,2)", Mathematics (MDPI) 14(1) 127, 2025-12-29. The MDPI
  page returns HTTP 403 to this container; only abstract/search summary was
  retrievable. Already flagged in
  `research/summaries/claimed-resolutions-2025-2026-caution.md`.
- **Confirmed method** (from search abstract): for fixed distinct primes
  p1..pm, the equation C(n+1,2) = p1^a1...pm^am has at most m solutions in
  n, a1..am. Verified for m=2,3 via linear forms in elliptic logarithms, with
  the first sub-conjecture proved by Zsigmondy's theorem on the primitive
  prime divisor of a^b − c^d.
- **Bearing**: fixed-column (k=2) structure, adjacent to but not Singmaster's
  N(a); carry as context only. Not a source of any uniform-in-a bound.

## What remains NOT freely obtainable (reported per policy)

- Singmaster 1971 (AMM 78) — paywalled; attested via held Singmaster 1975 FQ
  primary (tombstone at `research/sources/singmaster-1971.full.md`).
- Avanesov 1966 primary — attested via held GRKTU/de Weger.
- Laishram–Shorey 2005 (IMPAN) — 502/403-blocked; attested via held
  Shorey–Tijdeman review.
- Tian 2025 (MDPI) — 403-blocked; method confirmed via search abstract.
