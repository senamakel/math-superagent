# Pattern-finder deliverable 3: every measurable regularity of ν₂ is fold-generic — the last "prime-specific" signal is not

**Role:** pattern-recognition specialist. All numbers exact over the terms supplied (canonical `code/out/nu2_primes_xor_40000.json`, guards ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975, ν₂(40000)=20081 all reproduce). Every structural fact is a **conjecture** for all n, verified exactly on n=2..40000; labeled `measured`, not `proved`.

## What the sequence tools establish (exact over supplied terms, no structure to exploit)

| sequence | tool | verdict |
| --- | --- | --- |
| ν₂(n), n=2..100 | find_linear_recurrence order≤10 | no constant-coeff recurrence |
| ν₂(n), n=2..50 | analyze_sequence | not low-degree polynomial; only trivial parity periodicity |
| S(n), n=2..50 | find_linear_recurrence order≤8 | no recurrence |
| dS(n)=S(n+1)−S(n) | analyze_sequence | not polynomial; parity periodicity trivial |
| ν₂(2^k) dyadic | oeis_lookup | **MISS** (2,2,12,13,27,66,136,243,502,1003,2010,4184,8338,16464 not catalogued) |

No constant-coefficient linear recurrence or low-degree polynomial fits any of these. The structure must come from the problem, not a catalogue or an arithmetic fit.

## Exact structural facts, verified on all n=2..40000

1. **Identity:** `S(n) = (n−2) − 2·ν₂(n)`, hence `ν₂(n) = (n−2−S(n))/2`. (`excess-is-negative-character-sum`.)
2. **Parity:** `S(n) ≡ (n−2) (mod 2)` (0 violations) and `dS(n)` is **always odd** (0 violations). Rigorous: S sums n−2 terms each ±1.
3. **White-noise law:** corr(S(n),S(n+1)) = **0.0002** (full range); ACF1(dS) = −0.5009; var(S)/var(dS) = 0.5001; Σ|ACF(dS;k≥2)| = 0.024. So S = √n·Z with Z near-white; var(S)=O(n). These are the exact facts behind the density-1 input.

## The second-moment plateau — the exact input for density-1 SUPPLY

`E[S²]/(n−2)` prefix-mean: 1.1284@500 → 1.0601@1000 → 0.9966@2000 → 1.0256@4000 → 1.0164@8000 → 1.0163@16000 → 1.0014@24000 → 1.0033@32000 → **0.9996@40000**. Flat at ≈1, no upward drift. Per-doubling-block max `S²/(n−2)` stays in [5.4, 14.55] through n=40000 — no drift upward in the constant (measured uniform bound C≈15). **density-1 SUPPLY (`ν₂/n ≥ c·n` for a density-1 set, any c>0) follows from this plateau by Chebyshev** — this is the cleanest, most likely-derivable target (GOAL priority 1 / problem result 3).

Pointwise support: ν₂/n mean 0.49967 over [2,40000]; tail [30000,40000] mean 0.49994, min 0.49011; per-window minimum rising [1000,2000):0.45995 → [32000,40001):0.49014 (evidence ν₂/n → 1/2).

## The finite exceptional set (pointwise, stronger than density-1)

`{n : ν₂(n)/n < c}` last member: c=0.40→105, 0.42→274, 0.45→763, 0.46→1211, 0.47→3086, 0.48→5655, 0.485→9969, 0.49→27624. Tail [30000,40000] is **EMPTY** for every c ≤ 0.49. So for every c ≤ 0.48 the exceptional set is finite on the measured range — if the subgaussian/exponential tail (`E[S⁴]` bounded) were proved, Chebyshev over the 4th moment upgrades density-1 to *finiteness of every exceptional set* (pointwise SUPPLY, result 1/2).

## KEY new result: the last "prime-specific" signal is also fold-generic

The prior runs treated **dip sparsity / finiteness of exceptional sets** as the prime-specific signal (density-model control claimed it was NOT reproduced by Bernoulli strings). This is **refuted by direct measurement**:

| c | primes dip-count [2,3000) | random p=0.585 (trials) |
| --- | --- | --- |
| 0.45 | 81 | 68, 73, 78 |
| 0.48 | 367 | 355, 371, 365 |

| c | primes last-dip ≤7000 | random p=0.585 (trials) |
| --- | --- | --- |
| 0.45 | 763 | 699–996 |
| 0.48 | 5655 | 5595–6989 |

Matched random strings reproduce the dip counts and last-dip positions essentially exactly. **So NO measurable regularity of ν₂ is prime-specific**: every statistic — the white-noise law, the second-moment plateau, the rising per-window minimum, the dip sparsity — is what any balanced "unstructured" input achieves (iid at the measured prime switch density p≈0.585), and the primes merely sit in that generic-good class. This is the honest negative frame, and it is now *complete*.

## Consequence for GOAL

The barrier is exactly as the prior runs stated: proving `E[S²(n)] = O(n)` for the **specific prime string** h requires an arithmetic input about the primes beyond generic baldness. The candidates priced (raw-h autocorrelation — trivially satisfied by iid, `bounded-raw-autocorr-not-discriminating`; second-moment — the plateau is fold-generic) show no arithmetic handle specific to the primes is visible in the data. The weakest-input project (GOAL priority 2) is still open and unchanged: a submask-window second-moment / Walsh bound on h is strictly weaker than pointwise switch density, and would carry the whole density-1 form — but the data gives no evidence the primes satisfy anything `h`-specific that iid does not.

**Recommendation:** the highest-value, most-likely-derivable target remains the density-1 form via `E[S²]=O(n)`. The geometric side is proved (`fold-distance-enumerator-On`); the single open arithmetic statement is a second-moment / submask-window autocorrelation bound on the prime gap-parity string. A clean negative (the data supports no prime-specific regularity) would also close the GOAL's single hypothesis honestly: the fold `Φ` produces no observable work that the switch-density/frequency form cannot see — every output statistic is generic.

## Limitation stated plainly

A fit over finite terms is weak evidence; everything above is `measured` on n=2..40000 (and random trials ≤8000), a conjecture for all n. The sequence tools cannot extend a sequence — they only describe terms handed to them. The open arithmetic barrier (E[S²]=O(n) unconditionally for the primes) is not closed by any measurement here.
