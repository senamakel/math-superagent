# Adoption note — lcm-monomial-algebra

Status: ADOPTED (inventor decision round). Replacement for the `grounded` status
in `research/approaches/lcm-monomial-algebra.md`, which now reads `adopted`.

Why it beat the others:
- It is the ONLY candidate research could ground to a named theorem with
  hypotheses that hold here: Gasharov–Peeva–Welker (Math. Res. Lett. 6, 1999),
  lcm-lattice determines Betti numbers / minimal free resolution. Under the
  monomial bijection A ↦ x^A, a union-closed family with ∅,V is exactly an
  lcm-closed monomial set, so the lcm-lattice of I_F IS the ∪-structure. No
  source applies GPW/Betti to the UC abundance question, so the forcing step is
  genuinely open.
- It is a different algebra from the adopted Möbius semigroup algebra C[L,∨]:
  it works in the quotient ring k[x]/I_F and its free resolution, whose
  invariants have never been tied to abundance.
- polynomial-method-nullstellensatz is refuted (DeFranco's iff-Boolean-polynomial
  prior art that stops short; ITCS hardness of testing union-closedness).
- fkq-correlation is refuted (Ahlswede–Daykin's conclusion is an aggregate
  Σ-product / correlation bound, no per-element forcing; its UC application
  collapses to the refuted overlap method, Ellis).

Research's one technical correction folded into the first step: δ(i) (the
per-variable divisibility count = abundance) is MULTIGRADED data and lives in
the multigraded Betti table of S/I_F, NOT as a coefficient of the single-variable
Hilbert series.

First step (a tool_builder can start today):
1. With the canonical oracle (code/lib/uc.py), enumerate UC families on n ≤ 5
   (∅, V ∈ F).
2. Write I_F and its Alexander dual I_F^∨.
3. Compute the MULTIGRADED Betti table β_{i,α}(S/I_F) by exact Gröbner/linear
   algebra (sympy, degree reverse-lex, n ≤ 4 first).
4. Test whether max_i δ(i) − m/2 and each variable's divisibility count is
   visible as a multigraded Betti number or as homology of an open interval of
   the lcm-lattice.
5. Run the three negative controls: 2^[n] → every δ(i) = m/2 exactly with
   Boolean lcm-lattice; a non-union-closed family breaks lcm-closure so I_F's
   resolution is NOT pinned by the family's ∪-structure; finiteness via m ≤ 2^n.
6. If no multigraded Betti invariant tracks abundance for n ≤ 5, say so — that
   itself is a negative result bounding this route.

Persistence note: `remember_memory` is unavailable (server down all pass, per
research). The decision lives on disk (this note + the approach file + the
re-derived ledger + the board post). Store to Cognee when the server recovers.
