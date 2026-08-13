# Approach: Genus of the Φ-triple curve and Faltings classification

```approach
idea: The additive triple condition q1 + q2 = q3 with each qi = f(mi,ni) =
4 mini (mi²−ni²)/(mi²+ni²)² is a single rational equation in six integer
variables, hence a 5-dimensional hypersurface V ⊂ A⁶ (not a curve). The
honest geometric question is whether V has rational points with distinct
positive coordinates, and — the key move — what happens when one fixes the
*ratio data*. Two clean projections: (a) fix q1 = f(m0,n0) (a specific
Φ-value) and treat q2 = f(m,n) as a free parameter; the condition
q1 + q2 ∈ Φ, i.e. q1 + f(m,n) = f(p,q), is a 3-fold in (m,n,p,q) whose
integral points are the Φ-triples containing q1; (b) use the closed form
f(m,n) = sin(4 arctan(n/m)). The equation becomes sin(4α) + sin(4β) =
sin(4γ) with tan α, tan β, tan γ ∈ Q — a trigonometric Diophantine equation,
and the addition formula sin(4α)+sin(4β) = 2 sin(2(α+β)) cos(2(α−β)) factors
the left side into a product, reducing the additive condition to a product
condition in tangents.

mechanism: The value f(m,n) = 4mn(m²−n²)/(m²+n²)² is the image of the rational
point tan θ = n/m under the Chebyshev polynomial of degree 4, i.e. it is
T₄-type / sin-4θ in disguise. Setting x = tan α = n₁/m₁, y = tan β = n₂/m₂,
the condition q₁ + q₂ ∈ Φ is exactly: there exists z = tan γ rational with
sin(4α) + sin(4β) = sin(4γ). Writing s₁ = sin(4α), s₂ = sin(4β), this is a
single equation among rational points on the curve of degree 8. The cleanest
geometric model: fix q₁ (so α is fixed), and let β vary; the condition is
that the point (q₁ + f(tan β), ·) lies on the universal curve
{f(m,n) : (m,n) ∈ Q²}. This is a 3-fold; its *fibres over a fixed q₁ and a
fixed ratio of β* are curves whose genus is computable. Concretely: fix both
q₁ = f(m₀,n₀) AND the reduced ratio r = n₂/m₂ (a rational number), so that
q₂ = f(1, r); then q₁ + f(1,r) = f(p,q) is a curve in (p,q) — this is the
genus-computable object. Varying r sweeps a 1-parameter family of curves.
For the two specific Φ-values in Bremner's 7-square witness — q_v =
5544/7225 = f(9,2) and q_{u+v} = 336/625 = f(4,3) — the curves
f(9,2) + f(1,r) = f(p,q) and f(4,3) + f(1,r) = f(p,q) are explicit,
finite-coefficient, and their genus is a direct computation.

status: refuted
killed-by: f(m,n) is homogeneous of degree 0 (both numerator 4mn(m²−n²) and
  denominator (m²+n²)² scale by t⁴ under (m,n)→(tm,tn)), so f(p,q) depends
  only on the ratio r = q/p. Fixing q₁ AND the ratio r fixes q₂, hence fixes
  the constant C = q₁ + q₂; the fibre f(p,q) = C is then g(r)=C, a quartic in
  ONE ratio r with at most 4 roots, i.e. a finite union of rational lines
  through the origin (each genus 0). There is NO genus-≥2 curve here, so
  Faltings' finiteness does not apply, there is no elliptic-rank case to
  compute, and the "1-parameter family of curves" degenerates to lines with
  infinitely many rational points. The genus computation the candidate names
  as its first step returns 0 for every fibre, which closes the approach as
  formulated. Verification: research/notes/verdict_facts_check.py (FACT A,
  exact sympy). To get any genus ≥ 2 one would have to fix q₁ but NOT r and
  eliminate (m,n) — but that object is a surface/3-fold, not a curve, and no
  Faltings statement applies to it; the candidate's stated projection (fix
  q₁ and the ratio) is precisely the one that kills the geometry.

speculation-vs-established: REFUTED on the mechanism. Established (this run,
  checked): Φ reduction, f(m,n) = sin(4 arctan(n/m)) form, q_v = 5544/7225 =
  f(9,2), q_{u+v} = 336/625 = f(4,3). Established (literature): Faltings 1983
  (genus ≥ 2 ⇒ finite rational points). Refuted (this run, exact): the
  proposed fibre (fix q₁ and ratio r) is a union of rational lines, genus 0.
  The homogeneous-degree-0 degeneracy means the trigonometric factorisation
  sin(4α)+sin(4β)=2sin(2(α+β))cos(2(α−β)) is a genuine identity but does not
  classify a family of positive-genus curves; it collapses the dimension.
  No published genus computation for any non-degenerate Φ-triple curve exists,
  precisely because the family is degenerate.

precedent:
  - Φ reduction: this run's own code (ap_structure2.py, phi_exact_search.py),
    claims phi-universal-set, phi-no-triple-m400
  - Faltings (1983): Endlichkeitssätze für abelsche Varietäten über
    Zahlkörpern, Invent. Math. 73, 349–366 — curves of genus ≥ 2 over number
    fields have finitely many rational points (the theorem the candidate
    invokes; its hypothesis genus ≥ 2 is what the fibre fails)
  - Homogeneity of f: this run, code/out/phi_fibre_genus_run.py + research/
    notes/verdict_facts_check.py (FACT A, exact) — f(tm,tn)=f(m,n), fibres
    are ≤4 rational lines, genus 0
  - sin(4 arctan(n/m)) form of f: standard from AP-of-squares parametrisation
    (problem.md, Robertson reduction; this run's phi-universal-set)
  - No published non-degenerate genus computation for a Φ-triple curve is
    known to this library; the approach's own speculations (a) and (b) are
    both false for the stated fibre.
first-step: none — closed. A future Φ-triple attack must NOT fix the ratio r
  (that degenerates f to a quartic in one ratio). It must fix only q₁ and work
  with the full surface in (m,n,p,q); that is a Diophantine-geometry problem
  of a different type (a variety, not a curve), to which Faltings' curve
  theorem does not apply. Recorded so nobody re-proposes the ratio-fixing
  fibre as a "genus computation".
```
