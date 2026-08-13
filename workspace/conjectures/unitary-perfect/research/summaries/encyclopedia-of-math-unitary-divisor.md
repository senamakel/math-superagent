# Encyclopedia of Mathematics — *Unitary divisor* (informational)

Full text: [[encyclopedia-of-math-unitary-divisor.full]].

**Definitions and facts:**
- A unitary divisor `d` of `n` satisfies `gcd(d, n/d) = 1`; equivalently every prime factor of `d` appears with the same exponent in `d` as in `n`.
- `σ*(n)` (sum of unitary divisors) is multiplicative; `σ_k^*(n)` likewise. Dirichlet series `Σ σ_k^*(n) n^{−s} = ζ(s)ζ(s−k)/ζ(2s−k)`.
- The number of unitary divisors of `n` is `2^{ω(n)}`.
- A *unitary perfect* (unitarily perfect) number is `n` with `σ*(n) = 2n`. Every unitary perfect number is even. It is unknown whether there are infinitely many.

**Bearing.** Confirms the definitional base (multiplicative `σ*(p^e) = p^e + 1`, `2^{ω}` divisor count) used everywhere; adds nothing new beyond what Subbarao–Warren and the run's own notes establish. Not load-bearing as a source of a new result.

```claim
id: emath-unitary-divisor-defs
statement: A unitary perfect number is n with sigma*(n) = 2n; sigma* is
  multiplicative with sigma*(p^e) = p^e + 1; the number of unitary divisors is
  2^omega(n); every unitary perfect number is even; infinitude (even existence
  of a sixth) is open.
hypotheses: standard definitions
holds-here: yes (matches the oracle definition in GOAL.md and the five
  witnesses)
status: asserted (encyclopedia entry)
bearing: definitional consistency only; no new bound
contradicts: (none)
```
