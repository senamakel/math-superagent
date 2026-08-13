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

Unlike the S-unit or congruent-number approaches (which rename the genus
obstruction without exploiting the specific structure), this computes the
actual geometric object whose rational points are the Φ-triples, and it is
the natural next step after the Φ enumeration hit m,n ≤ 400.

status: proposed
speculation-vs-established: ESTABLISHED — the Φ reduction and f(m,n) = sin(4
  arctan(n/m)) form are this run's own checked code (phi-universal-set); the
  equation f(m1,n1)+f(m2,n2)=f(m3,n3) is a well-defined rational equation;
  Faltings applies to any genus-≥2 curve it projects to. SPECULATION — (a)
  that fixing q₁ and the ratio n₂/m₂ yields a non-degenerate curve (genus
  ≥ 2 rather than a degenerate genus 0/1 fibre); (b) that the specific curves
  at q = 5544/7225 and 336/625 have tractable geometry. The genus computation
  itself settles (a) immediately.
precedent:
  - Φ reduction: this run's own code (ap_structure2.py, phi_exact_search.py),
    claims phi-universal-set, phi-no-triple-m400
  - Faltings (1983): curves of genus ≥ 2 over number fields have finitely
    many rational points
  - The sin(4 arctan) form of f(m,n) is standard from the AP-of-squares
    parametrisation (problem.md, Robertson reduction)
  - No published genus computation for the Φ-triple curve is known to this
    library
first-step: Write the equation f(m1,n1) + f(m2,n2) = f(m3,n3) as a single
  polynomial by clearing denominators. Fix q1 = f(m0,n0) for a specific
  Φ-value (e.g., from Bremner's witness: (m0,n0) = (9,2) giving q =
  5544/7225, or (4,3) giving q = 336/625). Project to a curve in two
  variables by eliminating one pair. Compute genus using sympy/magma.
  Determine the geometry: rational, elliptic, or general type.
```