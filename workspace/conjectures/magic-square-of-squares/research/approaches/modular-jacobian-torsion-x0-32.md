```approach
id: modular-jacobian-torsion-x0-32
idea: The Robertson elliptic curve E: y² = x(x²−e⁴) has CM by Z[i] and is
  claimed to be the e-twist of X₀(32) = E₁: y² = x³ − x (genus 1, conductor
  32).  Its Jacobian J₀(32)(Q) = E₁(Q) has rank 0 (1 is not a congruent
  number) and torsion Z/2 × Z/2 (the cusps).  The three AP-linked doubled
  points 2P₁, 2P₂, 2P₃ of the MSS map to a divisor class in J₀(32)(Q); since
  that group is finite torsion, an MSS would force a non-cuspidal class into
  the cuspidal torsion — contradiction.
mechanism: Rational point P ∈ E_e(Q) with x(P) = a² (square) gives a
  rational point on a quadratic twist of a covering of X₀(32).  The AP
  condition on the three doubled points is intended to land in J₀(32)(Q)
  = Z/2 × Z/2, whose only rational classes are cuspidal torsion, forcing the
  three points to be cusps → degenerate squares → contradiction with
  distinctness.
status: refuted
killed-by: E_e: y² = x³ − e⁴x is the TRIVIAL twist — it is Q-ISOMORPHIC to
  y² = x³ − x (since e⁴ is a square-class 1), so it has rank 0 ONLY for this
  degenerate curve, and it is NOT the Robertson curve.  The actual Robertson
  curve is E: y² = x³ − c²x, where c is the ANTIDIAGONAL half-difference —
  c = 138600 for the Bremner witness, unrelated to e = 425 (this run's
  robertson-elliptic-reduction).  The squarefree twist class of c = 138600
  is 154, NOT 1: the real curve is a NONTRIVIAL quadratic twist of X₀(32)
  = y²=x³−x, and it has RANK 2, not rank 0 (computed this run).  Rational
  points of a nontrivial quadratic twist do NOT inject into J₀(32)(Q)=E₁(Q).
  There is no map from the MSS data to J₀(32)(Q), so "rational class is
  torsion" never engages.  Even in the irrelevant trivial-twist (e=1) case,
  the 2-torsion of y²=x³−x has x ∈ {0,±1} (three distinct values, no AP of
  length 3 with a free common difference that would force degeneracy — the
  "cannot all be cusps" step is unproved and in fact consistent, since
  torsion rational points exist).
first-step: (moot.)  The candidate's central computation — "the image of the
  three AP points in J₀(32)(Q)" — is undefined because there is no such map:
  the points live on a nontrivial twist whose Mordell–Weil group is not the
  base curve's.  The approach's own bookkeeping is self-inconsistent (writes
  E_e: y² = x(x²−e⁴) and calls it the e-twist of X₀(32), but that is the
  trivial Q-isomorphism class).
precedent: The Robertson curve is the quadratic TWIST family E: y²=x(x²−c²)
  of X₀(32)=y²=x³−x; rational points of a twist do not inject into the base
  Jacobian (standard twist theory; this round's search of
  twisted-Hasse-Weil / Selmer-of-twists literature confirms twist ranks are
  governed by the twist class, not the base rank).  The primitive e=1
  degenerate case (rank 0, torsion Z/2×Z/2, x∈{0,±1}) is exactly the
  freys-curve-four-q-isogenies ground already closed by
  freys-4-isogeny-misidentifies-doubling (this run).  Bremner's witness
  curve y²=x(x²−138600²) has rank 2 (this run, robertson_reduction and
  tool-builder rank computation) — a concrete counterexample to the
  "rank 0, only torsion" premise for every nondegenerate c.
speculation: (superseded.)  The key insight in the write-up — "for primitive
  e the curve has rank 0 so there are no non-torsion points" — applies only
  to the trivial Q-isomorphism class, on which an MSS's Robertson points do
  not live.  The moment c is a genuine (nontrivial twist-class) anti-diagonal
  half-difference — and the witness shows this is the only case that occurs
  — the Mordell–Weil group is a positive-rank twist group and the torsion
  trap is empty.
```

# Literature check: modular Jacobian X₀(32) / torsion trap (REFUTED)

Author: research specialist. Date: this round.

## What the reformulation is actually called

The candidate wants to use the **Mordell–Weil group of the Jacobian of the modular
curve X₀(32)** (= E₁: y² = x³ − x, genus 1, conductor 32, rank 0 because 1 is not a
congruent number, torsion Z/2 × Z/2 from the cusps) to trap the Robertson/MSS
configuration. This is a "rational-points of a quadratic twist inject into the base
Jacobian, which is finite torsion" argument.

## The precise facts, and whether they hold here

- `E: y² = x³ − c²x` is the quadratic twist of `E₁: y² = x³ − x` by the squarefree
  class of c. True.
- `J₀(32)(Q) = E₁(Q)` has rank 0 and torsion Z/2×Z/2. True (Fermat/Euler: 1 is not a
  congruent number; rank-0 twist literature: Feng–Xiong 2004, "On elliptic curves
  y²=x³−n²x with rank zero", J. Number Theory).
- **Falls apart at the twist.** A point of the *twist* `E: y²=x³−c²x` is a Q-point of a
  *different* curve. It does not live on `E₁` and does not map to `J₀(32)(Q)`. The
  Mordell–Weil group of a nontrivial quadratic twist is governed by the twist class and
  is generically NOT equal to (indeed is often disjoint from) the base curve's rational
  points. There is no induced map MSS-data → J₀(32)(Q), so "every rational class is
  torsion, hence the MSS class is torsion, hence cuspidal" never even starts.

## The concrete counterexample (this run's own computation)

The Robertson curve for the Bremner 7-square witness is `E: y² = x³ − c²x` with `c =
138600` (the anti-diagonal half-difference; the centre `e = 425` is NOT c). The squarefree
class of 138600 is 154, a nontrivial twist (154 ∉ squares). This run computed that
`E: y² = x³ − 138600²x` has **rank 2**, torsion 4, and contains the doubled points with
x(2P₁)=139129, x(2P₂)=180625 (two of the three AP terms realised) — a positive-rank
twist carrying the actual MSS-like configuration. So the premise "rank 0, only torsion,
no non-torsion points" is false for every genuine (nontrivial twist class) c.

## Who has applied it to this problem?

Nobody, and the modular/4-isogeny ground it stands on is already closed: the
`freys-curve-four-q-isogenies` approach (the same "map the MSS to X₀(4)-data / modular
jacobian torsion" family) was refuted by this run's `freys-4-isogeny-misidentifies-doubling`.
The candidate's own `X₀(4)² → X₀(32)` degeneracy map was lifted from that family; the
torsion trap does not add a computational handle because the relevant group is a twist's,
not the base's.

## What it would buy

Nothing obtainable. The essential fact — that a nontrivial quadratic twist of a rank-0
elliptic curve can (and for the actual MSS curves does) have positive rank — kills the
only lever. And by the existence of an MSS over Q(√3,√133), any "the configuration
forces a torsion class" argument that fired over Q would also fire over the extension,
where the configuration genuinely exists, so it would prove too much.

## Verdict

**Refuted.** The candidate confuses the trivial twist (y²=x³−e⁴x, Q-isomorphic to
E₁, rank 0) with the actual Robertson curve (y²=x³−c²x, c = anti-diagonal half-difference,
nontrivial twist class 154, rank 2 for the witness). Rational points of a nontrivial
quadratic twist do not inject into J₀(32)(Q), so the "rank 0, only torsion" trap never
engages for any nondegenerate MSS; and the degenerate primitive case it does engage for
is not the curve an MSS's points live on.
