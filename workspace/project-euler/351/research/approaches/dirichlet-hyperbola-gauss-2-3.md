# Dirichlet hyperbola / Gauss self-referential Φ recursion (Θ(n^{2/3}))

```approach
idea: Compute Φ(n) = Σ_{k≤n} φ(k) in Θ(n^{2/3}) by the Dirichlet hyperbola method applied to the Gauss divisor-sum identity, with memoized floor-quotient recursion — no φ array at all.
mechanism: Gauss gives Σ_{d|k} φ(d) = k, so summing over k ≤ n and swapping gives n(n+1)/2 = Σ_{d≤n} Φ(⌊n/d⌋), i.e. Φ(n) = n(n+1)/2 − Σ_{d=2}^{n} Φ(⌊n/d⌋). Only the O(√n) distinct values ⌊n/d⌋ appear, so Φ(n) is computed by a memoized recursion over those values; the recursion's total state is the O(√n) values {⌊n/j⌋}, and precomputing φ up to a cutoff t ≈ n^{2/3} by a small sieve bounds the leaves, giving Brown's Θ(n^{2/3}) time and O(√n) space (arXiv:2506.07386, already in `research/sources/`).
precedent: gauss-divisor-sum-of-totient; totient-sum-fast-recursion; https://arxiv.org/pdf/2506.07386; https://codeforces.com/blog/entry/117635; https://codeforces.com/blog/entry/54090
status: refuted
killed-by: Valid method, not the line: it is a sublinear *computation* of Φ(n) (Θ(n^{2/3}), the canonical Dujiao-sieve/Gauss floor-quotient recursion), not a new representation. The adopted Ehrhart derivation reduces H(n) to exactly this Φ, and the run already evaluates it; this route stands as an independent verification, not a new attack.
first-step: Implement memoized Φ(n) = n(n+1)/2 − Σ_{d=2}^{n} Φ(⌊n/d⌋) with distinct-floor grouping, precompute φ up to t = n^{2/3}, and verify Φ(10^k) for k=0..8 against A064018 (…, 3039635516365908) and H(10^8) = 11762187201804552.
```

## Grounding verdict

status: grounded

The reformulation is the standard **fast-prefix-sums / Dirichlet-hyperbola
method** (often called the *Dujiao sieve* in competitive-programming
literature) applied to the Gauss convolution Σ_{d|n}φ(d)=n. The recursion
Φ(n) = n(n+1)/2 − Σ_{d=2..n} Φ(⌊n/d⌋) is exact (it is just the Gauss identity
rearranged) and, with distinct-floor grouping, visits only O(√n) distinct
values ⌊n/d⌋. Precomputing φ (or Φ) up to a cutoff t ≈ n^{2/3} by a small
sieve bounds the leaves, giving Θ(n^{2/3}) time and Θ(n^{1/2}) space — this is
precisely the complexity class of Kulkov's framework ("H(⌊n/k⌋) for all
possible arguments in O(n^{2/3})", Codeforces blog entry 117635, applying to
φ = μ∗id) and of Brown's Mertens-first paper (arXiv:2506.07386, Θ(n^{2/3})
time).

Hypotheses hold here: n=10^8 is a single evaluation, the floor-quotient
machinery is exact integer arithmetic, and the recursion produces the same
Φ(10^8) = 3039635516365908. The claim `gauss-divisor-sum-of-totient` and
`totient-sum-fast-recursion` (Chai Wah Wu's A063985 recursion — the same
floor-grouped recursion for the cototient partial sums) are in the ledger.

Whether anyone applied it *to this problem*: the summatory-totient recursion
is exactly the sublinear computation of Φ used in the clamped literature
(Brown 2025 computes Φ(10^19) by it); it is not specific to PE 351 but is the
canonical way to evaluate Φ(10^8) without a full φ table.

What it buys: a genuinely **second, independent sublinear route** to
Φ(10^8)/H(10^8) at Θ(n^{2/3}) time and Θ(n^{1/2}) space — different complexity
class and different object (summatory Φ as a whole) than the adopted φ-sieve.
Run at full size it independently re-derives H(10^8) = 11762187201804552.

precedent:
  - gauss-divisor-sum-of-totient (ledger claim)
  - totient-sum-fast-recursion (ledger claim)
  - https://arxiv.org/pdf/2506.07386 (Brown 2025, Θ(n^{2/3}) totient sum)
  - https://codeforces.com/blog/entry/117635 (Kulkov, fast prefix sums / Dujiao sieve)
  - https://codeforces.com/blog/entry/54090 (Nisiyama_Suzune, cited in the Bloch/Summer-of-Number-Theory sources)

## Why it is a different line

The adopted method sieves φ over all k ≤ 10⁸ (O(n log log n), ~400 MB). This line never builds a full φ table: it computes Φ by the self-referential floor-quotient recursion, sublinear in n. It is a different complexity class and a different object of study (the summatory function Φ as a whole, not the pointwise φ).

## Grounding in the library

- `gauss-divisor-sum-of-totient` in `research/CLAIMS.md` — the identity Σ_{d|n}φ(d)=n and its rearrangement.
- `research/sources/arxiv-2506.07386-totient-summatory.full.md` (Brown 2025) — Θ(n^{2/3}) summatory totient, including the Mertens-first variant.
- `research/sources/kulkov-dirichlet-convolution-fast-prefix-sums.full.md` — the general floor-quotient / hyperbola framework for fast prefix sums of multiplicative functions.

## Cost

Θ(n^{2/3}) time, O(√n) memory — independent of the 10⁸-scale sieve budget, so it can be run at full size as a *second* independent computation of the same final answer.
