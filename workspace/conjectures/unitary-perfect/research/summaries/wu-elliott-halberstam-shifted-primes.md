<!-- source: https://hal.science/hal-03216054/document | converted from PDF -->

# Jie Wu 2020, *Elliott–Halberstam conjecture and values taken by the largest prime factor of shifted primes*, J. Number Theory 206 (2020) 282–295

Full text: `research/sources/wu-elliott-halberstam-shifted-primes.full.md`.

## What it establishes

Studies the distribution of primes p for which the largest prime factor `P⁺(p−a)`
of the shifted prime is large, through **primes in arithmetic progressions with
friable indices** — the exact literature family the Maciejewski paper names as
closest-but-inapplicable ([10] there: "shifted-prime smoothness literature
(Baker–Harman, Banks et al., Liu–Wu–Xi, Lamzouri...) controls primes p with
p−a friable over an initial segment of small primes").

Setting (Wu's notation): `π(x, y; q, a)` counts primes `p ≤ x`, `p ≡ a (mod q)`,
with `(p−a)/q` y-friable (all prime factors ≤ y). The paper's objects:

- **Conjecture 1/2 (Elliott–Halberstam, prime and friable-index variants):**
  `π(x, y; q, a)` behaves like `Li(x)/φ(q)` averaged over moduli, with
  `y`-friability of the index.
- **Thm 1 (EHprime):** with `EH_{\text{prime}}[ε]`, `ε = 1 − 1/η`, `η ∈ (1, 32/17]`,
  a quantitative asymptotic for counts of shifted primes with large prime
  factor.
- **Thm 2 (EHfriable):** for every `η ≥ 2`, under `EH_{\text{friable}}[ε(η)]`, an
  upper bound on the count of primes with `P⁺(p − a) > x^1/η`.
- **Lemmas 2.2 / 2.3:** Bombieri–Vinogradov-type and Brun–Titchmarsh-type
  estimates for the friable-index progression counting function.

The relevance to this problem is **structural**: it confirms — against a
primary held in the library — that the existing literature bounds *counts of
primes in friable-index progressions*, i.e. density statements about ambient
prime sets. It does **not** transfer to the *prime-divisor set of the single
fixed integer Φ_{4p}(2)*, which is precisely the "divisor-transference" gap the
paper identifies (its §5.3: "a finiteness proof must control the divisors of
Φ_{4p}(2) individually... no combination of recursive semigroup, exponent cap,
exact order appears together in the published literature"). Holding Wu 2020
also pins the *demarcation*: friable = size-cutoff smoothness; the run's
semigroup S_3^(≤3) is instead defined by recursive chains + exponent caps, so a
Bombieri–Vinogradov / Brun–Titchmarsh bound on friable indices cannot be
ported directly.

```claim
id: wu2020-friable-index-shifted-primes
statement: Jie Wu's 2020 JNT paper gives Bombieri-Vinogradov-type and
  Brun-Titchmarsh-type estimates, conditional on Elliott-Halberstam variants
  (EHprime, EHfriable), for pi(x, y; q, a) := #{p <= x : p ≡ a mod q,
  (p-a)/q is y-friable}. These bound the ambient prime counts in friable-index
  progressions; they are density statements, not divisor-level statements
  about a single fixed cyclotomic value.
hypotheses: a fixed non-zero, c > 1; the EH-type conjectures in the sharp
  forms
holds-here: yes as ambient-context; the friable-index object is exactly the
  family Maciejewski's paper excludes from applying to Phi_{4p}(2) -- friable
  is a size cutoff, while S_3^(<=3) is a recursive semigroup with exponent
  caps.
status: sourced (full text held)
bearing: pins the 'existing literature does not apply' claim to a primary
  text; confirms the divisor-transference gap is real and unmet
anchor: research/summaries/wu-elliott-halberstam-shifted-primes.md
answers: whether-friable-index-literature-transfers-to-cyclotomic-divisors
```