# Abel-equation Bautin-ideal reduction

```approach
idea: Change the object from the planar displacement function to a first-order Abel equation
     on the transversal cylinder, and let the cyclicity of the graphic be governed by the
     finitely generated Bautin ideal of that Abel equation (Briskin–Françoise–Yomdin theory),
     computed by exact Gröbner and pushed to a kernel-checked Lean theorem.

mechanism: A planar polynomial system in the polar chart (r,θ) with angular velocity B(θ)
     that keeps its sign on the period annulus reduces the Poincaré return map to the
     2π-periodic first-order equation  dr/dθ = A(θ,r)  — an Abel-type equation (polynomial
     in r, trigonometric in θ). The displacement function is then  r(2π;ρ) − ρ, and its
     zeroes are exactly the limit cycles near the annulus. Briskin–Françoise–Yomdin and the
     Yomdin school ("The Bautin ideal of the Abel equation", Nonlinearity 11 (1998) 431–443;
     Roytvarf, Pakovich, Briskin–Roytvarf–Yomdin) prove that for fixed degree the center
     conditions and the cyclicity of the origin of such an Abel equation are governed by a
     FINITELY GENERATED ideal in a polynomial ring in the Fourier coefficients — the Abel
     analogue of the classical Bautin ideal. That is exactly the structure this run already
     computes for the planar Lu/DRR five-coefficient chart (the L4/L6/L8 obstructions, the
     membership L10,L12∈⟨L4,L6,L8⟩, verified by Gröbner over Q). The reformulation: a graphic's
     finite cyclicity is a statement that this Abel Bautin ideal has finite codimension in the
     relevant ring, so the zero-count is bounded by the ideal's height / a Gröbner-basis
     computation — a finite algebraic question Lean can close (ideal membership, resultant,
     codimension) rather than an analytic paragraph. Test 1 (smooth test) is satisfied where it
     must be: the finiteness enters through algebraicity of the polynomial coefficients of P,Q,
     not through smoothness of the return germ.

status: proposed

first-step: Take one specific center/annulus graphic from the DRR list that the run already knows
     reduces to an Abel-type radial equation (e.g. a pp-type or a quadratic center), compute its
     Abel Bautin ideal exactly over Q by replicating Briskin–Françoise–Yomdin's construction
     with the run's bautin/ machinery, and verify that an explicit first few focal/period
     quantities span the ideal at low degree — reproducing a published small cyclicity bound
     (e.g. M(2)=3) through the Abel representation before trusting it on anything new. State the
     ideal-membership claim in Lean before computing (BautinRecurrence.lean pattern).
```
