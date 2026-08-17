# UC via the entropy–coupling method — Yu/Sawin two-atom sub-instance

Sub-instance of `G-coupling-half` on the Yu/Sawin symmetric two-atom
conditionally-iid class. **Refuted (capped)**: the certificate value at
density 1/2 is proved to be φ/2 ≈ 0.809 < 1. Recorded so no later turn
re-poses the surviving gap at the two-atom ceiling.

```skeleton
goal: The Yu/Sawin two-atom symmetric conditionally-iid coupling class reaches
       density 1/2: sup_α inf_{P two-atom} g(P,α)/Eh ≥ 1 at t = 1/2.
implies: this is the sub-instance of G-coupling-half obtained by restricting the
  coupling class to Yu's two-atom family; it is capped, so the surviving gap
  must use a genuinely larger class (Liu's C₃).
status: refuted
rests-on: yu-gamma-half-is-phi-over-2, yu-gamma-hat-nonincreasing, yu-optimization-objective
killed-by: yu-gamma-half-is-phi-over-2 (Γ̂(1/2) = φ/2 ≈ 0.80901699 < 1, the
  collapsed α=0 extremal proved by exact algebra) + yu-gamma-hat-nonincreasing
  (Γ̂ non-increasing in t, so Γ̂(1/2) ≤ Γ̂(t̂_max) < 1 at the crossing
  ≈ 0.38235). The two-atom relaxation certifies nothing at density 1/2.
```

```gap
id: G-yu-twoatom-half
lemma: The Yu/Sawin two-atom symmetric conditionally-iid coupling class reaches
       density 1/2: sup_α inf_{P two-atom} g(P,α)/Eh ≥ 1 at t = 1/2.
status: refuted
discharged-by: yu-gamma-half-is-phi-over-2 (Γ̂(1/2)=φ/2≈0.809<1, proved) and
  yu-gamma-hat-nonincreasing (Γ̂ non-increasing, so Γ̂(1/2) ≤ Γ̂(t̂_max) < 1).
next: none for extending this class — it is capped. The surviving gap is
  G-coupling-half on Liu's C₃ class.
```