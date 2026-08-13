# Approach: Genus of the Φ-triple curve and Faltings classification

```approach
idea: The additive triple condition q1 + q2 = q3 with each qi = f(mi,ni) =
4 mini (mi²−ni²)/(mi²+ni²)² is a single rational equation in six integer
variables. After homogenising and removing the denominator, it defines an
algebraic surface. Fixing one pair of parameters — say (m1,n1) and (m2,n2) as
parameters — and solving for (m3,n3) defines a curve over Q(m1,n1,m2,n2).
More usefully: fix the rational number q1 and treat q1 + f(m,n) = f(p,q) as a
curve. For a generic rational q, this is a curve of computable genus; for q
coming from Φ (i.e., q = f(m0,n0)), the curve becomes a specific Diophantine
curve whose rational points parametrise Φ-triples. The key structural fact:
f(m,n) = sin(4 arctan(n/m)). The equation sin(4α) + sin(4β) = sin(4γ) with
tan α, tan β, tan γ ∈ Q is a trigonometric Diophantine equation. The addition
formula sin(4α)+sin(4β) = 2 sin(2(α+β)) cos(2(α−β)) factors, and the
condition becomes a rational identity in tangents.

mechanism: Compute the genus of the curve C_q: f(m,n) + f(p,q) = f(r,s) with
q = f(m0,n0) fixed (a known Φ-value). This is a single equation in six
variables; by setting up the correct projection (homogenise, treat two
variables as coordinates on a curve), the genus is a computable number. If
genus = 0: the curve is rational, parametrising all Φ-triples containing q —
this would either yield a construction or prove that only finitely many q
admit Φ-triples. If genus = 1: the curve is elliptic, and the Mordell-Weil
group can be computed; if rank = 0, the Φ-triples for that q are from torsion
(finitely many, computable). If genus ≥ 2: Faltings says finitely many
rational points; the remaining step is to compute or bound them via
Chabauty–Coleman (genuinely needed here, unlike the unverified r<g for
Bremner's 7→8 curves) or the method of Dem'janenko. The existence of the
Bremner 7-square witness means q_v = 5544/7225 and q_{u+v} = 336/625 are both
in Φ with (m,n) = (9,2) and (4,3) respectively; plugging these specific
Φ-values as q gives concrete curves whose rational points are computable.

Unlike the S-unit or congruent-number approaches (which rename the genus
obstruction without exploiting the specific structure), this directly
computes the geometric object whose rational points are the Φ-triples. It is
the natural next step after the Φ enumeration hit m,n ≤ 400.

status: proposed
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