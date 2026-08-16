# Osculating curve / Wronski-map reformulation (adopted, hand-verified correction)

```approach
idea: Attach to a monic degree-n f its Hasse frame {H_0 f, H_1 f, …, H_{n-1} f}
       (H_i f = f^{(i)}/i! in char 0) and the curve
       C_f(x) = [H_0 f(x) : H_1 f(x) : … : H_{n-1} f(x)] ⊂ P^{n-1}.
       CORRECTED STATEMENT (verified by hand for n=2,3): C_f is the linear
       projection of the moment curve γ_n(x) = [1 : x : … : x^n] ⊂ P^n from the
       point ξ_f = the annihilator of V_f := span{H_0 f, …, H_{n-1} f}. The
       projection matrix L_f (n × (n+1), entries (L_f)[i,j] = C(i+j,i)·c_{i+j})
       has universal leading entries C(n,i) on its anti-diagonal i+j = n; all the
       f-dependence lives in the 1-dimensional kernel ξ_f ∈ P^n. Then:
         f is a pure power  ⟺  ξ_f ∈ γ_n,
       in which case C_f = π_{ξ_f}(γ_n) is the rational normal curve γ_{n-1} ⊂
       P^{n-1} (degree n-1); for every other f, C_f is a degree-n rational curve.
       Check (n=2): f = x²+c₁x+c₀, ξ_f = [1 : −c₁/2 : c₁²/2 − c₀]; for f=(x−a)²
       this is [1:a:a²] = γ₂(a). Check (n=3): f=(x−a)³ gives ξ_f = [1:a:a²:a³].
mechanism: The shared-root hypothesis is a list of incidence conditions between
       the projected moment curve and the coordinate flag: f(β)=H_i f(β)=0 ⟺
       C_f(β) ∈ H_0 ∩ H_i. CA is the assertion that n−1 such incidences force
       ξ_f onto γ_n, i.e. force the projection center onto the curve and C_f to
       drop degree n → n−1. The named theory is Schubert calculus on the moment
       curve / the Wronski map: V_f is a point of Gr(n, n+1) ≅ P^n (identified
       with ξ_f via annihilator), and the Wronski map Wr: Gr(n,n+1) → P(polys)
       is flat and finite of degree #SYT(rectangular shape) (Schubert 1886;
       Eisenbud–Harris; Eremenko–Gabrielov 2002; Purbhoo 2009), with fibres
       equal to intersections of osculating Schubert varieties and with explicit
       S_n Plücker-coordinate formulas for the inverse problem (Karp–Purbhoo
       arXiv:2309.04645). The bet (speculative, unproved) is that the incidence
       list C_f ∩ H_0 meeting each H_i is a Schubert condition on V_f/ξ_f whose
       only solution is ξ_f ∈ γ_n — a statement in the Wronski-map/Schubert
       circle, not in resultant elimination.
status: refuted
killed-by: non-distinct — coordinate-wise the incidence C_f(β) ∈ H_0 ∩ H_i is
      exactly H_i(f)(β) = 0, the root-difference identity e_{n−i}(β−β_1,…) = 0
      the adopted line owns; the projection-center invariant ξ_f is a repackaging
      of the same derivative-span data. The Wronski/Schubert machinery is aimed
      at generic incidence degeneracy, and no held source applies it to this
      specific n−1-incidence degeneracy, so the line adds a classical name but
      no new inference over root-difference-coloring. The curve reformulation is
      kept as a remark there; no separate line. Folded into
      research/approaches/root-difference-coloring.md.
first-step: (1) Oracle-guarded sympy, n=4,5,6: confirm C_f = π_{ξ_f}(γ_n), that
       ξ_f = annihilator(V_f) solves (L_f)ξ = 0, the anti-diagonal = C(n,i), the
       equivalence "f pure power ⟺ ξ_f ∈ γ_n", and the incidence "∃β: f(β)=
       H_i f(β)=0 ⟺ C_f(β) ∈ H_0 ∩ H_i" against lib.casas_alvero's gcd. (2) Char-p
       admissibility on the object: compute rank(L_f mod p) for n=4..20 at the
       named bad/good primes (Castryck Table 1; arithmetic-jet-lift) — expect the
       rank drop exactly when C(n,i) ≡ 0 (Lucas), and for n=p+1 the middle rows
       H_2,…,H_{p-1} vanish, so C_f collapses to a lower-dimensional projection:
       the named root-difference-coloring char-p break. (3) For n=4,5,6 pose the
       incidence as an explicit Schubert problem on the moment curve and check its
       solution set is the single pure-power point ξ_f ∈ γ_n.
precedent: eremenko-gabrielov-2002 (deg of complex Wronski map = #SYT rectangular,
       first computed by Schubert 1886); purbhoo-2009 (Wr flat finite, fibres =
       osculating Schubert intersections, monodromy = jeu de taquin, cites
       Eisenbud–Harris); karp-purbhoo-2023 (explicit S_n commuting-operator
       Plücker formulas for the inverse Wronski problem); gatto-scherbak-2013
       (survey: Wronskians and Schubert calculus). No source attacks CA through
       the osculating curve — the reformulation is this run's own, the machinery
       is classical.
charp-break: (corrected) over F_p the projection matrix L_f degenerates, not the
       curve: the universal anti-diagonal entries C(n,i) vanish mod p (Lucas), so
       rows H_i drop leading degree or are ≡ 0 and L_f's rank drops. For n = p+1,
       H_2,…,H_{p-1} ≡ 0 mod p, so C_f lands in a proper subspace and those
       coordinates impose no constraint — precisely the owned char-p break (middle
       Hasse derivatives vanish, root-difference-coloring). Schubert/Wronski-map
       theory is a char-0 (or good-char) theory; the rank drop of L_f is the named
       characteristic-using step.
```

## What changed at convergence, and the error that was caught

The first convergence draft claimed "`C_f` is a rational normal curve for every
monic `f`" and placed the invariant in an upper-triangular matrix `M_f`. That was
**wrong**, caught by hand computation before any tool run:

- `C_f = L_f ∘ γ_n` with `L_f` an `n × (n+1)` matrix. The universal `C(n,i)` sit
  on the **anti-diagonal** `i+j = n` (the leading coefficients of the `H_i f`),
  not a diagonal, and `L_f` has a 1-dimensional **kernel**, not an invertible
  square part.
- The correct invariant is that kernel point `ξ_f = annihilator(V_f) ∈ P^n`, the
  projection center. `C_f` is the projection of the moment curve from `ξ_f`.
- `f` pure power ⟺ `ξ_f ∈ γ_n` (hand-verified for n=2,3; the pattern
  `ξ_f = γ_n(a)` for `f=(x−a)^n` is checked). Then, and only then, `C_f` is the
  rational normal curve (degree n−1). For general `f` it is a degree-n rational
  curve.

So the curve is *not* constant — its degree is the invariant, and the degree
drops exactly at pure powers. That is a much better object than the first draft
had: CA becomes "n−1 hyperplane incidences force the projection center onto the
moment curve", and the mature Wronski-map/Schubert machinery is aimed at
precisely such incidence → degeneracy statements.

The first-step script `code/scratch/verify_osculating_facts.py` encodes the
*uncorrected* claims and is superseded; first-step (1) above replaces it.

## Status of the parts

- **Classical (sourced):** Wronski map flat/finite, degree = #SYT of rectangular
  shape (Schubert 1886; Eremenko–Gabrielov 2002); fibres = osculating Schubert
  intersections (Eisenbud–Harris via Purbhoo 2009); explicit S_n Plücker
  formulas for the inverse Wronski problem (Karp–Purbhoo 2023).
- **This run's own (hand-verified for n=2,3; needs oracle guard at n=4,5,6):**
  `C_f = π_{ξ_f}(γ_n)`, `ξ_f = annihilator(V_f)`, anti-diagonal `C(n,i)`,
  pure-power ⟺ `ξ_f ∈ γ_n`, degree n vs n−1.
- **Speculative (the load-bearing bet, honestly so):** that the n−1 incidence
  conditions force `ξ_f ∈ γ_n`. Unproved. The reformulation's value is that it
  makes this a Schubert/Wronski statement where degree counts and S_n formulas
  exist, instead of a resultant elimination.

## Why it is not a closed approach

`mason-stothers-wronskian` (refuted) applied Mason–Stothers to the scalar
Wronskian `W_i = f H_i′ − H_i f′` and died on a false additive identity; this
line uses the Wronski *map* on `Gr(n,n+1)` and Schubert calculus, a different
named object. `bezoutian-hankel-rank` (refuted) was Bézoutian matrix ranks;
this is the projective geometry of a flag relative to the moment curve.
`catalecticant-apolarity` (refuted) was apolar ideals; the flag `V_f` here is
the derivative span itself, and the apolar-dual viewpoint is avoided.
