# Écalle 1993 — Six Lectures on transseries, analysable functions, and the constructive proof of Dulac's conjecture

Full text: [[ecalle-1993-six-lectures-transseries-dulac.full]] (in: The Bifurcation
Theory of Differential Equations, NATO ASI Series C vol 408, Springer 1993, DOI
10.1007/978-94-015-8238-4_3). This is Écalle's own English survey of the 1992 Hermann
book's proof machinery — the accessible stand-in for the 1992 book (print-only, 404 on
archive.org).

## What the source establishes (held full text, abstract verbatim)

**Subject:** a rapid, self-contained introduction to the resummation methods of
**resurgence, compensation, and acceleration**, with three applications of decreasing
generality:
- **(A)** analytic singularities and local objects — singular analytic vector fields
  and local diffeomorphisms of ℂ*;
- **(B)** the construction of the fields of **transseries and analysable germs** — the
  broadest extension of the ring of real-analytic germs closed under all common
  operations including integration, whose elements are "wholly formalizable"
  (reducible to a properly structured set of real coefficients);
- **(C)** the proof of the **non-accumulation of limit cycles** for real-analytic,
  first-order differential equations (Dulac's conjecture).

**The red thread — the Analytic Principle:** "local entities arising naturally out of
a local analytic situation can be entirely 'formalized'." This is the exact statement
of what the smooth test (problem.md Test 1) requires: within the analysable class, the
formal transseries determines the map; a flat C^∞ germ is invisible to the transseries,
so the principle fails for C^∞ fields.

**Held capture status:** the Springer capture has the abstract, preview, and full
reference list; the chapter body is paywalled. The abstract-level content above is
verbatim; the deeper machinery (median accelero-summation, compensation) is carried at
the architecture level by claim `ecalle-1992-analysable-proof-architecture`.

## What it lets this run conclude

- The Écalle route's core is the **Analytic Principle**: formalisability within the
  analysable class is what makes the return map determined by its expansion. Any
  candidate finiteness argument for a degenerate graphic must either place its
  displacement germ inside an analysable/cohesive class or name the analogous
  quasianalyticity step; a formal-expansion argument without such a class is Dulac's
  1923 error (claim `h16-dulac-proof-contested` documents the Ilyashenko-side
  contention at the same step).
- It is the counterpart to Ilyashenko's almost-regular/cochain machinery
  (`h16-ilyashenko-1990-finiteness-theorems`): two independent proofs of the same
  pointwise theorem, both non-uniform.

```claim
id: ecalle-1993-analysable-germs-analytic-principle
statement: Écalle 1993 (NATO ASI C 408, survey of the 1992 Hermann book): the fields of transseries and analysable germs form the broadest extension of real-analytic germs closed under common operations including integration, with elements wholly formalizable; the proof of non-accumulation of limit cycles for real-analytic first-order equations (Dulac's conjecture) rests on the Analytic Principle (local entities from a local analytic situation are entirely formalizable). The held capture is abstract-level (Springer paywall on the body).
hypotheses: individual real-analytic planar vector fields (Dulac's problem); analysable/cohesive function class.
holds-here: yes — pointwise-finiteness pillar (Écalle route); gives no uniform bound.
status: asserted
evidence: held Springer capture with abstract verbatim (research/sources/ecalle-1993-six-lectures-transseries-dulac.full.md lines 20-27); claim ecalle-1992-analysable-proof-architecture for the architecture level.
falsifier: obtaining the chapter body and finding the proof incomplete in a load-bearing step (analogous to the Ilyashenko-side Yeung contention).
sources: https://doi.org/10.1007/978-94-015-8238-4_3
anchor: research/sources/ecalle-1993-six-lectures-transseries-dulac.full.md
follows-from: h16-dulac-finiteness-theorem
answers:
```
