# Blair Morgan — The Return of the Lemma: Launchpads, corridor obstructions, and the shape of a counterexample (2026)

## Status of the corridor claim in this run

Item (iii) (the pure minimal corridor 8→7→6→5→4 is impossible from Row 2) has since been
**independently confirmed by a forward re-derivation** in this run
(`code/out/verify_morgan_corridor.notes.md`, claim `morgan-corridor-obstruction-forward-verified`,
status: proved). Forward chain: frontier(y)=7 ⇒ x_7=0; frontier(z)=6 ⇒ x_6=0;
frontier(u)=5 ⇒ x_5=0; breach value v_4=|u_4−4|=4 with u_4∈{0,2} ⇒ x_4=0. Row 2 has
x_4..x_7=(2,2,2,2), so the corridor cannot originate at Row 2. It rules out only the
**minimal** first-erosion path: non-minimal breaches (value ≥6), later frontier-8 rows,
and stalled erosion remain — the frontier hypothesis and regeneration stay open.

## Abstract / metadata

**Source:** https://zenodo.org/records/19144967 (DOI 10.5281/zenodo.19144967), working paper v2.0, March 2026, author Blair Morgan (ORCID 0009-0003-1942-8103). Full text: `research/sources/blair-morgan-2026-return-of-the-lemma.full.md`. Companion: `blair-morgan-2026-local-condition-frontier.md` (v1.0, same programme).

## The {0,2} basin / frontier formulation

- **{0,2}-closure:** `{0,2}` is closed under `|a − b|`. Once a position enters `{0,2}`, it never leaves (one-way membrane / attractor basin).
- **Frontier:** at row r, the leftmost position `k ≥ 1` with `G_r[k] ∉ {0,2}`. Observed frontier positions: row 1 → 3, row 2 → 8, row 10 → 59, row 30 → 870, row 100 → >90,000. Never observed below position 8 after row 1 (all verified to 100,000+ rows).
- **Theorem:** If the frontier stays at position ≥ 4 for all r ≥ 2 (equivalently `G_r[3] ∈ {0,2}`), then Gilbreath's Conjecture holds. Proof: induction with lemmas Parity, {0,2}-Closure, Boundary Stability (`|{0,2} − 1| = 1`), Propagation (positions 1,2,3 in {0,2} at row r ⇒ positions 1,2 at row r+1 in {0,2}), and Initial Conditions (`G_1[1]=2, G_1[2]=2, G_2[1]=0, G_2[2]=2, G_2[3]=2`).
- **Frontier Hypothesis (open):** frontier ≥ 4 for all r ≥ 2. This is the remaining unproved gap; the paper isolates it exactly as this run isolates regeneration.

## The proved local obstruction (this paper's genuine result)

Row 2 has frontier 8 with prefix `[1, 0, 2, 2, 2, 2, 2, 2, 4, …]`. **Claim:** no pure minimal erosion corridor `8 → 7 → 6 → 5 → 4` starting from Row 2 is possible.

*Proof structure:* Suppose a frontier-8 launchpad row `x = (1, x_1, …, x_7, 4)` with `x_1..x_7 ∈ {0,2}` feeds a pure four-step corridor to a minimal breach (frontier value 4) at position 4. Write `y = Δx, z = Δ²x, u = Δ³x, v = Δ⁴x`. Then:
- `y_7 = |4 − x_7|` must be outside {0,2} ⇒ `x_7 ≠ 2` ⇒ `x_7 = 0`;
- `z_6 = |y_7 − y_6| = |4 − x_6|` must be outside {0,2} ⇒ `x_6 = 0`;
- `u_5 = |4 − x_5|` ⇒ `x_5 = 0`;
- `v_4 = |4 − x_4|` ⇒ `x_4 = 0`.

So any such launchpad must have `x_4 = x_5 = x_6 = x_7 = 0`, but Row 2 has `(x_4, x_5, x_6, x_7) = (2, 2, 2, 2)`. Hence Row 2 cannot initiate a pure minimal erosion corridor from frontier 8 to frontier 4. ∎

**Explicit limits:** this eliminates only (a) the minimal-breach case (value exactly 4 at position 4), (b) a pure one-step-per-row corridor `8→7→6→5→4`, (c) with Row 2 as launchpad. Later frontier-8 rows, non-minimal breaches (value 6+), and stalled/more complicated erosion remain possible. A supporting backward-generation script builds the finite set of length-9 launchpad prefixes that can feed such a corridor (the "finite doors" lemma), and Row 2's prefix is not in it.

## Absorption facts stated

`|4−2| = 2`, `|4−4| = 0`, `|6−4| = 2`, `|6−6| = 0` are all in {0,2}; only `|6−2| = 4` and `|6−0| = 6` produce values outside — the run's depth-1000 finding that intruder 4 with edge 2 is exactly the regeneration trigger is the same boundary arithmetic, in the run's (edge, intruder) coordinates.

## What remains open (per the paper)

Prove the Frontier Hypothesis: `G_r[3] ∈ {0,2}` for all r ≥ 2 (equivalently, the frontier never reaches position 4). Suggested routes: prime-gap analysis of positions 1–3; probabilistic bounds (erosion rate dominated by absorption rate); a backward constraint-tree proof.

## Bearing on this run

- The frontier hypothesis `G_r[3] ∈ {0,2}` is exactly the run's leading-block regeneration question restated with `b_k ≥ 3` replaced by the front positions. The run's stronger data (`b_k` minima 13, 24, 96, …; block length never near 0) implies the frontier condition far more strongly in the computed range.
- The corridor-obstruction result is a template for the run's own obstruction arguments at the (2,4) boundary: the same "backward forcing of constant blocks" technique is applied at frontier positions 4–7 here, and at the block-end edge in the run's regeneration thread.
- Caveats: not peer-reviewed; author credits an AI collaborator; the parity "unique odd" phrasing is loose (should be "position 0 odd, others even" — matching this run's proved parity wave). The minimal-corridor claim is sound as a four-row local computation (the run could re-verify it in minutes against the exact rows).