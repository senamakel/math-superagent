# Binyamini–Dor — uniform Petrov–Khovanskii, linear in deg ω

Full text: [[binyamini-dor-linear-abelian-integrals.full]]. arXiv:1108.1846;
Nonlinearity 25 (2012) 1931. Note: stored file is the arXiv **landing page**;
abstract-level claim only.

## What the source establishes (abstract level)

The number of zeros of Abelian integrals grows **at most linearly in the degree of
the 1-form ω**, uniformly. Petrov–Khovanskii proved this linearly-in-degω order
but existentially (no explicit constant); BNY gave an explicit bound of doubly
exponential shape; Binyamini–Dor combine the two: an **explicit** bound on the
number of zeros **linear in deg ω**: N(n,m) ≤ exp⁺(n²)·m + exp⁺(n²) (as recorded
in the claims ledger), for deg H ≤ n+1, deg ω ≤ m.

## What it implies here

- The best available explicit bound for the tangential problem is **linear in the
  form's degree with uniformly-exponential cost in H's degree** — better than the
  BNY double-exponential-in-degree shape for large forms and fixed Hamiltonian.
- Refines `h16-bny-abelian-bound`; same hypotheses (nonsingular ovals,
  non-conservative perturbation); does not touch H16.2 or graphic cyclicity.

```claim
id: h16-bd-abelian-linear-in-m
statement: The number of isolated real zeros of an Abelian integral I_{H,omega}
  (counted with multiplicity, summed over nonsingular ovals), deg H <= n+1,
  deg omega <= m, is at most exp^+(n^2)*m + exp^+(n^2): explicit and linear in
  deg omega.
hypotheses: nonsingular ovals; deg H, deg omega bounded; explicit constants
  constructive.
holds-here: yes (tangential problem only).
status: asserted
bearing: sharpens the Abelian-integral rung's explicit bound to linearity in
  deg omega; the uniform/tangential problem's best explicit two-parameter bound.
anchor: research/sources/binyamini-dor-linear-abelian-integrals.full.md
follows-from: h16-bny-abelian-bound
```