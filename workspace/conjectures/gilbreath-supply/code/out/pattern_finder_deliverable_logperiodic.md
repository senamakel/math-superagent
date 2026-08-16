# Pattern-finder deliverable — threshold-weight log-periodic structure (directives 45/46/47)

**Role:** pattern_finder (adversarial school). **Result:** the third pass's one
open computation — the structure of the linear-supply weight threshold — is
decisively resolved by exact computation extended to n=65536.

## The finding

The exact-mean linear-supply threshold weight

```
w*(n) = min { w : mean of ν₂(h)/n over all weight-w strings h ∈ F₂ⁿ ≥ 0.40 }
```

(mean half exact, closed form; no sampling) satisfies

```
w*(n) = n^0.555 · P(log₂ n)
```

where `P` is a **bounded, period-1-in-log₂(n) log-periodic factor of amplitude
≈ 0.07**. This is the classical Pascal-mod-2 counting-function fluctuation form
(OEIS A006046 structural analogy), and it is now **confirmed**, not just
conjectured.

## What each hypothesis test found (exact over n=256..65536)

| hypothesis | test | verdict |
|---|---|---|
| `w = c·√n` (1/2) | phase-1.0 OLS E=0.55499±0.00202, 27σ from 0.5; w²/n rises 0.77→1.74 not flat | **rejected** |
| `w = c·n^{log₂3−1}` (0.58496) | residual monotone-drifts 0.624→0.531 (spread 0.093); 14.8σ | **rejected** |
| `w = c·√n·(log n)^g` | best g=0.44 but E then not sublinear-power; subsumed | rejected as power |
| `5/9 = 0.5556` closed form | NOT separable from 0.555 (identical residual sd 0.01466; exponent gap 30× below periodic swing) | **plausible, not established** |
| log-periodic `n^0.555·P(log₂ n)` | flat at each fixed phase across 9 doublings; phase means differ by amplitude 0.069 | **confirmed** |

## Verdict

- `θ = w*/n → 0`: the mean half of linear supply is satisfiable at a sublinear
  switch count.
- Threshold weight `~n^0.555` ⇒ **linear supply is exact-mean-typical once the
  switch count exceeds ~n^0.555 switches** — a strictly weaker arithmetic demand
  on the primes than positive mod-4 switch density (`Θ(n)`).
- **This is problem.md result type 4** (input strictly weaker than switch
  density), the workspace's first affirmative weakening across three passes.
- One-sentence genericity gap, unchanged: **typical is not this string**.

## Honest bounds

- Per-n `w*` and `θ` are **exact** for n=8..65536 (closed-form mean; independent
  linear-scan reproduction of all 16 known values).
- The limit (→0), the exponent (~0.555) and the log-periodic amplitude (~0.07)
  are **fitted** over n ≤ 65536 — measured, not proved.
- `1/2` rejected >25σ; `log₂3−1` rejected >14σ; `5/9` plausible but **not
  separable** from the fitted 0.555 (do not declare it).

## Files

- `code/out/threshold_weight_logperiodic_extended.txt` — the decisive capture
- `code/pattern_finder/threshold_linearscan.py` — independent exact reproduction
- `code/pattern_finder/log_periodicity_extend.py`, `log_periodic_quantify.py`
- `code/pattern_finder/phase1_exponent.py`, `directive47_compare.py`,
  `mechanism_E.py`, `closedform_scan.py`, `closedform_nonseparable.py`
- `research/CONCLUSION-PASS3.md` — updated with the confirmed decomposition

**Status: measured-not-proved.** The per-n values are exact; the exponent and
log-periodic factor are numerical fits over the sampled range.
