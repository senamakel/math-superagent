# Binyamini–Dor 2011 — A uniform version of the Petrov–Khovanskii theorem

Full text: [[binyamini-dor-uniform-petrov-khovanskii-2011.full]] (arXiv:1108.1846;
published Nonlinearity 25 (2012) 1931–1946). The held capture is the arXiv abstract
page; the published statement is also carried by
[[binyamini-dor-linear-abelian-integrals.full]] (landing page) and the claim
`h16-bd-abelian-linear-in-m`.

## What the source establishes (abstract verbatim)

An Abelian integral is the integral over the level curves of a Hamiltonian H of an
algebraic form ω. The infinitesimal Hilbert 16th problem asks for the number of zeros
of Abelian integrals in terms of deg H and deg ω. **Petrov–Khovanskii:** the number
grows at most linearly with deg ω, but their bound is purely existential.
**BNY:** an explicit bound growing doubly-exponentially with the degree. **This
paper:** combines the two techniques to obtain an **explicit bound on the number of
zeros growing linearly with deg ω**.

## What it lets this run conclude

- The best explicit two-parameter bound for the tangential problem is
  linear-in-degω with uniformly-exponential cost in deg H — the claim
  `h16-bd-abelian-linear-in-m` (N(n,m) ≤ exp⁺(n²)·m + exp⁺(n²)) records the form.
- Same hypotheses as BNY (nonsingular ovals, non-conservative perturbation); it
  refines `h16-bny-abelian-bound` but does not touch H16.2 or graphic cyclicity.
- For the run's `h16-sharp-abelian-named-family` goal, Malev–Novikov's explicit
  (7/4)n+9 for one named H is the per-family sharp-type bound; Binyamini–Dor is the
  uniform-across-H bound. The two are the upper bounds against which a new named-family
  count is checked (Test 2: a claimed sharp count below the true number is refuted by
  a certified example; a claimed uniform bound above B-D's is not an improvement).

```claim
id: h16-bd-2011-uniform-petrov-khovanskii
statement: Binyamini–Dor (arXiv:1108.1846, Nonlinearity 25 (2012) 1931): explicit bound on the number of zeros of Abelian integrals growing linearly with deg ω (uniform in deg H with exponential cost), combining Petrov–Khovanskii's linear-in-degω existential bound with BNY's explicit doubly-exponential bound. Held at abstract level; the exact constants are carried by claim h16-bd-abelian-linear-in-m (N(n,m) ≤ exp^+(n^2)·m + exp^+(n^2)).
hypotheses: polynomial Hamiltonian H, algebraic form ω, nonsingular ovals, non-conservative perturbation (tangential problem).
holds-here: yes — the tangential problem's best explicit two-parameter bound; not H16.2.
status: asserted
evidence: arXiv abstract page held (research/sources/binyamini-dor-uniform-petrov-khovanskii-2011.full.md); claim h16-bd-abelian-linear-in-m.
falsifier: a counterexample with more zeros than the bound, or a correction to the published constants.
sources: https://doi.org/10.48550/arXiv.1108.1846
anchor: research/sources/binyamini-dor-uniform-petrov-khovanskii-2011.full.md
follows-from: h16-bny-abelian-bound
answers:
```
