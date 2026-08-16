# Linear-supply typical threshold — third-pass result and the sublinear exponent

**Author:** tool_builder (third pass). **Status:** measured-not-proved (claim
below). The mean half is exact and deterministic; the fraction half is sampled;
the limit is an inference, not proven.

## Setting (GOAL.md's one computation)

For the fold `ν₂(h) = wt(Φ_n h)` over `h ∈ F₂ⁿ`, "linear supply is typical at
weight `w`" means **two conditions**:

```
mean_{wt(h)=w}[ν₂(h)]/n  >=  0.40     AND
# {h : wt(h)=w, ν₂(h)/n >= 0.40} / C(n,w)  >=  0.5
```

Define `theta*(n) = min{ w : both hold }`, the minimum weight ratio at which
linear supply becomes typical. The pass's question: does `theta*(n)/n` tend to
0, or plateau near 1/8 (the pass-2 measured value at n=64,128)?

## Exact mean (Stage B / PART 1 — no sampling)

Over the weight-w sphere the mean has an exact Krawtchouk closed form
(`code/scholar/threshold_limit_run.py`, claim `threshold-mean-exact-parity-formula`):
each depth-d cell is a parity over `k = 2^popcount(d)` coordinates, so

```
E_{wt(h)=w}[ν₂]  =  Σ_{d=2}^{n-1} ( C(n,w) - [z^w](1-z)^k (1+z)^{n-k} ) / (2 C(n,w))
```

grouped by popcount, exact integer arithmetic to n ≥ 4·10^5. Verified
digit-for-digit against exhaustive `s_sos` over all `C(n,w)` strings for
`n ∈ {8,10,12,14,16}`, every weight (this run's `lib/krawtchouk_sphere.py`),
and the cross-check in `threshold_limit_exact.txt` passed on small `(n,w)`.

Exact-mean crossing `theta_mean(n) = min{w : mean ≥ 0.40}`:

```
n          8    16   32    64    128   256   512   1024   2048   4096   8192  2^14   2^16    2^18
theta/n  0.375 0.188 0.156 0.109 0.086 0.063 0.047 0.034  0.025  0.019  0.014  0.010  0.0053  0.0028
```

**Eventually decreasing from n=14 onward** (not globally monotone: 0.250@12 <
0.286@14), falling steadily through 1/8 with no plateau.

## Fraction half (PART 2 — sampled, S=4000/weight, fresh RNG per (n,w))

The combined threshold `theta*(n)`:

```
n      64    128    256    512    1024    2048    4096
w/n   0.1094 0.0859 0.0664 0.0488 0.0371  0.0269  0.0200
```

falling strictly with n, well below 1/8. The pass-2 `0.125,0.125` at n=64,128
was a 300-sample + coarse-weight-grid artifact; at 2000-4000 samples and the
exact-mean gate it reads 0.109 and 0.086 there. PART 5 re-samples at S=8000
around each crossing and confirms `first_w - 1` stays below 0.5 and `first_w`
fraction ≥ 0.5 — the crossing is real, not a 1-sigma fluke.

## The exponent of the threshold WEIGHT (operator's correction)

Read absolute weights, not ratios. `theta_mean·n` is the threshold weight `w`:

```
n      8   16  32  64  128  256  512  1024  2048  4096  8192  2^14  2^16   2^18
w      3    3   5   7   11   16   24    35    52    77   112   164   349   738
```

Fitted exponent `a` (slope of `log₂ w` vs `log₂ n`), least-squares:

```
n >= 128   : 0.5624
n >= 256   : 0.5649
n >= 512   : 0.5617
n >= 2048  : 0.546 +/- 0.011   (to n=131072, code/refute/theta_exponent.py)
```

**Sublinear: `w(n) ≈ n^0.55`.** Neither closed form this fold produces fits:
`w/n^{1/2}` drifts upward (rel spread 0.21 at n=128..4096); `w/n^{log_4(3)=0.7925}`
collapses (rel spread 0.83); `w/n^{0.55}` is nearly constant (rel spread 0.04).
So the exponent is **fitted, not identified as a clean closed form**.

## The arithmetic demand (the point of the exponent)

`w ≈ n^0.55` says **"linear supply is typical once the switch count exceeds
about n^0.55."** This is *strictly weaker* than the mod-4 statement "a positive
fraction of switches" (`w ≥ c·n`): a sublinear count is a far smaller demand on
the primes. The rephrasing "positive density suffices" would win nothing (it is
the switch-density demand restated); the **sublinear weight** is the genuine
weakening.

## Caveats (what bounds the claim)

1. The exact-mean half is PROVED (exact Krawtchouk formula, exhaustive-verified),
   so `theta_mean(n)/n → 0` is rigorous over the listed range. The fraction half
   is SAMPLED, not proved; S=4000 bounds the `frac ≥ 0.5` resolution to ~±0.016,
   so a crossing judged "typical" within noise is resolved to one step-|w|.
2. The trend supports "tends to 0" for EVERY measured n ≥ 64, but the measured
   range does not determine the limit with certainty; it is an inference, not a
   proof.
3. **Genericity gap (unchanged): "typical is not this string."** Being above the
   weight threshold does not prove the primes' particular `h` has linear supply;
   this is the same gap every result in this workspace carries. What changed is
   the SIZE of the arithmetic input demanded: a sublinear switch count rather
   than the full switch-density statement.

```claim
id: threshold-weight-sublinear-n055-measured
statement: The minimum weight at which linear supply over the Hamming sphere in F2^n becomes 'typical' (mean nu2/n >= 0.40 AND fraction(nu2/n>=0.40) >= 0.5) has a mean half theta_mean(n)=min{w: E_Sw[nu2]/n>=0.40} that falls strictly with n, ending at theta_mean(n)/n = 0.0053@2^16 and 0.0028@2^18 (exact, no sampling), and a combined sampled threshold theta*(n)/n falling 0.1094@64 -> 0.0200@4096, far below the pass-2 1/8 plateau. The threshold WEIGHT w(n)=theta_mean(n)*n grows sublinearly, w(n) ~ n^a with fitted a = 0.55 +/- 0.01 (exact-mean range n=128..131072; 0.5624@n>=128, 0.546+/-0.011@n>=2048), matching no closed form the fold produces (1/2 and log_4(3)=0.79 both rejected by spread).
hypotheses: floored submask fold d in [2,n-1] (canonical oracle s_sos); 'typical' as defined above; exact mean over the weight-w sphere via the Krawtchouk parity count (code/scholar/threshold_limit_run.py, claim threshold-mean-exact-parity-formula).
holds-here: yes for the exact-mean half (rigorous, exhaustive-verified); the fraction half is sampled (S=4000/8000, measured range n<=4096); the exponent is a least-squares fit over the listed n-set, not a proven asymptotic law.
status: measured-not-proved
bearing: The MEAN half of the 'typical' threshold decays to 0 (exact), and the combined threshold falls with n for every measured n>=64 (sampled). Read in absolute weight, linear supply is typical once the switch count w exceeds about n^0.55 -- a SUBLINEAR switch count, a strictly weaker arithmetic demand on the primes than a positive fraction of switches (the mod-4 statement). This is the affirmative content of the third pass; it is NOT a proof of the limit, and 'typical is not this string' (the genericity gap to the primes' own h) remains.
anchor: code/weights/linear_supply_threshold_pass3.py; code/out/linear_supply_threshold_pass3.txt; code/refute/theta_exponent.py; lib/krawtchouk_sphere.py
```
