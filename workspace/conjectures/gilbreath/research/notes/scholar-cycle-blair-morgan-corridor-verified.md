# Scholar cycle — Blair–Morgan corridor obstruction independently verified

## What this cycle did

The library was already extensively digested over five previous scholar cycles (148+
claim blocks, G-supply conditional theorem stated exactly, all load-bearing anchors
verified against primary text). The remaining marginal value was not another
re-digestion pass but **second-route verification of the one claim still resting only
on a source's word among the newest sources**.

The two newest held sources are Blair–Morgan 2026 (Zenodo working papers): the
"frontier basin" note and its corridor-obstruction item. Both carry claims
(`morgan-frontier-basin-and-corridor-obstruction`, `morgan-local-condition-sufficiency`)
that the ledger held as `asserted`. The **corridor obstruction** — a concrete,
self-contained finite claim — was independently re-derived as a **forward 4-step
proof**, confirming it and upgrading it to `status: proved`
(`morgan-corridor-obstruction-forward-verified`).

## What the forward re-derivation establishes

For a pure minimal erosion corridor 8→7→6→5→4 from a launchpad `x=(1,x_1..x_7,4)`,
`x_i∈{0,2}`, breaching with value exactly 4 at position 4:

1. `frontier(y)=7` ⇒ `y_7=|x_7−4|∉{0,2}` ⇒ `x_7=0` (y_7=4);
2. `frontier(z)=6` ⇒ `z_6=|x_6−x_7|=|x_6−4|∉{0,2}` ⇒ `x_6=0` (z_6=4);
3. `frontier(u)=5` ⇒ `u_5=|z_5−z_6|=|x_5−4|∉{0,2}` ⇒ `x_5=0` (u_5=4);
4. breach `v_4=|u_4−u_5|=|u_4−4|=4` with `u_4∈{0,2}` ⇒ `u_4=0`, then
   `u_4=0=z_4=x_4` ⇒ `x_4=0`.

So `x_4=x_5=x_6=x_7=0` is necessary; `x_1,x_2,x_3` are free (8 launchpads). Row 2 has
`x_4..x_7=(2,2,2,2)` (confirmed against `witnesses.json` `A_2`), so the minimal corridor
cannot originate at Row 2.

## Status and honest limits

- **Proved:** the specific minimal-breach first-erosion path from Row 2 is impossible.
  Independently of Morgan's backward "finite doors" construction (a genuine second route).
- **NOT proved / still open:** the frontier hypothesis (`G_r[3]∈{0,2}` for all r≥2), and
  regeneration. Non-minimal breaches (value ≥6), later frontier-8 rows, and stalled
  erosion remain. This is one local non-collapse, not regeneration.

## What does not help / was not re-read

- The corpus's many settled canonical sources (Odlyzko, CHT, Chase, LOS, ABGS, Granville,
  the Ducci tier, the OEIS records) were already digested to claim level in prior cycles
  with verified anchors; re-reading them would cost context to reproduce knowledge that is
  on disk. Their load-bearing claims (`abgs-2011-s9-mod4-switch-limit-open`,
  `lemma54-re-derived-proof`, `los-2016-consecutive-pair-mod4-bias`, the G-supply
  conditional theorem) were spot-checked and are accurate.
- The G-supply open gap (a lower bound `ν₂≥c·n`, two-point mod-4 switch correlation, named
  open by ABGS 2011 §9) is unchanged: no held source proves the switch-direction bound;
  Shiu/Ruzsa bound only the equal-residue (non-switch) side. Nothing in this cycle moved it.

## Contradictions flagged

No new contradiction. `morgan-corridor-obstruction-forward-verified` **confirms** the
asserted source claim (not contradicts). The existing ledger contradictions
(`odlyzko-block-lemma-exact` vs `-asserted`, `caldwell-proth-myth` vs retraction) remain
as recorded.

## Artifacts

- Proof note + claim block: `code/out/verify_morgan_corridor.notes.md`
- Queue-able exhaustive sweep (128 launchpads, second machine route):
  `code/out/verify_morgan_corridor.py`
- Source note cross-referenced: `research/summaries/blair-morgan-2026-return-of-the-lemma.md`
