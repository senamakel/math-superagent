# Scholar report — digest, verification, and adjudication-payload cycle

## Directive compliance (steer applied this cycle)

The operator's redirect asked that the finished allowable-sequence adjudication not be
dropped by tool-permission mismatch. Scholar does **not** hold `record_entry`; the fallback
the directive itself prescribes was applied: the payload was written to the workspace via
`write_document` and stored durably.

- `research/summaries/scholar-adjudication-allowable-sequence-circular-representation-refuted.md`
  — the full adjudication substance (both load-bearing mechanisms refuted, exact counts at
  n=4..7, the structural impossibility of reversal-depth = block index via the constant N−1
  pair-reversal count, the survivor: pointwise extreme-in-projection convexity, 64839/64839;
  the encoder replay bug fix; the "do not re-derive" instruction).
- The **approaches ledger closure** (`allowable-sequence-circular-representation`, status
  **refuted**) still needs a role holding `record_entry` (director or goals). The on-disk
  anchor is ready for it.
- `remember_memory` is down (memory server unresponsive; 14 failures across the run). Per the
  directive, the payload is written to the workspace instead of being silently abandoned; it
  should be stored to Cognee when the server recovers (note inside the file).

## What I read against the primaries

The library is mature (93+ claim blocks). This cycle's verification work:

1. **Baek, "On the Erdős–Tuza–Valtr Conjecture" (arXiv:2206.04260v2)** — full text on disk.
   Verified that the proofs are actually in the text: Theorem 3.2 (slope labeling exists),
   Theorem 3.6 (α-statistic injective into grid simplex T_{a,b}), Lemma 5.2 (interweaved
   laced cups force a (3,n−1)-gon), Theorem 5.10 (induction producing such a pair at size
   (n−1 choose 2)+2), and Theorem 2.7 (immediate consequence). **Upgraded three claims from
   asserted to proved:** `baek-ETV-n4n`, `etv-alpha-statistic-injective`,
   `baek-interweaved-laced-cups`. `etv-equivalent-to-es` stays **asserted** (it cites ETV
   1996, whose primary is unobtainable; the equivalence statement is not proved in the held
   text).
2. **Baek–Balko SoCG 2025 full text** — read the opening, split-gon definitions, Theorem 3/4/6,
   Theorem 7/8 verbatim. Confirmed the ledger's distinction: `baek-balko-split` proved
   (Lemma 10/11 proofs present; Lemma 9/12 "proof omitted"), `baek-balko-decomposable`
   **asserted** ("The proof of Theorem 8 is omitted", deferred to JCTA 2026). This is
   consistent with durable memory and the thread, not a contradiction.
3. **Beagley (Order 30, 2013)** and **Knauer–Trotter (arXiv:2303.08945)** — both held only as
   abstract/landing pages; replaced the placeholders with honest notes. New claim
   `beagley-order-dimension-esz` (status **asserted**, abstract-only): the order-dimension
   reformulation (ES extremal set has closed-set lattice dimension n−1; larger sets have
   dimension ≥ n) does **not** establish the missing direction — a set with a convex n-gon
   also has dimension ≥ n, so the theorem never forces the convex n-gon. The
   `convex-geometry-order-dimension` approach (status proposed) must not use it as its
   load-bearing step. `knauer-trotter-dimension-taxonomy` recorded as not-helpful (abstract
   convex geometries, no planarity, no ES content).
4. **Solymosi publications page & Valtr homepage** — replaced the remaining placeholder with a
   negative/provenance note and new claim `karolyi-solymosi-not-author-hosted` (catalogued):
   the Károlyi–Solymosi 2005/6 primary is confirmed unobtainable in open access; content is
   restated in the held Károlyi–Tóth 2012. Answers request `full-text-faithful-b96b`.
5. **Conlon–Fox–He–Mubayi–Suk–Verstraete HTML variant** — replaced placeholder with a redirect
   note to the substantive digest (claim `cfhmsv-big-line-big-convex`).

## Contradictions with recalled memory

**None.** Everything this cycle recorded is *consistent with* durable memory — the
allowable-sequence verdict re-affirmed the recalled refutations exactly (constant N−1
reversal count; contiguous-block convexity false in both directions; pointwise
extreme-in-projection survivor; fixed replay bug); the Baek–Balko proof-status distinction
matches the thread's "decomposable asserted, split proved" note; the ETV status upgrades
contradict nothing. No source contradicted another on any load-bearing claim.

## Conclusions

- **P(n,4,n) is now a proved restricted-class result on disk** — the first new case of the
  ETV conjecture since 1935, equivalent to the ES conjecture via Theorem 1.5, hence a genuine
  (if polynomially far) partial result below the ES(7) frontier. The α-statistic injectivity
  is a structural constraint testable on hypothetical extremal sets with the oracle.
- **The order-dimension approach's load-bearing theorem is abstract-only.** Anyone reviving
  `convex-geometry-order-dimension` must first obtain Beagley's proof or prove the missing
  converse; as held it does not force 2^{n-2}.
- **The two unobtainable primaries are closed, recorded, "do not re-search."**
- **Request rows are all answered** (ENDM 2015 digest answers `balko-valtr-attack-baa4` and
  `open-access-full-1e6e`; Solymosi note answers `full-text-faithful-b96b`).

## What the run still lacks

- **Approaches ledger closure** of `allowable-sequence-circular-representation` (needs a
  `record_entry`-holding role; anchor file ready).
- **Machine verification of the Horton construction** (`code/out/horton_verify.py`, handoff
  to coder already exists; capture never written). The verifier is written against the
  verified `lib.es_geom` oracle with hand-known positive/negative self-tests.
- **Store to Cognee** of the two durable-finding records once the memory server recovers.
- **ES(7) remains open**; the strongest route remains structural (split/decomposable theory,
  stability/uniqueness), and the pending computation — gsplit Phase-2 provenance re-capture,
  then the scored k=7 search — is where the run's attention belongs next, per the librarian's
  and the steering's shared conclusion.