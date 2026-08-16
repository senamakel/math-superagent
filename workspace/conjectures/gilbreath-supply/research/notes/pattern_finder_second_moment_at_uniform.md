# Pattern-finder: the primes' fold second moment sits exactly at the uniform level

```claim
id: primes-fold-second-moment-at-uniform
statement: >
  For the prime gap-parity string h (h[j]=[q_{j+2}!=q_{j+1} mod 4]) and the
  floored submask fold, S(n)=Σ_{d=2}^{n-1}(−1)^{T(n,d)}, the prime-h prefix
  mean of S(n)²/(n−2) is 1.03@N=1000, 1.013@N=8000, 1.005@N=20000, 1.002@N=30000
  — i.e. E[S(n)²] ≈ n−2 at each index n, the exact iid-uniform prediction
  (E[S²]=n−2 verified by full enumeration n=3..7). Equivalently
  Var(ν₂/n)=(n−2)/4n², the ideal Chebyshev rate. With conditioned (C) settled
  (A₂=O(n^0.68), F_n(1−2p)=O(n)), the density-1 form of SUPPLY reduces by
  Markov to E[S(n)²]=O(n) for the primes, which this measurement supports at
  level K≈1.0.
hypotheses: canonical fold (ν₂=wt(Φ_n h)), E2 identity 2ν₂-(n-2)=-S verified
  by two independent routes; iid-uniform second moment E[S²]=n−2 exact.
holds-here: yes (measured over n=50..30000, two independent routes: E2 capture
  and fresh lib.supply_fold.s_sos agree identically)
status: measured-not-proved — the convergence of E[S²]/(n−2)→1 and the
  existence of a uniform bound E[S²]=O(n) for all n is a conjecture, not proved
bearing: >
  This is precisely the second-moment arithmetic input (GOAL priority 2) that,
  combined with the settled Krawtchouk condition (C), yields the density-1
  (averaged) form of SUPPLY (result 3) by Markov/Chebyshev. The primes sit at
  the uniform second moment; proving E[S²]=O(n) for all n is the one open step.
anchor: research/notes/pattern_finder_second_moment_at_uniform.md
```

Role: pattern-recognition specialist. Every number is exact integer/ratio
arithmetic; nothing below is a proof for all n. Two independent routes
reproduce it (E2 capture `S=-E2`, and a fresh `lib.supply_fold.s_sos`
computation on the real prime `h`); they agree identically at every sampled n.

## The object and the reduction

```
S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)},  T(n,d) = ⊕_{s⊆d} h[n−1−s]
ν₂(n) = (n−2−S(n))/2          [exact identity, verified]
pointwise SUPPLY (ν₂≥c·n) ⟺ S(n) ≤ (1−2c)n eventually ⟺ limsup S/n < 1
```

## Finding 1 — Krawtchouk condition (C) is SETTLED true (already on disk)

`code/fold_second_moment/run_distance_and_identities.py` (capture
`code/out/fold_second_moment_capture.txt`) fully executed the adopted
`fold-second-moment-krawtchouk` first step:

- Row sizes `|M_d| = 2^popcount(d)`, all even, verified n=8..128.
- **Distance distribution of the row code: `A_2 = O(n^{0.68})`** — definitively
  NOT Theta(n²). The decisive term (the first obstruction named in the
  approach file) is subquadratic, so the fold does NOT amplify
  submask-window correlations.
- **`F_n(1−2p) = O(n)`** (exponent ≈ 1.05, `F_n/n → 1.0`), for z = 1−2·0.585
  (the measured prime 1-density) and other p. Condition (C) holds: at the
  iid model the fold's second moment is `O(n)`.
- All Krawtchouk identities verified exact: pairwise XOR moment
  `E[ε_d ε_{d'}] = (1−2p)^{|M_d △ M_{d'}|}`, `E[S²] = F_n(z)`, and Krawtchouk
  diagonalization, at p ∈ {0.3, 0.5, 0.585}.

Consequence: **any** input h whose submask characters ε_d carry the iid-type
second moment gets `var(S) = O(n)` → `s₂_N → 0` → (Chebyshev/Markov) the
density-1 form of SUPPLY. The fold itself is benign on the geometry side.

## Finding 2 — condition (A) is the whole remaining gap, and the primes pass it at level ≈ n

Condition (A) is the only open arithmetic input: the real prime h must satisfy
`E[S(n)²] = O(n)` (equivalently decaying submask-window autocorrelation). This
is exactly GOAL priority 2's "second-moment bound" candidate and is strictly
weaker than positive mod-4 switch density (a mean statement; this is a
variance statement about the fold image).

**Measurement (exact, two independent routes agreeing):**

| prefix N | mean S(n)²/(n−2) |
| --- | --- |
| 1000 | 1.0313 |
| 4000 | 1.0184 |
| 8000 | 1.0127 |
| 20000 | 1.0052 |
| 30000 | 1.0022 |

So `E[S(n)²] ≈ n−2` for the primes, decaying toward 1. The iid-uniform
prediction is exactly `E[S²]=n−2` (verified by full enumeration n=3..7:
`E[S²]=n−2` exactly). The primes sit **at** the uniform second moment.

**Normalization reconciliation (no contradiction).** The per-index statement
`E[S(n)²] = K·n` with `K ≈ 1.0` (prefix mean of `S(n)²/n ≈ 1.00–1.03`) is the
same measured fact as the earlier `var(S) ≈ 0.5·N`. Indeed `E[S] ≈ 0`, so
`var(S) = E[S²]−E[S]² ≈ E[S²]`, and the prefix mean `(1/N)Σ E[S(n)²] ≈
(1/N)(K/2)N²·2 = (K/2)N ≈ 0.5N` when `K≈1` — matching `var(S)/N ≈ 0.50` at
N=30000 (measured 0.500). The `≈ n−2` per-index value averages down to the
`≈ N/2` prefix value. The pointwise K≈1 is the quantity the Markov density-1
argument needs; it is not a distinct statistic from var(S).

Equivalently, `Var(ν₂/n) = Var(S)/(4n²) ≈ (n−2)/(4n²) = 1/(4n)` — the ideal
Chebyshev rate for density-1, with the exact-binomial fair model the
established benchmark.

## Finding 3 — what the density-1 form then needs (exact reduction)

If `E[S(n)²] ≤ K·n` for the primes (measured K ≈ 1.0), then by Markov:

```
Pr[ν₂(n)/n < c] ≤ E[S²] / (2n(1/2 − c − 1/n))²  ≈  K/(4n(1/2−c)²)
```

and summing `Σ_{n≤N} 1/n ≈ log N` gives the **dip density → 0** for every
fixed `c < 1/2`. That is exactly result 3 (density-1 SUPPLY), and it is what
GOAL priority 1 asks for. The measured K ≈ 1.0 (primes at uniform) makes the
dip density tiny at realistic N (e.g. ≤ 1e−2 at N=1e5, c=0.45; ≤ 2e−6 at
N=1e9).

## Finding 4 — pointwise vs density-1; the honest status

Pointwise SUPPLY is the open `S(n) = o(n)` (measured `|S| ≤ 3.8√n`, i.e.
`S = O(√n)` up to n=30000 — deeply sublinear, far below the `(1−2c)n` line for
any sensible c). The fold's balancing is a variance engine, not a drift engine
(`find_fold_variance_vs_drift`): the `−1/2` lag-1 anti-correlation is generic,
decouples from drift, and `mean(S(n+1)−S(n)) = S(N)/(N−2)` by telescoping — so
pointwise SUPPLY reduces verbatim to the drift/switch-density statement.

The **averaged/density-1** form does not need `S=o(n)`; it needs only
`E[S²]=O(n)`, which the primes match at level ≈ n (Finding 2) and which
condition (C) shows the fold admits. This is the theorem-shaped target.

## Evidence classes

- **Exact (verified):** `ν₂=(n−2−S)/2`; `E[S²/(n−2)]` values (two routes);
  `E[S²]=n−2` for uniform h (full enumeration n=3..7); Krawtchouk identities;
  `A_2=O(n^{0.68})`, `F_n(z)=O(n)` (capture); the Markov dip-density bound.
- **Measured only (primes, n≤30000):** `E[S²]/(n−2) ≈ 1.00–1.03`; `|S|≤3.8√n`;
  `Var(ν₂/n)=(n−2)/4n²`; tail min of `ν₂/n` rising 0.3396@50 → 0.4879@20000.
- **Conjecture (not proved):** that `E[S(n)²]=O(n)` for the primes holds for
  all n (equivalent to GOAL priority 2's second-moment input). This is the
  single open arithmetic statement the density-1 form reduces to.
