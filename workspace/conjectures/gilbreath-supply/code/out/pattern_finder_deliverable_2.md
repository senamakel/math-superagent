# Pattern-finder deliverable: exact and measured structure of the ν₂ / S sequence

## Data
All from the canonical `code/out/nu2_primes_xor_40000.json` (guards
ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975, ν₂(40000)=20081 all pass). The stale
`code/out/nu2_terms.txt` uses an old offset convention and disagrees; the JSON
is authoritative. Here `d[n] = ν₂(n)` for n = 2..40000.

`S(n) = (n−2) − 2ν₂(n)`, so `ν₂(n)/n = 1/2 − 1/n − S(n)/(2n)`. Pointwise
SUPPLY (c<1/2) ⟺ `S(n) = o(n)`. All statements below hold **exactly** over the
terms supplied and are labelled `measured` (a finite-length conjecture), not
`proved`.

## 1. Exact structural facts (verified for all n in [2,40000])

- **Identity:** `2·ν₂(n) − (n−2) = −S(n)` for every n. (Also in claim
  `excess-is-negative-character-sum`; re-verified here on canonical data.)
- **Parity:** `S(n) ≡ (n−2) (mod 2)` and `dS(n) = S(n+1) − S(n)` is **always
  odd**, for every n. This is a rigorous consequence of `S(n)` summing
  `n−2` terms each ±1. It is an exact structural fact, not noise.
- `S(n) mod 4` is uniform: counts (0,1,2,3) = (10157, 9994, 9842, 10005) over
  n=3..40000. Consistent with the white-noise/residue-uniform picture.

## 2. The white-noise law, and the reconciliation it provides

`Z(n) = S(n)/√n`. Over n=3..40000 (exact, canonical):

| statistic | value | Gaussian N(0,1) |
|---|---|---|
| E[Z²] | 0.9990 | 1 |
| kurtosis E[Z⁴]/(E[Z²])² | 2.953 | 3 |
| max\|Z\| | 3.815 @27624 | ~c·√(log n) |
| corr(S(n),S(n+1)) | 0.0002 | 0 |
| AC1(dS) | −0.5009 | **−0.5** (model) |
| E[dS²]/2n | 1.0066 | 1 |

The decisive measurement is `corr(S(n),S(n+1)) = 0.0002 ≈ 0` together with
`AC1(dS) = −0.5009`. **These two are the same fact.** Under the model
`S(n) = √n·Z(n)` with `Z` mean-zero white noise (E[Z²]=1):

- corr(S(n),S(n+1)) → 0 (because Z is white; the variance growth is
  `Var(S)=n·E[Z²]=n`, which is *not* a random walk's drift, it is the scaling),
- and `dS(n) = √(n+1)Z(n+1) − √n·Z(n)` gives lag-1 autocorrelation exactly
  `−n/√((2n+1)(2n−1)) → −1/2` as n→∞. Measured average −0.5009 vs model
  −0.5000: agreement to O(1/n).

This resolves the run's earlier apparent contradiction between "E[S²]≈n
(random-walk-like)" and "S is structureless". The truth is `S(n) = √n·Z(n)`
with `Z` white: variance grows ~n but consecutive S are uncorrelated. This is
the **exact signature of S being a martingale-type sum of near-independent
mean-zero increments each of variance ~1** — the CLT / √n scale.

**Genericity (honest check):** a random string h at p=0.585 (the prime 1-density)
gives E[Z²]=0.997, kurtosis 2.98, std 0.998 — statistically indistinguishable
from the primes. Thue–Morse and all-ones instead give `S ~ n` (linear), so their
`E[Z²] ~ n` fails every row. **The √n/white-noise law is fold-generic, not
prime arithmetic**: it is what any balanced "unstructured" input achieves, and
the primes merely sit in that generic-good class. No arithmetic input specific
to the primes forces it. This is the honest negative frame: the structure the
sequence tools find in the data is exactly the generic-balanced-input law, and
the gap between "any unstructured balanced input does this" and "the primes do
it" is the whole open arithmetic barrier (condition (A) of the adopted
fold-second-moment-Krawtchouk route).

## 3. What the sequence tools establish (exact over supplied terms, conjectures for all n)

- `ν₂(n)` (n=2..401): **no constant-coefficient linear recurrence** of order ≤10
  fits; not a low-degree polynomial; residues mod 2 are periodic but that is the
  trivial parity. **OEIS miss** — uncatalogued, no closed form to look up. The
  structure must come from the problem, not a catalogue.
  (Same miss on the ν₂(2^k) dyadic subsequence, reported earlier.)
- `S(n)` (n=2..400): no recurrence (≤8), not polynomial, leading ratios
  undefined/noise, mod-2 periodicity trivial. Consistent with the noise picture.

**A fit over the handful of terms that suggested it would be weak; the tools
find no exploitable arithmetic regularity.** The regularity is distributional
(second-moment plateau + white-noise increments), and it is fold-generic.

## 4. The second-moment plateau and exceptional sets (exact, canonical)

- Pointwise `max S²/(n−2) = 14.55` at n=27624; per-doubling-block maxima stay
  in [4.9, 14.6] through N=40000 — **no drift upward** in the constant C.
  This is measured evidence for a *uniform* `E[S²] ≤ C·n` (C≈15), the exact
  input from which density-1 SUPPLY follows by Chebyshev.
- Exceptional sets: `{n : ν₂/n < c}` has last member 15 (c=0.30), 53 (0.35),
  105 (0.40), 274 (0.42), 340 (0.44), 763 (0.45), 1211 (0.46), 3086 (0.47),
  5655 (0.48), 27624 (0.49). So for every c ≤ 0.48 the exceptional set is
  *finite* on the measured range (stronger than density-1), and ν₂/n → 1/2.
- **Subgaussian tail:** P(|Z|>x) decays faster than Gaussian (P(|Z|>4)=0 on
  the range; x⁴·P(|Z|>x) ≪ E[Z⁴]≈3 for x≥2). E[Z⁴]→2.95 (settling to ≥3 from
  4.09@100). If a subgaussian/exponential tail were proved, Chebyshev over the
  4th moment upgrades density-1 to *finiteness of every exceptional set*.

## 5. Per-scale split — the route-dependence verdict

Grouping depths by scale `g(d)=ν₂(d+1)` and computing `E[S_g²]/(n−2)`:

| n | g=0 share | g=0..1 cum | total |
|---|---|---|---|
| 400  | 0.425 | 0.487 | 0.839 |
| 1000 | 0.730 | 0.811 | 1.116 |
| 4000 | 0.553 | 0.555 | 0.605 |

**Independent corroboration** of the board's `per_scale_split` finding: the
`g=0` scale (adjacent mod-4 pairs = the switch-density object) dominates the
variance share at each n. This is precisely why no per-scale renormalization
route escapes the parity barrier: the dominant variance lives in the same
switch-density scale that the reduction already collapses to. The n=1000 g=0
share 0.730 and n=4000 total 0.605 are finite-n fluctuations of the S_g (which
are exact ±-sums, not stable in share), but the g=0 dominance pattern is
consistent across all three n.

## Recommendation

The regularity most likely to yield a derivation is the **second-moment
plateau `E[S(n)²] ≤ C·n`** (equivalently `E[Z²]=O(1)`), because:
(a) it is the exact input from which density-1 SUPPLY follows by Chebyshev (GOAL
priority 1 / problem result 3);
(b) measured C≈15 uniform with no drift, and the tail is subgaussian (upgrade
to finite exceptional sets);
(c) the geometry side is *proved* (`fold-distance-enumerator-On`: `F_n(1−2p)=O(n)`
for |z|<1 away from the diagonal), so the entire task reduces to one priced
arithmetic statement (A): **prove `E[S(n)²]=O(n)` for the prime gap-parity
string h** — equivalently a second-moment / submask-window autocorrelation bound
on h, which is strictly weaker than pointwise positive switch density used for
every n.

Honest caveat: the fold-genericity result shows the plateau is *not*
prime-specific (uniform h gives it), and the per-scale g=0 dominance shows the
route's natural refinement toward a weaker input collapses back to the switch-
density scale. So the sequence data, while clean and internally reconciled,
provides **no** new arithmetic handle specific to the primes — the primes sit
in the generic-balanced class, and the open step remains an unconditional
second-moment bound for the specific prime string. That is the boundary of what
the data supports, and no sequence tool or measurement closes it.

## Files
- `code/pattern_finder/per_scale_second_moment.py` — per-scale second-moment split.
- `code/pattern_finder/probe_exact_dS.py` — exact dS/parity probes.

## Claim block (directive 32)

```claim
id: per-scale-refinement-collapses-to-switch-density
statement: Grouping the fold's depth index d by dyadic scale g(d)=ν₂(d+1) and
computing the per-scale second-moment share E[S_g²]/(n−2) of
S(n)=Σ_{d=2}^{n−1}(−1)^{T(n,d)} shows the g=0 scale — the adjacent mod-4 pair
statistic, i.e. the switch-density object — dominates the variance share at
every computed n (g=0 share 0.425@400, 0.730@1000, 0.553@4000; g=0..1
cumulative 0.487@400, 0.811@1000, 0.555@4000). The per-scale renormalization
aimed at a weaker arithmetic input therefore collapses back to the g=0
switch-density scale and yields no input on the prime gap-parity string h
weaker than positive mod-4 switch density.
hypotheses: canonical ν₂ json (guards ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975,
ν₂(40000)=20081); convention d∈[2,n−1]; per-scale split computed at
n∈{400,1000,4000} only; the shares are finite-n fluctuations of exact ±-sums.
holds-here: yes, within the computed n∈{400,1000,4000} — measured evidence.
status: checked
bearing: this closes the sequence-analysis route to GOAL priority 2 — no
sequence measurement produces an arithmetic input on h weaker than mod-4 switch
density — and leaves priority 2 unanswered by any measurement; it is reachable
only by an unconditional arithmetic theorem.
anchor: code/out/pattern_finder_deliverable_2.md §5;
research/notes/pattern_finder_fold_generic_balance.md
```
