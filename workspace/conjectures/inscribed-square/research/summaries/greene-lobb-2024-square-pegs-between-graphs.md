# Greene–Lobb 2024 — Square pegs between two graphs

**Source:** Joshua Evan Greene, Andrew Lobb, "Square pegs between two graphs," arXiv:2407.07798 (2024); published in Commentarii Mathematici Helvetici (DOI 10.4171/cmh/619, 2026). Full text at [[research/sources/greene-lobb-2024-square-pegs-between-graphs.full.md]].

## What it establishes

**Main theorem.** Let f, g : [0,1] → R with f(0)=g(0), f(1)=g(1), f(t) > g(t) for 0 < t < 1, forming a Jordan curve γ(f,g) = graph(f) ∪ graph(g). If f and g both have Lipschitz constant **< 1+√2**, then γ(f,g) inscribes a square.

**Corollary (Lipschitz constant = 1 case).** If the Lipschitz constants are exactly 1, then γ(f,g) inscribes rectangles of every similarity class (θ-rectangles for all θ ∈ (0, π/2]).

**Method.** Jordan Floer homology (from the authors' "Floer homology and square pegs," arXiv:2404.05179). Spectral invariants ℓ₁, ℓ₂ of the Floer chain complex change Lipschitz-continuously under curve perturbation (Corollary 3.7: |ℓᵢ(γ₀,θ) − ℓᵢ(γ₁,θ)| ≤ 4d(γ₀,γ₁) for equal-area curves). Approximate the two-graph curve by PL curves of uniformly bounded length (Prop 4.2), track the inscribed rectangles as the curves converge, and use the "elegant rectangle" notion (Prop 4.1: every inscribed rectangle in a two-graph curve is elegant) to rule out shrinkout. The Lipschitz constant 1+√2 is the threshold where the two graphs can meet at an angle of 45° — beyond which the diagonal/rectangle degeneracy structure changes.

## Why it matters here

- This is the current state of the **two-graphs thread**: Tao (<1, 2017) → Rifford (=1 with quantitative bound, 2021) → Greene–Lobb (<1+√2, 2024). The two-graphs class is now superseded as a square-positive class by Asano–Ike (all rectifiable curves), but the *quantitative* and *structural* content (which rectangles, which thresholds, shrinkout analysis) is finer here.
- The 1+√2 threshold has a geometric meaning (the 45° angle at which the two graphs' normal cones meet the diagonal) — a concrete candidate for the exact obstruction the run could formalize.

## Claims

```claim
id: gl2024-two-graphs-1+sqrt2
statement: If f, g : [0,1] → R agree at endpoints, f > g in the interior, and both have Lipschitz constant < 1+√2, then the Jordan curve graph(f) ∪ graph(g) inscribes a square.
status: asserted-by-source (arXiv:2407.07798, 2024; published CMH 2026)
evidence: Greene–Lobb, arXiv:2407.07798, main theorem
holds-here: yes — extends tao2017-two-lipschitz-graphs (<1) and rifford2021-quantitative-two-graphs (=1) to <1+√2
falsifies: a two-graph curve with Lipschitz constants in [1, 1+√2) and no inscribed square; or a correction
```

```claim
id: gl2024-lipschitz-1-all-rectangles
statement: If f, g have Lipschitz constant exactly 1, then the two-graph Jordan curve γ(f,g) inscribes rectangles of every similarity class.
status: asserted-by-source
evidence: Greene–Lobb, arXiv:2407.07798, Lipschitz-1 case
holds-here: yes — the boundary case; strictly stronger than Tao's <1 square result
falsifies: a 1-Lipschitz two-graph curve with no inscribed θ-rectangle for some θ
```
