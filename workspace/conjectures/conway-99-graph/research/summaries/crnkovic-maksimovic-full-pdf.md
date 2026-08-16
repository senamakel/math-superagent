# Crnković & Maksimović (2020) — full PDF, Section 7 mechanism

Source URL: https://cdm.ucalgary.ca/article/download/62323/54015
DOI 10.55016/ojs/cdm.v15i1.62323, Contrib. Discrete Math. 15(1) 22–41 (2020).
This replaces the abstract-only record: the FULL text (1101 lines) is now in the
library at `research/sources/crnkovic-maksimovic-full-pdf.full.md`.

## What the paper is
Orbit-matrix method for constructing/classifying SRGs with a *composite-order*
automorphism group (generalising Behbahani–Lam 2011 prime-order orbit
matrices). Main computational work is on (49,18,7,6). Section 7 is the
(99,14,1,2) automorphism-group-of-order-6-or-9 exclusion, whose exact
mechanism is now read.

## The mechanism for (99,14,1,2) — exact and complete (Section 7)

The argument is computer-assisted orbit-matrix classification using GAP and
Mathematica. It proceeds assumption by assumption:

**Theorem 7.1 (Behbahani–Lam, quoted):** If srg(99,14,1,2) exists, the only
possible prime divisors of |Aut Γ| are 2 and 3, and every order-3 automorphism
is fixed-point-free.

**§7.1 Z6 acting:** assume G = Z6 = Z2×Z3. Orbit-length distributions
d=(d1,d2,d3,d6) satisfying the counting conditions (Thm 4.2) are, by Mathematica,
exactly three: (0,0,1,16), (0,0,3,15), (0,0,5,14), giving respectively 2, 4, 7
nonisomorphic orbit matrices. **None of these orbit matrices refines to an orbit
matrix for Z3 ⊲ Z6.** Since a Z6-automorph group would contain the normal Z3, and
its orbit matrix must refine, **no such refinement exists ⟹ no Z6 action.**

**§7.2 S3 acting:** d values giving #OM: (0,0,1,16)→2, (0,0,3,15)→4, (0,0,5,14)→7;
all other distributions give 0 (incl. (0,0,7,13),(0,0,9,12),(0,0,11,11),
(0,0,13,10),(0,0,15,9),(0,0,17,8)). The S3 orbit matrices do not refine to Z3 ⊲ S3
⟹ **no S3 action.**

**§7.3 E9 acting:** Z3×Z3. By Thm 7.1 (order-3 fixed-point-free) the only orbit
distribution is (0,0,11): eleven orbits each of length 9, no fixed points, no
order-3 orbits. Up to iso there is ONE orbit matrix O — the unique 11×11 block
matrix with diagonal 4 and off-diagonal 1. Refinement to Z3 ⊲ E9 fails
⟹ **no E9 action.**

**§7.4 Z9 acting:** cyclic order 9. Only distribution (0,0,11), only orbit matrix O.
"No SRG for Z9 acting with orbit matrix O" ⟹ **no Z9 action.**

**Theorem 7.3 (conclusion):** If srg(99,14,1,2) exists, |Aut Γ| = 2^a·3^b with
b ∈ {0,1}; order-3 automorphisms fixed-point-free; no automorphism group of
order six.

## What this establishes / what still holds
- Z6, S3, Z9, E9 all excluded as automorphism groups, **by a computer-assisted
  orbit-matrix enumeration whose search space is fully documented** (the orbit
  distributions and #OM counts above). This is the exact mechanism
  `research/notes/automorphism-orders-consolidated.md` attributed, now with the
  full computation and its exhaustiveness (all d satisfying Thm 4.2 enumerated;
  every orbit matrix checked for Z3 refinement).
- Combined with Cesarz–Woldar 2025 (computer-free: 2|G| ⟹ |G||6; 7|G| ⟹ G≅Z7):
  Candiate groups surviving everything are tiny. Open: whether G is trivial, and
  whether |G| is exactly Z2 (a=1,b=0) or trivial (a=0,b=0) — note b∈{0,1}
  allows b=1 only if... 3|G| but then no order-3 fixed points.
- This is a worked example of exactly the orbit-matrix method GOAL.md wants to
  push one order further. The search space here (a few orbit distributions, ≤7
  orbit matrices each) is stated precisely; any "exclude Z2 / show G trivial"
  claim would extend exactly this computation.

## Computer-assistance status
The Z6/S3/E9/Z9 exclusions are computer-assisted (GAP + Mathematica). Not
computer-free; the exhaustiveness of the orbit-distribution enumeration is the
argument that makes them theorems, and that enumeration is documented.

[[crnkovic-maksimovic-composite-automorphism]] [[crnkovic-maksimovic-full-pdf]]
