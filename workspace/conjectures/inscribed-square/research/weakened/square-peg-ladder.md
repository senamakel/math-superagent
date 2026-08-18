# Ladder: Inscribed Square Problem (Toeplitz's Conjecture)

```ladder
goal: Every Jordan curve γ: S¹ → R² inscribes a square — four distinct points on γ that are the vertices of a square.
difficulties: boundary-winding, shrinkout, degenerate-zeros, non-rectifiability, no-scale-certificate
status: open
```

## The difficulties, named exactly

1. **boundary-winding.** The parity proof works by tracking the map F (midpoint difference, chord difference) on the degenerate boundary of the cyclically-ordered configuration space (a Möbius band). For a general continuous curve, F on this boundary has no well-defined winding number around the origin — local monotonicity is exactly the hypothesis that makes it computable. Without it, the topological degree argument that produces an odd number of signed zeros of F collapses.

2. **shrinkout.** Approximate a wild Jordan curve by locally monotone curves (always possible — polygons suffice). Each approximant inscribes a genuine square (Stromquist). But their side lengths can converge to 0, so the limit is a single point, not a square. Any argument that passes through approximation must bound the side length away from 0, or it has proved nothing. Named by Tao (2017).

3. **degenerate-zeros.** Even when F has an interior zero, it may represent a degenerate configuration — adjacent parameters coinciding on the Möbius-band boundary, giving a "crossed" quadrilateral that satisfies the algebraic square conditions without being a genuine cyclically-ordered square. Ruling these out uses local structure a general continuous curve does not have.

4. **non-rectifiability.** The Asano–Ike (2024) sheaf-theoretic proof covers all *rectifiable* Jordan curves (finite 1-dimensional Hausdorff measure). A non-rectifiable curve has infinite length; it may fail to admit the continuous Legendrian lift that the sheaf method requires. The class of curves admitting such a lift lies somewhere between rectifiable curves and all Jordan curves, and its exact boundary is the sharp open question.

5. **no-scale-certificate.** There is no universal lower bound on the side length of an inscribed square for a general Jordan curve. Matschke's annulus theorems produce such bounds from homotopy constraints, and Rifford (2021) produces one from a Lipschitz constraint, but a general curve admits neither. Any proof must either produce a scale certificate from weaker hypotheses or prove existence without one — the latter is what the parity argument achieves for locally monotone curves, and what the sheaf argument achieves for rectifiable curves.

---

```rung
id: R0-ellipse-instance
statement: A non-circular ellipse x²/a² + y²/b² = 1 (a² ≠ b²) inscribes exactly one square, detectable as a transverse intersection C⁰₄[γ] ⋔ Slq in the compactified configuration space.
off: boundary-winding, shrinkout, degenerate-zeros, non-rectifiability, no-scale-certificate
stance: settled
merge: This is an instance of Stromquist's theorem (the ellipse is C∞, hence locally monotone). The merge to the next rung drops the explicit parametrization and asks: does the run's exact-arithmetic checker recover the CDM 2022 Prop. 26 count? That is an oracle-validation step, not new mathematics.
```

```rung
id: R1-locally-monotone
statement: Every locally monotone Jordan curve γ: S¹ → R² inscribes a square. (γ is locally monotone if every point has a neighbourhood on which γ is strictly monotone with respect to some linear functional.)
off: boundary-winding, degenerate-zeros
stance: settled
merge: Stromquist (1989). The boundary winding number of F is well-defined for locally monotone curves, the Qᵢ decomposition (Lemma 3.24 of Rius Casado's exposition) controls degenerate zeros, and the parity argument yields an odd number of genuine squares. Turning the next difficulty back on means dropping local monotonicity; the boundary winding stops being well-defined. Matschke's special-trapezoid criterion is the first device that replaces it, so the next rung asks whether a finite-scale combinatorial condition (no special trapezoid of size ε) suffices.
```

```rung
id: R2-special-trapezoid-free
statement: Every Jordan curve γ that inscribes no special trapezoid of size ε (for some ε ∈ (0,1)) inscribes a square. (A special trapezoid is an inscribed quadrilateral with three equal longer sides and one shorter side; its size ε is the cyclic length of the arc spanned by the short side.)
off: boundary-winding
stance: settled
merge: Matschke (2009), Corollary 2.10. The mod-2 intersection formulation (Theorem 2.8) replaces the boundary winding number with a well-defined parity count i(S, P₄(ω)) whenever γ has no square; the special-trapezoid condition forces this count to be 0, and the contradiction yields a square. Turning the next difficulty back on means: what if the curve DOES have special trapezoids at small scales but is still rectifiable? Asano–Ike settles this by an entirely different method.
```

```rung
id: R3-rectifiable
statement: Every rectifiable Jordan curve γ: S¹ → R² (finite 1-dimensional Hausdorff measure) inscribes a square — in fact, a θ-rectangle for every θ ∈ (0,π).
off: boundary-winding, shrinkout, degenerate-zeros
stance: settled
merge: Asano–Ike (2024), Theorem 1.1 + Corollary 5.9. The sheaf-theoretic method (Tamarkin category, continuous Legendrian lift) bypasses the configuration-space parity argument entirely — it does not need a boundary winding number, does not suffer shrinkout, and does not face the degenerate-zero problem. Turning the next difficulty back on means dropping rectifiability. The obstacle is exactly the continuous Legendrian lift condition: does every Jordan curve admit one? If yes, the conjecture is proved; if no, the Asano–Ike method cannot reach the general case, and the lift condition defines a maximal known class.
```

```rung
id: R4-legendrian-lift
statement: Every Jordan curve γ: S¹ → R² admits a continuous Legendrian lift — that is, there exists a sequence of smooth Jordan curves converging uniformly to γ whose primitives (of (γₙ ∘ e)∗λ) converge uniformly on compact subsets to a continuous limit.
off: boundary-winding, shrinkout, degenerate-zeros, non-rectifiability
stance: open
merge: This is the sharp intermediate question. If true, Asano–Ike Theorem 1.1 immediately implies the full conjecture. If false, the Asano–Ike method is bounded above by the class of curves admitting such a lift, and a counterexample curve without one is a precise obstruction result. The first move is to determine whether the lift condition characterizes rectifiability (i.e., is equivalent to it) or is strictly weaker. Asano–Ike prove rectifiable ⇒ lift; the converse is the gap. A curve with a lift but infinite length would be a new positive class; a curve without a lift would be a negative result bounding the sheaf method.
```

```rung
id: R5-full-conjecture
statement: Every Jordan curve γ: S¹ → R² inscribes a square. (Toeplitz's conjecture, 1911.)
off:
stance: open
merge: Not reached. This is the target. Every rung below it is settled by the literature except R4, which is open. The run cannot merge R4 into R5 — that would require proving the full conjecture, which is not expected. The run's contribution space is: formalize R1 (Stromquist) in Lean, verify R0 with the exact oracle, investigate R4 (what conditions force/forbid a continuous Legendrian lift on non-rectifiable curves), and pin the obstruction precisely.
```
