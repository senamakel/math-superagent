# Polstra, *Convex Hulls and the Casas-Alvero Conjecture for the Complex Plane* (2012)

Rose-Hulman Undergraduate Mathematics Journal 13(1), art. 2 (2012). Thomas
Polstra (Georgia State University), faculty sponsor Florian Enescu.

**Full text HELD.** `research/sources/polstra2012_convex-hulls-casas-alvero.full.md`
(24,778 bytes, 485 lines). Landing page:
https://scholar.rose-hulman.edu/rhumj/vol13/iss1/2; PDF endpoint
viewcontent.cgi?article=1090&context=rhumj (fetched via the download tool).

## What this source is

A peer-reviewed undergraduate-journal paper giving an **equivalent reformulation
of CA over C using the convex hull of the roots**, plus special cases proved.

## What it establishes (from the held full text)

- **Thm 3.1** (the load-bearing result, lines ~225-258): If f shares a root with
  each of its n-1 derivatives, then **each root of f is a vertex of its convex
  hull C_f IFF f has a single root of multiplicity n.** Proof: nested hulls
  C_{f^(n-1)} ⊆ ... ⊆ C_{f'} ⊆ C_f (Gauss–Lucas + Cor 2.3); the (n-1)-st
  derivative has one root z0 which f shares; z0 ∈ C_f and being a vertex (Prop
  2.7), it is a vertex of C_f' and hence a root of f' (Prop 2.8); iterating, z0
  is a root of every derivative, so f has only the root z0 of multiplicity n.
  **Contrapositive (usable form): a counterexample to CA over C must have a root
  that is NOT a vertex of C_f.** This is the geometric collapse step the run's
  root-difference-coloring approach rests on, and it is char-0-only (convex
  hull / Gauss–Lucas over C) — exactly the kind of step that must break in char p.
- **Cor 3.5**: if the roots of f lie on the boundary of a strictly convex set
  and f is CA, then f has a single root of multiplicity n.
- **Real-rooted case (Section 4)**: an equivalent condition to CA for real-rooted
  polynomials, via Vieta's relations and multiplicity patterns (cf. Yakubovich).

## Evidence class / falsifier

- Thm 3.1, Cor 3.5: **asserted-by-source (peer-reviewed journal), full proof held
  and read.** Hypotheses: char 0, analytic over C via Gauss–Lucas.
- Falsifier (for the run's use of it): if the convex-hull reformulation survived
  in char p, it could not be the char-0-only break step. It does not: convex
  hull / Gauss–Lucas have no F_p analogue (already recorded in the
  root-difference-coloring thread).
