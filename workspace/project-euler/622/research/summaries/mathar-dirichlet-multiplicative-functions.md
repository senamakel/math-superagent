# Mathar — "Survey of Dirichlet series of multiplicative arithmetic functions" (arXiv:1106.4038)

Source: https://arxiv.org/pdf/1106.4038 · full text: [[mathar-dirichlet-multiplicative-functions.full]]

## What it establishes

A 2200-line survey (arXiv:1106.4038v2) of Dirichlet generating functions of multiplicative arithmetic functions, rooted at powers, sums-of-divisors and Euler's totient. The facts the run already uses, stated cleanly here:

- **Multiplicativity (Def 1, eq 1.1):** a(nm) = a(n)a(m) for (n,m)=1; values determined by prime powers a(p^e) (eq 1.4).
- **Möbius function (2.1.2):** master equation a(p^e) = −1 if e=1, 0 if e>1; Dirichlet inverse of 1; D-series 1/ζ(s) (eq 2.7).
- **Divisor sums (Sec 3.5, eq 3.16–3.17):** σ_k(n) = ∏_p (1 + p^k + p^{2k} + ··· + p^{e_k·k}), with the geometric-sum formula
  σ_k(p^e) = (p^{k(e+1)} − 1)/(p^k − 1) for k>0, and σ_0(p^e) = e + 1.
  Dirichlet series σ_k(n) ↦ ζ(s)ζ(s−k); σ_k = n^k ⋆ 1 (Dirichlet convolution).
- Set k=1: σ(p^e) = (p^{e+1}−1)/(p−1); set k=0: τ(p^e) = e+1. Both are multiplicative.

## Consequences for this problem

Eq (3.17) is the exact source recorded in `divisor-sums-gcd-mersenne-sourceable` for the σ(p^e) and τ(p^e) prime-power formulas that the inclusion-exclusion / Möbius-inversion routes use (σ(2^d−1), τ(2^d−1) over d | 60). The Möbius master equation (2.7–2.8) corroborates `mobius-inversion-sourceable`. It is a **supporting reference**: the statements PE622 needs are already extracted and proved into the claim library; Mathar is the citable anchor for the formulas themselves.

## Does not settle

No statement about multiplicative *orders* mod n, no shuffle order formula, and no numerical enumeration. The survey covers Dirichlet-series machinery, not the ord_m(2)=60 computation.

## Status

The σ/τ formulas are standard and proved in the source (geometric sums). Hypotheses (prime p, k ≥ 0) hold here.

```claim
id: sigma-tau-prime-power-mathar
statement: For a prime p and k > 0, sigma_k(p^e) = (p^{k(e+1)} - 1)/(p^k - 1)
  and sigma_0(p^e) = e + 1; hence sigma(p^e) = (p^{e+1}-1)/(p-1) and
  tau(p^e) = e + 1, with sigma and tau multiplicative over coprime arguments.
hypotheses: p prime, e, k nonnegative integers (k > 0 in the ratio formula).
holds-here: yes (all moduli in 2^60-1 factor into such prime powers).
status: proved (source gives geometric-sum derivation)
bearing: citable anchor for the divisor-sum and divisor-count rungs
  (sigma(2^d-1), tau(2^d-1)) used by the Möbius-inversion and
  inclusion-exclusion routes.
anchor: research/sources/mathar-dirichlet-multiplicative-functions.full.md
  eq (3.16)-(3.17), sec 3.5; eq (2.7)-(2.8) for mu.
follows-from: divisor-sums-gcd-mersenne-sourceable
```
