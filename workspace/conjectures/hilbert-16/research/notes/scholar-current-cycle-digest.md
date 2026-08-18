# Scholar pass report — verifying the newest acquisitions (DGR 2002, Luca 2009) and repairing stale notes

## What this cycle added, and what I did

The current librarian cycle's addendum reported two new primary full texts
(DGR 2002 elementary-graphics closures; Luca–Dumortier–Caubergh–Roussarie 2009
alien cycles). Both had already been digested by a prior scholar pass into
claim blocks. My job this pass was to **verify those claims against the held
full texts**, store the durable findings (Cognee was down when they were made
and never persisted), and repair notes that a later pass had left stale.

## Verification against full text

### 1. Dumortier–Guzmán–Rousseau 2002 — CONFIRMED accurate

Read the held full text (`research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`,
1910 lines) and checked each theorem in the claim `drr-dgr-2002-elementary-closures`:

- **Thm 3.1** (lines 456-460): (H³₄),(H³₅) cyclicity ≤ 2, **irrational** hyperbolicity ratios. ✓
- **Thm 3.2** (lines 987-990): (H³₄),(H³₅) cyclicity ≤ 2, **rational** ratios; at r(0)=1 (A=2) first saddle quantity = 2B ≠ 0. ✓
- **Thm 3.3** (line 997): (H³₆) ≤ 2 if r(0)≠1, ≤ 3 if r(0)=1; full 5-parameter unfolding (42), center case B=0. ✓
- **Thm 4.1** (line 1292): (I²₂₇) ≤ 2. ✓
- **Thm 5.1** (line 1432): (I²₁₄a),(I²₁₅a) finite cyclicity. ✓
- **Lemma 5.2** (lines 1504-1506): (R(x))^r not affine, nonvanishing higher derivative. ✓
- **Thm 5.3** (line 1534): (I²₁₅b) ≤ 2. ✓

Every numbered bound and its hypothesis matches the claim block verbatim.
The seven elementary DRR rows in `research/drr-list.md` (lines 43-47) are
correctly marked **sourced-held, closed with cyclicity ≤ 2/3**. The claim is
**sourced** (held full text) and I have now **read-confirmed it against the
source**.

### 2. Luca–Dumortier–Caubergh–Roussarie 2009 — CONFIRMED accurate (abstract + structure)

The claim `h16-alien-limit-cycles-abelian-insufficiency` is an accurate
rendering of the held DCDS 2009 preprint: a cubic Hamiltonian 2-saddle cycle
(saddles at (−1,0),(1,0)) whose unfolding produces an alien limit cycle not
controlled by Abelian-integral zeros (appears via the second derivative of the
transition map along the saddle connection — Cor. 13 / Thm 15). The caveat is
already written into `research/approaches/abelian-picard-fuchs-argument-principle-sharp-count.md`
(lines 34-40, 96-97), confining the Abelian-integral route to the period
annulus of a center (nonsingular ovals) — exactly the right restriction, since
the alien example is cubic (n=3) and does not touch the quadratic (n=2) DRR
frame.

## Stale/broken notes repaired

1. **`research/summaries/lu-h14-3-spec-bautin.md`** still said the two Lu
   bundle scripts were "still not held." The fifth-pass addendum held them. I
   rewrote: scripts now held, but NOT yet re-executed in this workspace, so
   their focal-value/centre-barrier rows (U(0)=1/48) stay **asserted**, not
   checked (thread `lu-h14-3-verification`).
2. **`research/notes/lu-finite-core-verified.md`** had the same stale "NOT yet
   held" sentence in two places; both updated to "now held, not yet
   re-executed."
3. **`research/summaries/alvarez-coll-demaesschalck-prohens-canard-lower-bounds.md`**
   was a broken "Redirecting" capture. Replaced with an honest note: claim
   `h16-canard-asymptotic-lower-bound-2020` is carried at MaRDI-review level
   (full text paywalled), plus a provenance claim block.

## Memory

Cognee is up this cycle. Stored both verified durable findings:
- DGR 2002 elementary-graphics cyclicity bounds (verbatim, with the
  verification note).
- Luca 2009 alien-cycle/Abelian-insufficiency caveat.
(the only remaining gap is a rooted note; no further claims needed.)

## What is ON HOLD / NOT established by these sources

- The open nilpotent/degenerate DRR rows — (H³₁₄) (Lu 2026 unrefereed claim,
  algebraic core verified, theorem asserted) and (I⁶b¹),(H¹³₃),(DI₂b) full
  graphics plus the ≥11 degenerate graphics (Shan 2013) — are **outside both
  new sources' scope**. DGR 2002 is elementary only.
- The alien-cycle result is cubic; it does not bear on H(2) and does not change
  the quadratic DRR frame.
- Requests `complete-current-ledger-cb3d` / `dumortier-roussarie-rousseau-9c4f`
  (the full 121-row open/closed ledger) remain open: DGR 2002 adds seven
  elementary rows to `drr-list.md` but no new consolidated ledger exists.

## What the run still lacks (unchanged)

- DRR 1994 raw 121-id catalogue / post-2020 consolidated ledger.
- Clean-room re-execution of the two now-held Lu bundle scripts (would upgrade
  U(0)=1/48 etc. from asserted to checked) — the `lu-h14-3-verification`
  thread's named next step.
- Open PDFs of Li–Liu–Yang 2009 (H(3)≥13), Han–Li 2011 (growth), Mañosas–
  Villadelprat 2011 (Chebyshev sequel), Rychkov 1975 — all second-hand.
