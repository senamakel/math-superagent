# Scholar verification pass — 2026-08-13 (read the research agent's new batch)

## What this pass did

Read the full texts of the two re-downloaded priority papers end-to-end against their
summaries, verified the uniform-Mordell-Lang foundation tier and the concordant-forms
pair against their summaries, and checked the batch against the ledger, threads,
requests, and recalled memory. Storage: two `remember_memory` entries on disk.

## Verdict on the two re-downloaded papers

**Garcia-Fritz–Pasten, arXiv:2604.04850v2 (6 pp, 21KB, genuine PDF)** — summary
accurate, no correction needed. Verified directly in the full text:
- Thm 1.8: absolute C > 1, AP length on E/Q of rank r ≤ C^(r+1); unconditional,
  over any number field; proved via Nevanlinna + GGK uniform Mordell–Lang (the 2026
  note restates the 2021 IMRN result).
- Thm 1.2: conditional uniformity; the split-Jacobian construction is explicit: from an
  AP of length M ≥ 4 on E, X: s² = f(at²+b) is genus 2 with Jac(X) ~ E×E′, giving
  2⌊√(M−4)⌋+1 ≤ #X(Q) ≤ c^(1+2R). This is the direct mechanism by which a rank bound
  R would make the MSS a finite computation.
- Thm 1.3/Cor 1.4: finitely generated multiplicative groups, κ = 2c^(1+2R).
- §1.5 notes two further claimed proofs of Thm 1.8: Choi (arXiv:2510.03828, **conditional
  on a height conjecture of Lang**) and Harrison–Mudgal–Schmidt (arXiv:2603.06483,
  unconditional, on disk). HMS is a genuinely independent proof route, not a restatement.
- §2 cites **Yu–Yuan–Zhou arXiv:2602.01820** as giving "a completely explicit
  height-uniform upper bound" #X(k) ≤ c^(1+ρ) — the only source in the paper's chain
  that appears to make the constant explicit. Not in the library. Gap stands.

**Rome–Yamagishi, arXiv:2406.09364v2 (37 pp, genuine PDF)** — summary accurate.
- Thm 1.2: n×n magic square of squares for all n ≥ 4 (settles Várilly-Alvarado, n0(2)=4).
- Thm 1.3 with explicit n0(d) = 4min{2d,d(d+1)}+20 (d=3,4), 4⌈d(log d+4.20032)⌉+20 (d≥5).
- n=3 explicitly outside the method: σ_R(F0) ≥ n²−n puts Birch and Rydin-Myerson out of
  reach at n=3; the circle-method's column-independence count (Thm 2.4, n≥8) cannot
  descend to 3. Confirms the 3×3 open problem is qualitatively different from n≥4.
  `holds-here: no` as filed is right.

## Verdict on the foundation tier and concordant pair

- **DGH (arXiv:2001.10276)**, **GGK (arXiv:2105.15085v4)**, **Kühne equidistribution
  (arXiv:2101.10272)**: summaries faithful. The `holds-here: no` on DGH/Kühne (genus ≥ 2)
  is the single most valuable line: it pins why the effective lane for the genus-1
  Robertson curve is **DP07** (David–Philippon IMRP 2007 Thm 1.13), the unique
  uniform-ML result with a completely explicit constant, for self-products of an
  elliptic curve — stated as such on GGK p. 3, cross-checked in the DGH introduction.
- **Selder–Spindler (arXiv:1408.1522)** and **Knaf–Selder–Spindler (arXiv:1907.02148)**:
  faithful. Each satisfied MSS centre-AP difference d = u,v,u+v,u−v is a concordant-form
  instance with p=q=1, k=d on the congruent-number curve E(−d,d); neither paper touches
  the additive linkage among the four differences — the crux. Consistent with
  `phi-universal-set` / `phi-no-triple-m400`.

## Claims confirmed as filed (no edits needed)

`bremner-conjecture-proved`, `uniform-rank-ap-bounded`, `n-by-n-mss-exist-for-n-ge-4`,
`hms-2026-bremner-effective-constant`, `patterns-bremner-2026-no-mismatch-for-2E-Q`,
`gfp-2021-theorem-6-1-doubled-points-in-scope`, `dgh-uniform-mordell-lang-curves`,
`dgh-height-inequality-nondegenerate`, `ggk-uniform-mordell-lang-theorem`,
`dp07-explicit-uniform-ml-elliptic-self-products`, `kuhne-equidistribution-uniform-ml-curves`,
`kuhne-relative-bogomolov-fibered-products`, `gao-survey-uniform-ml-scope`,
`concordant-forms-iff-ell-torsion-order-2`, `concordant-single-ap-solutions-computable-large`,
`wu-bm-noninvariance-under-base-change`, `wu-chatelet-3folds-bm-noninvariance`,
`robertson-elliptic-reduction` (**complete — the truncated-at-"2E(Q)" row in CONTEXT.md
gaps is stale; the claim block now states the three doubled points, their x-coordinates,
the AP, and the membership rule**, and records the exact machine verification on Bremner's
witness: rank 2, exactly 2 of 3 main-diagonal x-coords in 2E(Q)).

## Contradictions / stale memory found

- **Recalled memory vs on-disk**: the durable-memory entry claiming Wu arXiv:2103.01784
  is an "abstract-only 6.6KB file" is stale — the full 78.9KB paper has been on disk
  since the original download; the summary note explicitly corrects it. No current
  belief depends on the stale version.
- **Recalled memory vs oracle**: CONTEXT.md "all_checks_passed: false" is stale;
  `near_misses.json` reports `all_checks_passed: true` (reconciliation 2026-08-12).
- **Filename misidentification**: `robertson-magic-squares-of-squares-1996.full.md` is
  a byte-for-byte duplicate of Bremner 1999; not a separate source.
- **No contradiction** between any on-disk source and its summary in this batch.

## Sources that do not help (with reasons)

- **Rome–Yamagishi** — neighbouring result (n ≥ 4); no 3×3 structural input; keeps the
  open question n=3-specific.
- **Wu 3-folds (arXiv:2010.04919)** — the Brauer–Manin approach it guards is already
  closed on Bremner II's K3 (S(Q) ≠ ∅); caution only.
- **Kühne relative Bogomolov (arXiv:2103.06203)** — encyclopedic-technical; no direct
  MSS statement.
- **Robertson-1996 file** — duplicate of Bremner 1999.

## Open gap carried forward

**Yu–Yuan–Zhou, arXiv:2602.01820** — the only completely-explicit height-uniform
Mordell bound in the GFP chain; could make the AP-length constant effective. Request
tool refuses a row (8 ledger claims match on topic, none covers YYZ); recorded in
`research/notes/librarian-cycle-2026-08-13.md` and `scholar-digest-summary.md`
instead. Next lane after that remains DP07 (Thm 1.13) for the genus-1/E^n shape.