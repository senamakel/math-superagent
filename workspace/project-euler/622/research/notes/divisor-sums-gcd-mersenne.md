# Divisor-sum rungs: clean sourceable statements

Supplies the sourcing for blueprint rungs `G-divisor-sums` (sigma/tau
multiplicative, prime-power formulas) and `G-gcd-mersenne`.

## sigma-prime-power formula

Mathar, *Survey of Dirichlet Series of Multiplicative Arithmetic Functions*
(`research/sources/mathar-dirichlet-multiplicative-functions.full.md`),
eq. (3.17) at line ~679:

```
σ_k(p^e) = (p^{k(e+1)} - 1) / (p^k - 1),   k > 0
σ_0(p^e) = e + 1
```

Setting k = 1 gives the classic
σ(p^e) = 1 + p + ... + p^e = (p^{e+1} - 1)/(p - 1).
Setting k = 0 gives τ(p^e) = e + 1 (divisor count). Both are clean,
citable statements, derived as geometric sums (Mathar cites [17, p. 239]).

The multiplicativity of σ over coprime arguments (σ(mn) = σ(m)σ(n) for
gcd(m,n)=1) is stated in the TCD course notes section 5.6 (sigma is
multiplicative, `research/sources/tcd-crt-orders-course-notes.full.md`)
and in EoM Sum of divisors
(`research/sources/eom-sum-of-divisors.full.md` line ~59).

## gcd-Mersenne

Wolfram MathWorld (GCD page, `research/sources/wolfram-gcd-mersenne.full.md`
line 243): GCD[2^m - 1, 2^n - 1] = 2^GCD[m,n] - 1 for positive integers
m, n. This is the clean form the `G-gcd-mersenne` rung needs.

## Claim

```claim
id: divisor-sums-gcd-mersenne-sourceable
statement: For a prime p and integer k >= 0, σ_k(p^e) = (p^{k(e+1)}-1)/(p^k-1)
  when k > 0 and σ_0(p^e) = e+1; hence σ(p^e)=(p^{e+1}-1)/(p-1) and
  τ(p^e)=e+1, and σ is multiplicative over coprime arguments. Separately,
  gcd(2^m - 1, 2^n - 1) = 2^{gcd(m,n)} - 1 for positive integers m, n.
hypotheses: p prime, e, k, m, n positive integers (k=0 case separate).
holds-here: yes (used to compute σ, τ, and the gcds in the inclusion-
  exclusion for divisors of 2^60 - 1).
bearing: gives the divisor-sums and gcd-Mersenne rungs of the Lean proof a
  real, citable source instead of an unanchored formula.
status: proved
anchor: Mathar eq. (3.17); TCD course notes sec 5.6 / EoM; Wolfram GCD page.
```
