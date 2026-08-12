# Thread: off-centre dual-mesh phase model (PE620)

```thread
question: What exactly are the tooth-phase congruences that make four planets (2x p, 2x q), each tangent to an off-centre sun S (s teeth, radius s/2pi) and an internal ring C (c teeth, radius c/2pi) with centre separation d, all mesh simultaneously — and does the resulting discrete count g(c,s,p,q) reproduce 9, 9, 205?
status: model derived in full from tooth-phase congruences; oracle verification pending (no code yet)
rests-on: assembly_condition_simple_planetary_guo (Guo 5.21-5.22), least_mesh_angle* (design-guide lattice), tangent_circle_center_ellipse
blocked-by: phase_model_probe.py (idler-phase model, not the thread's W-invariant model) tested only 2 of 4 chi/gamma sign variants — both eps=+1 and eps=-1 return g=0. Remaining 2 variants (independent signs on gamma and beta coefficients) must be probed. If all 4 return 0, fall back to direct enumeration of the 9 arrangements for (16,5,5,6).
next: (1) Extend phase_model_probe.py to probe all 4 independent sign combinations on the gamma-term and beta-term coefficients; (2) if all still return 0, enumerate the (16,5,5,6) configurations directly by tangency, compute tooth phases numerically, and output the 9 that survive — then work backwards from what they look like to the correct meshing condition.
```

## Why the coaxial lattice cannot transfer to PE620

**1. Tangency forces positions; there is no free angular choice.** For planet type t, radius rho_t = t/2pi: exact tangency to both gears forces |SP| = a_t := (s+t)/2pi and |CP| = b_t := (c-t)/2pi simultaneously. With the two centres at distance d, the centre P is the intersection of two circles -> exactly TWO points per type, mirror images across the line SC. A valid arrangement therefore occupies both p-positions and both q-positions and is determined by d alone. (This is why both dead models — scanning a beta-lattice about O or about S in code/lib/gears.py and code/pattern/discrete_model_probe.py — returned 0: the search space they scanned does not contain the geometry.)

**2. Phase congruence per planet.** Convention (Guo Table 5.1, eq. 5.22): phases counted at the pitch point; the sun mesh phase accrues +s*(contact angle) and the internal ring mesh phase accrues -c*(contact angle) — Guo's (5.22) is exactly dec(Z_s psi/2pi) = dec(-Z_r psi/2pi). Write the triangle angles at S, C, P as phi = angle PSC, chi = angle PCS, gamma = angle SPC (gamma = angle between the two contact rays at the planet; gamma = pi only coaxially). Each planet's spin theta_pj, the sun orientation theta_s0 and the ring orientation theta_c0 are free. The two mesh constraints per planet (external sun mesh, internal ring mesh) eliminate the spin and leave, per planet j:

E1: s(phi_j-th_s0) - t(phi_j+pi-th_pj+tau_p) = 2pi eps_s
E2: -c(chi_j-th_c0) - t(phi_j+pi-gamma_j-th_pj+tau_p) = 2pi eps_c   (mod 2pi)
E1-E2:  s*phi_j + c*chi_j - t_j*gamma_j = s*th_s0 + c*th_c0 + 2pi(eps_s-eps_c)   (mod 2pi).

The right-hand side is ONE common constant, so: all four per-planet invariants W_j := s*phi_j + c*chi_j - t_j*gamma_j must be pairwise congruent mod 2pi.

## Testable model (hand to the programmer)

Inputs c, s, p, q integers >= 5, p < q; variable d = |CS|.

- a_t = (s+t)/(2pi),  b_t = (c-t)/(2pi)  (t in {p,q})
- d_min = max(|a_p-b_p|, |a_q-b_q|)  (strict triangle inequality: positions non-degenerate)
- d_max = (c-s)/(2pi) - 1   (the 1 cm gap: R - r - d >= 1; NOTE d=0 coaxial excluded: it is only realisable when t=(c-s)/2)
- Triangle angles (law of cosines, all in (0,pi), phi+chi+gamma=pi):
  cos phi_t = (a_t^2 + d^2 - b_t^2)/(2 a_t d)
  cos chi_t = (b_t^2 + d^2 - a_t^2)/(2 b_t d)
  cos gamma_t = (a_t^2 + b_t^2 - d^2)/(2 a_t b_t)
- Positions: p-planets at sun-frame angles +phi_p and -phi_p (ring-frame +chi_p, -chi_p; gamma_p shared by the pair), q-planets at +-phi_q.

Congruences (radians, mod 2pi):
1. W_p+ = W_p-  <=>  s*phi_p + c*chi_p ≡ 0 (mod pi)        [mirror pair of type p]
2. W_q+ = W_q-  <=>  s*phi_q + c*chi_q ≡ 0 (mod pi)        [mirror pair of type q]
3. W_p+ = W_q+  <=>  s(phi_p-phi_q) + c(chi_p-chi_q) - p*gamma_p + q*gamma_q ≡ 0 (mod 2pi)  [cross-type]

g(c,s,p,q) = #{d in (d_min,d_max): 1,2,3 hold} x kappa, with kappa = mirror-identification factor in {1,2} to be fixed by the oracle (also decide whether endpoints/degenerate single-contact d count).

No exponential cost: each condition is a one-variable transcendental congruence; bracket the half-integer (for 1,2) or integer (for 3) levels of the left-hand side over the d interval and bisect the monotone branches. Cost per g is O(#solutions) — independent of any bound.

## Roles of the variables

- c (ring teeth): coefficient of chi in W; defines b_t and d_max.
- s (sun teeth): coefficient of phi; defines a_t and d_max.
- t = p, q (planet teeth): fixes the contact distances a_t, b_t — hence the ONLY two points each planet can occupy — and enters the phase congruence explicitly through t*gamma_t. In the coaxial limit t drops out except for tooth parity (t mod 2), matching the idler freedom.
- d: the single continuous arrangement parameter; the congruences quantise it to a finite set, which is exactly the statement's "only discrete positions mesh".
- gamma_t(d): survives off-centre because the two contact rays at the planet enclose gamma_t ≠ pi; t*gamma_t is the new coupling of planet tooth count to the meshing condition.

## Hypotheses; what the off-centre geometry invalidates

Holds: integer tooth counts; ideal X-zero involute teeth; pitch-point phase convention; planets independent (d_i = 1 trains); planet overlap permitted (no adjacency condition).

Invalidated off-centre: (i) "planet positions are multiples of beta = 2pi/(s+c) about the common centre" — there is no common centre, and positions are forced by tangency anyway; (ii) the plain sum rule (Z_s+Z_c)psi = 2pi n survives only as the coaxial limit d -> 0 (which additionally requires t = (c-s)/2). The three design guides and Guo state only the coaxial case; the run's earlier "holds-here: yes" on least_mesh_angle* and assembly_condition_simple_planetary_guo was an unchecked transfer. This thread is the check.

Sign conventions to pin by the oracle: W = s*phi + c*chi - t*gamma follows Guo (5.22)'s dec(Z_s psi) = dec(-Z_c psi). The 4 variants (independent signs of the chi and gamma terms) are the first probe; the model is correct iff exactly one variant reproduces g(16,5,5,6)=9, G(16)=9, G(20)=205.

## The coaxial limit is the sourced rule (consistency)

d -> 0 requires a_t = b_t, i.e. t = (c-s)/2 (the standard coaxial planet size). Then phi = chi = psi, gamma = pi, W = (s+c)psi - t*pi, and pairwise congruence gives psi in (2pi/(s+c))*Z, the least-mesh-angle lattice of all three design guides and Guo (5.21)-(5.22). The new model contains the sourced rule as its special case, with one new off-centre feature: for mixed planet sizes of opposite parity, p*gamma_p - q*gamma_q shifts the cross-type congruence by pi in the coaxial limit (parity effect), which never arises in the single-size trains the sources treat.

```claim
id: offcentre_dual_mesh_phase_invariant
statement: With a=(s+t)/(2pi), b=(c-t)/(2pi) and the triangle angles at S, C, P from the law of cosines, simultaneous meshing of every planet tangent to both gears is equivalent to the per-planet invariants W_j = s*phi_j + c*chi_j - t_j*gamma_j being pairwise congruent mod 2pi; for the two mirror positions of one type this reduces to s*phi_t + c*chi_t in pi*Z, and across types to s*(phi_p-phi_q) + c*(chi_p-chi_q) - p*gamma_p + q*gamma_q in 2pi*Z.
hypotheses: ideal X-zero involute gears; integer tooth counts; Guo pitch-point phase convention (internal ring phase -c*contact angle); sun and ring orientations and each planet spin free.
holds-here: unchecked (oracle pending: g(16,5,5,6)=9, G(16)=9, G(20)=205)
status: asserted (derived from tooth-phase congruences in this note; not yet numerically verified)
bearing: the correct discreteness for the off-centre problem; makes g a count of d-solutions of three explicit congruences — no position enumeration, no beta-lattice.
anchor: research/threads/offcentre-mesh-phase-model.md
contradicts: least_mesh_angle, least_mesh_angle_handbook, least_mesh_angle_uts, assembly_condition_simple_planetary_guo
```

```claim
id: offcentre_two_positions_per_type
statement: For fixed centre separation d and planet tooth count t, tangency to both sun (|SP|=(s+t)/(2pi)) and ring (|CP|=(c-t)/(2pi)) permits exactly two planet centres, mirror images across the line of centres; a valid PE620 arrangement therefore occupies both p-positions and both q-positions and is determined by d alone.
hypotheses: exact tangency; S strictly inside C; d in the open triangle-inequality range.
holds-here: yes (pure geometry)
status: asserted
bearing: explains why both single-centre lattice models (gears.py and discrete_model_probe.py, checked g=0) searched the wrong space; the count is over d, not over positions.
anchor: research/threads/offcentre-mesh-phase-model.md
```

```claim
id: coaxial_limit_reproduces_lattice
statement: As d -> 0 (realisable only when t=(c-s)/2 for every planet) the invariants reduce to W=(s+c)*psi - t*pi and pairwise congruence gives psi in (2pi/(s+c))*Z, reproducing the least-mesh-angle rule of all three design guides and Guo (5.21)-(5.22).
hypotheses: coaxial sun and ring; one planet per train.
holds-here: no (limit case; PE620 is off-centre)
status: asserted (closed-form reduction, consistent with Guo eq. 5.21-5.22 on disk)
bearing: proves the new model contains the sourced rule as its coaxial special case; the sources and this derivation are the same theory.
anchor: research/threads/offcentre-mesh-phase-model.md
```