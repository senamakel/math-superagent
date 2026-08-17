# Librarian cycle — library completeness re-verified, this cycle

What this cycle did: re-audited the actual on-disk library (not the summaries) against
the frontier ledger, the open requests, and the phase-1 bar, to confirm the "library is
finished" directive rather than take it on faith. Verdict: the library is complete for
the run's purposes; gathering stays closed; nothing added this cycle.

## Phase-1 bar — met, and re-confirmed source-anchored

`research/ROOT.md` states all three deliverables, each tied to a primary source in
`research/sources/`:

1. **Minimal-counterexample structure**: any counterexample has n = |∪F| ≥ 13
   (Vučković–Živković 2017, computer-assisted n ≤ 12, full text on disk) and
   |F| ≥ 4·13 − 1 = 51 (Roberts–Simpson 2010 + Hu 2017, both on disk); and
   |F| < 2^(n−1) (Karpas 2017, on disk).
2. **Current best constant**: published record ≈ 0.38234 (Yu, Entropy 2023, on disk);
   (3−√5)/2 = 0.381966 iid-entropy barrier peer-reviewed (Alweiss–Huang–Sellke, EJC
   2024, on disk); Cambie ≈ 0.3823455 and Liu ≈ 0.38271 remain preprints/conditional
   (both on disk). Where the entropy method is capped is stated as the iid-OR
   inequality barrier, not a barrier to the full conjecture.
3. **Settled classes**: lattice classes (modular Abe–Nakano, lower semimodular
   Reinhold, planar/large semimodular Czédli–Schmidt, breadth ≤ 2 / upper
   semimodular-few-join-irreducibles Joshi–Waphare; subgroup lattices
   Abdollahi–Woodroofe–Zaimi), graph formulation (Bruhn–Charbit–Schaudt–Telle), small
   sets (Ellis–Ivan–Leader: 3-sets do NOT force UC, with exact density), FC-families
   (Poonen/Vaughan/Morris/Marić–Živković–Vučković), separating families (Maßberg),
   approximate union-closed (Chase–Lovett). All full texts or survey restatements on
   disk.

## Open requests

`exact-current-published-c8b8` is closed in the claim store by several claims
(`published-record-current-verified`, `published-status-current`,
`librarian-cycle-2026c-published-record-reverified`, `librarian-record-still-stable-2026`),
each re-verified live against the arXiv/IEEE/journal records in later cycles. No open
row remains.

## Frontier — top rows verified on disk

Checked the ledger's ≥2-cited rows against the sources directory. Held as full texts:
Knill math/9409215, Bruhn–Schaudt survey (both copies), Gowers polymath, AHS, Cambie,
Liu, Yu, Balla–Bollobás–Eccles, Karpas, Marković 2007, Czédli 2009, Marić–Živković–
Vučković 2012, Pulaj (all), Raz 2017, Moghaddas, Morris, Hu, Nagel, Wikipedia.
Remaining not-held rows are:
- **Johnson–Vaughan 1999 "On Union-Closed Families, I"** (JCTA 85, cited ~20×) — its
  duality content is represented by the Bruhn–Schaudt survey restatement (on disk);
  not load-bearing as a primary.
- **Studer 2021 "An asymptotic version of Frankl's conjecture"** (AMM) — asymptotic;
  cited only by Nagel/Bhasin notes.
- **"Extremal Union-Closed Set Families"** (Graphs Combin 2019) — peripheral.
- **Poonen 1992 full proof, Reimer 2003 full proof, Hachimori–Kashiwabara 2024** —
  paywalled, recorded precisely as gaps in earlier notes; content via errata/survey/
  restatements.

None of these is load-bearing for the run's active fronts (entropy coupling ceiling at
t̂_max ≈ 0.3823455, abundance-profile, the Lean formalisation of the g(n,m) envelope).
Per the operator directive that the library is finished, none was added.

## Verified, not assumed

This cycle's value is that the completeness verdict was re-derived from the disk (file
listing, grep of full texts, claim-store search, ledger read) rather than repeated from
memory. The library satisfies the phase-1 bar; gathering stays closed; no request open.
The three paywalled primary-proof gaps remain as recorded, unobtainable, and
non-blocking.
