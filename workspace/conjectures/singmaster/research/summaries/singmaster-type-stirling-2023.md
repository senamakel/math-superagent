# Bazsó–Mező–Pintér–Tengely 2023 — Singmaster-type results for Stirling numbers

Source: A. Bazsó, I. Mező, Á. Pintér, Sz. Tengely, "Singmaster-type results for
Stirling numbers and some related diophantine equations", arXiv:2311.06080v1
(Nov 2023). Full text read:
`research/sources/singmaster-type-stirling-2023.full.md`.
URL: https://arxiv.org/html/2311.06080v1

## What the paper establishes

A **Singmaster analogue for Stirling numbers** of both kinds. Let `M_i(a)` be the
number of times `a` appears among Stirling numbers of the i-th kind.

- **Theorem 1** (second kind): for `a ≥ 2`,
  `M₂(a) ≤ 2 + 2·(log a)/W((1/2)log a)` — hence
  `M₂(a) = O(log a/(log log a − log log log a))`, where W is the **Lambert W
  function**. Method: direct Singmaster-style monotonicity argument (the central
  Stirling numbers `{2n}n` strictly increase; an `a` can have at most 2b
  solutions), with the bound `({2b}b) ≥ (b/2)^{b-1}` replacing the binomial's
  `C(2b,b) ≥ 2^b`.
- **Theorem 2** (first kind): **the same bound** `M₁(a) ≤ 2 + 2 log a/W(...)`,
  since `[2n n]_{≥2} = {2n n}_{≥2}` (associated Stirling numbers, no-fixed-point
  permutations vs no-singleton partitions, coincide).
- **Numerics (§3)**: for `a ≤ 100 000`, `M₂(a) ≤ 2` and `M₁(a) ≤ 2`; the
  `M₂(a)=2` witnesses are `a ∈ {15, 4095, 66066}`: `{5 2}={6 5}=15`,
  `{13 2}={91 90}=4095`, `{14 11}={364 363}=66066`. (15 and 4095 are
  Ramanujan–Nagell numbers `2^n−1 = m(m−1)/2`; 66066 comes from
  `{14 11}={364 363}`, refuting a conjecture of Ferenczik–Pintér–Porvázsnyik
  2011 that only (5,2,6,5) and (13,2,91,90) solve `{x k}={y l}` with max{k,l}≤50.)
- **Theorem 3**: for fixed `k ≠ 4`, the ABC-conjecture implies `n! = P_k(x)`
  (factorial = k-gonal number) has finitely many solutions; the finite list for
  `3 ≤ k ≤ 50`, `n ≤ 10^5` is computed and the 19-prime sieve resolves the rest.
- **Conjecture 1** (`{n n−3} = {m 2}` i.e. `C(n,4)+10C(n,5)+15C(n,6) = C(m,2)`:
  only (14,364)) and **Conjecture 2** (factorial–triangular `n! = m(m−1)/2`: only
  (1,2),(3,4),(5,16)) — both stated as out of reach.

## Bearing for this run

- **Adjacent, not load-bearing.** The Stirling analogue has the *same qualitative
  structure* as the binomial problem (a log/log-log-type upper bound via the
  monotonicity/central-element argument; a small finite witness set; a
  conjecture of boundedness) — good corroboration that the Singmaster machinery
  (Singmaster's own 1971 argument, the Lambert-W variant) is the standard tool
  for "how often does a number appear" across coefficient triangles, and that
  the log/log-log bound shape appears even where no N(3003)=8-level record is
  known.
- The paper's introduction **restates the binomial record** exactly as the run's
  ledger has it: `N(3003)=8` (citing MRSTT [9]), `N(a)=6` infinitely often
  (citing Lind [12], Singmaster [15,16]), Kane's record
  `O((log a)(log log log a)/(log log a)³)`, de Koninck–Doyon–Verreault's
  multinomial generalization. This is an independent secondary corroboration of
  `convention-n3003-eight` and `kane-method-ceiling`-adjacent record statements.
- It does **not** touch the binomial uniform-bound question and adds no method
  the run lacks (the Lambert-W refinement of Singmaster's O(log) argument is for
  Stirling numbers only; the binomial O(log a) baseline is already at
  `2+2 log₂ a` via the central-binomial argument). Filed as corroboration and a
  caution: the analogue's `M_i(a) ≤ 2+2 log a/W(...)` is *weaker* than the
  binomial's `2+2 log₂ a`, so no transfer of constants is possible.

## Claim

```claim
id: bazso-stirling-singmaster-analogue
statement: Bazso-Mezo-Pinter-Tengely 2023 (arXiv:2311.06080): for Stirling
  numbers of both kinds, Mi(a) <= 2 + 2 log a / W((1/2)log a) (a>=2; W = Lambert
  W), hence O(log a/(log log a - log log log a)). For a <= 100000, M2(a)<=2 with
  witnesses {15,4095,66066}, and M1(a)<=2 with witnesses {1,6,120}. The paper's
  intro independently restates the binomial record (N(3003)=8, N(a)=6
  infinitely often, Kane's O((log a)(log_3 a)/(log_2 a)^3)).
hypotheses: Stirling triangles of the two kinds; a positive integer >= 2.
holds-here: N/A for the binomial bound — this is an analogue; it corroborates the
  record and the "log/log-log" shape but transfers no constant to the binomial
  problem.
status: asserted-by-source (primary full text read; the theorem and tables
  quoted; the numerical claims are the paper's own)
bearing: corroborates the ledger's binomial record via an independent source;
  no new binomial method or bound.
anchor: research/sources/singmaster-type-stirling-2023.full.md
answers: none (adjacent corroboration only)
```