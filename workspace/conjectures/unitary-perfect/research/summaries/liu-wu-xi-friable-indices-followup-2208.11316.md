# Liu–Wu–Xi shifted-prime friable-index line (arXiv follow-up 2208.11316)

Source: arXiv:2208.11316 (2022 preprint). Its direct companion is the paper's
reference **[10]**: J. Liu, J. Wu, P. Xi, *Primes in arithmetic progressions
with friable indices*, Sci. China Math. 63 (2020) 23–38
(DOI 10.1007/s11425-018-9480-6, paywalled — not held; this arXiv paper is the
morally-adjacent primary and states the key friable-index theorem).
Full text: `research/sources/liu-wu-xi-friable-indices-followup-2208.11316.full.md`.

## What it establishes

The paper is about **shifted primes p with large prime factor P⁺(p−1)** — the
observation that many primes have p−1 with a factor > x^c. Key tools and
results of the surrounding Liu–Wu–Xi school:

- Chen–Chen conjecture (R): for c ∈ [1/(k+1), 1/k), primes p ≤ x with
  `P⁺(p−1) ≥ x^c` satisfy `T_c(x) = T'_c(x) + O(x log log x/(log x)^2)`.
- The refined lower bound (attributed to Liu–Wu–Xi [18]/[10]):
  `lim inf T_c(x)/π(x) ≥ 1 − 4ρ(1/c)` for `0 < c < 0.3734...`, where θ₂ is the
  unique root of `θ − 4ρ(1/θ) = 0` and ρ is the Dickman function.
- Goldfeld/Luca et al. lemmas (von Mangoldt-weighted prime-in-progression
  sums L(x;u,v)).

## Why it matters for this run

This is the "friable shifted primes" family the paper's §5.3 explicitly says
**does not apply** to `H_even`. Bonding it to a held primary text pins the
demarcation:

- These theorems control the **ambient count** of primes p (varying over a
  range x) whose index (p−1)/q is friable — a density statement over all
  primes.
- The run's `S_3^(≤3)` requires (i) a **recursive** prime-chain condition (not
  a size cutoff), (ii) an **exponent cap** v_q ≤ 3, and (iii) the **exact
  order** condition `ord_r(2) = 4k` on the divisors of a *single fixed*
  `Φ_{4p}(2)` — not a congruence.
- So the largest-prime-factor construction here (P⁺(p−1) ≥ x^c) is a different
  object from "every prime divisor of (r−1)/(4p) lies in P_3 with exponent ≤ 3".

```claim
id: lwx-friable-index-ambient-not-divisor
statement: The Liu-Wu-Xi family bounds the AMBIENT count of primes p <= x with
  P+(p-1) having a large factor / friable index (e.g. lim inf T_c(x)/pi(x)
  >= 1 - 4 rho(1/c) for 0 < c < 0.3734). It is a density statement over all
  primes and does not transfer to the prime-divisor set of a fixed Phi_{4p}(2)
  subject to the recursive semigroup + exponent-cap + exact-order conditions
  of S_3^{(<=3)}.
hypotheses: varying primes over a range x, friable-index = size-cutoff smoothness
holds-here: no direct bearing -- the paper's S_3^{(<=3)} semigroup is recursive
  and exponent-capped, not size-friable, and the object is typed by exact order
status: sourced (the demarcation the Maciejewski paper draws is backed by a held text)
bearing: confirms the paper's "existing literature does not apply" claim for the
  divisor-transference gap; the run's S_3^{(<=3)} friable-index split is real.
anchor: research/sources/liu-wu-xi-friable-indices-followup-2208.11316.full.md
answers: why-friable-index-literature-does-not-close-conjecture-24
```
