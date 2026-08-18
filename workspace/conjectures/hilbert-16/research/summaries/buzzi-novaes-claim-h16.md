# Buzzi–Novaes 2024 — refutation of a claimed closed form for H(n)

Full text: [[buzzi-novaes-claim-h16.full]]. arXiv:2411.09594.

## What the source establishes

- **Best-known lower bound for the growth of H(n):** from Christopher–Lloyd 1995,
  refined by Han–Li 2012:
  **liminf H(n)/((n+2)² log(n+2)) ≥ 1/(2 log 2)**.
  So H(n) grows at least as fast as (n+2)² log(n+2)/(2 log 2).
- **Consequence:** H(n) cannot be bounded above by ANY quadratic polynomial in n.
- **Refutation:** the Entropy (2024) paper of da Silva–Vieira–Leonel claiming the
  closed form **H(n) = 2(n−1)(4(n−1)−2)** is false. 4 reasons:
  (a) it is quadratic in n, contradicting the n²log n lower bound;
  (b) an explicit sequence (Li–Chan–Chung 2002, correcting Christopher–Lloyd)
      gives H(2k−1) ≥ S_k = 4^{k−1}(k − 13/6) + (2k−1)/3, which exceeds the claimed
      form for k ≥ 35;
  (c) their "limit cycle via information geometry" definition (assertion A: a
      periodic state where the Fisher-information scalar curvature R is positive
      near equilibria and |R| is singular) is neither necessary nor sufficient for
      limit cycles — explicit polynomial systems: a cubic with a unique limit
      cycle where R(0,0)=−1<0 (A fails); a center with no limit cycle where
      (A) holds for every periodic orbit; a system with 2 nested limit cycles
      where R(0,0)=−80/289<0.
- So **counting singularities of |R| does not bound the number of limit cycles.**

## What it lets this run conclude

- It **confirms problem.md's** recalled n²log n growth (the Han–Li refinement is
  the precise asymptotic; the constant 1/(2 log 2) on (n+2)²log(n+2)).
- It **corrects** the existing `h16-lower-bounds` claim prose in
  research/notes/claims.md, which had inverted the direction ("best confirmed
  asymptotic is the (n+2)²/ln(n+2) bound, which contradicts any quadratic upper
  bound"). The full text makes the direction unambiguous: H(n) is ordered
  n² log n, unbounded above by any quadratic.
- It is the run's **test-2 reference**: any claimed upper bound on H(n) (or on a
  degree-n family) below order n² log n is refuted before examination.
- It does not help H(2) < ∞ directly: n²log n is about large n; the bound is
  silent for n=2 (H(2)≥4 is the only n=2 lower bound). The quadratic closed form
  was irrelevant to H(2) anyway.

```claim
id: h16-hn-lower-bound-asymptotic
statement: The Hilbert number H(n) grows at least as fast as
  (n+2)^2 log(n+2)/(2 log 2); equivalently liminf H(n)/((n+2)^2 log(n+2)) >=
  1/(2 log 2); so H(n) is not bounded above by any quadratic polynomial in n.
hypotheses: none beyond degree; Christopher-Lloyd 1995, Han-Li 2012 refinement.
holds-here: yes
status: asserted
bearing: Test-2 reference; refutes any polynomial upper bound of order < n^2 log n,
  including the Entropy-2024 quadratic closed form.
anchor: research/sources/buzzi-novaes-claim-h16.full.md
contradicts:
follows-from:
```

```claim
id: h16-geometry-limitcycle-defn-refuted
statement: The "information-geometry" definition of a limit cycle (count of
  singularities of |R| for a Fisher-information scalar curvature) is neither
  necessary nor sufficient for limit cycles, so it cannot bound H(n).
hypotheses: none -- demonstrated by explicit polynomial systems.
holds-here: yes
status: asserted
bearing: rules out that approach to H(n); a recorded dead end so the next attempt
  does not reuse it.
anchor: research/sources/buzzi-novaes-claim-h16.full.md
```
