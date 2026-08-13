# Approach: tooth-labelling-crt

```approach
idea: Recast meshing directly as congruences on tooth-index labels without passing through continuous angle variables. Label ring teeth 0,…,c−1 and sun teeth 0,…,s−1 by their angular position modulo 2π. For a fixed geometric arrangement (given by centre separation d and planet positions), the ring tooth index i_C at the ring–planet contact point and the sun tooth index i_S at the sun–planet contact point satisfy i_S ≡ i_C + δ_t(d) (mod g) where δ_t(d) is a rational offset determined by the geometry and g = gcd(c,s, something). Four planets yield four such congruences. The free global orientations of the sun and ring (two degrees of freedom) absorb two of them, leaving two independent congruence conditions — a system of the form A·x ≡ b (mod M) where A is a 2×4 or similar matrix over Z_M. The number of solutions g(c,s,p,q) is the count of solution vectors mod M. If the system's Smith normal form reveals that g(c,s,p,q) depends only on gcd/lcm structures of (c,s,p,q), then G(n) = Σ g(s+p+q,s,p,q) can be evaluated by iterating over divisor structures rather than over (s,p,q) triples, reducing the cost from O(n³) to roughly O(n log n) or O(d(n)²).

mechanism: The key observation is that a gear with t teeth acts as a "tooth counter": rotating it by one full revolution advances the mesh by exactly t teeth on each mating gear. For a planet at a fixed position determined by d, the geometry fixes which ring tooth and which sun tooth are simultaneously in contact with a given planet tooth. This defines a linear relation between ring tooth index, sun tooth index, and planet tooth index modulo the tooth counts. Aggregating over four planets and eliminating the planet-spin degrees of freedom leaves congruences purely in ring and sun tooth indices. This is essentially a discrete-log / CRT problem in the abelian group Z_c × Z_s. The finite count g(c,s,p,q) arises because only finitely many d-values satisfy the geometric prerequisites (triangle inequalities, gap constraint), and among those, the congruence system may have 0, 1, or several solutions. The method succeeds if the geometry-induced offset δ_t(d) is a rational function of d with small denominator, since then the congruence becomes a Diophantine condition on d.

status: refuted
killed-by: gcdfactor_payoff_unsupported_and_monotone_endpoint_obviates
precedent: https://www.matec-conferences.org/articles/matecconf/abs/2020/25/matecconf_icmtmte2020_03027/matecconf_icmtmte2020_03027.html (Kurasov 2020, gear eccentric systems, toothed-contours integer congruences eq. 7/8 — off-centre precedent) ; https://doaj.org/article/0e0dcfac68cb471bb90e2cdf7561f8ef (Xue 2020, unified assembly, uneven spacing) ; https://www.science.gov/topicpages/g/gcd+greatest+common (no) ; thread `offcentre-mesh-phase-model` (claims `offcentre_dual_mesh_phase_invariant`, `offcentre_two_positions_per_type`) ; Guo 2011 eq. 5.21–5.25 ; sibling [[number-theoretic-crt]] (grounded)
first-step: (not pursued — the congruence reformulation is correct but its gcd-closed-form payoff is unsupported by the literature, and the monotone-endpoint structure makes the CRT decomposition unnecessary: g is a one-dimensional endpoint count, not a system of independent congruences)
```

## Research verdict — reformulation grounded, closed-form half not

This candidate is the same tooth-count-congruence reformulation as the sibling
`number-theoretic-crt` (already split/grounded in this run). The verdict there
carries over wholesale; the added value of this file is the concrete
proposal that **δ_t(d) factors through a gcd-based modulus**, which is the one
new claim to check.

**Grounded half — the congruence-discreteness reformulation, including the
off-centre case.** Kurasov 2020 (gear eccentric systems, "toothed contours"
method) gives universal assembly conditions for *eccentric* (off-centre) gear
systems as integer congruences of angle×tooth-count sums equal to an integer
multiple of π — eq. (7): `2φv·zv + φn·zn − φC1·zC1 − φC2·zC2 − π·K = 0`;
eq. (8): `φv·zv + φn·zn + φC'1·zC1 + φC'2·zC2 − 2π·K' = 0`. This is the same
structural object as the W-invariant (s·φ+c·χ−t·γ ≡ 0 mod π/2π) and it applies
to the off-centre sun, matching PE620. Xue 2020 (unified assembly, even and
uneven planet spacing) frames the same discreteness as "assembly misalignment
angle = integer multiple of the minimum non-zero misalignment angle", a
gcd/lcm-framed criterion. So phrasing meshing as tooth-count congruences — the
core of this candidate — is grounded, including off-centre.

**Unsupported half — the gcd-closed-form / multiplicativity claim.** The
candidate's payoff (G(500) over divisor structures in O(n log n)) rests on g
depending only on gcd/lcm structures and having a Smith-normal-form/CRT closed
form. None of the sources (Kurasov, Guo, Xue, Zou, Sun) establishes g is
multiplicative or has a closed form; each gives a *per-assembly* congruence, not
a seat-count formula. This is a conjecture with no precedent on disk. Worse, the
candidate's own mechanism is self-undermining there: it claims "counting tooth
index assignments ≡ counting d values", but in PE620 the position is *forced by
tangency* (two mirror points per type, `offcentre_two_positions_per_type`) and
the single free variable is centre-distance d — so four independent ring-tooth
indices would massively overcount. The tooth-index count and the d-count encode
the *same one-dimensional* discreteness; they do not decouple into independent
congruences. The proposed gcd-factorisation of δ_t(d) remains untested — it is
the key unknown, and it has no literature precedent either way.

Status: **grounded** for the congruence reformulation (incl. off-centre); the
**gcd-closed-form/multiplicative half — neither grounded nor refuted**: simply
not found in the literature and contradicted in outline by the tangency-forces-
position structure. Must be tested against a correct g before it pays.

```claim
id: tooth_count_congruence_reformulation_grounded
statement: Phrasing the PE620 meshing discreteness as integer congruences on tooth-count sums (angle x tooth-count === integer multiple of pi) is well-precedented INCLUDING for the off-centre (eccentric) case: Kurasov 2020 (gear eccentric systems, toothed-contours method) eq.7 2*phi_v*z_v + phi_n*z_n - phi_C1*z_C1 - phi_C2*z_C2 - pi*K = 0 and eq.8 give the assembly condition exactly this way for eccentric gears; Xue 2020 frames it as 'assembly misalignment angle = integer multiple of the minimum non-zero misalignment angle'. This grounds the tooth-labelling-crt reformulation.
hypotheses: ideal involute gears; integer tooth counts; the assembly discreteness is an integer-multiple-of-minimum-angle condition.
holds-here: yes for the reformulation itself.
status: grounded (reformulation); the multiplicative/gcd-closed-form half and the gcd-factorisation of delta_t(d) are UNSUPPORTED (no source establishes g is multiplicative or closed-form; the tangency-forces-position structure means four ring-tooth indices are NOT independent, so the index<->d identification overcounts).
bearing: supports casting g as count of solutions to tooth-count congruences; does NOT support an O(n log n) divisor-structure sum for G(500).
anchor: research/approaches/tooth-labelling-crt.md (also sibling number-theoretic-crt)
```


**Verification requirement:** both halves must reproduce g(16,5,5,6)=9,
G(16)=9, G(20)=205 before any closed-form claim earns trust.

**Source caveat:** Kurasov 2020 is 403-blocked to the downloader; eq. (7)/(8)
come from the search-engine extraction of the open-access MATEC PDF and the full
derivation is unverified directly.
```