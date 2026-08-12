# Gear eccentric systems: assembly condition by "toothed contours" (integer relations) — Kurasov 2020

Source: D. Kurasov (Kurgan State University), "Assembly conditions for
mechanical systems with gear elements", MATEC Web of Conferences 329, 03027
(2020), DOI 10.1051/matecconf/202032903027, ICMTMTE 2020.
https://www.matec-conferences.org/articles/matecconf/abs/2020/25/matecconf_icmtmte2020_03027/matecconf_icmtmte2020_03027.html
(both the PDF and HTML page returned HTTP 403 to our downloader; the abstract
and the universal equations below are taken verbatim from the search-engine
snippet of the open-access PDF.)

## What it establishes (closest off-centre precedent for candidate number-theoretic-crt)

The paper gives a general method for the **assembly conditions of mechanical
systems with toothed elements**, in particular **gear eccentric systems (GES)**
— where an off-centre gear, exactly the PE620 situation of an off-centre sun —
and any toothed system, via the **"toothed contours"** method: model the
interacting tooth rims as a continuous contour (a gear chain) and require the
total length of the engaging arcs around the closed loop to satisfy a discrete,
integer-based condition. The universal assembly condition for a pair of
satellites is stated in two equivalent forms:

    eq. (7):  2·φv·zv + φn·zn − φC1·zC1 − φC2·zC2 − π·K = 0
    eq. (8):  φv·zv + φn·zn + φC'1·zC1 + φC'2·zC2 − 2π·K' = 0

where the φ's are central angles measured at the engagement poles, the z's are
gear tooth counts, and K, K′ are integers encoding the number of links/steps in
the engagement chain.

## Implication for PE620 candidate `number-theoretic-crt`

This is the best direct precedent for the candidate's reformulation: it treats
the *off-centre* (eccentric) case and expresses the assembly condition as
**integer congruences of φ·(tooth-count) sums = π·K (or 2π·K')**. That is
structurally the same object as the thread's W-invariant (s·φ + c·χ − t·γ ≡
0 mod π/2π) — a signed sum of central-angle times tooth-count equated to an
integer multiple of π. It independently corroborates the phase-congruence
discreteness for eccentric (off-centre) gear systems, not just the coaxal one.

**What it does NOT provide:** a closed-form/gcd-only multiplicative formula for
g, nor a CRT/Smith-normal-form count that makes G(500) sub-cubic. It gives a
per-pair assembly congruence — the discrete language — not a seat-counting
formula. So it grounds the *reformulation* (tooth-count congruences are the
right discrete description of the off-centre meshing), but supports neither the
specific offset/modulus conjecture nor the claim that g is multiplicative.

## Cross-references

- Guo 2011 eq. 5.21–5.25, Parker & Lin 2004 (mesh phases), Simionescu 1998
  (unified assembly condition), Xue 2020 (unified, unevenly spaced), Zou 2015,
  Sun 2017: the coaxal/extended tooth-count assembly-condition literature.
- Thread `offcentre-mesh-phase-model`: the PE620-specific W-invariant, which
  this paper's eq. (7)/(8) structurally mirror.
