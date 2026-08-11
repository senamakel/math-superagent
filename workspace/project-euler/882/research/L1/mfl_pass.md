# Kombinatorische Spiele mit Pass — Morrison, Friedman, Landsberg (2011)

**Source:** Morrison, R. E., Friedman, E. J., Landsberg, A. S., "Combinatorial
games with a pass: a dynamical systems approach," *Chaos* 21, 043108 (2011).
arXiv:1204.3222 (open access — the AIP DOI 10.1063/1.3650234 is paywalled).
Full text stored at `L0/raw_mfl_pass.full.md` (abstract-level page).

## What it establishes
- Studies how adding a **one-time pass** (a player may skip a turn instead of a
  substantive move) changes a combinatorial game, by recasting the game as a
  dynamical system (recursive maps over P/N-position geometry).
- **Two contrasting outcomes:** in 3-pile Nim the pass *dramatically* alters the
  structure and increases complexity (standard Sprague–Grundy solution breaks
  down); in 3-row Chomp the pass has *minimal* impact. The recursion-operator
  analysis connects passes to a class of "generic (perturbed) games," with a
  (non-rigorous) numerical stability study to predict pass effects.
- Core message: **a pass can change a game's structure unpredictably — a lot
  (Nim) or a little (Chomp) — so the no-pass theory alone does not determine
  the game with a pass.**

## Why it applies here
The problem's skip is a pass-like device (only Zero may skip, budgeted). This
source is the closest *quantitative caution* in the library: it is evidence that
one cannot read S(n) off the no-skip value A−B ([[disjsum]], [[surreal]]),
since a pass perturbs the game's structure substantially in general. It
corroborates the run's decision to compute S(n) by a dedicated (A,B) minimax DP
over skip budgets rather than from the CGT no-skip value, and complements the
rigorous scoring-game pass theory of [[pass_waiting]] with a dynamical view of
how a pass "breaks" naive structural prediction.

## Caveat
- The paper analyzes a *single, one-time* pass in *impartial* Nim/Chomp; our
  skip is *repeated, budgeted, and partisan*. It is a structural caution (passes
  perturb games non-trivially), not a recipe; S(n) comes from the DP.
