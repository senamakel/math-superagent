# Milne, Algebraic Number Theory (course notes)

**Source URL:** https://www.jmilne.org/math/CourseNotes/ANT210.pdf
**Type:** University lecture notes (J. S. Milne, University of Michigan, Math 676)
**Status:** Summary-level record — retrieved via read_sources; full PDF text not stored (download blocked by network boundary). The mathematical statements below were captured from the retrieved chapter content.

## Why this source is in the library

This is the standard treatment of the algebra behind the problem's machinery: rings of integers, Dedekind domains, ideal factorisation, the ideal class group, the finiteness of the class number, units and Dirichlet's unit theorem, and the chapter on cyclotomic extensions and Fermat's Last Theorem (Chapter 6, pp. 82–88). The run needs the ideal-theoretic framework before it can work in Z[zeta_p].

## Content relevant to the problem

- A number field K has a ring of integers O_K; O_K is a Dedekind domain, so nonzero ideals factor uniquely into prime ideals even when elements do not factor uniquely (Sections 2, 3). This is precisely the failure of unique factorisation that the problem's obstruction lives in.
- The ideal class group Cl(K) measures how far O_K is from a principal ideal domain (Section 3.5). The class number is finite (Section 4, via Minkowski/lattice arguments).
- Units: the unit group of O_K is {roots of unity} × free abelian group (Dirichlet's unit theorem, Section 5). For Z[sqrt(2)], units are {±(1+sqrt(2))^m}; this is the simplest illustration of infinite unit rank.
- **Chapter 6: Cyclotomic Extensions; Fermat's Last Theorem** (pp. 82–88) is the load-bearing chapter for this problem:
  - Z[zeta_p] is the ring of integers of Q(zeta_p).
  - The prime p ramifies in Q(zeta_p); the specific ramification pattern is analysed.
  - The FLT-style factorisation: an equation like z^p = x^p + y^p is studied in the cyclotomic field by factorising (x + zeta_p^i y) and examining the principalisation of the ideal (x + zeta_p^i y). The ideal-theoretic constraint comes from the class group.
  - Regular primes (those not dividing the class number of Q(zeta_p)) are where the Kummer approach works; the class group is the obstruction elsewhere.
  - Units in cyclotomic fields and Dirichlet's unit theorem applied.

## How this maps onto the problem

The equation x^p - y^q = 1 with p an odd prime forces working in Q(zeta_p), where x^p - 1 = y^q factors as
  x^p - 1 = product_{i=1}^{p} (x - zeta_p^i)
in Z[zeta_p]. The ideals (x - zeta_p^i) are pairwise nearly coprime off the ramified prime (1 - zeta_p), so the q-th power y^q forces each to be (up to the ramified prime) a q-th power of an ideal. Converting that ideal relation into an element relation requires the relevant ideals to be principal — the class group is the obstruction. This is exactly the mechanism Milne's Chapter 6 lays out for FLT and it transfers directly.

## Verified statements (from retrieved content)

- O_K is a Dedekind domain; ideal factorisation is unique up to order. [retrieved, section 3]
- The class group is finite. [retrieved, section 4]
- Unit group structure = finite roots of unity × free abelian group. [retrieved, section 5]
- Z[zeta_p] is the ring of integers of Q(zeta_p); p ramifies there; regular-prime/class-group mechanism governs the FLT-style ideal factorisation x^p - 1 = prod(x - zeta^i). [retrieved, chapter 6]

## Not verified / not available

- The exact pages of Chapter 6 beyond the outline above were not all retrieved. For the precise ramification index and the exact regularity proof, consult the full PDF or Washington (GTM 83).
