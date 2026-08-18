# DRR status — settled state (thread)

```thread
question: Which of the 121 DRR graphics have finite cyclicity proved, which
          remain open, and the paper closing each recently closed row?
status: settled
rests-on: h16-drr-121-graphics, h16-drr-closed-rows-2015, h16-drr-open-rows,
          drr-rr-closes-i14, drr-rr-boundary-only-for-3-graphics
next: the enumeration is answered — RR 2015 leave exactly one graphic
      (H14_3) with no partial result; Lu 2026 claims it. Live action is
      verification of Lu's finite core, in thread lu-h14-3-verification.
```

## Established (from held primary text)

## Established (from held primary text)

- Frame: 121 graphics in S²×K; finite cyclicity of all ⇔ H(2)<∞.
  Sources: RSZ 2015 (arXiv:1502.00689), RR 2015 (arXiv:1506.07104), Ilyashenko
  2002 — all held in full.
- **88 of 121** closed as of RSZ 2015 (their own verbatim count).
- RR 2015 fully closes **(I₁₄¹)**; closes only the boundary limit periodic sets
  of **(I₆b¹)**, **(H₁₃³)**, **(DI₂b)**; **(H₁₄³)** is the one graphic through a
  triple point at infinity with no partial result.
- This run's arithmetic: **89 fully closed, 3 partial, ≥32 not fully closed**;
  11 degenerate graphics (other than DF1a, DF2a) open per Shan 2013 (reported).

## Open targets (ranked)

1. `(H₄¹³)` — hemicycle through triple point at infinity, two semi-hyperbolic
   points on the equator; no partial result existed (RR 2015). **UPDATE 2026:
   H. Lu, arXiv:2607.13785 (unrefereed preprint, 80pp) claims local uniform
   finite cyclicity for exactly this graphic, identified as B=0 in RR 2015
   Theorem 3.1's family. Claim not verified; see claim
   h16-drr-h14-3-lu-2026-claim and note
   research/notes/lu-h14-3-open-graphic-claim.md.** Verification is the live
   action: peer/community check, plus checking "local uniform finite cyclicity
   in one collar" matches DRR's definition (DRR 1994 not held).
2. `(I₆b¹)`, `(H₁₃³)`, `(DI₂b)` — boundary set done, full graphic open; RR 2015
   says H₁₃³ should be "straightforward" with I₁₄¹-type arguments (done
   alongside generic (H₁₂³)), I₆b¹ needs new 2-equation methods (four Dulac
   maps of second type), DI₂b likewise with semi-hyperbolic points.
3. The 11 degenerate graphics other than DF1a, DF2a (per Shan 2013 thesis;
   needs primary confirmation of each id).
4. RSZ Thm 3.2's hypothesis μ₁=0 (fixed connection on blow-up sphere for the
   I₉b²-type graphic in sector Sxhh5) — authors conjecture it is unnecessary.

## Update (steer directive): target inventory answered

The inventory question is now answered: Roussarie–Rousseau 2015 leave **exactly
one** graphic through a triple nilpotent point at infinity with no partial
result — **(H14_3)** (hemicycle, two semi-hyperbolic points along the equator).
H. Lu, arXiv:2607.13785 (Jul 2026, unrefereed, 80pp) claims local uniform finite
cyclicity of it and ships a reproducibility bundle. The next action is NOT more
enumeration — it is the independent verification/refutation of Lu's finite
computational core, tracked in `research/threads/lu-h14-3-verification.md` and
task `verify-lu-h14-3-finite-core`. The full 121-row raw enumeration remains
blocked on DRR 1994 not being held (recorded as a gap).

## Gaps / dead ends

- Full 121-row open/closed enumeration NOT producible: DRR 1994 raw catalogue
  not held. The requests ledger needs DRR 1994 (or a post-2020 Rousseau survey
  with per-row status) to complete the table.
- 121 vs 125 unresolved (Shan 2013 counts 125).
- DF2a closure attribution (2009 vs 2018) unresolved — marked reported.
- A deep-research suggested label H₁₃⁴ was checked against the primary text,
  which uses H₁₄³; the guess is dropped.

## Where the claims live

`research/notes/claims.md` ids: h16-drr-121-graphics,
h16-drr-closed-rows-2015, h16-drr-open-rows, h16-drr-121-vs-125-discrepancy,
plus drr-rsz-closes-i12-i13, drr-rr-closes-i14,
drr-rr-boundary-only-for-3-graphics, drr-121-graphics-reduction in the
summaries. Machine-readable table: `research/drr-list.md`.