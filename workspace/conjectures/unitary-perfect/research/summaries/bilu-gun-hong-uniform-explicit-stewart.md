<!-- source: https://arxiv.org/pdf/2108.09857 | converted from PDF -->

# Bilu, Gun & Hong 2022, *Uniform explicit Stewart's theorem on prime factors of linear recurrences* (arXiv:2108.09857v5)

Full text: `research/sources/bilu-gun-hong-uniform-explicit-stewart.full.md`.

## What it establishes

Fully explicit, uniform version of Stewart (2013, Acta Math. 211:291–314) on
the largest prime divisor / p-adic valuations of Lucas–Lehmer terms `γ^n − 1`.

- **Thm 1.1 (Stewart 2013):** for `γ ∈ Q`, or `[Q(γ):Q] = 2` with norm ±1 and
  γ not a root of unity, there is some `n₀` (depending only on `ω(γ)` and the
  field) such that for every `n > n₀` some prime `p | γ^n − 1` satisfies
  `p ≥ n exp((log n)/(104 log log n))` — answered Erdős's and Schinzel's
  questions.
- **Thm 1.2 (this paper, rational case):** `n₀ = exp(10⁶)` absolute; for every
  `n ≥ n₀` there is `p | γ^n − 1` with `p ≥ n exp(0.0005 log n / log log n)`.
- **Thm 1.3 (this paper, quadratic case):** for `[Q(γ):Q] = 2`, `Nγ = ±1`,
  `n₀ = exp exp(max{10⁹, 3|D_K|})`; for `n ≥ n₀` some prime below `γ^n − 1`
  has `p ≥ n exp(0.0002 log n / log log n)`.
- **Thm 1.4 / 1.5:** p-adic valuation upper bounds `ν_p(γ^n − 1) ≤
  Np·exp(−c log Np/log log Np)·h(γ)·log n`, uniform in ω(γ).
- **Prop 8.2 (primitive divisor facts used by the whole field):** a primitive
  divisor `p` of `γ^n − 1` divides `Φ_n(γ)` with `Np ≡ 1 mod n`; for degree-2
  norm-1 γ, `p ≡ ±1 mod n`; non-primitive part `ν_p(Φ_n(γ)) ≤ ν_p(n)` for
  `n ≥ 2d+1`.

## Bearing on this problem

This is the modern primary for the paper's **hypothesis (H2)**
"ω(Φ_{4p}(2)) ≥ C log p" and for the run's Hong–Stewart claims. Applying
Thm 1.3 with `γ = 2`, degree 1 (or the quadratic embellishments with
`γ = ±2`), and `n = 4p`: Stewart gives a *largest* prime factor
`P(2^{4p} − 1) ≥ 4p·exp(c log(4p)/log log(4p))` — a largest-prime bound,
**not** a lower bound on ω(Φ_{4p}(2)). The paper's own (H2) is
"best regarded as a conjectural target"; this source confirms that the
Stewart/tradition results bound P(u_n), not ω(u_n). So it pinpoints why (H2)
is genuinely missing, and supplies the explicit valuation bound (Thm 1.5) that
the run's `hong-stewart-nonprimitive-bound` claim rests on.

```claim
id: bgh2022-explicit-stewart-prime-factor
statement: For gamma a rational != ±1 with n >= exp(10^6), some prime p | gamma^n - 1
  has p >= n exp(0.0005 log n / log log n); for gamma quadratic norm ±1 with
  n >= exp exp(max{10^9, 3|D_K|}), some prime below gamma^n - 1 has
  p >= n exp(0.0002 log n / log log n). The exponent is explicit and uniform
  in omega(gamma).
hypotheses: gamma not a root of unity, norm ±1 in the quadratic case
holds-here: yes for gamma = 2, n = 4p -- the largest prime factor of 2^{4p} - 1
  (hence of Phi_{4p}(2)) is exponentially larger than n
status: sourced (full text held); quantified in the paper, including through
  the numerical Prime Number Theorem of Bennett-Martin-O'Bryant-Rechnitzer
bearing: this is a largest-prime-factor theorem, NOT an omega lower bound; it
  sharpens why hypothesis (H2) of Maciejewski's Theorem 30 is not a
  consequence of the Stewart tradition
anchor: research/summaries/bilu-gun-hong-uniform-explicit-stewart.md
answers: whether-stewart-bounds-omega, explicit-stewart-constants
```