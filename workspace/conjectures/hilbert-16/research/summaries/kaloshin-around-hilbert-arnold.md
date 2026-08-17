# Kaloshin — Around Hilbert–Arnold Problem

Full text: [[kaloshin-around-hilbert-arnold.html.full]]. arXiv:math/0111053.

## What the source establishes

Lecture notes surveying the **Hilbert–Arnold problem** (a quantitative, parametric
offshoot of H16): for a generic k-parameter family of polynomial/smooth planar
fields, bound the cyclicity of polycycles.

- **Local Hilbert–Arnold (weak form), Kaloshin's solution [K1]:** gives an
  **independent proof** of the **Ilyashenko–Yakovenko Finiteness Theorem** for
  elementary polycycles.
- **Elementarity is the hypothesis that carries the weight** (as in the Ilyashenko
  survey): the elementary-singularity condition is what makes the return map's
  expansion appear in a finite-dimensional space (Ramified / Dulac type maps), so
  finite cyclicity is provable by the fewnomial / Khovanskii argument.
- The fourth lecture generalises to **spatial (3D) polycycles** and applies the
  Grigoriev–Yakovenko construction to the growth of periodic points — out of scope
  for this planar problem.

## What it lets this run conclude

Confirms the elementary-polycycle Hilbert–Arnold results and the explicit bound
(2^{25k²}, stated in the Ilyashenko survey). The mechanism (fewnomial/Khovanskii
zero-count on Ramified return maps) is the calibrated model for the run's
elementary-polycycle rung, and the boundary it stops at (nilpotent/degenerate
vertices give non-Ramified expansions) is the degenerate-graphics gate.

```claim
id: h16-kaloshin-indep-proof
statement: Kaloshin's weak local Hilbert-Arnold theorem gives an independent
  proof of the Ilyashenko-Yakovenko finiteness theorem: cyclicity of an
  elementary polycycle in a generic k-parameter family is finite.
hypotheses: elementary polycycle; generic finite-parameter family.
holds-here: yes (elementary case undisputed).
status: asserted
bearing: independent confirmation of the elementary finite-cyclicity pillar.
anchor: research/sources/kaloshin-around-hilbert-arnold.html.full.md
follows-from: h16-kaloshin-elementary-bound
```

## Does not help

Beyond the elementary case, Kaloshin's notes explicitly do not cover nilpotent /
degenerate polycycles (the exact wall the open DRR graphics sit at). Confirms the
status; adds no new route through the degenerate gate.
