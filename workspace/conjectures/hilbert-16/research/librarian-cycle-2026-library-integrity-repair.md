# Librarian cycle report — 2026 library integrity repair

## What this cycle did

This was a **library-integrity repair cycle**, not a broadening cycle. The library
already meets the phase-1 sufficiency test (research/ROOT.md) and carries 200+
primary sources. The audit found the actual defect: **claims cited everywhere but
readable nowhere**.

### The defect, precisely

The runtime's ledgers (threads, claims, entailment) resolve `rests-on:`,
`follows-from:` and `contradicts:` edges only to **claim blocks** — files in
`research/claims/` with a `statement` field. Before this cycle:

- The settled thread `drr-status` rested on five claim ids with **no claim block on
  disk** (`h16-drr-121-graphics`, `h16-drr-closed-rows-2015`, `h16-drr-open-rows`,
  `drr-rr-closes-i14`, `drr-rr-boundary-only-for-3-graphics`).
- drr-list.md referenced two more (`drr-ledger-no-consolidated-post2020`,
  `drr-shan-2013-table11-ledger`).
- The `pedregal-variational-claim-test` thread rested on two more
  (`h16-pedregal-variational-claim-unrefereed`, `h16-ominimality-route-roussarie`).
- Three scholar blocks contradicted `h16-dulac-finiteness-theorem`, also missing.
- Two blocks existed but had **no statement field** (`h16-abelian-integral-bounds`,
  `gmv2008-ect-criterion`), so the parser read them as "claiming nothing".
- The entailment ledger flagged 7 edges as "following from nothing" — 4 were
  phantom, 3 were real.

This is exactly the failure mode the role exists to prevent: a later run would
have cited `h16-drr-121-graphics` as if the library established it, and nothing on
disk would have said what it is.

### The repair

Fifteen claim blocks filed or repaired in `research/claims/`, each with statement,
hypotheses, holds-here, status, evidence, falsifier, sources, anchors:

1. `h16-drr-121-graphics` — the DRR reduction frame (asserted-by-source, anchors:
   RSZ 2015, RR 2015, Ilyashenko 2002, UHasselt record).
2. `h16-drr-closed-rows-2015` — 88 closed by 2015 (verbatim RSZ anchor).
3. `h16-drr-open-rows` — (H³₁₄) + 11 degenerate open (RR 2015 line 63, Shan 2013).
4. `drr-rr-closes-i14` — (I¹₁₄) closed by RR 2015 Thm 1.2.
5. `drr-rr-boundary-only-for-3-graphics` — (I¹₆b),(H³₁₃),(DI₂b) boundary-only.
6. `drr-ledger-no-consolidated-post2020` — negative bibliographic finding.
7. `drr-shan-2013-table11-ledger` — the 125-convention per-class ledger.
8. `h16-dulac-finiteness-theorem` — Ilyashenko/Écalle individual finiteness, with
   the Yeung contention and the uniformity caveat.
9. `h16-quadratic-closed-form-refuted` — the Entropy-2024 H(n)=2(n−1)(4(n−1)−2)
   refutation (Buzzi–Novaes), which the prose `contradicts:` line was gesturing at.
10. `h16-canard-asymptotic-lower-bound-2020` — the canard n² log n lower bound,
    at MaRDI-review level (full text paywalled).
11. `h16-lower-bounds` — the consolidated test-2 calibration H(2)≥4, H(3)≥13,
    H(4)≥28, H(n)≳n²log n.
12. `h16-pedregal-variational-claim-unrefereed` — dead-route assessment.
13. `h16-ominimality-route-roussarie` — NRH_d o-minimality closure (KRS 2009 held).
14. `h16-mourtada-1991-hyperbolic-finite-cyclicity-primary` — moved into
    research/claims/ so the two Dukov edges resolve (content unchanged).
15. `h16-abelian-integral-bounds`, `gmv2008-ect-criterion` — statements restored.

Also fixed: three prose `contradicts:` lines the parser split into phantom ids
(`a`, `claim`, `quadratic-upper-bound`); removed the false
`follows-from: Cited.marin_fake_saddle_transition` edge (a Lean namespace axiom,
not a claim id — the attribution lives in the `formalisation:` field).

### Audit result

- `threads` ledger: no "resting on nothing recorded" section remains.
- `claims` ledger: no "could not be read" and no "no claim of that id is on disk"
  entries remain; all contradictions resolve to real ids.
- `entailment` ledger: only the intended entries remain ("Established for free",
  "Supporting themselves"); no "following from nothing".

## Search results this cycle

- DRR 1994 paper: re-confirmed paywalled (ScienceDirect S0022039684710618); the
  1997 Rousseau survey (S0362546X97001752) also paywalled, content subsumed by
  held sources. The two DRR-ledger requests stay open — they are unfillable from
  one source and the triangulated inventory (research/drr-list.md) is the honest
  answer.
- Abelian special-family request: already answered by held sources (Sun–Dai 2025,
  An–Dai–Hu 2025, Mucino–Rebollo 2025, Hong–Hong–Lu 2020, FTV2013, GMV, BNY,
  BD). The 2025 2D Picard–Fuchs paper (S0007449725000697) is paywalled with no
  open copy found.
- Frontier top rows: already held (Écalle 1992, Ilyashenko 1990/1991, Shi
  Songling 1980, BNY 2010, Roussarie 1986) or appropriately recorded as
  paywalled (Andronov bifurcations book).

## Standing

research/ROOT.md phase-1 criterion remains met. The library now backs every
claim id the ledgers cite. No new source was downloaded this cycle (all search
candidates were already held or paywalled); the value was making the existing
library readable.
