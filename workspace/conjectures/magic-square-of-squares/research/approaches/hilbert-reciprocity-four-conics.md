# Approach: Hilbert reciprocity / four conics (REFUTED)

```approach
idea: Express each of the four AP conditions c ± d both squares as the splitting
of a quaternion algebra A_d = (c+d, c−d)_Q, compute the product of the four
algebras in the Brauer group, and apply Hilbert reciprocity to derive a
contradiction from local invariants.
```

## Verdict

**status: refuted.** The hoped-for contradiction cannot arise, for two independent
reasons, one of which makes the entire computation vacuous. This is a documented
dead end worth keeping so the next round does not propose it again.

## Why it dies (killed-by)

**Reason 1 — each A_d is trivially split by the hypothesis itself.** The AP
condition for difference d is that `c+d` and `c−d` are **both perfect squares**.
The Hilbert symbol has the property `(a², b)_p = 1` for every p (a square in any
entry makes the symbol 1), so `(c+d, c−d)_p = 1` at every place by the very
assumption that `c±d` are squares. Hence each quaternion algebra `A_d` is the
trivial element of Br(Q), its local invariant is 0 everywhere, and the product of
the four algebras is tautologically trivial. There are no nontrivial local
invariants to run Hilbert reciprocity against.

**Reason 2 — geometrically, all four points lie on the same conic, and local
solubility is everywhere.** Write `c = e²`. Each AP `c±d` both squares gives
`e² + d = A²`, `e² − d = B²`, so `A² + B² = 2e²`: every (A,B) lies on the **single
conic** `X² + Y² = 2e²`. A ternary quadratic form / conic over Q has a rational
point if and only if it has one over every completion (Hasse–Minkowski). The run
already establishes that the full system is locally solvable mod every prime
power (problem.md), so this conic is everywhere locally solvable and Hasse–
Minkowski permits (indeed, `X=Y=e` gives a real point; and the run's oracle has
found many `c±d`-both-square pairs, e.g. both realised AP differences in
Bremner's 7-square witness) a rational point. There is **no local-to-global
obstruction** at the level of a single conic over Q.

**Why the literature moves beyond this.** A conic (genus 0) cannot carry a
Brauer obstruction over Q; Brauer–Manin obstruction needs the **K3 surface**,
exactly what the `brauer-manin-k3-surface` approach targets. The heuristic
"additive relations might force a nontrivial product" contradicts the fact that
the four algebras are *individually* the zero element of Br(Q); a product of zeros
is zero no matter how the ADDITIVE relations are arranged.

## Precedent

- Quaternion-algebra / Hilbert-symbol framework (standard): any quaternion
  algebra (a,b) over Q splits iff it splits at every place; Hilbert reciprocity
  says the sum of local invariants is 0 (a tautology over Q — it is *always*
  true, so it cannot obstruct anything by itself). Sources:
  - Lam, "Introduction to Quadratic Forms over Fields", for Hilbert symbols;
  - Hasse–Minkowski theorem for ternary forms/conics over Q.
- The conclusion matches the run's own `Ruled out` entry: "Pure modular/local
  sieves cannot prove non-existence — the system is locally solvable mod every
  prime power." This candidate is exactly a local-solubility argument and dies on
  the same ground.

## What the refutation establishes

A proof of non-existence **cannot** come from Q-level quaternion algebras / a
single-conic obstruction: the AP conditions make every such algebra trivial and
local solubility is global. Any surviving obstruction must be attached to the
higher-dimensional variety itself (the K3 surface via Brauer–Manin), where
`Br(S)/Br(Q)` can be nonzero even though `Br(Q) = 0`.
