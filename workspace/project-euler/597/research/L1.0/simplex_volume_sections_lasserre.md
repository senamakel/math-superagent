# Closed-form simplex volume sections — Lasserre (L0.1)

<!-- source: https://hal.science/hal-01095071/document | Lasserre, Optim. Lett. 9(7):1263-1269 (2015) -->
Reader note, one level up from the digest
[[pdf:research/L0.1/simplex_volume_sections_lasserre.md]]; full PDF at the URL.

## What it contributes
Closed-form (piecewise polynomial, exact rational) volume of a simplex section
Δ∩{a^T x ≤ t} by Laplace transform — the last, previously-missing step that makes
the run's simplex-volume view of p(n,L) ([[dirichlet_distribution_wikipedia.full]])
actually computable without quadrature or enumeration.

## Link to the rest
Works with the sealed machinery of [[L0.0]]: the parity region of p(n,L) is a
finite union of sub-simplices cut by linear inequalities; each cut is a Lasserre
section, so the whole probability is a finite exact rational — the route to the
10-dp target p(13,1800) that MC cannot reach.
