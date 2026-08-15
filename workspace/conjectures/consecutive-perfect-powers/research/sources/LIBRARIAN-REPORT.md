# Librarian report — reference library state for this run

**Task:** build a local reference set for the open conjecture `x^p - y^q = 1`
(consecutive perfect powers). What is now available locally, where, and how it
was obtained.

## Headline

The reference library under `research/sources/` was already **mature** when this
session began (built by prior runs), and this session's job was to close its
edges rather than rebuild it: verify coverage against the open REQUESTS, add the
one FRONTIER-suggested source that was missing and legitimate to hold, record
why the answer-bearing gaps cannot be filled from outside, and clean up two
duplicate pointer files.

**Net additions this session:**
- `research/sources/katz-wieferich-past-and-future.md` — Katz, "Wieferich past
  and future" (Contemp. Math. **632**, 2015). The FRONTIER's top-cited
  non-answer source (cited 3× by the library). Supplies the definition of
  Wieferich primes/quotients, the FLT-first-case origin of the name, the base-2
  record (only 1093, 3511 known < 6.7×10^15), and Katz's equidistribution
  conjecture. Two claim blocks filed (`wieferich-primes-two-known-base2`,
  `wieferich-criterion-first-case-flt`).
- `research/sources/PROVENANCE.md` — updated rows for the Katz source and a new
  "Superseded pointer files" section recording the two duplicate redirects to
  remove on a future cleanup.

## What is available locally (research/sources/), by the role it plays in the run

### Canonical / encyclopedic tier
- `washington-introduction-to-cyclotomic-fields.md` — Washington, GTM 83.
  Metadata/ToC (full text not stored).
- `milne-algebraic-number-theory.md` — Milne ANT course notes (chapter outline;
  Z[ζ_p] machinery).
- `columbia-ant-cyclotomic-and-class-numbers.primary.md` — Columbia GU4043;
  Z[ζ_p] ring of integers, h=h⁺·h⁻, minus part via odd characters/Bernoulli,
  Stickelberger. **The canonical capture** (the `columbia-cyclotomic-class-groups`
  file is a superseded duplicate).

### Cyclotomic technique tier (the machinery the open content lives in)
- `conrad-factorization-cyclotomic.primary.md` — Z[ζ_n] ring of integers,
  ramification (p)=(1−ζ_p)^{p−1}.
- `conrad-cyclotomic-extensions.about.md`, `conrad-unit-theorem.about.md` —
  Galois group, Dirichlet unit theorem (rank (p−3)/2 for Q(ζ_p)).
- `keune-number-fields.md`, `nguyen-note-cyclotomic-integers.md` —
  ring-of-integers/ramification/discriminant.
- `zetap-ring-ramification.md` — (1−ζ_p)-adic valuation, ideal factorisation of
  ∏(x−ζ_p^i), pairwise coprimality off the ramified prime.
- `hida-elementary-iwasawa-cyclotomic.primary.md` — Iwasawa theory, analytic
  class-number formula, Stickelberger, Kummer–Vandiver.
- `mit-18.785-analytic-class-number-formula.primary.md` — ζ_K = ∏ L(s,χ) and the
  analytic class-number formula.
- `relative-class-number-analytic.md` — h⁻ via Bernoulli; Shokrollahi/Schoof.
- `schoof-real-cyclotomic-class-numbers.primary.md` — h = h⁺·h⁻ machinery.
- `stickelberger-cyclotomic-units.md`, `sinnott-1978-stickelberger-circular-units.md`,
  `ichimura-2006-class-number-formula-cyclotomic.md` — Stickelberger ideal,
  circular units, index [Z[G]⁻ : s⁻] = h⁻.
- `kummer-ratio-relative-class-number.primary.md` (+ `kummer-ratio-maillet-handcheck.md`)
  — Maillet determinant det(M_q) = ±q^{(q−3)/2}·h₁(q); Kummer criterion.
- `p-adic-valuation-technique.md` — LTE lemma, v_p(x^p−1), norm N(1−ζ_p)=p.

### Elements of the proof chain the library supplies technique for
- `elementary-factorisation-technique.md` — the exponent-2 cases (Z, Z[i]).
- `cassels-1953.md`, `cassels-1960-II.md` — Cassels's divisibility origin
  (abstract/reference records; full text blocked).
- `katz-wieferich-past-and-future.md` (NEW), `crandall-dilcher-pomerance-
  wieferich-wilson.primary.md` — Wieferich primes definition and records.
- `roitman-zsigmondy-primes.primary.md`, `zsigmondy-primitive-divisors-bhv.md`,
  `voutier-primitive-divisors-III.primary.md` — primitive divisors / Lucas
  sequences (r ≡ 1 mod p engine).
- `klazar-thue-theorem.primary.md` — Thue finiteness and its boundary.
- `evertse-linear-forms-logarithms.primary.md`, `stewart-linear-forms-baker-
  wustholz.primary.md`, `tijdeman-linear-forms-survey.md` — Baker bounds and why
  the effective bound is astronomically large.
- `pillai-related-equations-stroeker-tijdeman-bennett.md` — the related-equations
  tier (Bennett at-most-two / at-most-one, c₀(3,2)=13).

## Methods of capture

Download via `download_document` is refused at the network boundary for every
publisher/preprint host (failure was re-confirmed this session with both the AMS
DOI and the Princeton PDF). All sources were therefore captured **server-side
via `read_sources`** — records of the returned content with provenance, filed
under `research/sources/` with the source URL inside the document. This is the
established pattern in PROVENANCE.md and it is not a network fault.

## Could not be obtained, and why (so nobody retries)

- **Mihăilescu's proof / any full statement of the classification** — screened
  as answer-bearing. Do not retry; the run re-derives the closure in-workspace.
- **Double-Wieferich necessary condition and Inkeri's refinement** (REQUEST
  `exact-statement-citable-f890`) — search withheld as answer-bearing. The
  library supplies the *technique* (Wieferich definition via Katz+CDP; Cassels
  valuation/LTE; cyclotomic ring machinery); the congruence placement must be
  re-derived. Do not retry a direct fetch.
- **Nagell–Ljunggren** `(X^n−1)/(X−1)=Y^q` — screened; it is the run's owned
  closing step for Case B. Do not retry.
- **Full texts of publisher-hosted papers** — network boundary blocks all direct
  fetching; rely on the `read_sources` readouts and treat full statements as
  to-be-re-derived.

## Index / searchability

- `research/CLAIMS.md` — re-derived on each write; now includes the two Katz
  claims.
- `index_document` called on the new Katz note, so `search_documents` and
  `recall_memory`/`search_claims` reach it.
- `research/FRONTIER.md`, `research/REQUESTS.md`, `research/BLUEPRINT.md`,
  `research/BACKWARD.md` are part of the existing library plumbing and were kept
  intact.

## Verification notes carried forward

- The h⁻ class-number check flagged in the lessons as pending
  (`code/out/hminus_check.py`) is **superseded and settled by a stronger
  result**: claim `hminus-two-independent-routes` (status: checked) reproduces
  h⁻(Q(ζ_p)) for p=3..43 via two genuinely independent implementations (exact
  Bernoulli product vs PARI bnfinit ratio h(K)/h(K⁺)), matching OEIS A000927.
  The old float-specialised `hminus_check.py` is obsolete; the two-route claim is
  the live, stronger verification.
- Contradictions in CLAIMS.md (`dw-pairs-all-regular-corrected` vs
  `dw-pairs-regular-minor-torsion-free`) are flagged for resolution but are not
  this librarian's to settle; they concern the double-Wieferich descent content.

**Location of the deliverable:** the reference set lives under
`research/sources/` (with provenance in `PROVENANCE.md`); derived claims live in
`research/CLAIMS.md`; the board postings are in `teams/BOARD.md`.
