# Xu, "Congruence Classes of Supporting the Erdős–Straus Conjecture I: Tame Solutions"

Source: arXiv:2605.23601 (22 May 2026), HTML: https://arxiv.org/html/2605.23601v1 (62 pages)
Full text: `research/sources/xu-tame-solutions-24m1.full.md`

## What it establishes (sourced, primary)

Attacks the open classes from the `n ≡ 1 mod 24` parametrisation: reduce to
primes `n = 24m + 1` (as Salez did). Define a **tame solution**: with
`n1 ≤ n2 ≤ n3`, one has `n1 = 6m + k` with `1 ≤ k ≤ 12m`; a solution is tame
if `n2, n3 | (6m+k)(24m+1)`. `n = 24m+1` is **wild** if it has no tame
solution.

- Computation: only **nine wild primes** among the 7185 primes `24m+1`,
  `m ≤ 30000`; and all 586 tame primes among the 591 primes with `m ≤ 2000`
  are covered by the congruence-class families derived in the paper.
- The paper derives tame solutions for `n = 24m+1` with m parameterised by
  congruence classes — i.e. family identities for sub-classes of the open
  classes, though the six mod-840 classes are not yet fully covered (nine wild
  primes remain even at m ≤ 30000, and no covering system is completed).

## Consequence

Confirms at a finer granularity that the open classes are pointwise solvable
(wild primes are rare) but that no full covering by tame-solution congruence
families is yet known. The tame/wild dichotomy is a new structural tool: a
counterexample would have to be wild AND outside every derived congruence
family. Useful framing for the run's covering-system ansatz search — it can
test families in the "tame" shape (n1 small, n2,n3 divisors of a quadratic) and
check coverage against the nine wild primes.

```claim
id: xu-tame-wild-dichotomy
statement: For primes n = 24m+1, a solution is tame when n2,n3 divide (6m+k)(24m+1) with n1=6m+k; only nine wild primes (no tame solution) exist among the 7185 primes with m ≤ 30000, and congruence-class families cover all 586 tame primes with m ≤ 2000.
hypotheses: n = 24m+1 prime, m ≤ 30000 (computational), tame definition as stated.
holds-here: true — the six open classes are contained in n ≡ 1 (mod 24).
status: sourced (arXiv:2605.23601, computational + partial families; not a complete proof).
bearing: families covering sub-classes of the open classes exist in the tame shape; the residual obstruction is the wild primes, which a new family must handle.
anchor: research/sources/xu-tame-solutions-24m1.full.md
```