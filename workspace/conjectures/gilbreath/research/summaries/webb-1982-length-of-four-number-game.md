# Webb, "The Length of the Four-Number Game", Fibonacci Quarterly 20.1 (1982) 33–35

Source: https://www.fq.math.ca/Scanned/20-1/webb.pdf (full text at
`research/sources/webb-1982-length-of-four-number-game.full.md`).

## What it establishes

The four-number game is the cyclic Ducci map on 4-tuples with the
(in this paper) specific ordering `D(w,x,y,z) = (|w−z|, |w−x|, |x−y|, |y−z|)`.
Every integer 4-tuple reaches `(0,0,0,0)` in finitely many steps (length
`L(S)`), and the paper answers *how long* a game can be in terms of the
initial maximum.

- **Max is non-increasing under D** (opening observation, `|Sₙ₊₁| ≤ |Sₙ|`
  where `|S| := max` of the tuple) — the same Lyapunov fact the run proved
  for the half-infinite Gilbreath operator.
- **Theorem 1**: if `max(S) ≤ tₙ` (n-th Tribonacci number, `t₀=0, t₁=1, t₂=1,
  t_k = t_{k−1}+t_{k−2}+t_{k−3}`), then `L(S) ≤ L(Tₙ)+1 = 3⌊n/2⌋+1` where
  `Tₙ = (tₙ, t_{n−1}, t_{n−2}, t_{n−3})`. **Game length is bounded by the
  initial max; and unbounded as a function of max** (e.g. `L(Tₙ) = 3⌊n/2⌋`).
- **Run structure forces the dynamics**: `L(S) ≤ 6` unless the initial tuple
  is monotonically decreasing (up to cyclic permutation and reversal); and a
  long game must pass through a sequence of monotone-decreasing tuples with
  "additive" structure (ratios approaching the real root `r ≈ 1.839` of
  `x³ − x² − x − 1 = 0`, the Tribonacci constant). This is a direct primary
  statement of *oscillation/run-shape determining iteration length* — the
  mechanism the run's `total-variation-oscillation-potential` approach asked
  the literature for.
- Extremal structure: `L(S) = L(Tₙ)+1` is attained (e.g. by
  `(tₙ, t_{n−2}+t_{n−3}, t_{n−3}, 0)`).

## Relation to this run

Webb's "no uniform bound" fact (lengths arbitrarily large for large inputs)
is the cyclic-case limit superseded for the half-infinite object by
Eppstein's anti-Gilbreath construction — this run already knows the general
2-then-odds class escapes. What survives is the **proof template**: max is a
Lyapunov function, and the *run-shape* (monotonicity) of the tuple classifies
which dynamics are possible; non-monotone inputs die in ≤ 6 steps in the
cyclic world.

**Caveat — do not read this as support for the run's raw run-count
potential.** The run's own machine refutation
(`code/out/check_runcount_lemma.py`, `check_runcount_lemma.captured.txt` +
`check_runcount_lemma_class.captured.txt`, exhaustive over 6,725,600 strings
and over the halved {0,1} class the triangle actually lives in) refutes
`r(T(x)) ≤ r(x)` and `t(T(x)) ≤ t(x)` for the half-infinite operator
T(x)_i = |x_i − x_{i+1}|: first counterexample (6,6,6,6,6,6,5,5) (2 runs → 3),
and inside the {0,2} regime (0,0,2,2) → (0,2,0) (2 runs → 3). Webb's
monotonicity theorem is a cyclic-4-tuple statement about the *initial tuple's
shape* controlling *game length* — a different, weaker claim than a per-step
monotone potential, and it does not survive transfer to the nonlinear
half-infinite operator. The corrected-direction template (factored-max/weighted
run count à la Chamberland's Ducci proof) is what survives from this family;
the approach file records the status as refuted.

```claim
id: webb-four-number-game-length-tribonacci
statement: For the cyclic four-number game D(w,x,y,z)=(|w−z|,|w−x|,|x−y|,|y−z|), if max(S0) ≤ t_n (Tribonacci) then the game reaches zero in at most 3*floor(n/2)+1 steps; lengths are unbounded as the initial max grows, and any game of length > 6 must begin (up to symmetry) with a monotonically decreasing tuple.
hypotheses: 4-tuples of nonnegative integers; cyclic closure |a−b| wraps around.
holds-here: no (cyclic 4-tuple setting; the half-infinite Gilbreath triangle is neither cyclic nor length-4)
status: proved (in source); primary source landed
bearing: primary antecedent of the total-variation-oscillation-potential approach; confirms the run-shape-controls-dynamics mechanism and gives the exact potential template (max non-increasing + monotonicity classification) that the approach proposes to localize to a left window
anchor: research/sources/webb-1982-length-of-four-number-game.full.md
answers: is-there-a-variationdiminishing-theorem-for-the-difference-map
```

## What could not be obtained

Webb's paper itself is free (FQ archive). The related papers it cites —
Zvengrowski 1979 (Math. Mag. 52(1) 36–37) and Beardon 2011 (Am. Math. Monthly
118(7) 650–652, "Cyclic Absolute Differences of Integers") — are paywalled
at Math. Mag./AMM; no free scan was found in this cycle. Both are cyclic-case
Ducci statements; their content is partially covered by the free primary
papers Ciamberlini–Marengoni 1937 (via the Ducci surveys), Glaser–Schöffl
1995 and Calkin–Stevens–Thomas 2005 already in the library, plus the
Brown–Merzel limiting-behavior theorem quoted in CZ 2011.