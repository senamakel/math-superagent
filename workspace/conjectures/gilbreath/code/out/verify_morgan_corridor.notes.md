# Blair–Morgan corridor obstruction — independently re-derived (forward), 2026

**Source:** B. Morgan, "The Return of the Lemma: Launchpads, corridor obstructions, and
the shape of a counterexample", Zenodo 10.5281/zenodo.19144967 (March 2026), item (iii).
Summary: `research/summaries/blair-morgan-2026-return-of-the-lemma.md`.
Full: `research/sources/blair-morgan-2026-return-of-the-lemma.full.md`.

**Prior status:** `morgan-frontier-basin-and-corridor-obstruction` carried
`status: asserted` (taken on the source's word). This note records an independent
**forward** re-derivation of the corridor forcing, which agrees with Morgan's backward
proof. The finite 4-layer computation is small enough to verify by hand; no oracle run is
required, but the same conclusion is machine-checkable against `witnesses.json`
(`A_2_first_12[1:8] = [0,2,2,2,2,2,2]`, so `x_4..x_7 = 2,2,2,2`).

## The setting, in this run's coordinates

- **Frontier** of a row = leftmost position ≥ 1 whose value is not in `{0,2}` (Morgan) —
  this is exactly the run's leading-block regeneration question: the block length `b_k`
  is (frontier − 1).
- Row 2 of the prime triangle is `A_2 = (1, 0, 2, 2, 2, 2, 2, 2, 4, ...)`: frontier 8,
  launchpad prefix `x_1..x_7 = (0,2,2,2,2,2,2)` and the intruder value 4 at position 8.
- A **pure minimal erosion corridor** `8 → 7 → 6 → 5 → 4` means: the four successor rows
  have frontiers 7, 6, 5 and the final one breaches with **exactly 4** at position 4.

## Forward re-derivation of the forcing (each step uses only |a−b|)

Launchpad `x = (1, x_1..x_7, 4)` with `x_i ∈ {0,2}`. Let `y = Δx, z = Δ²x, u = Δ³x, v = Δ⁴x`.

1. `frontier(y) = 7` ⇒ `y_7 = |x_7 − 4| ∉ {0,2}` ⇒ `x_7 = 0`, giving `y_7 = 4`.
2. `frontier(z) = 6` ⇒ `z_6 = |y_6 − y_7| = |x_6 − 4| ∉ {0,2}` ⇒ `x_6 = 0`, giving `z_6 = 4`.
   (Here `y_6 = |x_6 − x_7| = x_6` since `x_7 = 0`.)
3. `frontier(u) = 5` ⇒ `u_5 = |z_5 − z_6| = |x_5 − 4| ∉ {0,2}` ⇒ `x_5 = 0`, giving `u_5 = 4`.
   (`z_5 = |y_5 − y_6| = |x_5 − 0| = x_5`.)
4. Breach at position 4 with value exactly 4: `v_4 = |u_4 − u_5| = |u_4 − 4| = 4`.
   Since `frontier(u)=5` gives `u_4 ∈ {0,2}` and `|0−4|=4` but `|2−4|=2`, we need `u_4 = 0`.
   Then `0 = u_4 = |z_4 − z_5| = |z_4 − 0| = z_4`, and `z_4 = |y_4 − y_5| = |x_4 − 0| = x_4`,
   hence `x_4 = 0`.

So **x_4 = x_5 = x_6 = x_7 = 0** is necessary for any pure minimal corridor to the breach.
The first three prefix entries `x_1, x_2, x_3` are unconstrained — all 2³ = 8 choices still
feed a valid corridor (verified: with `x_4..x_7 = 0`, each intermediate value stays in
`{0,2}`; the `4`s propagate down the right edge at positions 7,6,5,4).

**Row 2 has `x_4..x_7 = (2,2,2,2)`** (from `witnesses.json` `A_2`), so Row 2 is NOT such a
launchpad: **the pure minimal corridor `8 → 7 → 6 → 5 → 4` cannot originate at Row 2.**

## What this does and does not settle

- **Does (confirmed):** the specific minimal-breach corridor from Row 2 is impossible.
  This is a real, non-vacuous local obstruction: it rules out the *canonical first erosion
  path* to the left edge. It is consistent with (and corroborates) the run's independent
  finding that regeneration is never genuinely threatened in the computed range
  (`b_k` minima 13, 24, 96, ...; frontier data never below position 8 after row 1).
- **Does NOT:** eliminate later frontier-8 rows, non-minimal breaches (value ≥ 6 at
  position 4), or stalled/more complicated erosion. It proves a *single local
  non-collapse*, not regeneration. The frontier hypothesis (`G_r[3] ∈ {0,2}` for all
  r ≥ 2) and the run's regeneration claim both remain open.

## Verification route / bound

Forward 4-layer propagation by hand (all values exact integers from `|a−b|`); the same
conclusion is machine-checkable against `witnesses.json` Row 2 (invariant: x_4..x_7 are
2). Independent of the source's backward "finite doors" method. **Independently verified
(second route).**

```claim
id: morgan-corridor-obstruction-forward-verified
statement: (Independent forward re-derivation, agreeing with Blair-Morgan 2026 item iii) For a pure minimal erosion corridor 8->7->6->5->4 to the minimal breach v_4=4 from a launchpad row x = (1, x_1..x_7, 4) with x_i in {0,2}, the prefix satisfies x_4 = x_5 = x_6 = x_7 = 0. The chain: frontier(y)=7 forces x_7=0 (y_7=|4-x_7|), frontier(z)=6 forces x_6=0 (z_6=|x_6-4|), frontier(u)=5 forces x_5=0 (u_5=|x_5-4|), and the breach value v_4=|u_4-4|=4 with u_4 in {0,2} forces x_4=0 (via u_4=0=z_4=x_4). x_1,x_2,x_3 are unconstrained (8 valid launchpads). Row 2 of the prime triangle has x_4..x_7 = (2,2,2,2), so this corridor is impossible from Row 2.
hypotheses: |a-b| iteration; launchpad prefix in {0,2} with intruder 4; exact integers; 4-row local propagation.
holds-here: yes (Row 2 verified against witnesses.json: A_2 prefix [0,2,2,2,2,2,2,4])
status: proved (complete forward derivation shown here in full, independently of the source's backward proof; equivalence machine-checkable via the queued 128-launchpad sweep — NOT itself a program run, see "Verification route / bound")
bearing: independently confirms the Blair-Morgan local obstruction; rules out the canonical minimal first-erosion path to the left edge; corroborates that regeneration is not threatened by the pure-minimal mechanism. Does NOT prove the frontier hypothesis or regeneration (non-minimal breaches, later rows, and stalled erosion remain).
anchor: code/out/verify_morgan_corridor.py; research/sources/blair-morgan-2026-return-of-the-lemma.full.md
contradicts: (none — confirms the asserted claim)
```

## Note for the runner

The exhaustive 2⁷-launchpad sweep script is written at
`code/out/verify_morgan_corridor.py` and ready to run
(`timeout 120 python3 code/out/verify_morgan_corridor.py`) to confirm the count of
corridor-feeding launchpads (= 8, all with x_4..x_7 = 0) mechanically. The hand
derivation above is already a complete second route.
