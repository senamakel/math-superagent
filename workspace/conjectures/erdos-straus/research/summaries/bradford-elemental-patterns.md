# Bradford, "Elemental Patterns from the Erdős–Straus Conjecture"

Source: arXiv:2403.16047 (24 Mar 2024), HTML: https://arxiv.org/html/2403.16047v1
Full text: `research/sources/bradford-elemental-patterns.full.md`

## What it establishes (sourced, primary)

A **two-variable reduction** of the Erdős–Straus conjecture. For a prime `p`,
any solution `x ≤ y ≤ z` of `4/p = 1/x + 1/y + 1/z` is Type I (`p ∤ y`) or
Type II (`p | y`). Bradford proves:

- **Proposition 1 (Type I sufficient)**: if `⌈p/4⌉ ≤ x ≤ ⌈p/2⌉` and `d | x²`
  with `d ≡ −px mod (4x−p)`, then with
  `y = (px+d)/(4x−p)`, `z = p(x + px²/d)/(4x−p)`, we get a Type I solution.
- **Proposition 2 (Type II sufficient)**: if in addition `d ≤ x` and
  `d ≡ −x mod (4x−p)`, then with `y = p(x+d)/(4x−p)`,
  `z = p(x + x²/d)/(4x−p)`, we get a Type II solution.
- **Propositions 3–4 (necessary)**: conversely, every Type I/II solution has
  this form for some divisor `d | x²` of the stated congruence shapes. So the
  conjecture is **equivalent** to: for every prime p there is an x in
  `[⌈p/4⌉, ⌈p/2⌉]` and a divisor d | x² meeting one of two congruences mod
  `4x−p` (Conjecture 1). This is a one-dimensional reduction: solve pairs
  `(x, d)` instead of triples.
- Explicit check: for primes `p ≠ 2` with `p ≢ 1 mod 24`, a Type I solution
  exists already at `k=0`; for `p ≡ 3 mod 4`, `k` divides `⌈p/4⌉`.
- Table 1/2 list, for primes < 100, the k-offsets (`x = ⌈p/4⌉ + k`) that yield
  Type I / Type II solutions.

## Why the run needs it

This is the modern reduction that the 2025/2026 computaional papers (Mihnea–
Dumitru 2025, Bello–Hernández et al. 2026) build on. The parametrisation can
be verified locally: given x and d, `(x, y, z)` is an exact solution. It is
also the natural framing for an ansatz search — instead of searching triples,
search pairs `(x(k), d(k))` over the class `n = p = 840k+1`, with `d(k) | x(k)²`
and the congruence mod `4x(k)−p` holding identically in k (which would require
`4x(k)−p | p·x(k)+d(k)` as polynomials — but note Schinzel Theorem 1 says a
fixed-shape polynomial identity covering the class cannot exist, so any
polynomial family in k would have to fail integrality at the squares or
otherwise leave the Z[x] shape).

```claim
id: bradford-two-variable-reduction
statement: For prime p, the Erdős–Straus equation 4/p = 1/x+1/y+1/z has a solution iff there is x with ⌈p/4⌉ ≤ x ≤ ⌈p/2⌉ and d | x² with (Type I) d ≡ −px mod (4x−p), or (Type II) d ≤ x and d ≡ −x mod (4x−p); the map from (x,d) to (x,y,z) is explicit and bijective onto Type I/II solutions.
hypotheses: p prime; Type I/II classification (Elsholtz–Tao type-definition).
holds-here: true — the open classes are primes p ≡ 1 (mod 840), so p odd prime; Type I/II covers all solutions.
status: sourced (Bradford 2024, Propositions 1–4 with proofs; corroborated by Mihnea–Dumitru 2025 use of the same conditions).
bearing: the run's construction problem becomes: find polynomial families x(k), d(k) meeting one of the two congruences identically over n=840k+1 — engaging directly with Schinzel's obstruction.
anchor: research/sources/bradford-elemental-patterns.full.md
```