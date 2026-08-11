# PE591 — Best Approximations by Quadratic Integers: derivation

## 1. Reduction of the problem

For non-square `d`, `BQA_d(pi, n)` = argmin over integer pairs `(a, b)` with
`|a| <= n`, `|b| <= n` of `|pi - (a + b*sqrt(d))|`. The integral part is
`I_d(a + b*sqrt(d)) = a`.

Fix `b` first. The best `a` for that `b` is the nearest integer to
`pi - b*sqrt(d)` (clamped to `[-n, n]`; for the data here the winner never
saturates). The resulting error is

```
|pi - (a + b*sqrt(d))|  =  ||b*sqrt(d) - pi||_Z        (distance to nearest integer)
```

Write `alpha_d = {sqrt(d)} = sqrt(d) - floor(sqrt(d))` and `beta = {pi} = pi - 3`.
Since integer parts vanish modulo 1:

```
||b*sqrt(d) - pi||_Z  =  ||b*alpha_d - beta||_Z ,        alpha_d in (0,1), beta in [0,1).
```

Both signs of `b` matter (`BQA_2(pi,10) = 6 - 2 sqrt(2)` has `b = -2`).
`b > 0` is the problem for `+beta`; for `b < 0`, put `m = -b > 0`:

```
||-m*sqrt(d) - pi||_Z  =  ||m*alpha_d + beta||_Z  =  ||m*alpha_d - (1 - beta)||_Z
```

so the negative-b side is the same problem with `beta' = 1 - beta = {-pi}`.
The bound `|b| <= n` becomes `b in [0, L]` with `L = floor(n / sqrt(d))` (and
the same `L` on the `beta'` side).

**Work per d (n = 10^13):** compute the exact minimum of `f(b) = ||b*alpha_d - beta||_Z`
over `0 <= b <= L ~ 10^13 / sqrt(d) ~ 3.4e11 .. 1e13`, and of the same function
with `beta'`; take the global smaller error; then
`a = nint(pi - b*sqrt(d))` with the sign of `b` kept, and add `|a|`.

A scan over `[0, L]` is impossible (L ~ 10^13 for each of 90 d). The following
theorem makes the minimizer findable from an O(log L)-sized list.

## 2. Governing theorem (Cabanillas, arXiv:1904.01874)

**Source:** E. Cabanillas, *A variant of Ostrowski numeration*, arXiv:1904.01874v2
(https://arxiv.org/abs/1904.01874, PDF https://arxiv.org/pdf/1904.01874),
Sections 2.3 and 4.3. Precise statement transcribed in
`research/cabanillas_prop9_10_exact_statement.md`; see also the summary
`research/cabanillas_variant_pdf.md`.

**Setup.** alpha in [0,1) with continued fraction [a_k]; convergent denominators
q_k with q_{-1} = 0, q_0 = 1; delta_{-1} = 1, delta_0 = alpha,
delta_k = -a_k * delta_{k-1} + delta_{k-2}, so delta_k = |q_k*alpha - p_k| -> 0.

**Definition 6 (best alpha-approximation).** `{n*alpha}` is a *best
alpha-approximation of beta* iff `||n*alpha - beta|| < ||k*alpha - beta||` for
every `0 <= k < n`. A best alpha-approximation is a best **right** or best
**left** alpha-approximation of beta.

**Algorithm 3(ii) — the alpha-numeration of beta in [0,1).**
With `beta_0 = beta`:

```
b_k = min(a_k, ceil(beta_{k-1} / delta_{k-1})),   beta_k = b_k * delta_{k-1} - beta_{k-1},   k = 1, 2, ...
```

The digit sequence (b_k) is the alpha-numeration of beta.

**Proposition 9 (best RIGHT positive approximations, alpha irrational).**
`{n alpha} >= beta` is a best right alpha-approximation of beta only for:
n = 0; the terminal prefix `n = sum_{i=1}^s b_i q_{i-1}` (if b_k = 0 for all
k > s); and

```
n = sum_{i=1}^{2k-1} b_i q_{i-1} + j * q_{2k-1},   j in {0, ..., b_{2k} - 1},  k >= 1.
```

**Proposition 10 (best LEFT positive approximations, alpha irrational).**
`{n alpha} <= beta` is a best left alpha-approximation of beta only for:
the terminal prefix as above; and

```
n = sum_{i=1}^{2k} b_i q_{i-1} + j * q_{2k},   j in {0, ..., b_{2k+1} - 1},  k >= 0.
```

## 3. Why it applies, and what it reduces the work to

- **Hypotheses.** `alpha = {sqrt(d)}` with d non-square is irrational (the
  irrational-alpha Case 2 of Props. 9/10); `beta = {pi} in [0,1)` and
  `beta' = 1 - beta in [0,1)` fall in the stated range. Nothing requires beta
  to be irrational.
- **Consequence.** The sequence `n -> ||n*alpha - beta||` has its *record*
  values exactly at the best alpha-approximations (Def. 6), and each best
  alpha-approximation is right or left; therefore the **global minimum over
  `n <= L` is attained in the union of the Prop. 9 and Prop. 10 candidate lists
  restricted to `n <= L`** (plus n = 0). This holds for beta and, separately,
  for beta' = 1 - beta, covering both signs of b.
- **Cost.** q_k grows at least geometrically (q_k >= Fibonacci_k), so only
  `k = O(log L)` and `O(log L)` candidates survive `n <= L`. For L ~ 10^13 the
  per-d work is a few hundred candidates, each an exact integer built from the
  alpha-numeration digits; no scan of [0, L] is needed.

## 4. Algorithm (solution_bothsides.py)

For each of the 90 non-square d in [2, 99], with n = 10^13:

1. `L = floor(n / sqrt(d))`; compute the CF terms a_k of alpha = {sqrt(d)} and
   denominators q_k (mpmath, 80 digits; number of terms increased until
   `q_k > 4*L` so the candidate construction is fully resolved).
2. Compute the alpha-numeration (b_k) of beta = {pi} and of beta' = 1 - beta
   by Algorithm 3(ii) (exact integer digits from the real arithmetic).
3. Generate Prop. 9 + Prop. 10 candidate n's (both parities of k, all j up to
   the digit bound), keep `0 <= n <= L`, dedupe; same set for beta'.
4. Select the candidate with minimal `||n*alpha - beta||` on the beta side and
   on the beta' side; the smaller error decides the sign of b:
   `b = +n` (beta side) or `b = -n` (beta' side).
5. `a = nint(pi - b*sqrt(d))`; record `(d, b, a, |a|)`.

All arithmetic is exact integer except the final float-position comparison of
candidate distances, done at 80 decimal digits with the rigorous gap between
candidates far above the 1e-80 working precision (validated below against brute
force at scales where brute force is feasible).

`S = sum |a_d|` over the 90 rows.

## 5. Verification

- **Statement oracle.** `brute.py` (naive scan of (a,b) in [-n,n]^2,
  a = round(pi - b sqrt(d)) clamped) reproduces examples 1-3:
  (6,-2), (-55,26), (560323,-211781). `solution_bothsides.py` reproduces all
  four examples including `I_2(BQA_2(pi,10^13)) = -6188084046055`
  (b = 4375636191520), i.e. example 4 at full scale.
- **Independent route (brute force at the largest reachable scales).**
  `brute_n7.py` scans all b in [-L, L] at mpmath dps=40 for 16 d at n = 10^7;
  the solver run at the same n matches (b, a) **exactly on all 16 d**
  (`verify_n7_rerun.py`). `toolkits/validate_bothsides.py` scans all 90 d,
  both signs of b, at n = 10^6: zero mismatches vs the solver at the same n.
- **Independent re-sum.** The |a| column of `results_full_bothsides.txt` was
  re-summed with exact integers, bypassing the solver's accumulator:
  526007984625966, equal to the printed S.
- **Structural laws.** |a_d| = |nint(b_d*sqrt(d) - pi)| on 90/90 rows; the
  m^2-divisibility scaling law holds 36/36.

## 6. Result

```
S = 526007984625966
```