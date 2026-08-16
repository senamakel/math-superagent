# Approach: Teissier polar invariants — the origin paper's own algebra

```approach
idea: Return to the origin of the conjecture instead of its projection. CA was
       born from Casas-Alvero's 2001 irreducibility criterion for plane curve
       germs, built on Teissier's polar invariants: the sequence of intersection
       multiplicities (contact numbers) of a germ with its successive polar
       curves. For the univariate object f the polar tower is exactly
       f, f', f'', …, f^{(n-1)}, so the CA hypothesis gcd(f, f^{(i)}) ≠ 1
       records only the NONVANISHING of the i-th contact number, and throws away
       its value. The proposal: promote the run's n−1 binary gcd conditions to
       the full polar-invariant sequence (the multiplicities of the gcds), and
       run the known classification — Teissier's inequalities among the polar
       invariants, Merle's theorem (which determines a one-branch germ from its
       semigroup and polar invariants), and Casas-Alvero's own irreducibility
       criterion — to force the sequence to be that of the cusp (x−a)^n.
mechanism: The run works in the resultant/coefficient projection, where the
       conditions are the R_i = Res(f, f^{(i)}) and every statement is an
       elimination. The native object is finer: the polar contact numbers
       κ_i = deg gcd(f, f^{(i)}) ∈ {1,…,n−i} form a length-(n−1) integer
       sequence that the current machinery never constrains as a *sequence* (it
       only records which κ_i are ≥ 1). Teissier's theory gives inequalities
       among the κ_i and the multiplicity structure (the "polar invariants and
       the semigroup" circle: Merle 1977, Casas-Alvero 2001). The bet is that a
       hypothetical non-pure-power f cannot carry a polar sequence satisfying
       all n−1 nonvanishing conditions AND the inequalities, except in the
       unibranch/cusp case κ_i = n−i for all i — i.e. the inequalities close the
       gap that the binary conditions leave open. The char-0 content is located
       by construction: contact numbers and the valuation-theoretic semigroup of
       a germ exist only in char 0 (they are analytic objects); over F_p the
       polar tower degenerates (H_i ≡ 0 for i ≥ p) and there is no valuation
       semigroup to constrain — the char-p witnesses live exactly in that
       absence.
status: proposed
first-step: (1) Read the origin paper's actual theorem from the held source
       (research/sources/casas-alvero_higher-order-polar-germs_2001.full.md,
       currently only summarized): state the irreducibility criterion verbatim
       and the polar-invariant sequence it uses. (2) tool_builder: for the char-p
       witnesses (x^{p+1}−x^p, p=2,3,5) and for the guard set, compute the full
       contact sequence κ_i = deg gcd(f, H_i f) exactly (sympy over Q and over
       F_p via lib.casas_alvero) and record how the sequence differs between a
       pure power, a char-p witness, and a generic f. (3) State the Teissier/
       Merle inequalities precisely (sourced, not recalled) and test whether a
       degree-20 counterexample's κ_i sequence, if nonempty, must violate one.
precedent: none. The origin paper appears in the library only as a citation and
       a summary line saying its singularity-theory content was declared out of
       scope; its algebraic content (the irreducibility criterion and the polar
       invariants) has never been read. This proposal deliberately re-opens that
       scoped-out corner with a specific justification: the polar multiplicities
       are the one invariant of the hypothesis the run has never used, and the
       origin criterion is the one named theorem the run has never stated.
charp-break: contact numbers are valuations of intersections of analytic
       branches; no such semigroup/invariant exists in positive characteristic.
       Concretely the polar tower over F_p is H_1,…,H_{p-1} followed by H_i ≡ 0,
       so the sequence κ_i is defined only up to p−1 and the inequalities that
       would force collapse are unstatable — the char-p falsehood is exactly the
       failure of the polar-invariant classification to extend to char p.
```

## What is known and what is speculative

- **Sourced (needs verbatim reading):** Casas-Alvero's irreducibility criterion
  (J. Algebra 240, 2001) and Teissier's polar invariants; Merle's theorem on
  the semigroup of a one-branch germ. These are named results but their exact
  hypotheses have not been stated in this run — the first step exists to fix that.
- **This run's own (binary, owned):** κ_i ≥ 1 ⟺ gcd(f, f^{(i)}) ≠ 1; pure power
  ⟺ κ_i = n−i for all i. The novelty here is treating (κ_1,…,κ_{n−1}) as one
  constrained sequence rather than n−1 separate predicates.
- **Speculative (the load-bearing bet, honest):** that Teissier's inequalities
  plus κ_i ≥ 1 force κ_i = n−i. Unproved, and the bridge "the univariate f is a
  genuine polar object of a germ" is itself the thing research must confirm —
  it is not asserted here.

## Why it is not a closed approach

`milnor-local-multiplicity` (refuted) was the Milnor number of the *CA ideal*
(R_1,…,R_{n−1}) — intersection theory on the coefficient scheme, already subsumed
by the Ghosh/Schaub–Spivakovsky complete-intersection machinery. This line is
intersection theory on the *germ and its polars* — the contact numbers κ_i of f
with its own derivative tower — a different invariant attached to a different
object, and the one the origin paper was actually built on.
