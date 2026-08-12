# Algorithms for Trigonometric Polynomials — Mulholland & Monagan

[[monagan-algorithms-for-trigonometric-polynomials.full]] · source:
https://www.cecm.sfu.ca/personal/monaganm/papers/trigpoly.pdf (Mulholland, UBC; Monagan, SFU)

## What it establishes (algebraic substrate, already noted; no change)

The tangent half-angle substitution t = tan(θ/2), sin θ = 2t/(1+t²), cos θ = (1−t²)/(1+t²)
is a ring morphism Q[sin,cos] → Q(t) with kernel ⟨s²+c²−1⟩ (Lemma 3). Consequences:

- **Degree bound (Lemma 4):** a trig polynomial of trig degree d lands on a(t)/(1+t²)^d
  with deg_t a ≤ 2d. The substitution at most doubles the degree.
- **Theorem 1 (inverse):** any rational a(t)/(1+t²)^n with 1+t² ∤ a and deg a ≤ 2n is the
  image of a unique trig polynomial of degree n — reversible on the right class.
- Division, factorisation, GCD of trig polynomials reduce to the same problems on a(t).

## Implication for PE620

Confirms the tangent-half-angle route (approach file `tangent-half-angle.md`) is algebraically
sound and exact: the phase conditions become rational in t, degree ≤ 2× trig degree, and
Sturm's theorem then counts real roots exactly. But the technique's guarantee is **upstream**
of the meshing model: it root-counts whatever congruence the W-invariant gives, and cannot
validate the discreteness itself. It is the counting *machinery*, conditional on
`offcentre_dual_mesh_phase_invariant` being the right discreteness.

## New since the prior note

The prior note flagged this route as "conditional on an unverified model." Since then the
run (via `tangency_enum.py`, claim `tangency_enum_oracle_match`, checked) has pinned the
residue sign convention and reproduced g(16,5,5,6)=9 by *direct enumeration* — so the
upstream model is now oracle-validated (still G(16), G(20) pending). This upgrades the
half-angle route from "conditional on an unverified model" to a viable *exact replacement
for the numerical grid scan*: with the sign convention fixed, the polynomial P(t) whose
real roots count g is now well-defined, and Sturm gives g with no numerical scanning.
Status: grounded.

```claim
id: tangent_half_angle_exact_root_count
statement: The tangent half-angle substitution t = tan(theta/2) maps a trigonometric polynomial of degree d to a rational a(t)/(1+t^2)^d with deg a <= 2d, reversibly on the right class; combined with Sturm's theorem this counts real roots of trig phase congruences exactly (e.g. the INRIA ALIAS pipeline), with no numerical scanning.
hypotheses: congruences expressed as vanishing of a trigonometric polynomial; X-zero ideal gears; the phase (W-invariant) model already established.
holds-here: yes as exact counting machinery once the W-model's sign convention is fixed (now oracle-pinned by tangency_enum); caveat: clearing square roots from arccos-of-rational terms can push degree well above 2(c+s) and inject spurious roots needing filtering.
status: sourced (Mulholland & Monagan Lemmas 3-4, Thm 1; Sturm theorem)
bearing: the exact, non-grid route to g(c,s,p,q) and to the G(500) sum, replacing the 1M-point numeric scans; cost independent of the bound once the polynomial is formed.
anchor: research/sources/monagan-algorithms-for-trigonometric-polynomials.full.md
```
