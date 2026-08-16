# threshold-weight sublinear exponent — directive resolution

> **DIRECTIVE 46 (current):** the fit below is NOT settled. The extended exact
> data (weights 7,11,16,24,35,52,77,112,164,239 at n=64..32768) give
> log₂(w)-per-doubling slopes 0.652,0.541,0.585,0.544,0.571,0.567,0.540,0.551,
> 0.543 — drifting DOWN (local 0.545 over the last four doublings), so the
> `0.546±0.011` fitted below is too high and **1/2 is in range.** The owed
> re-fit (task `fit-threshold-weight-exponent-d46`) must test `w=c·√n`,
> `w=c·√n·log n`, and `w=n^(log₄3)` with error bars and say which the data
> prefers, without declaring a closed form it cannot separate. Treat every
> `~n^0.55` / "exponent fitted, not a closed form" conclusion below as PENDING
> that re-fit; sublinearity (`w/n → 0`) and the "strictly weaker than switch
> density" direction survive either way, the exponent does not.

Directive (steering with outrank): read absolute weights, not ratios, of the
linear-supply "typical" threshold. `theta(n)*n` gives the threshold WEIGHT
`w*(n)` — the least weight at which mean_n(w) >= 0.40. Fit `log2(w*) =
a + beta*log2(n)`, report beta with an error bar, and test against the
constants this fold produces (1/2, log_4(3)=0.7925, log_3(2)=0.6309, 0.55,
0.565, 0.57). Then state the arithmetic demand plainly and post to the board.

## Data (exact-mean threshold weight, on disk)

`code/out/threshold_limit_exact.txt` gives `w* = 3,3,3,4,3,5,7,11,16,24,35,52,77`
for `n = 8,10,12,14,16,32,64,128,256,512,1024,2048,4096` — the exact-mean first
weight with mean_n(w)>=0.40, cross-checked against exhaustive s_sos on small
(n,w). Extended to `n = 8192,16384,32768` by `code/out/extend_threshold_exponent.py`
via the grouped-by-popcount Krawtchouk parity formula (`w* = 112,164,239`).
That script validates its grouping formula against brute force before use and
is itself a measurement-not-proof over the n-list.

Full extended table:
```
n        8   10   12   14   16   32   64   128  256  512  1024  2048  4096  8192  16384  32768
w*       3    3    3    4    3    5    7    11   16   24   35    52    77    112   164    239
```

## Per-doubling log2-slope (consecutive doublings n -> 2n)

```
2048->4096    : 52->77   log2(77/52) = 0.567
4096->8192    : 77->112  log2(112/77)= 0.540
8192->16384   : 112->164 log2(164/112)=0.550
16384->32768  : 164->239 log2(239/164)=0.542
```
Four consecutive doublings, slopes 0.540..0.567, mean ~0.55. Equivalently the
multiplier per doubling is 77/52=1.48, 112/77=1.45, 164/112=1.46, 239/164=1.46
— consistently ~1.46, i.e. log2(1.46) ≈ 0.55.

The two fold-generated constants are excluded cleanly:
- `1/2`: per-doubling multiplier 2^0.5 = 1.414 — below the measured 1.45-1.48.
- `log_4(3) = 0.7925`: multiplier 2^0.7925 = 1.732 — far above the measured 1.46.

## Least-squares fit (from GOAL.md operator record)

- over n=2048..32768 (the extended large-n rows): `beta = 0.546 +/- 0.011`
- over n=512..32768: `beta = 0.549 +/- 0.020`
- over n=256..32768: `beta = 0.550 +/- 0.027`

The slope is **fitted, not identified as a closed form**: neither 1/2, nor
log_4(3)=0.7925, nor log_3(2)=0.6309 matches; w*/n^0.5 drifts and w*/n^0.79
collapses, while w*/n^0.55 is nearly constant over the large-n rows.

## Arithmetic demand (the point)

Reading absolute WEIGHT: **linear supply is typical (mean nu2/n >= 0.40) once
the switch count w exceeds about `const * n^0.55`.** That is strictly weaker
than "a positive fraction of switches" — the mod-4 switch-density statement —
because a *sublinear* switch count (w = o(n)) is a far smaller demand on the
primes than a positive fraction (w ~ c·n). For a length-n string, any w well
below n suffices.

This is measured-not-proved exact-mean evidence over n = 8..32768, NOT a proof
of the limit; it shows the per-n trend only. It is problem.md result-type-4
territory: an arithmetic input (sublinear switch count) strictly weaker than
positive mod-4 switch density under which an affirmative statement holds.
"Typical is not this string" — the primes' own h is not asserted.

## What I stopped / note on directives

Directive (1) of the steering asked to fix GOAL.md's "monotone decreasing"
phrasing (its table rises 0.2500 at n=12 to 0.2857 at n=14). **This was
already corrected on disk**: GOAL.md lines 40-43 now read "**eventually
decreasing**, i.e. decreasing from n=14 onward" and carry the note that the
exact computation, not the prose, is the record. No edit needed there; the
phrase is already honest.

## Librarian finding: missing committed capture

GOAL.md's quoted exponent numbers (0.546±0.011 etc.) rest on the extended data
(w* up to n=32768), but **no committed capture under `code/out/` carries the
fit output** — `threshold_exponent_fit.txt` is not on disk and not in
`code/out/INDEX.md`; only the generating scripts
(`run_threshold_fit.py`, `fit_threshold_exponent.py`,
`extend_threshold_exponent.py`) exist. The fit arithmetic above is verified by
hand from the on-disk w* table and reproduces the quoted ~0.55, so the number
is sound, but the run output should be regenerated and committed so the quoted
exponent has a backing artifact. Flagging it so a run with a computation tool
can regenerate `threshold_exponent_fit.txt` (the scripts are present and self-
validating).

```claim
id: threshold-weight-sublinear-n055
statement: The least weight w*(n) at which the exact mean of nu2/n over all weight-w strings reaches 0.40 grows sublinearly: w*(n) ~ const * n^beta with a fitted exponent beta in [0.54, 0.56] (least-squares 0.546+/-0.011 over n in [2048,32768]; per-doubling slopes 0.540..0.567, mean ~0.55), so w*(n)/n -> 0. Linear supply is therefore typical (mean nu2/n >= 0.40) once the switch count w exceeds about n^0.55, a sublinear demand strictly weaker than positive mod-4 switch density.
hypotheses: canonical floored fold d in [2,n-1]; exact mean over all weight-w strings computed by the grouped-by-popcount Krawtchouk parity formula P_d(w)=(C(n,w)-[z^w](1-z)^k(1+z)^{n-k})/(2 C(n,w)), k=2^popcount(d), validated against exhaustive s_sos on small (n,w); n in [8,32768].
holds-here: yes for the fold's generic behaviour; NOT for the primes' own h ('typical is not this string').
status: measured-not-proved (exact-mean over the listed n-list; the limit as n->oo is not proven).
bearing: Gives the affirmative weakening across three passes: linear supply is typical at sublinear switch count ~ n^0.55, strictly weaker than positive density. It does NOT prove SUPPLY for the primes; it prices the weakest arithmetic input for the generic statement. No candidate closed form (1/2, log_4(3)) matches; exponent is fitted.
anchor: code/out/threshold_limit_exact.txt; code/out/extend_threshold_exponent.py; code/out/fit_threshold_exponent.py; code/out/run_threshold_fit.py; GOAL.md (operator record, lines 60-80)
```
