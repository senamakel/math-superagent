# Pattern-finder deliverable: the exploitable structure in SUPPLY's data

## The one reconciled, best-confirmed regularity

**Per-index second-moment plateau.** `S(n) = (n−2) − 2ν₂(n)`, and
`E[S(n)²] ≈ (n−2) · (1+o(1))` per index — the exact iid-uniform-prediction
level. This single fact reconciles two earlier "divergent" scalings (the
0.5·N prefix mean and the 0.75·n window mean are the same `(n−2)` truth seen
at different `n`).

Verified two independent exact routes to N=131072:
```
prefix mean S²/(n−2):  1.059 (1k) → 1.026 (4k) → 1.016 (8k) → 1.016 (16k)
                       → 1.007 (20k) → 1.003 (30k) → 0.9996 (40k)
half-window mean:       0.964 (65536..131072)
```

**Why this is the lever.** `Pr[ν₂/n < c] ≤ E[S²]/((1−2c)²n²) = O(1/n)`
(Markov). Summed over `n ≤ N` gives dip density `O(log N / N) → 0` for every
fixed `c < 1/2` — **result 3, density-1 SUPPLY** — provided `E[S²] = O(n)`
uniformly. The primes sit at constant ≈ 1, the strongest possible level.

## Heavy-tail sparsity (attacks the falsifier, survived)

- max `S²/(n−2) < 16` uniformly over [50,131072] (max 14.55 at n=27624);
- fraction of n with `S²/(n−2) > 9` ≈ 0.002, constant;
- the plateau is a mean statement carried by a rare ~0.2% spike set, not by
  drifting excursions;
- the uniform `|S(n)| ≤ 3.8√n` bound (which drives `s₂_N→0`) survives to
  N=131072.

## What did NOT hold (also recorded so nobody rebuilds it)

- **No 2-adic/automaton structure.** `D(n)=S(n+1)−S(n)` grouped by `v₂(n)` and
  by `n mod 8`: every group mean is noise-band (std(D)≈200), no trend — no
  dyadic-martingale lever.
- **No sign bias.** frac S>0 = 0.4986, mean S = +0.5 (tiny): the centered-at-
  zero assumption behind Chebyshev holds empirically.
- **No recurrence / not in OEIS** — for both ν₂(n) and S(n), on the *correct*,
  guard-checked canonical terms ([2,1,2,1,2,1,6,3,...]). (A stale
  `nu2_terms.txt`, listing 19/28 instead of 18/27, had fed an earlier check;
  corrected here.)

## Handoff

The open arithmetic step is **prove `E[S(n)²] = O(n)` for the real prime `h`**
from an input weaker than positive mod-4 switch density (a submask-window
autocorrelation / second-moment / Walsh bound on `h`). The measurements bound
its difficulty: constant ≈ 1, spikes rare and provably non-growing (empirical),
no sign bias, no 2-adic obstruction. This is the named GOAL priority-2 /
priority-1 gap, now with the lever quantified and the falsifier (spike growth)
directly attacked.
