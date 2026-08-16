# Lagarias, "Ternary Expansions of Powers of 2"

Source: arXiv:math/0512006v4 (math.DS / math.NT), 11 Jul 2008. Full text: `research/sources/lagarias-2009-ternary-pdf.full.md`. Published: J. London Math. Soc. 79 (2009) 562–588.

## The theorem that fixes the obstruction for this run

Erdős asked how frequently `2^n` omits digit 2 in ternary; conjectured only finitely many n. Lagarias reframes it as dynamics on `Z_3` under `y → 2y`.

**Witnesses:** `2^0=1=(1)_3`, `2^2=4=(11)_3`, `2^8=256=(100111)_3`.

**Theorem 1.4 (generalizes Narkiewicz to all λ).** For each nonzero `λ ∈ Z_3` and each `X ≥ 2`,
```
Ñ_λ(X) := #{ n ≤ X : (λ·2^n)_3 omits digit 2 } ≤ 2·X^α0,   α0 = log_3 2 ≈ 0.63092.
```

**Theorem 1.5 (Hausdorff dimension of 3-adic exceptional sets).**
- `dim_H(E^(1)(Z_3)) = α0 ≈ 0.63092`
- `(1/2)log_3 2 ≤ dim_H(E^(2)(Z_3)) ≤ 1/2`
- `(1/6)log_3 2 ≤ dim_H(E^(3)(Z_3)) ≤ dim_H(E^(2)(Z_3))`
where `E^(k)(Z_3) = {λ : at least k values of λ·2^n omit digit 2}`.

**Theorem 1.6 (intersections of 3-adic Cantor translates).** For `M` not a power of 3,
```
dim_H(C(1,M)) = dim_H(Σ_{3,2} ∩ (1/M)Σ_{3,2}) ≤ 1/2
```
and `dim_H(C(1,7)) = log_3((1+√5)/2) ≈ 0.438` exactly.

**Conjecture B:** the 3-adic exceptional set `E(Z_3) := {λ : infinitely many λ·2^n omit digit 2}` has Hausdorff dimension zero. Erdős's conjecture is EQUIVALENT to `1 ∉ E(Z_3)`.

## What dimension results do and do NOT give — the gap this run must state

Lagarias is explicit: the real method reaches only the `log_3 X` most-significant digits, the 3-adic method only the `log_3 X` least-significant, and "the vast number of digits in the middle of the expansion are not exploited in either method." A statement that `dim_H(E(Z_3)) = 0` — or that `S` (the digit-{0,1} Cantor set) has dimension `log_3 2 < 1` — says the exceptional SET is small in measure, but does NOT say which specific integers `n` give digit-2-free `2^n`. Dimension 0 of `E(Z_3)` would not imply `1 ∉ E(Z_3)`: a single point `λ` (like `λ=1`) could still be exceptional, and no dimension statement rules that out. **This is the precise sense in which "Hausdorff dimension of S" cannot be the deliverable.**

Conjecture E (generalization of Furstenberg): for multiplicatively independent `p,q`, any finite pattern of q-ary digits occurs in `(p^n)_q` for all sufficiently large n. Erdős's original is the case p=2, q=3, pattern "2".

## Status

Sourced, peer-reviewed (J. London Math. Soc.) / arXiv v4. This is the standard reference the whole run's 3-adic route rests on. Relevant flags for the run: (a) the 3-adic and real methods are "independent" (high vs low digits) and (b) Lagarias explicitly poses as open the problem of combining them to get β < log_3 2 — that is the very gap the run's middle-digits aim would fill.
