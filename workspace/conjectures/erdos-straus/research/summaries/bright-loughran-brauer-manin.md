# Bright & Loughran, "Brauer–Manin obstruction for Erdős–Straus surfaces"

Source: arXiv:1908.02526 (Bull. LMS 52 (2020) 746–761).
Full text: `research/sources/bright-loughran-brauer-manin.full.md`

## What it establishes (sourced)

- The `4/p = 1/x+1/y+1/z` solution set is the set of integer points on an
  "Erdős–Straus surface" (a variety / Cayley-type surface).
- Main result: **there is no Brauer–Manin obstruction** to the existence of
  points on these surfaces. I.e. the failure of the Hasse principle (integer
  points don't lift from modular solutions) is *not* explained by a Brauer–
  Manin obstruction.
- Consequence: this rules out one class of explanations for why modular
  identities fail; the reason the six squares resist is the Schinzel/
  quadratic-reciprocity vanishing (Prop 1.6 of Elsholtz–Tao), not a
  Brauer–Manin obstruction.

## Implication

Bounds the kind of obstruction that could attack the problem. The library now
has the singularities/rational-point angle as well as the elementary modular
identity angle.
