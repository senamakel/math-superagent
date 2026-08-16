# Pattern-finder deliverable 4: the fourth-moment plateau — the exact upgrade input from density-1 to finite exceptional sets

**Role:** pattern-recognition specialist. All numbers exact over the canonical
`code/out/nu2_primes_xor_40000.json` (guards ν₂(53)=18, ν₂(64)=27,
ν₂(4000)=1975, ν₂(40000)=20081 all reproduced). Every structural statement is a
**conjecture** for all n, verified exactly on n=2..40000, and labelled
`measured`, not `proved`.

## The object and its input-hierarchy position

With `S(n)=(n−2)−2·ν₂(n)` (signed excess) and `Z(n)=S(n)/√n`, pointwise SUPPLY
(any c<1/2) is `S(n)=o(n)`, equivalently `ν₂(n)/n→1/2`. The run's open target
(GOAL priority 1, claim `prime-E-S2-On-sharp-conjecture`) is the second moment
`E[S(n)²]=O(n)` (`E[Z²]=O(1)`), which by Chebyshev gives only **density-1**
SUPPLY.

The new measurement: the fourth moment plateaus *too*.

## Measured facts (exact over n=2..40000, canonical oracle)

### 1. E[Z⁴] settles at ≈2.95, no upward drift
| block | E[Z²] | E[Z⁴] | kurtosis |
| --- | --- | --- | --- |
| [4096,8192) | 1.014 | 3.032 | 2.95 |
| [8192,16384) | 1.014 | 3.013 | 2.93 |
| [16384,32768) | 0.989 | 2.894 | 2.96 |
| [32768,40001) | 0.986 | 2.832 | 2.91 |
| **all [2,40000]** | **0.9990** | **2.9474** | **2.953** |

Kurtosis is ≈3 (the Gaussian value) with 4th moment settling to ≥2.83 in every
dyadic block from 4096 upward; the early blocks (n<512, E[Z⁴] between 3.5 and
6) are finite-size fluctuations of the exact ±-sums and decay to the plateau.
Equivalently `E[S⁴]/n² → ≈2.9`, i.e. **`E[S⁴] = O(n²)`** with constant ≈3.

### 2. Pointwise max S²/n is bounded, no block drift
Pointwise `max S(n)²/n` over the whole range is **14.55** (at n=27624). Dyadic
block maxima: [16384,32768)=14.55, [32768,40001)=13.71, and every earlier block
is below 14.6. **No upward drift** in the pointwise constant C≈15. Put as a
pointwise bound, `|S(n)| ≤ 3.8·√n` on the whole measured range — the measured
form of the subgaussian tail whose proof is named in ROOT as the strongest
open input.

### 3. The consequence, stated precisely
If `E[S(n)⁴] ≤ C·n²` (with fixed C, any C) were **proved** for the prime string
h, then Chebyshev with the 4th moment gives
`P(|S(n)| > cn) ≤ E[S⁴]/(c⁴n⁴) ≤ C/(c⁴n²)`, and the right-hand side is
**summable** in n. By Borel–Cantelli, almost surely (in the probabilistic
language; deterministically, since |S(n)|/n is a fixed sequence, the bound is
`|{n≤N : |S(n)|>cn}| = O(1)` — a bounded number of large deviations total), so
every exceptional set `{n : ν₂(n)/n < c}` for `c<1/2` is **finite**: full
pointwise SUPPLY (problem.md result 1/2), not merely density-1.

**This is the precise quantitative gap-sentence:** the difference between
"density-1 SUPPLY" (needs `E[S²]=O(n)`) and "pointwise SUPPLY" (needs a
summable tail) is exactly the difference between a 2nd- and a 4th-moment bound.
The measured E[Z⁴]≈2.95, E[S⁴]≈3n² with no drift, is the cleanest single
number in the data backing the target.

## Honesty checks

### Fold-genericity (the prior run's standard, applied here)
The 4th-moment plateau is **fold-generic, not prime-specific** — consistent
with the established complete-genericity frame. Exact fold of iid Bernoulli
strings at the measured prime switch density p≈0.585 (3 trials, n≤4000):

| input | E[Z²] | E[Z⁴] |
| --- | --- | --- |
| PRIMES [2,40000] | 1.0000 | 2.9508 |
| RAND p=.585 trial0 | 1.0128 | 3.2529 |
| RAND p=.585 trial1 | 1.0005 | 2.9428 |
| RAND p=.585 trial2 | 0.9663 | 2.7638 |

The primes sit inside the generic-balanced class for the 4th moment just as
they do for the 2nd. So the measurement gives the *target shape and constant*,
not a prime-specific mechanism.

### Negative direction the 4th-moment line cannot close
The 4th-moment bound has the SAME insufficiency the 2nd has: it is an
*unconditional arithmetic statement about the specific prime string h* that no
fold-generic argument reaches (the genericity result shows uniform h has it
too). So this is the same open arithmetic barrier (A), just one rung up in
moment. It does not escape the parity barrier; it sharpens what proving the
barrier's negation costs.

## What the sequence tools establish (exact over supplied terms, conjectures for all n)

- `ν₂(n)` n=2..401: **no constant-coefficient linear recurrence** of order
  ≤10; **not a low-degree polynomial** (12 differences not constant); only
  trivial parity residue periodicity. **OEIS miss** on the dyadic subsequence
  ν₂(2^k)=(0,2,2,12,13,27,66,136,243,502,1003,2010,4184,8338,16464) — no
  catalogue match, no closed form to look up.
- `S(n)`, `dS(n)=S(n+1)−S(n)`: no recurrence (≤8), not polynomial. dS is
  always odd (exact, 0 violations over [2,40000]) — the established parity
  fact, not noise.
- The only exploitable structure the tools find is **distributional**:
  S(n)=√n·Z(n), Z near-white (corr(S(n),S(n+1))=0.00015, ACF1(dS)=−0.5009,
  var(S)/var(dS)=0.5001 over the full range — all reproduced here), and now
  the 4th-moment plateau.

These conclusions were independently reproduced this run (the sequence tools do
not get novel verdicts for material already fed to them; the verdicts are the
same as in deliverables 2 and 3).

## Recommendation

The regularity most likely to yield a real theorem is unchanged from the prior
runs but now has a precise quantitative form: **prove `E[S(n)⁴]=O(n²)` for the
prime gap-parity string h** (measured constant ≈3, no drift), which — unlike
the 2nd-moment plateau — upgrades density-1 SUPPLY to **finite every
exceptional set, i.e. full pointwise SUPPLY**, by a summable Chebyshev-Borel–
Cantelli step. The geometric side is already proved
(`fold-distance-enumerator-On`); the single open step is the unconditional
4th-moment bound for the specific prime string.

Honest boundary: the plateau is fold-generic, so the measurement supplies the
target and the constant, not a prime-specific mechanism. Whether the primes
satisfy any `h`-specific moment bound that iid fails remains open and is the
true arithmetic content.

## Files
- this note: `code/out/pattern_fourth_moment_upgrade.md`
- canonical data: `code/out/nu2_primes_xor_40000.json`
- fold oracle: `code/lib/supply_fold.py`, `code/lib/nu2.py`

```claim
id: fourth-moment-plateau-3n2
statement: For the prime gap-parity fold, the normalized excess Z(n)=S(n)/√n
with S(n)=(n−2)−2·ν₂(n) satisfies E[Z⁴]≈2.95 over n=2..40000 (kurtosis≈2.953,
settling to ≥2.83 in every dyadic block from 4096 up), equivalently
E[S⁴]≈3·n² (E[S⁴]/n²→≈2.9, no upward drift beyond the finite-n blocks) and
pointwise max S²/n=14.55 (C≈15, no block drift). If E[S⁴]≤C·n² were proved for
the prime h, Chebyshev-4th + summability would give |{n:ν₂/n<c}|<∞ for every
c<1/2 — full pointwise SUPPLY, not just density-1. Measured fold-generic:
iid Bernoulli at the prime switch density gives E[Z⁴] up to 3.25, so the
plateau is not prime-specific.
hypotheses: canonical nu2 json (guards ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975,
ν₂(40000)=20081); convention d∈[2,n−1]; n=2..40000 measured, 3 iid trials
n≤4000.
holds-here: yes, within the computed range — measured evidence, not a proof.
status: checked
bearing: names the exact quantitative input that would upgrade density-1 SUPPLY
(GOAL priority 1) to pointwise SUPPLY (problem result 1/2): a 4th-moment bound
in place of the 2nd. Same parity barrier as the 2nd-moment target, one rung up;
no prime-specific mechanism visible in the data.
anchor: code/out/pattern_fourth_moment_upgrade.md
```
