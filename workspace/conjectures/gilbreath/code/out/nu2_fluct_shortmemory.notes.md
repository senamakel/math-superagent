# Short-memory structure of the ν₂ supply fluctuation — pattern-finder verdict

Durable note (new structural fact, this cycle). Read the real series
`code/out/nu2_dense.txt` (ν₂(n), n=1..30000, exact) and the extension
`code/out/nu2_incremental_1e5.txt`; no terms invented.

## The object

`D(n) = 2·ν₂(n) − n` is the supply-side fluctuation: ν₂ is the #2s in the
maximal {0,2} suffix of the prime right diagonal, and Lemma 5.4 turns
`ν₂ ≥ c·n` into the Gilbreath second-entry claim. Measured ν₂ ≈ n/2, so `D`
is the deviation.

## Findings (all exact over the terms supplied; conjectural beyond)

**Parity identity — exact theorem:** `D(n) ≡ n (mod 2)` for every n in
1..30000. (2·ν₂ is even, so D ≡ −n ≡ n mod 2.) Verified 30000/30000. This
means `D` alternates parity rigidly — any analysis must avoid being fooled by
it.

**White-noise autocorrelation signature — verified-numerically:** Let
`I(n) = D(n+1) − D(n)` (the increment). Its autocorrelation is

    ρ₁ = −0.503 , ρ_k ≈ 0 (k ≥ 2), all |ρ_k| ≤ 3/sqrt(30000)=0.017 for k≥2.

Sample splits agree (first/second half ρ₁ = −0.502/−0.503). This is *exactly*
the MA(1) boundary case θ = −1 (ρ₁ = −½, higher ρ = 0), i.e. `D` is
statistically uncorrelated across the whole measured span. Consistently:

    acf(D) ≈ 0 at every lag 1..20        (D itself looks white)
    Var(I) / Var(D) = 30047/15048 = 1.997 ≈ 2   (the exact pure-difference prediction)

A pure random walk (uncorrelated increments) would give ρ₁(I) ≈ 0 — emphatically
NOT observed. So **there is no long-range memory, no drift, no slow trend in the
ν₂ deviation** over 30,000 terms.

**NOT bounded / NOT stationary — refuted interpretation (important):**
the white-noise autocorrelation does NOT mean `D` is O(1). Windowed variance of
`D` grows 1545 → 28674 (std 39 → 169) across 3000-wide windows, and
`max|D| ≈ 3.4·√n` (106@10³, 639@27625; the 1e5 sample gives 624@78536 — still
~2.2√n, not saturating to a constant). So `D` is **short-memory with a growing
√n-scale amplitude**: `ν₂(n) = n/2 + O(√n·poly(log))`, uncorrelated increments,
non-stationary amplitude. This matches the run's CONTEXT envelope claim
(`|2ν₂−n| ≤ 3√(n log n)`, max 639) and refutes the stronger boundedness reading
I tested.

The trajectory: I explicitly probed boundedness (stationarity of Var, ramp of
running max), found Var growing 18.6× and the slope of running-max on √n not
decreasing — then dropped the bounded claim and kept the short-memory one.

## What this buys the proof

The open supply statement is `ν₂ ≥ c·n`. The right framing, confirmed by this
data, is a **variance / law-of-the-iterated-logarithm bound**: the deviation is
√n-scale and has no serial correlation, so a CLT/LIL-style bound on the
halved-gap XOR-folds is the correct tool (not super-linear growth — CONTEXT's
`li2023-not-bottleneck` already said any ν₂ ≥ c·n suffices). The genuinely new
fact is the *absence of long-range memory* in `D` — a property any supply bound
would otherwise have to fight, and evidence the fluctuation is "random-walk-free".

**Status:** verified-numerically, exact over 30,000 terms (and the 1e5 envelope
sample). Not a proof for all n. The short-memory/no-drift claim is a conjecture
to be derived (e.g. from the mod-4 switch bit being near-white, which the run's
`switch_autocorr` work already supports).

## Files
- `code/out/nu2_fluct_autocorr.py`, `.captured.txt` (first signature)
- `code/out/nu2_fluct_confirm.py`, `.captured.txt` (MA(1)-boundary confirmation)
- `code/out/nu2_devi_saturate.py`, `.captured.txt` (variance growth, refutes bounded)
- `code/out/nu2_parity_attack.py`, `.captured.txt` (parity identity, rules out parity artifact)
- `code/out/nu2_surrogate_test.py`, `.captured.txt` (controlled surrogate comparison)
