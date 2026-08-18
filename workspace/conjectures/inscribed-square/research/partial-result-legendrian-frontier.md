# Partial result — exact formalization and the Legendrian-lift frontier

## Chosen line of attack

This run chose **configuration-space/topological methods, formalized in Lean,
with exact computation only as an oracle**. The general Toeplitz conjecture is
not a numerical optimization problem: a finite search over candidate points
cannot address an arbitrary continuous Jordan curve. The structural reduction
used here is the modern Legendrian-lift formulation of the configuration-space
argument (Asano–Ike), because the library shows that it covers every
rectifiable curve and isolates one sharp missing hypothesis for the general
case.

## What is formally pinned down

`code/lean/Lib/Statement.lean` gives a kernel-elaborated type for the conjecture.
It represents the circle as `AddCircle (1 : ℝ)` and the plane as
`EuclideanSpace ℝ (Fin 2)`. A Jordan curve is a continuous injective map. The
square predicate is stated by the exact diagonal conditions:

- common diagonal midpoint;
- perpendicular diagonals;
- equal diagonal lengths;
- four parameters in cyclic order and pairwise distinct.

`lean_check` compiled the file. Its only unproved item is the intended theorem
body `by sorry`; `#print axioms` reports
`[propext, sorryAx, Classical.choice, Quot.sound]`. This is a formal statement,
not a proof of the conjecture.

`code/lean/Lib/Stromquist.lean` independently elaborates the cited theorem that
every locally monotone Jordan curve inscribes a square. The locally monotone
condition is written on real lifts because `AddCircle` has no order. The theorem
is deliberately an axiom under `namespace Cited`, with a docstring citing
Stromquist (1989), Mathematika 36, 187–197, and Matschke's 2014 survey. It
compiled with no `sorry`; its axiom report is `conditional` and includes
`Cited.stromquist_square_peg`.

The sanity file `code/lean/SanityCyclic.lean` also passed without `sorry`,
checking that the cyclic-order predicate forces the parameters to be distinct.
Full compiler records are in `code/out/lean/` and the claim descriptions are in
`code/out/lean-formalisation.md`.

## The structural frontier

Asano–Ike Theorem 1.1 (arXiv:2412.21057v3, 5 Jan 2026; still an arXiv preprint,
not peer-reviewed according to the status checks recorded in
`research/sources/asano-ike-2024-status.md`) says:

> If a Jordan curve `c` is the uniform limit of smooth Jordan curves `c_n` and
the primitives `f_n` of `(c_n ∘ e)^* λ` converge uniformly on compact subsets
to a continuous `f`, then `c` inscribes a θ-rectangle for every `θ ∈ (0,π)`.

At `θ = π/2` this is a square. The paper proves that every rectifiable Jordan
curve satisfies the lift condition. Thus the remaining exact question is:

> Does every continuous Jordan curve admit such a continuous Legendrian lift?

If yes, the cited theorem would settle Toeplitz's conjecture. If no, a
non-rectifiable Jordan curve without a lift is a precise obstruction to this
method. No checked source in this workspace proves either alternative, and no
checked source claims a counterexample to Toeplitz's conjecture.

A minimal counterexample, if one exists, must therefore be non-rectifiable,
outside the known open-dense/symmetry/two-graph classes, and must defeat the
nondegeneracy mechanism: boundary winding, exclusion of degenerate zeros, or a
positive side-length bound (shrinkout).

## Exact computational evidence

The valid oracle is `code/brute.py`, an intentionally exponential small-instance
oracle using exact integer/rational squared distances. It was executed and
reproduced:

- unit square → one square, indices `(0,1,2,3)`;
- 2×1 rectangle → no square;
- diamond (rotated square) → one square, indices `(0,1,2,3)`.

A second independent exact run is `code/square_peg/verify_symmetric.py`, with
output in `code/out/verify_symmetric.txt`. It imports the exact boundary solver
without path hacks, uses `Fraction`, checks polygon simplicity by exact segment
intersection, and agrees with the vertex-only oracle on the three sanity cases.
It additionally found the exact square
`((0,0),(0,2),(2,2),(2,0))` on the line-symmetric hexagon
`[(0,0),(2,0),(3,1),(2,2),(0,2),(-1,1)]`, and found no square on the selected
irregular nonsymmetric pentagon. The symmetric result is only an instance of
the published Nielsen–Wright symmetry theorem; it is not new evidence for the
general conjecture.

These computations are checks of exact polygonal instances, not approximate
witnesses for arbitrary curves and not a full-size search. The attempted ellipse
reproduction was rejected and documented in
`research/approaches/ellipse-oracle-invalid.md`: its rational angle formula was
wrong, so no ellipse computation is claimed.

## Honest remaining gap

The run did not prove the continuous Legendrian-lift frontier, nor the full
Toeplitz conjecture. The next mathematically meaningful move is to formalize
that lift predicate and the implication from it to the square theorem, then
attack whether the class is strictly larger than rectifiable. A proposed
extension to arbitrary continuous unions of graphs was not trusted because the
global periodic parametrization and primitive convergence were not proved here.
