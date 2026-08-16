# Pattern-finder: the second-moment plateau reconciled, and its heavy-tail sparsity

```claim
id: primes-fold-second-moment-plateau-per-index
statement: >
  For the prime gap-parity string h (floored submask fold), the two apparently
  different variance scalings of S(n)=(n−2)−2ν₂(n) reported earlier (prefix
  mean of S² ≈ 0.5·N; window mean over [N/2,N] ≈ 0.75·n) are the SAME per-index
  fact E[S(n)²] ≈ n−2: the prefix mean of (n−2) over n≤N is ≈ N/2 and the
  window mean is ≈ 3N/4. Equivalently E[S(n)²]/(n−2) → 1 (the exact iid-uniform
  level). The heavy tail is sparse: max S(n)²/(n−2) < 16 uniformly over
  [50,131072] (max 14.55 at n=27624), fraction >9 ≈ 0.002 constant, mean
  ≈ 1.0. No 2-adic structure in D(n)=S(n+1)−S(n) (grouped by v₂(n) and n mod 8,
  all noise-band); no sign bias (frac S>0 = 0.4986); the uniform |S(n)| ≤ 3.8√n
  bound survives to N=131072 (max 3.81 at [50,40000], 3.12 in [65536,131072]).
hypotheses: canonical floored fold; S(n)=(n−2)−2ν₂(n) exact; guard checks
  ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975 pass on the data used.
holds-here: yes (measured, two independent exact routes: N=40000 guard-checked
  json and fresh SOS-fold to N=131072).
status: measured-not-proved — the per-index convergence to (n−2) and the
  existence of a uniform E[S²]=O(n) bound for all n is a conjecture, not proved.
bearing: E[S²]=O(n) is exactly the arithmetic input (GOAL priority 2, weaker
  than positive mod-4 switch density) that, with condition (C) settled, yields
  result 3 (density-1 SUPPLY) by Markov/Chebyshev: Pr[ν₂/n<c] ≤ E[S²]/((1−2c)²n²)
  = O(1/n), summed to O(log N/N)→0 for every fixed c<1/2.
anchor: research/notes/pattern_finder_second_moment_plateau.md
```

Role: pattern-recognition specialist. All numbers exact integer/ratio arithmetic
from the canonical floored fold `S(n)=(n−2)−2ν₂(n)`, `ν₂(n)=wt(Φ_n h)`, over
the guard-checked N=40000 data (`code/out/nu2_primes_xor_40000.json`, verified:
ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975) plus fresh exact SOS-fold computation to
N=131072 (`code/pattern_finder/attack_second_moment.py`). Nothing here is a
proof for all n — every claim is a conjecture / exact measurement.

## The one original observation: the two "different" variance scalings are ONE fact

Earlier pattern-finder notes reported **two** scalings of `var(S)` as if they
were in tension:

- "prefix mean of S² ≈ 0.5·N"  (measured 0.497..0.512)
- "within-dyadic-window mean of S² ≈ 0.74..0.79·n"  (measured 0.736..0.787)

These are **not contradictory and not two scalings**. They are the same
per-index statement viewed at a different `n`:

    E[S(n)²] ≈ n − 2         (pointwise, per index n)

- Prefix mean  `(1/N)Σ_{n≤N} S(n)² ≈ (1/N)Σ(n−2) ≈ N/2`  → the "0.5N" number.
- Window mean over `[N/2, N]` ≈ mean of `(n−2)` there ≈ `(3/4)N` → the "0.75N" number.

So the correct, single claim is **`E[S(n)²] = (n−2)·(1+o(1))` per index** —
equivalently `E[S(n)²]/(n−2) → 1`. That is the iid-uniform-prediction level
and it is exactly the arithmetic input (GOAL priority 2's "second-moment
bound") that the Markov/Chebyshev density-1 argument needs. The reconciliation
is what removes the apparent discrepancy between the two prior reports.

## Measured (exact) support for the plateau, n ≤ 131072

`prefix-mean of S(n)²/(n−2)`:
```
N=1000  1.059    4000  1.026    8000  1.016    16000  1.016
N=20000 1.007    30000 1.003    40000 0.9996    131072 (half-window) 0.964
```
So the plateau is real and the excess `E[S²]−(n−2)` has **prefix mean O(1)**
(−111..+125 over N up to 40000), i.e. `o(n)` by two orders.

### Heavy-tail sparsity (the falsifier, attacked)
The risk to "E[S²]=O(n)" is a rare spike growing with n. Measured behaviour of
`S(n)²/(n−2)`:
- n ≤ 40000: fraction >1 is 0.319, >4 is 0.045, **>9 is 0.0025, >16 is 0**;
  max = 14.55 at n=27624.
- window [65536,131072]: max = 9.74, fraction >9 = 0.0020, **>16 = 0**;
  mean = 0.964.

So the spikes do **not** grow: max `S²/(n−2)` < 16 uniformly in [50,131072],
and the fraction of n with `S²/(n−2)>9` is ~0.002 and stays ~constant. The
distribution is heavy but spiked-sparse: the plateau is a mean statement
pushed up by a rare ~0.2% set, not by drifting excursions.

### The uniform √n bound (extends)
`max |S(n)|/√n` over [50,40000] = 3.81 at n=27624; over [65536,131072] = 3.12.
The `|S(n)| ≤ C√n` with C ≈ 3.8 uniform bound (which drives `s₂_N→0` and hence
density-1 SUPPLY via the analytic `s₂_N ≤ (C²/4)(log N)/N`) survives the
extension.

## What was attacked and did NOT hold (also a result)

1. **No dyadic/2-adic increment structure.** `D(n)=S(n+1)−S(n)` grouped by
   `v₂(n)` and by `n mod 8`: all group means are noise-band (std(D)≈200
   everywhere, group means from −43 to +5, erratic across v₂ with no trend).
   So no 2-adic regularity in the increments that a dyadic-martingale or
   automaton route could exploit. D is always odd (S parity = n parity).

2. **No sign bias.** Fraction of S>0 is 0.4986, S<0 is 0.4977, mean S = +0.52
   (tiny vs |S| mean ~106). The centered-at-zero assumption behind the
   Markov/Chebyshev tail argument holds empirically. Skew proxy tiny (+0.03).

3. **nu2 sequence not in OEIS** (confirmed on the correct canonical terms
   [2,1,2,1,2,1,6,3,4,2,...]; an earlier stale-file check had used the wrong
   `nu2_terms.txt` which lists 19/28 instead of 18/27 — the canonical guard
   sequence is 18/27).

## The honest structural statement

The densest, most lever-like, and now best-confirmed regularity is the
**per-index second-moment plateau `E[S(n)²] ≈ (n−2)`**, which:

- equals the exact iid-uniform prediction (strongest possible level for a
  bounded-autocorrelation input on `h`),
- survives to N=131072 with the spike set provably not growing (empirically
  bounded spikes),
- is exactly the Markov input that yields result 3 (density-1 SUPPLY) for
  every fixed c < 1/2 via `Pr[ν₂/n<c] ≤ E[S²]/((1−2c)²n²) = O(1/n)`, summed
  to `O(log N/N) → 0`.

The single open step remains: **prove** `E[S(n)²] = O(n)` for the prime `h`
(uniformly in n) from an arithmetic input weaker than positive mod-4 switch
density. The measurements here bound the difficulty: the constant is ≈ 1, the
spikes are rare and bounded, and the plateau is a mean statement about
`h`'s submask-window autocorrelation (the cross-term `ρ(d₁,d₂)` sum, whose
prefix mean is O(1)).

Verdict: this is the same second-moment input the prior run already named, but
now (a) reconciled into a single per-index fact, (b) given a bounded-spike
characterisation to N=131072, and (c) shown stable across the union of two
independent exact routes (N=40000 json and fresh SOS to 131072).
