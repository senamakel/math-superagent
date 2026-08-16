# Behbahani (2009) — PhD thesis "On strongly regular graphs"

Source URL: https://spectrum.library.concordia.ca/id/eprint/976720/1/NR63369.pdf
(Thesis, Concordia University, 2009, supervisor C. Lam; 121 leaves.)
Full text: research/sources/behbahani-2009-phd-thesis-pdf.full.md (7285 lines).

## What the thesis is
The PRIMARY source for the orbit-matrix method (row/column orbit matrices of an
SRG under an automorphism group), and for the "only possible prime divisors 2 and
3" result on Aut of a putative srg(99,14,1,2). This is the result later quoted by
Crnković–Maksimović as their Theorem 7.1 and by Cesarz–Woldar. Confirmed here
verbatim.

## Exact results located in the full text

**Theorem 4.14 (thesis numbering; = C–M Thm 7.1).** If an srg(99,14,1,2) exists,
the only possible prime divisors of the size of its automorphism group are 2 and 3.
Moreover, if it has an automorphism of order 3, then it has no fixed points.

Also in the tables (Table 3 / Table 21): srg(99,14,1,2) possible primes {2,3}.

**Makhnev–Minakova Theorem 1.6 (quoted in thesis §1.6).** If G=srg(99,14,1,2), p
an automorphism of prime order p, and A the subgraph induced by the fixed points
of p, then:
  (1) A is the singleton graph and p equals 2 or 7;
  (2) A is the empty graph and p equals 3 or 11;
  (3) A is the triangle graph and p = 3.
This is the fixed-point subgraph structure result. Combined with Behbahani's
"only primes 2,3", the p=7 and p=11 branches are excluded, and p=3 must be the
empty fixed-point subgraph (no fixed points, matching (2) or (3) but thesis says
order-3 automorphisms have no fixed points, so A empty).

**Method:** orbit matrices (Ch. 2-3); upper bound on number of fixed points of an
automorphism (Ch. 3, "3.5 Upper bounds on the number of fixed points"); SRG
program (Ch. 4) that given the size/order of an automorphism generates all orbit
matrices, then all SRGs from each. Applied to unknown SRG parameter sets listed in
Table 3 (65-…100 base cases) and to known ones (49,18,7,6; etc.).

## Relevance / what it settles for this run
- Confirms from the primary source the exact "only primes 2,3; order-3
  fixed-point-free" claim that the library previously held only secondhand
  (C–M Thm 7.1, Cesarz–Woldar citations). Upgrades that claim's evidence class
  to "read from primary source".
- Gives the precise Makhnev–Minakova fixed-point subgraph dichotomy (Thm 1.6),
  which is the local/structural input the automorphism-orbit arguments use. This
  is the substrate on which Cesarz–Woldar build their 2|6 and 7⟹Z7 computer-free
  proofs.
- Computer-assisted status: the orbit-matrix classification for (99,14,1,2) is
  computer-assisted (the SRG program generating all orbit matrices). Confirms the
  taxonomies in research/notes/automorphism-orders-consolidated.md.

[[crnkovic-maksimovic-full-pdf]] [[behbahani-lam-2011-srg-nontrivial-automorphisms]]
