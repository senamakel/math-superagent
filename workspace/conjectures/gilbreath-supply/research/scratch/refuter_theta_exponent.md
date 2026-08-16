# Refuter — attack on "about n^0.57 switches suffice" (threshold-weight exponent)

**Status: analysis + hand arithmetic against the on-disk exact column; not a
TPTP model search (reason below).**

## The claim under attack (steering directive / GOAL.md third-pass head)

The exact Krawtchouk mean threshold weight `theta(n) = min{w : E_Sw[nu2]/n >= 0.40}`
is reported as

```
n     8   10  12  14  16  32  64  128  256  512  1024  2048  4096
w     3    3   3   4   3   5   7   11   16   24    35    52    77
```

and the directive reads the per-doubling slope of `log2(w)` vs `log2(n)` as
settling near 0.57, hence "about n^0.57 switches suffice" — a sublinear demand,
argued to be strictly weaker than a positive fraction.

I attack two things, with deliberately honest strength:
1. that "0.57" is a settled constant that is a clean closed form — I claim the
   data cannot establish it, that the run's own theory says the exponent drifts
   to 1/2, and that 0.79 (the only alternative candidate given) is refuted;
2. that this represents a weakening of the arithmetic demand on the *primes* —
   I claim it cannot, because the result is over random weight-w strings and the
   transfer to the fixed prime string is exactly the unproven part.

## 1. The closed-form test, done honestly

The directive offers candidates `log_4(3)`, `1/2`, `log(3)/log(4)`. Note first
that `log_4(3)` and `log(3)/log(4)` are the **same number**,
`ln3/ln4 = 0.792481`. So there are two distinct candidates: **0.7925** and
**1/2**. The directive's "0.57" is not one of its own list — it is the best
*constant* fit to the short measured window, which is exactly why it must not be
treated as a closed form.

Per-doubling slopes of `log2 w` vs `log2 n` from the exact column:

| transition | w | slope |
|---|---|---|
| 8→16 | 3→3 | 0 (*) |
| 16→32 | 3→5 | log2(5/3)=0.737 |
| 32→64 | 5→7 | log2(7/5)=0.485 |
| 64→128 | 7→11 | log2(11/7)=0.652 |
| 128→256 | 11→16 | log2(16/11)=0.541 |
| 256→512 | 16→24 | log2(24/16)=0.585 |
| 512→1024 | 24→35 | log2(35/24)=0.544 |
| 1024→2048 | 35→52 | log2(52/35)=0.571 |
| 2048→4096 | 52→77 | log2(77/52)=0.568 |

(* the 8→16 row gives 0 exactly, which is why the directive omits it; it is a
small-n transient, not part of any claimed regime.)

window-mean of the last six slopes: (0.485+0.652+0.541+0.585+0.544+0.571+0.568)/7
≈ 0.564; last three ≈ 0.561. So within the observable window L=5..12 the slope
sits near 0.56–0.57 with scatter ±0.05, no clear monotone trend.

**Candidate 0.7925 (log_4 3).** REFUTED on the existing column: the measured
slope is 0.54–0.57 at L=5..12, and nothing in the column is close to 0.79. To
reach 0.79 the slope would need a sharp upward turn past L=12 that the run's own
saturation theory rules out (below). Decisive on existing data.

**Candidate 1/2.** The run's own theory
(`research/notes/scholar_threshold_exact_mean.md`, "asymptotic saturation")
predicts, for fixed density alpha and popcount concentration,

```
w ~ n^{1/2} * 2^{0.42 sqrt(log2 n)},   i.e.  log2 w = L/2 + 0.42 sqrt(L)
```

with slope `d log2 w / dL = 1/2 + 0.21/sqrt(L)`. At L=12 the theory predicts
0.561; the measured last-three mean is 0.561. **The data are consistent with the
drift-to-1/2 hypothesis to well within the scatter.** 1/2 is the honest closed
form (limit), with a subpolynomial correction on top.

**So the honest statement is `w ~ n^{1/2+o(1)}`**, and "0.57" is a small-window
constant fit, not a settled limit and not a clean closed form. The sublinear
conclusion survives; the numeric coefficient as a claimed *limit* does not.

**Limitation stated plainly.** At n=4096 (L=12), the constant-0.57 and
drift-to-1/2 hypotheses differ by only ~0.01 in slope, below the ±0.05 scatter.
Distinguishing them needs n ≳ 2^20 (L≈20, theory predicts 0.547, still only
0.02 below 0.57). So I cannot *prove* the exponent tends to 1/2 from these data
either; what is established is (a) 0.79 is wrong, (b) the data support 1/2 +
subpolynomial over a constant 0.57 (both fit; the former is the run's own
theory, the latter has no theoretical basis and a constant non-1/2 exponent
would contradict the concentration argument). `measured-not-proved`.

## 2. The demand on the primes is NOT weakened — the genericity gap is the whole difficulty.

The threshold result is a statement about **random weight-w strings** (uniform
on the sphere): a typical weight-w string has linear fold weight once
`w ~ n^{1/2+o(1)}`. This refines the already-settled `R-random-pointwise`
(`wt(Phi_n h) >= c n` w.h.p. for uniform h) only by showing a *sublinear* number
of ones already suffices for typicality.

The primes are one **fixed** string, and they do have ≈ 0.585n switches — far
more than n^0.57 — but that count is irrelevant unless the primes' specific
arrangement is *typical* (non-adversarial) for this fold, and that is exactly
what is unproven and is the goal itself (`typical is not this string` is the
run's own standing caveat). So the result does **not** lower the arithmetic
demand on the primes from "positive switch density" to "n^0.57 switches". It
lowers the demand *conditional on non-adversariality*, and non-adversariality
is the open problem. Reading the third pass as the first weakening *toward
SUPPLY* overstates it: it is a refinement of the fold-on-random statistic, not a
statement about the primes at all.

## 3. Why this is not a TPTP finite-model attack

The claim is asymptotic (`w ~ n^p`, `slope -> ?`), a limit over all `n`. It is
not a finite first-order property that a finite model could satisfy/falsify;
`find_counterexample` searches finite models falsifying a conjecture, which
cannot express "the exponent tends to c as n->infty". So I did not write a TPTP
file — encoding something asymptotic as finite would have reported the answer to
a different question. The attack is analytic + arithmetic against the exact
on-disk column (which is itself exact integer computation to n=4096, not an
approximation). This is the honest-encoding limitation the refuter rules name.

## What survives / what is refuted

- **Survives:** sublinearity (`w = n^{1/2+o(1)}`); the exact mean; monotone
  decrease of `theta/n` toward 0.
- **Refuted:** "0.57 is a settled exponent / clean closed form" — it is a
  small-window fit on a theory-predicted drift to 1/2; 0.79 (log_4 3) is wrong.
- **Refuted as stated:** "about n^0.57 switches suffice → weaker demand on the
  primes" — the exponent is the wrong number and the transfer to the primes is
  unproven; the honest form is `n^{1/2+o(1)}` switches suffice *for a typical
  random string*, which says nothing about the primes' fixed arrangement.

## Answer: which of the four

Attacked: the threshold-weight exponent claim (the pass's head, per steering).
Answer: **refuted** as stated (0.57/0.79 wrong as limits; 1/2 + subpolynomial
is the supported closed form), with the *sublinear* content surviving and the
primes-transfer left open. The refutation is arithmetic against an exact column,
not a finite-model search — declared explicitly.
