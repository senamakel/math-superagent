# Pattern-finder: the second-moment plateau is the exact density-1 input

Independent recomputation from `code/out/nu2_primes_xor_40000.json`
(guarded: ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975, μ₄₀₀₀=0.497259, S(4000)=48 — all
canonical). Everything below holds **exactly over every term n = 2..40000**;
each is a conjecture to derive, not a proof.

## The sharpest object

`S(n) := (n−2) − 2·ν₂(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)}`, the endpoint
character sum (claim `excess-is-negative-character-sum`, checked). SUPPLY
`ν₂ ≥ c·n` is exactly `S(n) ≤ (1−2c)n − 2` eventually. Measured `|S(n)| ≤ 712`
and `|S|/√n ≤ 3.815` over the whole range — i.e. **S = O(√n) pointwise**, a
statement strictly stronger than SUPPLY, holding exactly over every n≤40000.

## The second-moment plateau (the density-1 input)

Cumulative second moment tracks the uniform model:

```
N       Σ_{n≤N} S(n)²  /  Σ_{n≤N}(n−2)  = ratio
100     0.9617
1000    1.0249
4000    1.0276
20000   0.9983
40000   0.9944
```

Equivalently `E[S(n)²] ≈ (n−2)`, and the prefix mean of `S²/n` is ~0.999 at
40000. The pointwise ratio `S(n)²/(n−2)` is spiky: max 14.55 at n=27624, but
few excursions — `>4: 4.54%`, `>9: 0.25%`, `>16: 0%` of n≤40000.

**Why this is the exact input density-1 SUPPLY needs.** If
`E[S(n)²] ≤ C·n` were proved for one finite C, then by Markov/Chebyshev

```
#{n≤N : ν₂/n < 1/2 − δ}  =  #{n : S(n) > 2δn}
        ≤ (1/4δ²) Σ_{n≤N} S(n)²/n²  ≤  (C/4δ²) Σ 1/n  =  (C/4δ²) log N ,
```

so the exceptional set has density `O(log N/N) → 0`: **ν₂/n ≥ 1/2 − δ on a
density-1 set**. This is GOAL priority 1 and directive 14's `s2_N → 0` in
exactly the form that yields the theorem. The conditional algebra is rigorous;
the open step is producing the uniform constant bound `E[S²] ≤ C n`
unconditionally for the primes — the arithmetic barrier.

Measured constant: pointwise `max_n S(n)²/(n−2) = 14.55` over n≤40000, so a
uniform C ≈ 15 holds over the measured range (finite-length, not a theorem).

## Variance decay (confirms the same plateau)

`s2_N = Var(ν₂/n over [2,N])`: `s2_N·N = 0.799@1000 → 1.699@40000` consistent
with the log null `log(N)/(4N)` (Ratio B ≈ 1.3, claim
`fair-variance-log-null-tail-clean-40000`). Sliding window of fixed size 500:
`s2·500 = 0.172@[500,1000) → 0.003@[39000,39500)`, verifying the per-index
variance `1/(4n)` (from `wt(Φ_n h) ~ Binomial(n−2,1/2)`, proved) so the prefix
variance is their average `≈ log(N)/(4N)`.

## Rising tail min (evidence for pointwise ν₂/n → 1/2)

```
X (tail start)   min_{n≥X} ν₂(n)/n
50     0.3396
200    0.4161
1000   0.4600
5000   0.4780
10000  0.4850
20000  0.4880
30000  0.4901
```

Dip sets are finite: `{ν₂/n < 0.35}` ends at 53, `< 0.40` ends at 105,
`< 0.42` ends at 274, `< 0.45` ends at 763, `< 0.48` ends at 5655. All finite in
the measured range — evidence, not proof.

## Structureless S(n) — confirmations of the dyadic dead end

S(n) shows NO exploitable structure over the full 40000:

- **No dyadic self-similarity**: `corr(S(2n), S(n)) = 0.0073`,
  `corr(S(2n+1), S(n)) = −0.0071`, `corr(S(2n), S(2n+1)) = −0.011`.
- **No autocorrelation** at any lag (|r| < 0.03 at lags 1,2,3,5,10,20,50,100).
- **No even/odd asymmetry**: mean(ν₂/n | even) vs odd differ by < 0.0003.
- **No polynomial, no low-order linear recurrence** (both tools: none fit).
- **S(n) ≡ n (mod 2) only** — forced by the definition, not structure.
- **Dyadic values are small**: S(2^m) = 0,−2,2,−10,4,8,−6,−18,24,18,40,74,
  −178,−294,−162 for m=1..15 — all o(2^m), consistent with S=O(√n) but with no
  index that lets one predict the next.

This independently re-corroborates the refuted `dyadic-gap-character-correlation`
approach: the fold weight on the primes is a structureless, second-moment
stationary noise (like uniform input), not a dyadic-gap correlation that a
single-shift character bound could control.

## The discriminator vs negative controls

The second-moment plateau is **prime-specific among the closed-door classes**:
Thue–Morse has ν₂/n → 0.011 sublinear (closed door 3), so S(n) ~ n, so
`E[S²] ~ n²` NOT `n` — the plateau **fails** for Thue–Morse. All-ones is the
kernel (ν₂=O(1), S before the floor ~ n) — also fails the plateau. The primes
and uniform-h both sit at `E[S²] ≈ n−2`. So the plateau is not satisfied by any
aperiodic-but-2-regular input, which is precisely the family the five closed
doors show is the only risk.

## Deliverable statement

**Conjecture (measured exact over n≤40000):** for the prime-h fold,
`E[S(n)²] ≤ C·n` for a finite constant C (measured ≈ 15 pointwise, cumulative
ratio → 1). If proved, this yields density-1 SUPPLY by Chebyshev. It is the
weakest arithmetic input in this run's catalogue that gives the density-1 form,
and it is orthogonal to the (dead-end) switch-density reduction because it is a
second-moment condition on the folded image, satisfiable by the primes while
failing every 2-regular control.

Not a proof. The unconditional constant bound for the primes is open — that is
the arithmetic barrier, unchanged.
