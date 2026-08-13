# Ventas, "A Ceiling Continued Fraction Approach to the Erdős–Straus Conjecture" (2026)

Source: https://arxiv.org/abs/2605.04551 (arXiv:2605.04551v1, 6 May 2026),
Andrés Ventas.
Full text: `research/sources/ventas-fct-heuristic-fulltext.full.md`
(His earlier paper with the same FCT framework is also in the library as
`research/sources/ventas-ceiling-continued-fraction.full.md`.)

## What it establishes (sourced, preprint)

**Framework.** FCT (Fraction Ceiling Transform): a rational `m/n ∈ (0,1]` is
represented via nested ceiling fractions. For ESC, the key is the **orbit of a
prime p**: integers `p + i` (i small, "sources") whose divisor structure
yields a three-term representation.

**Theorem 2.3 (Divisors of External Sources).** If `p + i` has a divisor
`d ≡ 3 (mod 4)` and `4i | (p + d)`, then `4/p` has a direct three-term
solution given by FCT(p, (p+d)/i).

**Other structure.**
- Primes p ≡ 3 (mod 4) have immediate two-term representations in this
  framework; p ≡ 1 (mod 4) is the hard case where the divisor condition
  applies.
- Theorem 2.5 (Grid of Congruences): a computational acceleration — the task
  reduces to covering primes by grids of congruences (a finite sieve), rather
  than per-prime factoring.
- Theorem 2.6 (Factors of External Sources) + Corollary 4.1: support the
  probabilistic analysis.
- **Heuristic result**: failure probability decays super-polynomially under a
  Cramér-type model; Borel–Cantelli gives *heuristic* evidence that
  counterexamples, if any, form a finite set (not a proof). Computational
  tests: 10⁹ primes around 10^17, 10^52 and 10⁷ primes around 10^131 — no
  counterexamples at small search depth.

## Relation to the library

- Same author's earlier paper (`ventas-ceiling-continued-fraction.full.md`)
  already in library; this is the published/preprint expansion.
- The divisor condition `d ≡ 3 (mod 4)` on `p+i` recalls **Obláth's** classical
  criterion (n+1 divisible by a prime ≡ 3 mod 4 ⇒ 4/n solvable) and
  **Mballa's** divisor-b≡3 (mod 4) symmetric solutions for n ≡ 1 (mod 4) —
  the same "shift by a 3-mod-4 divisor" mechanism surfaced three times
  independently.

## Consequences for this run

The FCT route is *not* a polynomial-identity family (it is a per-prime
divisor search over small shifts), so it is not blocked by Schinzel's
theorem — but it does not deliver a single identity either, which is this
run's deliverable. The useful extract: the condition `4i | (p+d)` with
`d | p+i`, d ≡ 3 mod 4 is a *finite-sieve* criterion; testing whether a
candidate family `p = 840k + r` with r an open class can satisfy it for
finitely many i is a finite check (per i) and so is a legitimate ansatz
space for a covering sub-family. Status: heuristic + computational, no
identity.

```claim
id: ventas-fct-external-source-criterion
statement: If p+i has a divisor d ≡ 3 (mod 4) with 4i | (p+d), then 4/p has a direct three-term solution (FCT construction); computational tests on 10⁹ primes near 10^17/10^52 and 10⁷ near 10^131 found no counterexamples at small depth, and a Cramér-model argument makes the failure probability super-polynomially small (heuristic).
hypotheses: p prime; i ≥ 1; divisor condition.
holds-here: true — gives a finite-sieve criterion for solvability that can be checked per small i for candidate families on the open classes.
status: asserted (preprint; heuristic + computational, not a proof).
bearing: one escape route from Schinzel's polynomial obstruction: per-i finite conditions instead of one polynomial identity; but no identity, so not the deliverable itself.
anchor: research/sources/ventas-fct-heuristic-fulltext.full.md
```