# Behbahani (2009) PhD thesis — full PDF — automorphism prime-divisor table

<!-- source: https://spectrum.library.concordia.ca/id/eprint/976720/1/NR63369.pdf -->
<!-- full text: research/sources/behbahani-2009-phd-thesis-pdf.full.md (7285 lines) -->

This is the full PDF of Behbahani's 2009 Concordia PhD thesis (supervisor
C. Lam), the PRIMARY source of the orbit-matrix method and of the
automorphism-group constraints. The short digest
(`research/summaries/behbahani-2009-phd-thesis.md`) already records Theorem
4.14 (99 → primes {2,3}, order-3 fixed-point-free) and Makhnev–Minakova Thm
1.6 (fixed-point subgraph dichotomy). This PDF digest adds the full **Table 3**
of possible prime divisors and the symmetric result for (85,14,3,2).

## Table 3 — possible prime divisors of |Aut| for the unknown SRGs (p. 9–10)

| graph | possible primes |
|---|---|
| srg(65,32,15,16) | 2,3,5 |
| srg(69,20,7,5) | 2,3 |
| srg(75,32,10,16) | 2,3 |
| srg(76,30,8,14) | 2,3 |
| srg(76,35,18,14) | 2,3,5 |
| **srg(85,14,3,2)** | **2** |
| srg(85,30,11,10) | 2,3,5,17 |
| srg(85,42,20,21) | 2,3,5,7 |
| srg(88,27,6,9) | 2,3,5,11 |
| srg(95,40,12,20) | 2,3,5 |
| srg(96,35,10,14) | 2,3,5 |
| srg(96,38,10,18) | 2,3,5 |
| srg(96,45,24,18) | 2,3,5 |
| **srg(99,14,1,2)** | **2,3** |
| srg(99,42,21,15) | 2,3,5,7,11 |
| srg(100,33,8,12) | 2,3,5,11 |

## The companion result for (85,14,3,2) — NEW

"The only possible prime divisor of the size of the automorphism group of
srg(85,14,3,2) is 2" — i.e. if srg(85,14,3,2) existed its automorphism group
would be a **2-group** (order a power of 2). This is thesis Table 13, and it
kills Paduchikh's Theorem 1.5 cases (1)-(3) (which allowed primes 3,5,7,17).

**Paduchikh Theorem 1.5** (for srg(85,14,3,2)): for a prime-order automorphism
with fixed-point subgraph A, one of: (1) p=5 or 17, A empty; (2) p=7 and A a
1-clique, or p=5 and A a 5-clique; (3) p=3, A a quadrangle or 2×5 lattice; (4)
p=2, neighbourhood of any vertex of A connected, A a union of x isolated
vertices and y isolated triangles with (y=1,x∈{4,6}) or (y=0,x=5).

## Contrast with 99 (the two k=14,λ~1 cases diverge on automorphisms)
- (99,14,1,2): primes {2,3}; order-3 fixed-point-free; |G| | 2³·3³·7·11
  further refined by Cesarz–Woldar (2|G| → |G||6; 7|G| → G≅Z7).
- (85,14,3,2): primes {2} only — a 2-group, EVEN more constrained than 99.
  Yet (85,14,3,2) does not exist (Shpectorov–Zhao 2025). So "very small
  automorphism group" is NOT sufficient for existence; the two share k=14 and
  μ=2, differ in λ (1 vs 3), and the 85-graph dies by local-enumeration while
  99 survives. This is direct evidence that the 99 obstruction is NOT
  automorphism-group size — reinforcing that a non-symmetry local/counting
  argument is the route.

## Status / caution
- Primary source (PhD thesis, peer-examined). The Table-3 entries are
  computer-assisted (orbit-matrix + SRG program). The (85 → primes {2})
  statement is the thesis's own result (Table 13) and is quoted verbatim at
  lines 935–940.
- The (85,14,3,2)-automorphism result is **consistent** with, and amplifies,
  the claim that the 85-nonexistence is not an automorphism story.

```claim
id: behbahani-85-graph-primes-2-only
statement: Behbahani 2009 (PhD thesis, from the full PDF's Table 13): the only
  possible prime divisor of |Aut srg(85,14,3,2)| is 2 (so Aut is a 2-group if
  the graph existed). This rules out Paduchikh's Thm 1.5 cases (1)-(3) for the
  85-graph. By contrast (99,14,1,2) has possible primes {2,3} (Table 3,
  Thm 4.14), with order-3 fixed-point-free.
hypotheses: existence of the respective srg assumed; the results are
  constraints on the hypothetical automorphism group.
holds-here: yes — the 85-graph is the closest μ=2 k=14 settled analogue, and
  this shows its (and 99's) obstruction is not automorphism size.
status: sourced (Behbahani PhD thesis full PDF, Table 3 and Table 13; the
  results are computer-assisted orbit-matrix work, asserted-by-source here).
bearing: shows Aut-size is not the deciding factor for the k=14 mu=2 family —
  both the 2-group-only 85-set (nonexistent) and the {2,3} 99-set (open) are
  small-group cases, so the 99 obstruction must be local/counting, reinforcing
  the k14-l1-local thread.
anchor: research/sources/behbahani-2009-phd-thesis-pdf.full.md
contradicts: none; complements behbahani-2009 results and the shpectorov-zhao
  template.
```

[[behbahani-2009-phd-thesis-pdf.full]]
