# Scholar pass report — summary digest completion & evidence corrections

## What this pass did

Digested the reference library into usable notes. Two threads of work:

### A. Verified+fixed the two newest sources (this cycle's acquisitions)

1. **Prohens & Torregrosa 2019** (H(4)≥28 … H(10)≥142) — Theorem 1, Corollary
   2(a),(b) verified verbatim against the full text (lines 70-79). Corrected an
   imprecision: Prop. 6's object is a **rational first integral**
   `(2x⁴−x²+y²−2x−2)⁵/(8x⁵−5x³+5xy²−10x²−5x−4)⁴`, NOT a "quartic Hamiltonian".
   Important for Lean: it is a quotient object; the three-centre condition is
   the polynomial-statable part. Fixed in summary + claim note (`holds-here`).
2. **Liénard degree-5 (Rychkov vs general)**: Rychkov 1975 settles the odd-only
   degree-5 Liénard at ≤2; the general mixed-parity degree-5 case stays OPEN.
   Already stored from prior pass; confirmed consistent. This REFINES
   `h16-lienard-n5-open`, does not strike it.

### B. Completed the summary notes (removed ~17 "Digest only" placeholder stubs)

All placeholder summaries in research/summaries/ replaced with real notes
(claim-oriented, each wikilinking its full text). New/rewritten notes:
Grau–Mañosas–Villadelprat (TAMS 2010), Torregrosa 2024 (M(3)≥12), Villanueva–
Tucker 2026 (Bautin-ideal enclosure), Bautin 1952 (M(2)=3 primary), Moussu
(Bourbaki), Hilbert 1900 (canonical H16), Ilyashenko 2016 (revised proof digest),
Huzak 2022 (canard cyclicity), Llibre–Schlomiuk 2004 (QW3), Rousseau–Zhu 2004
(15 pp-graphics), Pedregal 2021 (refuted/unverified), Speissegger o-minimality,
Caubergh 2012 (uniform-finiteness theorem), Gasull–Lázaro–Torregrosa 2010,
plus landing-page pointers for Bautin-mathnet, Villanueva-Tucker-arxiv,
Speissegger-arxiv.

### C. Claim-ledger corrections (the most valuable outcome)

1. **`h16-grau-manosas-villadelprat-chebyshev-2010`**: removed a stale duplicate
   that said "full text NOT yet held"; the authority is now the single correct
   block (Theorems A/B + the GGI four-new-cases result). Grau full text IS held.
2. **`h16-gasull-lazaro-torregrosa-abelian-zero-bounds-2010`**: evidence-class
   corrected from "full text held" to **sourced-at-abstract-level** — the held
   file is only the arXiv landing page, so exact (K,n) bounds are NOT verified.
3. **`h16-prohens-torregrosa-h4-28-primary`**: `holds-here` corrected (rational
   first integral, not quartic Hamiltonian).

## Contradictions / cross-source notes

- Gasull–Lázaro–Torregrosa now flagged as abstract-only; the concrete Chebyshev
  instrument the run can lean on is Grau–Mañosas–Villadelprat (fully held).
- Pedregal 2021 reaffirmed as refuted/unverified (variational, Test-1 fails);
  its contrast with the o-minimal route is the cleanest statement of where a
  valid uniform-finiteness proof must use analyticity.

## Memory server status

Cognee is down this cycle (health-check timeout; recall worked at session start
but remember_memory fails). Per the workspace rule, all findings are persisted in
the claims ledger (research/notes/claims.md), the summary notes, and this report.
Store to memory when Cognee recovers.

## Gaps the run still has

- Gasull–Lázaro–Torregrosa 2010 article body (for the exact Abelian zero bounds).
- Grau full text was the "to be downloaded next" item — now held; the new dry
  request is the Abelian-integral zero-count instrument (see APPROACHES).
- The LLT (Li–Liu–Yang 2009) and Han–Li 2012 paywalled primaries remain
  second-hand (unchanged).
