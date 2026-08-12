# Assembly conditions for mechanical systems with gear elements — Kurasov 2020 (full text)

[[research/sources/kurasov-2020-assembly-conditions-pq.full.md]] · source:
https://www.matec-conferences.org/articles/matecconf/abs/2020/25/matecconf_icmtmte2020_03027/matecconf_icmtmte2020_03027.html
(DOI 10.1051/matecconf/202032903027, ICMTMTE 2020, open access CC-BY).
Full text obtained via ProQuest media PDF:
https://media.proquest.com/media/hms/PFT/1/JedAI?_s=vC1zpiGPgr60n2YmV0DkeZsbApo%3D
after three direct MATEC PDF/HTML fetches returned HTTP 403. Recorded so nobody
re-attempts the direct MATEC route.

## What it establishes (closest off-centre precedent in the library)

The paper is about **gear eccentric systems (GES)** — a planetary mechanism in which
the central gear is *off-centre* inside an internal ring, with **satellites of
different diameters** (the diameter difference provides the eccentricity). This is
structurally the closest published device to PE620: an internal ring C, an off-centre
central gear S, and two planets of different sizes p ≠ q meshing both. The paper's key
statements:

1. **GES assembly conditions differ from coaxial ones.** "The geometric conditions of
   the existence of GES are essentially similar to similar conditions for coaxial
   planetary mechanisms, but **their mathematical expressions are completely
   different**": (i) neighbourhood condition; (ii) correspondence of tooth counts to
   location (the actual assembly condition); (iii) correspondence of initial wheel
   diameters to their location — *instead of* the coaxial condition. This is the
   paper-level confirmation of the run's finding that the coaxial least-mesh-angle
   lattice does not transfer to PE620's off-centre geometry.

2. **Coaxial formula (eq. 1)** — the sanity baseline: for a coaxial planetary
   transmission with one satellite layer, the assembly condition is
   **(Z₁ + Z₃)/k = C**, C an integer, k the number of satellites. This matches Guo
   (5.21), the design guides' least-mesh-angle rule, and the run's
   `assembly_condition_simple_planetary_guo`.

3. **Toothed-contours / gear-chains method (the general frame).** Model the closed
   chain of engaging tooth rims as arcs of pitch circles; the total arc length
   between engagement poles must be a multiple of the separation step
   (eq. 6: φ₁+φ₂+φ₃+φ₄ = K·P, K the integer "number of chain links"). Works when
   initial circles deviate from pitch circles: the integer is then the sum of the
   dividing steps over the loop.

4. **Universal GES assembly equation for a pair of satellites (eq. 7), and its
   equivalent form (eq. 8):** a signed sum of (central-angle × tooth-count) over the
   engagement poles equals an integer multiple of π terms,
   `±z_C1·φ_C1 ± z_C2·φ_C2 ± ... = π·K` (OCR-garbled in the PDF; the reading from the
   search abstract is `2·φv·zv + φn·zn − φC1·zC1 − φC2·zC2 − π·K = 0` with the
   satellites' angles doubled, φ_C′ = 2φ_C, K′ = K + z_C1 + z_C2).
   **This is precisely the run's W-invariant structure** — a signed (angle ×
   tooth-count) sum ≡ integer (mod π or 2π) — as an *assembly* condition for an
   *off-centre* system with *two different-size satellites*. It corroborates
   `offcentre_dual_mesh_phase_invariant` and `split_torque_curvilinear_quadrilateral_condition`
   at source level, for the eccentric case specifically.

5. **Separate diameter/location condition (Section 4)** — the geometric closure of
   the off-centre position: closed vector loop AB + BC − AC = 0 over the triangle of
   the two satellite centres and the gear centre, giving cosine/sine equations
   (eqs. 10-11; with radial tension parameter Δ, eqs. 13-14) linking tooth counts,
   angles and the eccentricity e_h. This is the same law-of-cosines triangle the run's
   tangency model uses — and the paper's separation of (tooth-count assembly) from
   (diameter/location conformity) matches the run's separation of the phase congruence
   from the tangency positions.

6. **Design algorithm (Section 5):** choose integer planet tooth counts and integer K
   parameters (rounding), refine against allowable interference, check the
   neighbourhood condition. Confirms the parameters are integers and the count is a
   discrete enumeration over K-levels — the run's "count of integer-level crossings"
   reading of g.

## Implication for PE620

This is the strongest source-level support yet that the off-centre discreteness is
a **system of per-planet-pair congruences of signed (angle × tooth-count) sums
equated to integers** — the W-model — and that the coaxial divisibility rule
(Z_c + Z_s)/k ∈ ℤ is only the coaxial baseline, not the off-centre count. It also
confirms that a *pair-of-satellites* formulation (the run's UU/LL mirror pairs) is
the natural unit of counting, and that planets of different diameters are exactly the
GES configuration the theory was built for.

**What it does not provide:** no closed-form/gcd-only formula for g; no guidance on
counting over the full valid d-interval (the paper is a design recipe, not a counting
theorem); eq. (7)'s exact signs are OCR-garbled in the PDF (the ± assignments for
internal vs external mesh must still come from Guo 5.22 / Zhao-Li eq. 39, which the
oracle already pinned as σ=η=θ=−1).

```claim
id: kurasov_ges_offcentre_assembly_system
statement: For a gear eccentric system (off-centre gear inside an internal ring with satellites of different diameters), the assembly condition is NOT the coaxial formula (Z_ring+Z_sun)/k integer; it is instead a system of equations, one per satellite pair, each a signed sum of (central-angle x tooth-count) over the engagement poles equal to an integer multiple of pi (eq. 7/8; eq. 6: total pitch-arc length between poles = K x pitch), plus a separate diameter/location closure (vector-loop cosine/sine equations, eqs. 10-14). The coaxial rule (Z1+Z3)/k = C (eq. 1) is stated as the baseline for coaxial trains only.
hypotheses: toothed rims as contiguous arcs (pitch circles = initial circles or initial circles deviating from pitch circles, integer = sum of dividing steps); ideal involute X-zero teeth; integer tooth counts and integer K parameters.
holds-here: yes in structure — PE620 is an off-centre gear inside an internal ring with two different-size planets; the per-pair signed angle*tooth-count congruence system is the run's W-invariant; the separate diameter/tangency closure is the run's triangle-of-centres position model.
status: sourced (Kurasov 2020, MATEC Web Conf. 329:03027, full text on disk; eqs. 1, 6, 7, 8, 10-14; eq. 7 signs OCR-garbled, reading taken from the search abstract)
bearing: strongest off-centre precedent that the coaxial lattice is the wrong discreteness for PE620 and that per-pair signed (angle x tooth-count) congruences are the right one; corroborates offcentre_dual_mesh_phase_invariant and split_torque_curvilinear_quadrilateral_condition for the eccentric case.
anchor: research/sources/kurasov-2020-assembly-conditions-pq.full.md
answers: offcentre-mesh-phase-model (source-level corroboration for the eccentric case)
```

## Access note

Direct MATEC HTML + PDF and the ProQuest viewer page gave only navigation chrome;
the `media.proquest.com/media/hms/PFT/1/JedAI?...` link inside the viewer page is the
actual 295-kB CC-BY PDF and downloaded cleanly. Do not retry the direct MATEC route.

## Cross-references

- Guo 2011 eq. (5.21)-(5.22), Zhao-Li 2018 eq. 39, Segade-Robleda 2012 eq. (1)-(7):
  the coaxial/split-torque signed-sum assembly conditions this paper's eq. (7)/(8)
  match for the eccentric case.
- Thread `offcentre-mesh-phase-model`: the W-invariant this corroborates.
- `research/approaches/number-theoretic-crt.md`: the CRT reformulation this grounds
  (integer congruences) but does not close (no multiplicative formula).