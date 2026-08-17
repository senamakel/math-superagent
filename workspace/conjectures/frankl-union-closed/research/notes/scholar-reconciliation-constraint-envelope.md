# Scholar reconciliation — reference library against the investigation (this cycle)

Scope: verify the reference library's coverage against the current attack
(abundance-profile front + the constraint-envelope hunt), confirm the newest
verified results are in the on-disk claim store, and flag contradictions/gaps.

## What I verified this cycle

- **The library is complete and internally consistent.** Every load-bearing
  claim traced: KPT Thm 5(3) statement in the source (research/summaries/
  kabela-polk-teska-abundant-elements-2022.md) matches the filed claims
  `kpt-thm5-corrob-n4` / `kpt-thm5-counterexample-corollary` (f ≥ min{n, 2k−n+1},
  so f=0 ⟹ n_max ≥ 2k_min+1). The combine constraints note cites the five held
  claims (A) kpt-thm5-counterexample-corollary, (B) karpas-large-families,
  (C) verified-m-small, (D) no-degree-1-element-in-minimal-counterexample,
  (E) rarest-count-floor — all present in the store via `search_claims`.
- **The two newest verified results are in the on-disk claim store** (they were
  never written to durable Cognee memory because the store was down when they
  finished):
  1. `cc-no-abundance-without-closure-on-4` — 74 non-UC families on [4] satisfy
     the arithmetic counterexample constraints yet have no abundant element.
     Conclusion: union-closure is the indispensable hypothesis (GOAL.md control
     #2, made concrete).
  2. `odd-filter-max-density-extremal-nonboolean` — the odd filter is NOT the
     unique most-balanced non-Boolean UC family; n+1 minimizers (odd filter + n
     power-set-minus-singletons) all at 2^{n−1}/(2^n−1).
  Cognee is down this cycle (3 failed `remember_memory` calls), so these durable
  writes are parked in the on-disk claim store, exactly the remedy the combine
  finding records.
- **The `abundance-profile` thread's "resting on nothing recorded" is a spelling
  mismatch, not a gap**: it cites `ahs-barrier` and `eil-small-sets`; the store
  holds them as `ahs-barrier-3-minus-rt5-over-2` and
  `ellis-ivan-leader-small-set-3-fails` / `ellis-ivan-leader-smallest-set-frequency`.
  No real gap. I updated the thread file to fold in the resolved constraint
  envelope and corrected the resting-on names at the source.

## Sources that do NOT help (stated plainly, so nobody re-reads them)

- **Demontis 2405.03731** (claims a full proof of UC): filed as an *unaudited
  claimed proof* — 0 citations, 26-day acceptance at a predatory-adjacent venue
  (OPAST Curr Res Stat Math), never uses or cites the entropy/(3−√5)/2
  literature, self-contained to a suspicious degree for a 45-year-old problem.
  **Nothing in it may be cited as established.** Claim
  `demontis-claimed-uc-proof-unaudited`. If the run ever revisits the
  conjecture head-on, the candidate failing step is the final
  `2|D_i| ≥ ...` inequality from Theorems 4–5.
- **Raz 2017 + Markovic 2007**: the former shows Reimer's condition alone does
  not imply an abundant element (useful negative control on the averaging
  method); Markovic proves UC for largest set ≤ 10, subsumed by the Bošnjak–
  Marković n≤11 verification bound. Digest already accurate.

## Contradictions

- **None live.** The two `search_claims` "contradiction" flags from the
  librarian report (`morris-conj3` vs `pulaj-morris-counterexample`) are
  resolved — Pulaj refuted Morris's conjecture and both sides record the
  "refuted" stance. The `ahs-barrier` vs dependent-coupling tension is a
  *scope* distinction (iid barrier vs full conjecture), not a contradiction,
  and the `contradiction-sawin-ahs` thread records it as settled.

## What the run still lacks (durable memory)

- **Cognee durable memory is empty of the two newest verified results.**
  `remember_memory` is refused by an outage. The on-disk claim store covers
  this (these claims ARE filed and findable), so nothing is lost — but when the
  memory service recovers, the next cycle should store
  `cc-no-abundance-without-closure-on-4` and `odd-filter-max-density-extremal-...`
  durably so they surface in cross-run recall. The combine finding's own
  "read the note, don't re-derive" remedy is the standing mitigation.

## The reconciliation as a usable fact

A minimal counterexample's abundance profile must satisfy: (A) largest set ≥
2·(smallest set)+1, (B) m < 2^{n−1}, (C) n_ground ≥ 13 and m ≥ 51, (D) no
degree-1 element, (Spence) |F| odd = 2k+1 with a tight-witness property — and
the run's own exhaustive [4] scan proves pure counting (A),(B),(D) is NOT
enough: union-closure must be used. That is the frontier the abundance-profile
front now guards, and it is recorded in research/threads/abundance-profile.md.
