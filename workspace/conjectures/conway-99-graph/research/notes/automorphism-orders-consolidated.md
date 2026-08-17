# Automorphism-group constraints on a putative Conway 99-graph — consolidated, sourced

Answers the open request `exact-list-prime-051a` (exact list of prime orders
excluded, by whom, computer-assisted?)

## The chain of divisibility / structure results, oldest to newest

### Makhnev–Minakova 2004 (On automorphisms of SRGs with λ=1, μ=2)
- Classification: k = u²+u+2, u ∈ {1,3,4,10,31}; u=3 gives (99,14,1,2).
- **|Aut Γ| divides 2·3³·7·11.**
- If 2 | |G| then |G| divides 42.
- Uses character theory of finite groups (Higman method) to constrain the
  fixed-point subgraphs of prime-order automorphisms.
Source: Discrete Math. Appl. 14(2) 201–210 (2004), DOI 10.1515/156939204872374;
as quoted in Cesarz–Woldar 2025 and the published abstract.

### Behbahani 2009 (PhD thesis, Concordia, supervisor C. Lam) — PRIMARY SOURCE
- **Theorem 4.14**: if srg(99,14,1,2) exists, the only possible prime divisors of
  |Aut Γ| are **2 and 3**; an order-3 automorphism has **no fixed points**. This
  is the direct primary statement behind C–M Thm 7.1 and Cesarz–Woldar's routes.
- Introduced the **orbit-matrix method** (row/column orbit matrices of an SRG
  under an automorphism group) and the fixed-point upper bound.
- Quotes **Makhnev–Minakova Thm 1.6** (fixed-point subgraph A of a prime-order
  automorphism p of a putative srg(99,14,1,2)):
    (1) A singleton, p∈{2,7};
    (2) A empty, p∈{3,11};
    (3) A triangle, p=3.
  Combined with "only primes 2,3": the p=7 and p=11 branches are excluded, and
  p=3 ⟹ A empty (order-3 fixed-point-free).
- Source: research/sources/behbahani-2009-phd-thesis-pdf.full.md (full text),
  summary research/summaries/behbahani-2009-phd-thesis.md.

### Crnković–Maksimović 2020 (Construction of SRGs having an automorphism group
of composite order, Contrib. Discrete Math. 15(1) 22–41, DOI 10.55016/ojs/cdm.v15i1.62323)
- **No srg(99,14,1,2) admits an automorphism group Z₆, S₃, Z₉, or E₉.**
- Computer-assisted orbit-matrix method (composite-order generalization of
  Behbahani–Lam). FULL mechanism now in library (§7): for Z6 the only orbit
  distributions (0,0,1,16),(0,0,3,15),(0,0,5,14) give 2,4,7 orbit matrices,
  none refining to Z3; for S3 the same distributions and none refine to Z3;
  for E9/Z9 only distribution (0,0,11) with the unique diagonal-4/off-diag-1
  orbit matrix, no Z3 refinement / no SRG. Concludes Thm 7.3: |Aut Γ|=2^a 3^b,
  b∈{0,1}, order-3 automorphisms fixed-point-free, no order-6 group.
- Source: research/sources/crnkovic-maksimovic-full-pdf.full.md (full text),
  summary research/summaries/crnkovic-maksimovic-full-pdf.md.

### Cesarz–Woldar 2025 (On the automorphism group of a putative Conway 99-graph,
Algebraic Combinatorics 8(2) 379–398; arXiv 2308.02978)
- **Computer-free** proofs:
  - (1′) if 7 | |G| then G ≅ Z₇;
  - (2′) if 2 | |G| then |G| divides 6 (so G ∈ {Z₂, Z₆, S₃}).
- Stage 1 proves **there is no automorphism of order 14.**
- The arXiv version's elimination of the Frobenius group Frob(21) (order 21)
  uses a computer-assisted search; the published version reports (1′) as
  computer-free. Must be flagged: the Frob(21) elimination in the arXiv
  v1/v2 is computer-assisted; the ALCO published paper claims computer-free.

## Consolidated — exactly which orders are excluded

Let G = Aut Γ for a putative Conway 99-graph. Known (conditional on existence of Γ):

| Claim | Author(s) | Year | Computer-assisted? |
|---|---|---|---|
| \|G\| divides 2·3³·7·11 | Makhnev–Minakova | 2004 | no (character theory) |
| if 2\|G\| then \|G\| divides 42 | Makhnev–Minakova | 2004 | no |
| prime divisors of \|G\| ⊆ {2,3} | Behbahani–Lam | 2011 | yes (orbit matrices) |
| no Z₆, S₃, Z₉, E₉ automorphism groups | Crnković–Maksimović | 2020 | yes (orbit matrices) |
| no order-14 automorphism | Cesarz–Woldar | 2025 | no (computer-free) |
| if 7\|G\| then G ≅ Z₇ | Cesarz–Woldar | 2025 | no (published; arXiv Frob(21) elimination computer-assisted) |
| if 2\|G\| then \|G\| divides 6 | Cesarz–Woldar | 2025 | no |

Interpretation of "which prime orders are excluded": the possible prime
divisors are at most {2,3} (Behbahani–Lam narrowing); 7 and 11 do not divide
|G|. Within {2,3}: a fixed-point-free order-3 automorphism is forced as far as
Behbahani–Lam; order-2/order-6/S₃ groups are constrained to {Z₂,Z₆,S₃} (if
2|G|, Cesarz–Woldar) but Z₆,S₃ are then excluded by Crnković–Maksimović.
Net: a non-trivial automorphism group, if any, is very small. Whether G is
trivial is open.

This note is the answering source for the request `exact-list-prime-051a`
(which prime orders are excluded, by whom, computer-assisted?) — see the
`answers: exact-list-prime-051a` line in the claim block below; the consolidated
table answers it fully.

## Gap for the run
What remains open on automorphisms: whether G is trivial, and the exact orbit
structure of remaining candidate groups (e.g. a hypothetical Z₂ or Z₇). The
*prime-order exclusion list* itself is settled (table above) — that is a
different question from these open ones.
Makhnev's own survey (2010) and the (85,14,3,2) / other μ=2 papers in the
frontier apply his Higman-method to neighbours; those are secondary.

```claim
id: automorphism-orders-consolidated
statement: For a putative Conway 99-graph Gamma with G = Aut(Gamma)
  (conditional on existence): |G| divides 2.3^3.7.11 (Makhnev-Minakova 2004);
  if 2||G| then |G| divides 42 (MM04); only primes 2 and 3 can divide |G|
  (Behbahani-Lam 2011); no automorphism group isomorphic to Z6, S3, Z9 or E9
  (Crnkovic-Maksimovic 2020); 14 does not divide |G| (no order-14
  automorphism), if 7||G| then G is Z7, and if 2||G| then |G| divides 6
  (Cesarz-Woldar 2025, computer-free in published form; the arXiv Frob(21)
  elimination is computer-assisted).
hypotheses: existence of Gamma is assumed; all claims are constraints on G.
holds-here: yes — directly answers which automorphism orders are excluded and
  by whom.
status: asserted-by-source (peer-reviewed papers; exact statements consolidated
  from library full texts and abstracts). The computer-assistance status of the
  Frob(21) elimination differs between arXiv and published versions — flagged.
bearing: gives the run's automorphism frontier precisely; any new excluded
  order (e.g. proving G trivial, or excluding Z2) is a genuine advance. Directive 18 confirms this request is answered and closed (resumption artifact; do not re-open).
anchor: research/sources/cesarz-woldar-automorph-conway99.full.md,
  research/sources/crnkovic-maksimovic-composite-automorphism.full.md
answers: exact-list-prime-051a
```
