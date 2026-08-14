# Mertens-first: Lehman's identity → M(n), then Mertens-first totient formula → Φ(n)

```approach
idea: Compute Φ(n) by first computing the Mertens function M(x) = Σ_{k≤x} μ(k) via Lehman's identity / the Deleglise–Rivat recursion, then assemble Φ(n) through the Mertens-first totient formula — a different intermediate object (μ's summatory) than the adopted φ-sieve.
mechanism: The Mertens-first formula (Brown 2025, in `research/CLAIMS.md` as `mertens-first-totient-formula`) expresses Φ(n) for ab = n as Σ_{x≤a} μ(x)·⌊n/x⌋(⌊n/x⌋+1)/2 + Σ_{y≤b} y·M(⌊n/y⌋) − (b(b+1)/2)·M(a), so Φ(n) is recovered from M on the O(√n) floor-quotient values. M itself is computed by Lehman's identity (`lehman-mertens-identity`) or the Deleglise–Rivat recursion (`mertens-recursion`: M(n) = 1 + ⌊β⌋M(α) − Σ_{x≤α} μ(x)⌊n/x⌋ − Σ_{y=2..β} M(⌊n/y⌋) for αβ=n), which are Θ(n^{2/3}) (Deleglise–Rivat 1996) or Θ(n^{3/5}) (Helfgott–Thompson 2023) — no φ sieve and no full μ table.
precedent: lehman-mertens-identity; mertens-recursion; mertens-first-totient-formula; heath-brown-mobius-identity; https://doi.org/10.1080/10586458.1996.10504594; https://arxiv.org/pdf/2506.07386; https://doi.org/10.1007/s40993-022-00408-8; https://doi.org/10.1090/S0025-5718-98-00977-6; OEIS A002321
status: refuted
killed-by: Valid method, not the line: its leading term Σ_{x≤a}μ(x)⌊n/x⌋(⌊n/x⌋+1)/2 is exactly the μ-sum the adopted Ehrhart derivation produces (a=n, b=1), so the geometric and Mertens-first routes meet at one identity; the Deléglise–Rivat M(n) machinery is a computational engine for a distinct intermediate object, not a new representation.
first-step: Implement the Deleglise–Rivat M(n) recursion with memoization over floor quotients, verify M(10^k) against A002321 (Mertens) for k=0..8, then feed it into the Mertens-first formula and check Φ(10^8) = 3039635516365908 and H(10^8) = 11762187201804552.
```

## Grounding verdict

status: grounded

The reformulation is the standard **Mertens-first / Deléglise–Rivat** route of
analytic number theory. Each ingredient is a named, sourced identity in the
ledger:

- **Lehman's identity** (Deléglise & Rivat 1996, *Experimental Mathematics*
  5(4):291–295, DOI 10.1080/10586458.1996.10504594): for 1 ≤ u ≤ x,
  M(x) = M(u) − Σ_{m≤u} μ(m) Σ_{u/m<n≤x/m} M(⌊x/(mn)⌋). This is the
  `lehman-mertens-identity` claim.
- **Deléglise–Rivat recursion** (`mertens-recursion`): M(n) = 1 + ⌊β⌋M(α)
  − Σ_{x≤α} μ(x)⌊n/x⌋ − Σ_{y=2..β} M(⌊n/y⌋), αβ = n, with
  O(x^{2/3}·(log log x)^{1/3}) time and O(x^{1/3}·(log log x)^{2/3}) space.
- **Mertens-first totient formula** (`mertens-first-totient-formula`, Brown
  arXiv:2506.07386): Φ(n) = Σ_{x≤a}μ(x)⌊n/x⌋(⌊n/x⌋+1)/2 + Σ_{y≤b}y·M(⌊n/y⌋)
  − (b(b+1)/2)·M(a), ab = n.
- **Helfgott–Thompson** improvement to M(x) in O(x^{3/5}) bit time
  (`heath-brown-mobius-identity`, DOI 10.1007/s40993-022-00408-8),
  `Research in Number Theory` 9(1):6 (2023).

Hypotheses hold here: n=10^8, M(⌊10^8/y⌋) is obtained by sieving μ up to
√n≈10^4 and applying the recursion (far cheaper than a full DR run), then Φ
via the Mertens-first formula reproduces Φ(10^8)=3039635516365908. The
Mertens check-values M(10^k) for k=0..8 are in OEIS A002321 (already sourced).

Whether anyone applied it *to this problem*: the Mertens-first totient sum is
exactly Brown's Algorithm 1/13, used there to compute Φ(10^19); it is the
established analytic route to summatory totients, not PE-351-specific but the
canonical sublinear Mertens-based method. The Deleglise–Rivat lineage is
confirmed independently by Helfgott–Thompson (DOI 10.1007/s40993-022-00408-8)
and Deléglise–Rivat 1998 (Computing ψ(x), DOI 10.1090/S0025-5718-98-00977-6).

What it buys: a **third independent sublinear route** to Φ(10^8)/H(10^8),
distinct intermediate object (Möbius summatory M, not φ), well-developed
analytic lineage — a second verification route beyond the φ-sieve and the
Gauss recursion. Run at full size it independently re-derives
H(10^8)=11762187201804552.

precedent:
  - lehman-mertens-identity (ledger claim)
  - mertens-recursion (ledger claim)
  - mertens-first-totient-formula (ledger claim)
  - heath-brown-mobius-identity (ledger claim)
  - https://doi.org/10.1080/10586458.1996.10504594 (Deléglise & Rivat 1996)
  - https://arxiv.org/pdf/2506.07386 (Brown 2025, Mertens-first totient formula)
  - https://doi.org/10.1007/s40993-022-00408-8 (Helfgott & Thompson 2023)
  - https://doi.org/10.1090/S0025-5718-98-00977-6 (Deléglise & Rivat 1998, Computing ψ(x))
  - OEIS A002321 (Mertens, already sourced in library)

## Why it is a different line

Distinct from both the adopted φ-sieve and the Dirichlet-hyperbola/Gauss line: it computes the *Möbius summatory function M*, not the totient summatory Φ, and uses the Lehman/Deleglise–Rivat identity family rather than the Gauss divisor-sum recursion. It is a well-developed algorithm of analytic number theory (Meissel–Lehmer lineage), and all its ingredients are already claimed in the ledger.

## Grounding in the library

- `lehman-mertens-identity`, `mertens-recursion`, `mertens-first-totient-formula` in `research/CLAIMS.md` (from `research/summaries/deleglise-rivat-summatory-mobius-correct.md`, `research/summaries/arxiv-2506.07386-totient-summatory.html.md`).
- `research/sources/deleglise-rivat-summatory-mobius-correct.full.md`, `research/sources/helfgott-thompson-summing-mobius.full.md`, `research/sources/hurst-mertens-function-computations.full.md`.

## Cost

Θ(n^{2/3}) (Deleglise–Rivat) or Θ(n^{3/5}) (Helfgott–Thompson) time, O(√n) space — a second independent sublinear route to the same final answer.
