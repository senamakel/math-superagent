# Boppana's binary-entropy inequality — exact symbolic verification

**Inequality (Boppana, arXiv:2301.09664):**
for the binary entropy `h(t) = −t·log₂t − (1−t)·log₂(1−t)` (any base) and the
golden ratio `φ = (1+√5)/2`,

```
h(t²) ≥ φ·t·h(t)      for all t ∈ [0,1].
```

**What it is.** This is the tight one-variable inequality driving the iid-OR
entropy method for Frankl's union-closed sets conjecture. Its saturation point
is exactly the `(3−√5)/2` barrier: the extremal distribution behind the iid-OR
argument saturates this inequality there, which is why that argument cannot
push the frequent-element constant past `(3−√5)/2 ≈ 0.382`. Alweiss–Huang–Sellke
(arXiv:2211.11731) verify Gilmer's explicit version of this inequality by
computer calculation; Boppana gives a clean differential-calculus proof.
Both are sourced (`research/sources/boppana-entropy-inequality-2023.full.md`,
`research/sources/alweiss-huang-sellke-barrier-2022.full.md`).

---

## 1. Exact equality at the saturation point

Let `φ = (1+√5)/2` (positive root of `x²−x−1=0`, so `φ² = φ+1`) and set

```
t₀ = 1/φ = (√5−1)/2   (positive root of t² + t − 1 = 0, so t₀² + t₀ = 1).
```

At `t₀` each step is exact:

1. **`φ·t₀ = 1`** — by definition of `t₀`, `φ·(1/φ) = 1`.
2. **`t₀² = 1 − t₀`** — from `t₀² + t₀ = 1`.
3. **Entropy symmetry:** `h(z) = h(1−z)` for every `z` (the two arguments are
   swapped). Hence `h(t₀²) = h(1−t₀) = h(t₀)`.
4. Therefore
   ```
   LHS = h(t₀²) = h(t₀)
   RHS = φ·t₀·h(t₀) = 1·h(t₀) = h(t₀)
   ```
   so `h(t₀²) = φ·t₀·h(t₀)` **exactly** — the inequality is tight here.

**sympy check:** `simplify(h(t₀²) − φ·t₀·h(t₀))` returns exactly `0` (in both
nats and bits). Numeric value of both sides: `0.9594187…` bits (independent
evaluation of both expressions, equal to the printed precision).

## 2. Exact relation between φ and (3−√5)/2

```
t₀²  = (√5−1)²/4 = (6−2√5)/4 = (3−√5)/2
1/φ² = 2/(3+√5)   = 2(3−√5)/4 = (3−√5)/2
```

Exact identities verified symbolically (`simplify(diff)=0`):
`t₀² = (3−√5)/2 = 1/φ² = 1 − 1/φ`, and `1/φ² + 1/φ = 1`.
So the barrier value `(3−√5)/2` is `1/φ²`, and the saturation point on the
`t`-axis is `t₀ = 1/φ`.

## 3. Structure and monotonicity of the difference

`D(t) = h(t²) − φ·t·h(t)` (in nats; scaling by `ln 2` does not change signs).

- **Exact symmetry-free decomposition of the derivative:**
  `D′(t) = A(t) + B(t)·ln t + C(t)·ln(1−t)` with the *clean factors*
  ```
  B(t) = t·(√5 − 3),          C(t) = −(1+√5)(2t−1)/2,
  A(t) = 2t·ln(1−t²)  (plus rational terms).
  ```
- **Saturation point is the unique interior zero.** `D(t₀) = 0` exactly (above).
  `D ≥ 0` on a 200-point rational grid at 40-digit precision (min ≈ 5.5×10⁻⁷,
  at the grid point nearest to `t₀`, expected positive because the exact interior
  minimizer `t₀` is off-grid). `D′(t₀) = 0` (high-precision, 120 digits) and
  `D″(t₀) = 0.28358985… > 0`, a strict local minimum. By Fermat's theorem the
  interior zero of a nonnegative function is a critical point, consistent.
- **Endpoints:** `D(0) = D(1) = 0` exactly; `D > 0` strictly on the interior
  (checked at `t = 1/3, 1/2, 3/4`).

## Verdict

- **Exact saturatiuequality: proved symbolically.** The chain
  `φ·t₀=1`, `t₀²=1−t₀`, `h(z)=h(1−z)` gives equality identically; sympy's
  `simplify` of the difference returns `0`. All constants live in `ℚ(√5)`,
  computed exactly (Rational/sqrt, no floats).
- **The full inequality `D ≥ 0` on [0,1]: proven in the literature** by
  differential calculus (Boppana arXiv:2301.09664, cited); here it is
  **verified numerically** on a fine exact-arithmetic grid at high precision and
  structurally corroborated (unique interior minimum at `t₀`, strict
  `D″(t₀)>0`, clean factorisation of `D′`). sympy does **not** collapse an
  independent closed-form algebraic proof of `D ≥ 0` across the whole interval,
  so I do not claim a self-contained symbolic proof of that direction.

**No full union-closed-set result is claimed.** This is only the one-variable
entropy inequality (and its saturation algebra) that is the engine of the
iid-OR entropy line.

*Command:* `python code/out/boppana_verify.py`, `boppana_verify2.py`,
`boppana_factor_attempt.py`, `boppana_saturation.py`, `boppana_dprime.py`.
