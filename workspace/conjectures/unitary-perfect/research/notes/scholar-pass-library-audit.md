# Scholar pass 2026-08-14 — library audit and digest completion

## What was done

Read the complete texts of the three load-bearing primary sources (Maciejewski
arXiv:2605.20475, Graham 1989, Wall 1975) and audited all 41 summary files.

1. **Maciejewski full text verified verbatim** — every named object (3-Higgs
   definition §1.1; impostor kernels §2; three filters §3; Prop 4/5, Thm 7/8,
   Thms 9–19, Lemma 20, Thm 21, C23–26/29, Thm 30, Prop 31/Cor 32) is present
   in the document, not only in the notes. The abstract-only status in
   `problem.md` is stale — fixed there. New precision recorded in
   `research/notes/paper-extraction.md` (Lemma 20 exact table, the five
   composite-k candidates, Prop 5 proof, the 279→272 internal arithmetic).
2. **Graham 1989 and Wall 1975 summarised properly** — the "Digest only"
   template banner on Graham (which made a genuine digest look like a stub)
   and Wall 1975 replaced with real, under-1000-token digests carrying the
   theorem statements, method, and consequence for this run.
3. **Bootstrap banners removed** from Wall 1972, Wall 1975-cambridge, and
   A002827-internal-format (real digests that looked like stubs).
4. **Wall 1975 read cover-to-cover** — confirms the fifth UPN's factorization
   and the origin of the "10^102" orphan: the bound is `N < W ≈ 1.46e23`,
   seed cap `a < 38`; "10^102" is not in the paper.
5. **No-value sources flagged** so nobody re-reads: Hagis 1985 (UHP search,
   no bearing on UPNs), Villemin (pop page with wrong 1966 date), Guy 2nd/3rd
   ed. (paywall/front-matter only), Leangenius (JS shell), cunningham (wrong
   table for H_even targets), Goto primaary (paywalled, only zbMATH review
   held), BHV 2001 (OCR unusable, status asserted).

## What remains genuinely open (unchanged)

- Frei 1978 primary text (REQUESTS row 1) — the m≥144 / ω≥144 / n>10^440
  3-not-divisibility bound is OEIS-recorded only.
- Goto 2007 primary (REQUESTS row 3) — the `N < 2^(2^k)` bound is
  zbMATH-review-recorded only.
- The "10^102" anchor (REQUESTS row 4) — Wall–Hagis 1972 letter and Guy §B3
  are the likely carriers, neither held.
- The analytic target: divisor-level control of the prime divisors of
  `Φ_{4p}(2)` (thread `divisor-level-phi4p`, paper's Conjectures 23/24/29) —
  nothing in the library changes the exponential `2^{2p}/p` scale gap.

## Durable findings stored

Four `remember_memory` entries (Maciejewski verification; summary-file audit;
Wall 1975 read; OEIS/Cohen/Wall/Hagis/BHV/Guy audit) plus the CLAIMS.md
corruption correction. All source-backed, all anchored.

## Files touched

- `problem.md` — corrected the stale "full text is not held" statement.
- `research/notes/paper-extraction.md` — verified-against-the-full-text
  section.
- `research/summaries/graham-1989-squarefree-odd-part.md` — real digest +
  claim.
- `research/summaries/wall-1975-fifth-unitary-perfect-number-pdf.md` — real
  digest + claim + 10^102 correction.
- `research/summaries/oeis-a002827-internal-format.md` — real digest + claim.
- `research/summaries/wall-1972-*.md`, `wall-1975-*-cambridge.md` — banner
  cleanup.
- `CONTEXT.md` — Established (provenance, Graham fix, Maciejewski verified,
  Wall 1975), Ruled out (10^102→10^23), Contradictions (279/272 resolved,
  CLAIMS.md corruption).