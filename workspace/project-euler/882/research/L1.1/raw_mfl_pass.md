# Combinatorial Games with a Pass (Morrison–Friedman–Landsberg 2011)

- Source: https://arxiv.org/abs/1204.3222 — full text `research/L0/raw_mfl_pass.full.md`.
- **Proper analysis in [[mfl_pass]]** (same paper). This note is just the raw
  arXiv abstract.
- Framing: treats combinatorial games as dynamical systems to study how a
  one-time "pass" move changes them. **Nim**: pass radically restructures the
  game (S–G solution breaks). **Chomp**: pass has minimal impact. Recursion
  operators connect passes to "generic perturbed games"; pass effects predicted
  by (non-rigorous) numerical stability.
- Consequence for this problem: a pass can perturb structure unpredictably, so
  S(n) cannot be read off the no-skip value A−B ([[disjsum]], [[surreal]]); it
  must come from the skip-budget DP. Agile: our skip is repeated, budgeted,
  partisan — not their one-time impartial pass.
