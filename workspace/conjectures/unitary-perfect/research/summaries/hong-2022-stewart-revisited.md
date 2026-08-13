# Hong (2022), *A refined Stewart-type lower bound* (arXiv:2204.01858)

Full text: [[hong-2022-stewart-revisited.full]] (readable OCR).

**Setup.** `P(m)` = largest prime factor of `m`. `Φ_n(x)` the `n`-th cyclotomic polynomial. `γ` an algebraic number of degree 2, not a root of unity, with `N γ = ±1`; `ω(γ)` counts the prime ideals of `K = Q(γ)` with `ν_p(γ) ≠ 0`; `D_K` the field discriminant.

**Results used by this run.**
- **Theorem 2.2** (uniform explicit Stewart bound): for `p0 = exp exp max{10^8, 2|D_K|}` and every prime ideal `p` of `K` with underlying prime `p ≥ p0`,
  `ν_p(γ^n − 1) ≤ p exp(−0.001 log p / log log p) · h(γ) · log^* n`.
- **Proposition 2.4**: if `p` is a *primitive* divisor of `u_n`, then `ν_p(Φ_n(γ)) ≥ 1` and `N p ≡ 1 (mod n)`, in particular `N p ≥ n + 1`. (This is the primitive-divisor structural fact the Maciejewski branch needs; cf. BHV.)

**Why relevant.** The run's divisor-level thread (`research/threads/divisor-level-phi4p.md`) uses the bound on the *non-primitive* part of `2^{2p} + 1` to say the primitive divisors must carry log-mass `≫ p`: `log(2^{2p}+1) = log 5 + log Φ_{4p}(2) ~ 2p log 2`, and the non-primitive contribution is `O(log(4p))` by Hong's valuation bound. That is the log-mass side of the exponential gap `2^{2p}/p` that blocks the density/Chebotarev route. So this source is what makes the "analytic target must be divisor-level" conclusion precise.

**Hypotheses checked.** Theorem 2.2 is stated for degree-2 `γ`, `N γ = ±1`, `n ≥ p0` (doubly-exponential in the discriminant — enormous but non-conditional). It applies to `γ = 2` (degree 1) only via the quadratic case; this run uses it as the Maciejewski paper does, as the source of "non-primitive part is `O(log n)`", and records it as asserted-by-source for this application rather than re-proved.

```claim
id: hong-stewart-nonprimitive-bound
statement: For degree-2 algebraic γ with Nγ = ±1 and n >= exp exp(...), the
  growth of primes dividing γ^n - 1 is governed by an explicit Stewart-type
  lower bound; the non-primitive part of 2^(2p)+1 is O(log(4p)) so the
  primitive divisors must carry log-mass comparable to 2p log 2.
hypotheses: gamma = 2 in the quadratic case (via Prop 2.4 primitive-divisor
  structure); n large; Nγ = ±1
holds-here: yes as the Maciejewski paper applies it (non-conditional, no GRH),
  establishing the log-mass / reciprocal-mass scale gap
status: asserted - the bound is proved in the source but its application to
  gamma=2 here follows the citing paper and is not independently re-verified
bearing: pins the exponential 2^(2p)/p gap that rules out density/Chebotarev as
  the scale for closing H_even; only a divisor-level (transference) statement
  about the prime support of Phi_{4p}(2) can close it
anchor: research/threads/divisor-level-phi4p.md
contradicts: (none)
answers: whether-scalegap-is-exponential
```
