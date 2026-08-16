# Fourier / influence analysis of union-closed indicator functions

```approach
idea: Replace the family F by its indicator f: {0,1}^n → {0,1}, f(A) = 1 ⟺ A ∈ F.
  Union-closure is exactly the functional equation f(A)·f(B) ≤ f(A∨B), and UC
  is exactly: some coordinate x has Σ_{A ∋ x} f(A) ≥ (1/2)·Σ_A f(A), i.e. the
  marginal abundance of x on the support of f is ≥ 1/2. Attack this with the
  Fourier–Walsh expansion f = Σ_{S} f̂(S) χ_S and the theory of influence
  (KKL, Friedgut junta, Russo–Margulis): abundance and influences are both
  first-moment data of the spectrum, and the join-closure constraint
  f(A)f(B) ≤ f(A∨B) is a quadratic inequality in the values of f that must
  translate into a *nonlinear constraint on the Fourier coefficients* — the
  analogue of "H(A∨B) ≤ H(A)" but written in the Walsh basis instead of in
  entropy.
mechanism: The entropy method's one-variable miracle h(2p−p²) ≤ h(p) is a
  *diagonal* (log-)moment identity; the Walsh basis carries the full spectrum,
  and the constraint f(A)f(B) ≤ f(A∨B) mixes low- and high-degree Fourier
  coefficients in a way entropy averages away. Concretely, a "all abundances
  < 1/2" hypothesis is a family of linear constraints on the f̂({x}) and f̂(∅);
  combined with the quadratic closure constraints one can try to derive a
  KKL-style tension (total influence lower-bounded by concentration vs.
  upper-bounded by the rare-abundance hypothesis). The named toolkit is
  Fourier analysis of boolean functions and its influence inequalities; the
  operative new hypothesis is that the join-closure constraint is a
  "log-supermodularity"-type condition whose Fourier signature is recognizable.
status: grounded
precedent: lozin-zamaraev-horn (Lozin–Zamaraev, JCTA 2023, "Union-closed sets and Horn Boolean functions", https://doi.org/10.1016/j.jcta.2023.105818) — the indicator-f Boolean reformulation and the abundant⟺good / rare⟺good variable dictionary ARE exactly this approach's kernel, published and named, verified for Horn, submodular, and double Horn boolean-function classes; chen-etal-property-testing (Chen–De–Li–Nadimpalli–Servedio, ITCS 2024, https://doi.org/10.4230/lipics.itcs.2024.33) — property-testing hardness of union-closedness from a boolean-function analysis angle. NOTE (found nothing): the KKL / Russo–Margulis influence-inference step — that f(A)f(B)≤f(A∨B) forces a usable constraint on the Fourier spectrum yielding the rare-abundance contradiction — has NO published application to union-closed; no source connects influence theory to an abundance bound (searched "KKL influence Fourier union-closed abundance", "Fourier entropy influence boolean functions"). Unverified: whether the (3−√5)/2 barrier reappears as a Fourier identity.
first-step: Implement the Walsh transform for the oracle families; for each
  small family compute the full spectrum f̂(S), the abundance vector, and the
  influences, and look for a universal relation between the closure equation
  f(A)f(B) ≤ f(A∨B) and the spectrum (e.g. a bound on f̂({x}) in terms of
  f̂(∅) and the rare-abundance hypothesis). Test whether the known barrier
  (3−√5)/2 reappears as a specific Fourier identity.
```

## Speculation, marked

That the closure constraint has a tractable Fourier/influence signature from
which a KKL-type contradiction follows is speculative; the entropy line already
encodes a first moment and research may find the influence route to be exactly
it in disguise. The non-speculative kernel is the exact reformulation
UC ⟺ coordinate-abundance ≥ 1/2 on the support of a function satisfying
f(A)f(B) ≤ f(A∨B), stated purely in {0,1}-function language, which is a
different object from the lattice algebra or the coupling optimization already
in the record.
