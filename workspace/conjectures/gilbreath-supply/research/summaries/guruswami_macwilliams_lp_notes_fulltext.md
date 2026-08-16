# Summary — Guruswami, "Fourier Transform, MacWilliams identities, and the LP bound"

Source: V. Guruswami, CMU Introduction to Coding Theory, Notes 5.1 (Feb 2010). Source URL: https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/notes/notes5a.pdf. Full text: [[research/sources/guruswami_macwilliams_lp_notes_fulltext.full]].

## What this establishes

A self-contained course-notes treatment of the **MacWilliams identity from Fourier analysis on the Boolean cube**, and its use to derive the **linear-programming (LP / Delsarte / MRRW) bound**.

- **Fourier basis of the cube.** Functions `f : {0,1}^n → R` with inner product `⟨f,g⟩ = E_x f(x)g(x)`; the characters `χ_α(x) = (−1)^{α·x}` form an orthonormal basis.
- **Dual-character sum.** `Σ_{c∈C} (−1)^{α·c} = |C|` if `α ∈ C^⊥`, else `0`. Hence `1_C` Fourier-transforms to `(1/|C|)1_{C^⊥}̂` scaling.
- **Lemma 10 (the Krawtchouk evaluation).** `Σ_{α:wt(α)=ℓ} (−1)^{α·x} = Σ_{j=0}^ℓ (−1)^j C(i,j)C(n−i,ℓ−j) =: K_ℓ(i)` depends only on `wt(x)=i`.
- **MacWilliams identity.** `W^{C^⊥}_ℓ = (1/|C|) Σ_{i=0}^n W^C_i K_ℓ(i)`, i.e. `W^C_ℓ = E_{x∈C}[K_ℓ(wt x)]`, or as a functional equation `W^{C^⊥}(z) = (1/|C|)Σ_i W^C_i (1−z)^i(1+z)^{n−i}`.
- **LP bound.** The distance distribution of any code (linear or not) satisfies the Delsarte LP: `Σ_i K_ℓ(i) A_i ≥ 0` for all `ℓ≥1` (positivity of the dual's distance distribution), `A_i=0` for `i<d`; maximising `Σ A_i` upper-bounds `A(n,d)`. The dual LP minimises `β(0)` over `β(X)=1+Σ β_ℓ K_ℓ(X)` with `β(j)≤0` for `j≥d`, `β_i≥0` — MRRW's bound is the construction of a feasible dual solution from orthogonal-polynomial theory.

## Why it matters for SUPPLY

This is the **cleanest single derivation of the exact spectral structure behind request `walsh-spectral-subset-b904`.** Key points for the ran's open gap:

- `wt(Φ_n h)` can be read as a sum of Walsh coefficients of the input `h`, and the Krawtchouk evaluations `K_ℓ(i)` are precisely the numbers that control how an `F₂`-linear map's output weight relates to the input's weight-distribution.
- The **Delsarte LP structure** is the closest existing template for the requested bound: positivity of a dual transformation (`W^{C^⊥}_ℓ ≥ 0` from `Σ_i W_i K_ℓ(i)`) is a *linear constraint the weight distribution must satisfy*, the same shape as a "Lucas/submask-positive" constraint on `Φ`'s image.
- The Fourier-basis view (`χ_α`, `(−1)^{α·x}`) is exactly the Walsh coordinate system in which the submask-XOR fold lives.

**Does not settle the request:** the notes give identities and bounds on *code sizes* (`A(n,d)`), not a per-input `wt(Φ_n h) ≥ c·n` for the prime string `h`. The LP story shows the transform machinery exists but the specific input-dependent bound for SUPPLY is not among its outputs.

## Evidence class / falsifier

Proved (course notes, full proofs). Would be misused as a source for `wt(Φ_n h) ≥ c·n` directly; it bounds code sizes, not a single folded vector's weight from an input hypothesis.

```claim
id: guruswami-macwilliams-lp-from-fourier
statement: Over the Boolean cube, the MacWilliams identity W^{C^⊥}_ℓ = (1/|C|) Σ_i W^C_i K_ℓ(i) follows from Fourier analysis (dual-character sums and the Krawtchouk evaluation Σ_{wt α=ℓ}(−1)^{α·x} = K_ℓ(wt x)); positivity of the dual weight distribution forces the Delsarte linear constraints Σ_i K_ℓ(i) A_i ≥ 0, whose LP optimum upper-bounds A(n,d) (MRRW).
hypotheses: C ⊆ {0,1}^n any code; F_2 linearity of the dual-code relationship; Krawtchouk polynomials over q=2 (or F_q).
holds-here: Holds in the exact coordinate system (Boolean cube, Walsh basis, Krawtchouk transform) in which the submask-XOR fold Φ of SUPPLY lives.
status: proved (course notes, self-contained)
bearing: The cleanest derivation of the Walsh/Krawtchouk/Delsarte-LP spectral structure behind request walsh-spectral-subset-b904. Confirms the transform machinery is available (dual-positivity constraints are the template shape), but it bounds code sizes, not wt(Φ_n h) for the fixed prime input — the input-dependent bound remains the open gap.
anchor: research/sources/guruswami_macwilliams_lp_notes_fulltext.full.md, §1–3
```
