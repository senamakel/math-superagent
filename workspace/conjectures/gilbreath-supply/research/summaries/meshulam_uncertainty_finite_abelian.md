# Summary — Meshulam, An uncertainty inequality for finite abelian groups

Source: Roy Meshulam, "An Uncertainty Inequality for Finite Abelian Groups", arXiv:math.CO/0312407 (2003); published as *European Journal of Combinatorics* 27(1) (2006) 37–63. Source URL: https://arxiv.org/abs/math.CO/0312407 (full text: https://arxiv.org/html/math/0312407v1). Local full text: `research/sources/meshulam_uncertainty_finite_abelian_html.full.md`.

## What this source establishes

**Theorem 1.2 (answering a question of Tao).** Let `G` be a finite abelian group of order `n`, and `0 ≠ f : G → C` with `|supp f| = k`. Let `d₁ = d₁(n,k)` be the largest divisor of `n` with `d₁ ≤ k` and `d₂ = d₂(n,k)` the smallest divisor with `d₂ ≥ k`. Then

`|supp f̂| ≥ (n/(d₁d₂))·(d₁ + d₂ − k)`,

a strict improvement of the classical `|supp f|·|supp f̂| ≥ n` whenever `k` lies strictly between consecutive divisors of `n`. Tao's remark: the point `(|supp f|, |supp f̂|)` lies on or above the **convex hull** of the points `(|H|, |G/H|)` over all subgroups `H ≤ G`, whereas the classical inequality only says it lies above the hyperbola.

Engine: Theorem 1.1 (the prime-order additive bound, for which Meshulam credits Tao/Biró with `|supp f|+|supp f̂| ≥ p+1` on `Z/pZ`), plus:
- **Proposition 1.3** (subgroup/factor-group reduction): `θ(G,k) ≥ θ(H,s)·θ(G/H,t)` for suitable `st ≤ k`.
- **Proposition 1.4** (submultiplicativity of `u(n,k) = (n/(d₁d₂))(d₁+d₂−k)`).

Also recalls the **non-abelian** analog (Theorem 4.1, from Meshulam 1992): for finite `G` with irreps `ρ_i` of dimension `d_i`, `|supp f|·μ(f) ≥ |G|` where `μ(f) = Σ_i d_i·rank f̂(ρ_i)`.

## The (Z/2)ⁿ specialization — why it matters for SUPPLY

The relevant group is the elementary 2-group `G = (Z/2)^n`, whose Fourier transform is the **Walsh–Hadamard transform** (characters `χ_S(x) = (−1)^{⟨S,x⟩}`, `S ⊆ [n]`). Here the divisors of `n = |G| = 2^n` are exactly `2^j`, `0 ≤ j ≤ n`. Meshulam's Theorem 1.2 specializes: if `2^j ≤ k = |supp f| ≤ 2^{j+1}` then

`|supp f̂| ≥ (2^n/2^{j}·2^{j+1})·(2^j + 2^{j+1} − k) = 2^{n−j−1}·(3·2^j − k) = 3·2^{n−1} − 2^{n−j−1}·k`.

The convex-hull statement becomes: the point `(|supp f|, |supp f̂|)` lies on/above the convex hull of `{(2^j, 2^{n−j}) : 0 ≤ j ≤ n}`, which are exactly the subgroup-indicator pairs `(|H|, |G/H|)`. This is the **sharpest Walsh-side trade-off on the Boolean cube** — precisely the coordinate system (`F₂^n`, Walsh basis) in which the submask-XOR fold `Φ_n` of SUPPLY is an `F₂`-linear map.

## What it does and does not give for `wt(Φ_n h) ≥ c·n`

This is the primary, exactly-on-target reference for the Walsh-spectral side of the run's open request `walsh-spectral-subset-b904`. It fixes:
- the exact product and additive/convex-hull uncertainty structure on `(Z/2)^n`,
- the extremals: **subgroup indicators** (affine subspaces of the cube), which in the SUPPLY picture are precisely the structured low-weight inputs — the all-ones vector `h = 1` (the kernel of `Φ`, `Φ_n 1 = 0`) is the `j=n` indicator `|H|=2^n`; dyadic/Thue–Morse-type degenerations sit at intermediate subgroup levels. These are exactly the five-closed-doors witnesses.

It does **not** give a lower bound on `wt(Φ_n h)` from an input hypothesis on `h`: `wt(Φ_n h)` is an image-weight (co-domain) quantity, not a Walsh-basis support size, and the extremals are exactly the low-weight structured inputs the closed doors forbid. So the value is directional and structural — it is the canonical statement of what the Walsh side can constrain and where the equality cases (the obstruction) live — but the search for an arithmetic input on `h` forcing `wt(Φ_n h) ≥ c·n` remains open.

## Evidence class

Proved theorem (published, full induction proof via subgroup/factor reduction). The (Z/2)ⁿ specialization is a direct corollary recorded here, not independently reproved.

```claim
id: meshulam-finite-abelian-divisor-bound
statement: For 0 ≠ f ∈ L(G), G finite abelian of order n, |supp f| = k, with d1 = largest divisor of n ≤ k and d2 = smallest divisor ≥ k: |supp f̂| ≥ (n/(d1 d2))(d1 + d2 − k). Equivalently the point (|supp f|, |supp f̂|) lies on/above the convex hull of {(|H|, |G/H|)} over subgroups H ≤ G. On (Z/2)^n this is the Walsh basis: if 2^j ≤ k ≤ 2^{j+1} then |supp f̂| ≥ 2^{n−j−1}(3·2^j − k), extremals = subgroup/affine-subspace indicators.
hypotheses: G finite abelian; f non-zero complex; f̂ the (unnormalized) Fourier transform; k = |supp f|.
holds-here: Yes for the object — the relevant group is (Z/2)^n with the Walsh–Hadamard transform, the exact coordinate system of the submask-XOR fold Φ_n (Lucas reads binary submasks, i.e. supports S ⊆ [n]).
status: proved (Meshulam 2003/2006 Thm 1.2; Tao's Thm 1.1 as the prime-order base; the (Z/2)^n specialization is a direct corollary recorded here)
bearing: The primary, exactly-on-target Walsh-side reference for request walsh-spectral-subset-b904. Fixes the divisor-sharpened uncertainty bound on the Boolean cube and its extremal subgroup-indicator structure. Directional only: it constrains Walsh-basis supports, not co-domain image weight, and the extremals are precisely the structured low-weight inputs the five closed doors forbid relying on — so it sharpens the obstruction but does not by itself yield wt(Φ_n h) ≥ c·n.
anchor: research/sources/meshulam_uncertainty_finite_abelian_html.full.md (Thm 1.2, Prop 1.3–1.4, Thm 4.1)
```

## What would falsify its bearing

If someone tried to apply Meshulam's Theorem 1.2 as a bound on `wt(Φ_n h)`: it would fail for two independent reasons — (a) `wt(Φ_n h)` is a co-domain image weight, not a support size in the Walsh basis (the mapping `h ↦ Φ_n h` is not the Fourier transform, it is the submask-XOR zeta transform), and (b) the equality cases of the uncertainty bound are exactly subspace/affine indicators, on which `Φ` has provably low-weight images (the all-ones kernel vector and the dyadic degenerations of the five closed doors). So Meshulam sharpens the Walsh-side structure but cannot itself be the lower-bound engine.
