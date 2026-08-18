# Rifford 2021 — A quantitative version of Tao's result on the Toeplitz Square Peg Problem

**Source:** Ludovic Rifford, "A quantitative version of Tao's result on the Toeplitz Square Peg Problem," arXiv:2106.01914 (2021). Full text at [[research/sources/rifford2021-quantitative-tao.full.md]].

## What it establishes

Pushes Tao's two-Lipschitz-graphs theorem from Lipschitz constant < 1 to **= 1**, and adds a **universal lower bound** on the inscribed square's side length.

**Theorem 1.1.** There exists a universal constant C > 0 such that: if I = [T₀, T₁] is an interval, f, g : I → R are 1-Lipschitz functions with f(T₀)=g(T₀), f(T₁)=g(T₁), and f(t) < g(t) for all t ∈ (T₀, T₁), then the union of the graphs of f and g (a Jordan curve) inscribes a square whose side length ≥ C · max(g−f).

**Key improvement over Tao 2017:** Tao's theorem required Lipschitz constants < 1; Rifford extends to = 1 (the boundary case). The side-length lower bound C·max(g−f) is the first explicit quantitative bound for this class and directly rules out shrinkout — the inscribed square cannot be arbitrarily small relative to the curve's height.

The proof uses an analytic approach (integrals, monotonicity formulas, and a bootstrap argument) rather than the homological/integral method of Tao. The constant C is not computed explicitly, but the proof gives a method to extract it.

## Why it matters here

- The two-graphs class is one of the three restricted classes in ROOT.md. Rifford's bound adds a **scale certificate** — a concrete lower bound on the square side length — which is exactly what a formalization needs to prove nondegeneracy.
- The Lipschitz-1 boundary case is the natural limit of the two-graphs approach; Greene–Lobb's "Square pegs between two graphs" (Lipschitz < 1+√2, using Floer homology) later exceeds it.
- oracle target: given two 1-Lipschitz functions with explicit algebraic expressions, the checker can verify the inscribed square has side length ≥ C·max(g−f) for some explicit C.

## Claims

```claim
id: rifford2021-quantitative-two-graphs
statement: There exists a universal constant C > 0 such that the union of two 1-Lipschitz graphs f, g : [T₀, T₁] → R (agreeing at endpoints, f<g in the interior) inscribes a square of side length ≥ C · max(g−f).
status: asserted-by-source
evidence: Rifford, arXiv:2106.01914, Theorem 1.1
holds-here: yes — extends Tao's class to Lipschitz constant = 1 and adds a quantitative lower bound; the universal constant C is not computed explicitly
falsifies: a counterexample pair of 1-Lipschitz functions with no inscribed square, or a proof that C must be 0
```